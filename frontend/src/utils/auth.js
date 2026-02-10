// src/utils/auth.js
import { ref } from "vue"

export const accessToken = ref(localStorage.getItem("accessToken"))
export const refreshToken = ref(localStorage.getItem("refreshToken"))

export function setTokens(access, refresh) {
  accessToken.value = access
  refreshToken.value = refresh

  localStorage.setItem("accessToken", access)
  localStorage.setItem("refreshToken", refresh)
}

export function clearTokens() {
  accessToken.value = null
  refreshToken.value = null

  localStorage.removeItem("accessToken")
  localStorage.removeItem("refreshToken")
}