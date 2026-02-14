import { apiFetch } from "../utils/api"

export function useApi() {
  const api = {
    async get(url, options = {}) {
      try {
        const response = await apiFetch(url, {
          ...options,
          method: "GET"
        })

        if (!response.ok) {
          const error = await response.json()
          throw new Error(error.detail || error.message || "Request failed")
        }

        return await response.json()
      } catch (error) {
        console.error("API GET error:", error)
        throw error
      }
    },

    async post(url, data, options = {}) {
      try {
        const response = await apiFetch(url, {
          ...options,
          method: "POST",
          body: data instanceof FormData ? data : JSON.stringify(data)
        })

        if (!response.ok) {
          const error = await response.json()
          throw new Error(error.detail || error.message || "Request failed")
        }

        return await response.json()
      } catch (error) {
        console.error("API POST error:", error)
        throw error
      }
    },

    async put(url, data, options = {}) {
      try {
        const response = await apiFetch(url, {
          ...options,
          method: "PUT",
          body: data instanceof FormData ? data : JSON.stringify(data)
        })

        if (!response.ok) {
          const error = await response.json()
          throw new Error(error.detail || error.message || "Request failed")
        }

        return await response.json()
      } catch (error) {
        console.error("API PUT error:", error)
        throw error
      }
    },

    async patch(url, data, options = {}) {
      try {
        const response = await apiFetch(url, {
          ...options,
          method: "PATCH",
          body: data instanceof FormData ? data : JSON.stringify(data)
        })

        if (!response.ok) {
          const error = await response.json()
          throw new Error(error.detail || error.message || "Request failed")
        }

        return await response.json()
      } catch (error) {
        console.error("API PATCH error:", error)
        throw error
      }
    },

    async delete(url, options = {}) {
      try {
        const response = await apiFetch(url, {
          ...options,
          method: "DELETE"
        })

        if (!response.ok) {
          const error = await response.json()
          throw new Error(error.detail || error.message || "Request failed")
        }

        if (response.status === 204) {
          return null
        }

        return await response.json()
      } catch (error) {
        console.error("API DELETE error:", error)
        throw error
      }
    }
  }

  return { api }
}
