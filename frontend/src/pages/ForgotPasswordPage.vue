<template>
  <div class="min-h-screen bg-gradient-to-br from-teal-500 via-cyan-500 to-blue-500 flex items-center justify-center p-4">
    
    <div class="w-full max-w-md">
      
      <!-- Card -->
      <div class="bg-white rounded-3xl shadow-2xl p-8">
        
        <!-- Header -->
        <div class="text-center mb-8">
          <div class="w-16 h-16 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg">
            <KeyRound :size="32" class="text-white" />
          </div>
          <h1 class="text-3xl font-bold text-gray-900 mb-2">Forgot Password?</h1>
          <p class="text-gray-600">No worries! We'll send you reset instructions.</p>
        </div>

        <!-- Success State -->
        <div v-if="emailSent" class="text-center py-8">
          <div class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <Mail :size="40" class="text-green-600" />
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">Check your email!</h3>
          <p class="text-gray-600 mb-6">
            We've sent password reset instructions to:<br>
            <strong>{{ email }}</strong>
          </p>
          <p class="text-sm text-gray-500 mb-6">
            Didn't receive it? Check your spam folder or
            <button
              @click="resetForm"
              class="text-teal-600 font-semibold hover:underline"
            >
              try again
            </button>
          </p>
          <RouterLink
            to="/login"
            class="inline-flex items-center gap-2 text-teal-600 font-semibold hover:text-teal-700"
          >
            <ArrowLeft :size="20" />
            Back to login
          </RouterLink>
        </div>

        <!-- Form -->
        <form v-else @submit.prevent="handleSubmit">
          
          <!-- Email Input -->
          <div class="mb-6">
            <label class="block text-sm font-semibold text-gray-700 mb-2">
              Email Address
            </label>
            <div class="relative">
              <Mail :size="20" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
              <input
                v-model="email"
                type="email"
                required
                placeholder="you@example.com"
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
            <span v-else>Send Reset Link</span>
          </button>

          <!-- Back to Login -->
          <div class="mt-6 text-center">
            <RouterLink
              to="/login"
              class="inline-flex items-center gap-2 text-gray-600 hover:text-gray-900 font-medium transition-colors"
            >
              <ArrowLeft :size="18" />
              Back to login
            </RouterLink>
          </div>

        </form>

      </div>

      <!-- Help Text -->
      <p class="text-center text-white/90 text-sm mt-6">
        Remember your password?
        <RouterLink to="/login" class="font-semibold hover:underline">
          Sign in
        </RouterLink>
      </p>

    </div>

  </div>
</template>

<script setup>
import { ref } from "vue"
import { apiFetch } from "../utils/api"
import {
  KeyRound,
  Mail,
  ArrowLeft,
  AlertCircle,
  Loader2
} from "lucide-vue-next"

const email = ref("")
const loading = ref(false)
const error = ref("")
const emailSent = ref(false)

async function handleSubmit() {
  error.value = ""
  loading.value = true

  try {
    const res = await apiFetch("/auth/forgot-password", {
      method: "POST",
      body: JSON.stringify({ email: email.value })
    })

    if (res.ok) {
      emailSent.value = true
    } else {
      const data = await res.json()
      error.value = data.detail || "Failed to send reset email. Please try again."
    }
  } catch (err) {
    console.error("Forgot password error:", err)
    error.value = "Something went wrong. Please try again."
  } finally {
    loading.value = false
  }
}

function resetForm() {
  emailSent.value = false
  email.value = ""
  error.value = ""
}
</script>