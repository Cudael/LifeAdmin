<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-teal-50 to-cyan-50">
    <div class="text-center">
      <div class="w-20 h-20 border-4 border-teal-200 border-t-teal-500 rounded-full animate-spin mx-auto mb-6"></div>
      <h2 class="text-2xl font-bold text-gray-900 mb-2">Signing you in...</h2>
      <p class="text-gray-600">Please wait a moment</p>
      <p v-if="errorMessage" class="text-red-600 mt-4">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { setTokens } from '../utils/auth'

const router = useRouter()
const errorMessage = ref('')

onMounted(async () => {
  try {
    // Get tokens from URL
    const urlParams = new URLSearchParams(window.location.search)
    const token = urlParams.get('token')
    const refreshToken = urlParams.get('refresh_token')
    
    console.log('OAuth callback - Token received:', token ? 'Yes' : 'No')
    console.log('OAuth callback - Refresh token received:', refreshToken ? 'Yes' : 'No')
    
    if (!token) {
      console.error('No token received from OAuth callback')
      errorMessage.value = 'No authentication token received'
      setTimeout(() => {
        router.push('/login?error=oauth_failed')
      }, 2000)
      return
    }
    
    // Save tokens
    setTokens(token, refreshToken || null)
    
    console.log('Tokens saved, redirecting to dashboard...')
    
    // Small delay to ensure token is saved
    setTimeout(() => {
      router.push('/dashboard')
    }, 500)
    
  } catch (error) {
    console.error('Auth callback error:', error)
    errorMessage.value = 'Authentication failed'
    setTimeout(() => {
      router.push('/login?error=oauth_failed')
    }, 2000)
  }
})
</script>