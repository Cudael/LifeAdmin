<template>
  <div class="min-h-screen bg-gradient-to-br from-teal-500 via-cyan-500 to-blue-500 flex items-center justify-center p-4">
    
    <div class="w-full max-w-md">
      
      <!-- Card -->
      <div class="bg-white rounded-3xl shadow-2xl p-8">
        
        <!-- Loading State -->
        <div v-if="verifying" class="text-center py-12">
          <Loader2 :size="48" class="animate-spin text-teal-500 mx-auto mb-4" />
          <p class="text-gray-600">Verifying reset link...</p>
        </div>

        <!-- Invalid Token -->
        <div v-else-if="!tokenValid" class="text-center py-8">
          <div class="w-20 h-20 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <AlertCircle :size="40" class="text-red-600" />
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">Invalid Reset Link</h3>
          <p class="text-gray-600 mb-6">{{ tokenError }}</p>
          <RouterLink
            to="/forgot-password"
            class="inline-block px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white font-semibold rounded-xl hover:shadow-lg transition-all"
          >
            Request New Link
          </RouterLink>
        </div>

        <!-- Success State -->
        <div v-else-if="resetSuccess" class="text-center py-8">
          <div class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <CheckCircle2 :size="40" class="text-green-600" />
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">Password Reset!</h3>
          <p class="text-gray-600 mb-6">
            Your password has been successfully reset.
          </p>
          <RouterLink
            to="/login"
            class="inline-block px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white font-semibold rounded-xl hover:shadow-lg transition-all"
          >
            Go to Login
          </RouterLink>
        </div>

        <!-- Reset Form -->
        <div v-else>
          
          <!-- Header -->
          <div class="text-center mb-8">
            <div class="w-16 h-16 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg">
              <Lock :size="32" class="text-white" />
            </div>
            <h1 class="text-3xl font-bold text-gray-900 mb-2">Reset Password</h1>
            <p class="text-gray-600">Enter your new password below</p>
          </div>

          <!-- Form -->
          <form @submit.prevent="handleSubmit">
            
            <!-- New Password -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-2">
                New Password
              </label>
              <div class="relative">
                <Lock :size="20" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
                <input
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  minlength="8"
                  placeholder="Enter new password"
                  class="w-full pl-12 pr-12 py-3 border-2 border-gray-200 rounded-xl focus:border-teal-500 focus:outline-none transition-colors"
                  :disabled="loading"
                />
                <button
                  type="button"
                  @click="showPassword = !showPassword"
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
                >
                  <Eye v-if="!showPassword" :size="20" />
                  <EyeOff v-else :size="20" />
                </button>
              </div>
              <p class="text-xs text-gray-500 mt-2">Must be at least 8 characters</p>
            </div>

            <!-- Confirm Password -->
            <div class="mb-6">
              <label class="block text-sm font-semibold text-gray-700 mb-2">
                Confirm Password
              </label>
              <div class="relative">
                <Lock :size="20" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
                <input
                  v-model="confirmPassword"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  minlength="8"
                  placeholder="Confirm new password"
                  class="w-full pl-12 pr-4 py-3 border-2 border-gray-200 rounded-xl focus:border-teal-500 focus:outline-none transition-colors"
                  :disabled="loading"
                />
              </div>
            </div>

            <!-- Error Message -->
            <div v-if="error" class="mb-6 p-4 bg-red-50 border border-red-200 rounded-xl flex items-start gap-3">
              <AlertCircle :size="20" class="text-red-600 flex-shrink-0 mt-0.5" />
              <p class="text-sm text-red-800">{{ error }}</p>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="loading"
              class="w-full py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white font-semibold rounded-xl shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <Loader2 v-if="loading" :size="20" class="animate-spin" />
              <span v-else>Reset Password</span>
            </button>

          </form>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import { apiFetch } from "../utils/api"
import {
  Lock,
  Eye,
  EyeOff,
  AlertCircle,
  CheckCircle2,
  Loader2
} from "lucide-vue-next"

const route = useRoute()

const token = ref("")
const password = ref("")
const confirmPassword = ref("")
const showPassword = ref(false)
const loading = ref(false)
const verifying = ref(true)
const tokenValid = ref(false)
const tokenError = ref("")
const error = ref("")
const resetSuccess = ref(false)

onMounted(async () => {
  // Get token from URL
  token.value = route.query.token || ""
  
  if (!token.value) {
    tokenValid.value = false
    tokenError.value = "No reset token provided"
    verifying.value = false
    return
  }

  // Verify token
  await verifyToken()
})

async function verifyToken() {
  verifying.value = true
  
  try {
    const res = await apiFetch("/auth/verify-reset-token", {
      method: "POST",
      body: JSON.stringify({ token: token.value })
    })

    const data = await res.json()

    if (data.valid) {
      tokenValid.value = true
    } else {
      tokenValid.value = false
      tokenError.value = data.message || "Invalid or expired reset token"
    }
  } catch (err) {
    console.error("Token verification error:", err)
    tokenValid.value = false
    tokenError.value = "Failed to verify reset token"
  } finally {
    verifying.value = false
  }
}

async function handleSubmit() {
  error.value = ""

  // Validation
  if (password.value.length < 8) {
    error.value = "Password must be at least 8 characters"
    return
  }

  if (password.value !== confirmPassword.value) {
    error.value = "Passwords do not match"
    return
  }

  loading.value = true

  try {
    const res = await apiFetch("/auth/reset-password", {
      method: "POST",
      body: JSON.stringify({
        token: token.value,
        password: password.value
      })
    })

    if (res.ok) {
      resetSuccess.value = true
    } else {
      const data = await res.json()
      error.value = data.detail || "Failed to reset password. Please try again."
    }
  } catch (err) {
    console.error("Reset password error:", err)
    error.value = "Something went wrong. Please try again."
  } finally {
    loading.value = false
  }
}
</script>