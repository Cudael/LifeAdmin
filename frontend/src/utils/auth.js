// src/utils/auth.js
import { ref } from "vue"

// Use consistent key names
const ACCESS_TOKEN_KEY = "access_token"
const REFRESH_TOKEN_KEY = "refresh_token"

export const accessToken = ref(localStorage.getItem(ACCESS_TOKEN_KEY))
export const refreshToken = ref(localStorage.getItem(REFRESH_TOKEN_KEY))

export function setTokens(access, refresh) {
  accessToken.value = access
  refreshToken.value = refresh

  localStorage.setItem(ACCESS_TOKEN_KEY, access)
  if (refresh) {
    localStorage.setItem(REFRESH_TOKEN_KEY, refresh)
  }
  
  console.log('✅ Tokens saved:', {
    access: access ? 'Yes' : 'No',
    refresh: refresh ? 'Yes' : 'No'
  })
}

export function clearTokens() {
  accessToken.value = null
  refreshToken.value = null

  localStorage.removeItem(ACCESS_TOKEN_KEY)
  localStorage.removeItem(REFRESH_TOKEN_KEY)
  
  console.log('🗑️ Tokens cleared')
}

export function getAccessToken() {
  return accessToken.value
}

export function getRefreshToken() {
  return refreshToken.value
}