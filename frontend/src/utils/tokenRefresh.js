// Automatic token refresh utility
import { accessToken, refreshToken, setTokens, clearTokens } from "./auth"
import { log, error } from "./logger"

const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000"

// Time constants for readability
const HOUR_IN_MS = 1000 * 60 * 60 // 1 hour in milliseconds
const DAY_IN_SECONDS = 60 * 60 * 24 // 1 day in seconds

// Check interval: check if token needs refresh every hour
const CHECK_INTERVAL_MS = HOUR_IN_MS

let refreshIntervalId = null
let isRefreshing = false // Flag to prevent concurrent refresh attempts

// Decode JWT to check expiration (without verification)
function decodeToken(token) {
  try {
    const base64Url = token.split('.')[1]
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split('')
        .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    )
    return JSON.parse(jsonPayload)
  } catch (e) {
    return null
  }
}

// Check if token is expired or will expire soon
function shouldRefreshToken(token) {
  if (!token) return false
  
  const decoded = decodeToken(token)
  if (!decoded || !decoded.exp) return false
  
  const now = Date.now() / 1000 // Current time in seconds
  const timeUntilExpiry = decoded.exp - now
  
  // Refresh if less than 1 day remaining
  return timeUntilExpiry < DAY_IN_SECONDS
}

// Perform token refresh
async function performTokenRefresh() {
  // Prevent concurrent refresh attempts
  if (isRefreshing) {
    log('⏭️ Refresh already in progress, skipping')
    return false
  }
  
  if (!refreshToken.value) {
    log('⏭️ No refresh token available, skipping refresh')
    return false
  }

  isRefreshing = true

  try {
    log('🔄 Attempting automatic token refresh...')
    
    const response = await fetch(`${BASE_URL}/auth/refresh`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ refresh_token: refreshToken.value })
    })

    if (response.ok) {
      const data = await response.json()
      setTokens(data.access_token, data.refresh_token)
      log('✅ Token refreshed successfully')
      return true
    } else {
      log('❌ Token refresh failed:', response.status)
      clearTokens()
      window.location.href = "/login"
      return false
    }
  } catch (err) {
    error('❌ Token refresh error:', err)
    return false
  } finally {
    isRefreshing = false
  }
}

// Start automatic token refresh
export function startTokenRefresh() {
  // Stop any existing interval
  stopTokenRefresh()
  
  // Only start if we have a refresh token
  if (!refreshToken.value) {
    log('⏭️ No refresh token, not starting automatic refresh')
    return
  }

  log('🚀 Starting automatic token refresh check (every hour)')
  
  // Check immediately if we should refresh
  if (shouldRefreshToken(accessToken.value)) {
    performTokenRefresh()
  }
  
  // Set up periodic check - check every hour if token needs refresh
  refreshIntervalId = setInterval(() => {
    if (accessToken.value && refreshToken.value) {
      // Only refresh if token will expire soon (within 1 day)
      if (shouldRefreshToken(accessToken.value)) {
        performTokenRefresh()
      }
    } else {
      log('⏭️ No tokens available, stopping refresh')
      stopTokenRefresh()
    }
  }, CHECK_INTERVAL_MS)
}

// Stop automatic token refresh
export function stopTokenRefresh() {
  if (refreshIntervalId) {
    clearInterval(refreshIntervalId)
    refreshIntervalId = null
    log('⏹️ Stopped automatic token refresh')
  }
}

// Initialize on page load if tokens exist
export function initTokenRefresh() {
  if (accessToken.value && refreshToken.value) {
    startTokenRefresh()
  }
}
