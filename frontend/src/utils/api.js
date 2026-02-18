import { accessToken, refreshToken, setTokens, clearTokens } from "./auth"
import router from '../router'

export const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000"

export async function apiFetch(url, options = {}) {
  async function doFetch() {
    const headers = {
      ...(options.headers || {}),
      ...(accessToken.value ? { Authorization: `Bearer ${accessToken.value}` } : {})
    }

    const isFormData = options.body instanceof FormData
    if (!isFormData && !headers["Content-Type"]) {
      headers["Content-Type"] = "application/json"
    }

    return fetch(BASE_URL + url, {
      ...options,
      headers
    })
  }

  let response = await doFetch()

  if (response.status === 401 && refreshToken.value) {
    try {
      const refreshRes = await fetch(BASE_URL + "/auth/refresh", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh_token: refreshToken.value })
      })

      // Guard: make sure we got JSON back, not an HTML error page
      const contentType = refreshRes.headers.get("content-type") || ""
      if (!refreshRes.ok || !contentType.includes("application/json")) {
        clearTokens()
        router.push('/login')
        return null
      }

      const data = await refreshRes.json()
      setTokens(data.access_token, data.refresh_token)

      // retry original request
      response = await doFetch()
    } catch (err) {
      console.error('Token refresh error:', err)
      clearTokens()
      router.push('/login')
      return null
    }
  }

  return response
}