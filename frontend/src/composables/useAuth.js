import { ref, computed } from "vue"
import { accessToken, setTokens, clearTokens } from "../utils/auth"
import { apiFetch } from "../utils/api"

export function useAuth() {
  const user = ref(null)
  const loading = ref(false)
  const isAuthenticated = computed(() => !!accessToken.value)

  async function login(email, password) {
    loading.value = true
    try {
      const response = await apiFetch("/auth/login", {
        method: "POST",
        body: JSON.stringify({ email, password })
      })

      if (!response.ok) {
        const error = await response.json()
        throw new Error(error.detail || "Login failed")
      }

      const data = await response.json()
      setTokens(data.access_token, data.refresh_token)
      user.value = data.user
      return data
    } finally {
      loading.value = false
    }
  }

  async function register(email, password) {
    loading.value = true
    try {
      const response = await apiFetch("/auth/register", {
        method: "POST",
        body: JSON.stringify({ email, password })
      })

      if (!response.ok) {
        const error = await response.json()
        throw new Error(error.detail || "Registration failed")
      }

      const data = await response.json()
      setTokens(data.access_token, data.refresh_token)
      user.value = data.user
      return data
    } finally {
      loading.value = false
    }
  }

  function logout() {
    clearTokens()
    user.value = null
  }

  async function checkAuthStatus() {
    if (!accessToken.value) {
      return false
    }

    loading.value = true
    try {
      const response = await apiFetch("/auth/me")
      
      if (response.ok) {
        const data = await response.json()
        user.value = data
        return true
      } else {
        clearTokens()
        user.value = null
        return false
      }
    } catch (error) {
      clearTokens()
      user.value = null
      return false
    } finally {
      loading.value = false
    }
  }

  return {
    user,
    isAuthenticated,
    loading,
    login,
    register,
    logout,
    checkAuthStatus
  }
}
