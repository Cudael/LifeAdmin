import { accessToken, refreshToken, setTokens, clearTokens } from "./auth"

const BASE_URL = "http://localhost:8000"

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
    // try refresh
    const refreshRes = await fetch(BASE_URL + "/auth/refresh", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refresh_token: refreshToken.value })
    })

    if (refreshRes.ok) {
      const data = await refreshRes.json()
      setTokens(data.access_token, data.refresh_token)

      // retry original request
      response = await doFetch()
    } else {
      clearTokens()
      window.location.href = "/login"
      return
    }
  }

  return response
}