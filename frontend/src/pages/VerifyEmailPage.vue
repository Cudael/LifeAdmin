<template>
  <div class="min-h-screen bg-gradient-to-br from-teal-500 via-cyan-500 to-blue-500 flex items-center justify-center p-4">
    
    <div class="w-full max-w-md">
      
      <div class="bg-white rounded-3xl shadow-2xl p-8">
        
        <!-- Loading State -->
        <div v-if="verifying" class="text-center py-12">
          <Loader2 :size="48" class="animate-spin text-teal-500 mx-auto mb-4" />
          <p class="text-gray-600">Verifying your email...</p>
        </div>

        <!-- Success State -->
        <div v-else-if="success" class="text-center py-8">
          <div class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <CheckCircle2 :size="40" class="text-green-600" />
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">Email Verified!</h3>
          <p class="text-gray-600 mb-6">
            Your email has been successfully verified. You can now access all features.
          </p>
          <RouterLink
            to="/dashboard"
            class="inline-block px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white font-semibold rounded-xl hover:shadow-lg transition-all"
          >
            Go to Dashboard
          </RouterLink>
        </div>

        <!-- Error State -->
        <div v-else class="text-center py-8">
          <div class="w-20 h-20 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <AlertCircle :size="40" class="text-red-600" />
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">Verification Failed</h3>
          <p class="text-gray-600 mb-6">{{ errorMessage }}</p>
          
          <div class="space-y-3">
            <button
              @click="resendEmail"
              :disabled="resending"
              class="w-full px-6 py-3 bg-teal-600 text-white rounded-xl font-semibold hover:bg-teal-700 transition-colors disabled:opacity-50 flex items-center justify-center gap-2"
            >
              <Loader2 v-if="resending" :size="20" class="animate-spin" />
              <Mail v-else :size="20" />
              {{ resending ? 'Sending...' : 'Resend Verification Email' }}
            </button>
            
            <RouterLink
              to="/login"
              class="block px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-colors text-center"
            >
              Back to Login
            </RouterLink>
          </div>
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
  CheckCircle2,
  AlertCircle,
  Loader2,
  Mail
} from "lucide-vue-next"

const route = useRoute()

const verifying = ref(true)
const success = ref(false)
const errorMessage = ref("")
const resending = ref(false)

onMounted(async () => {
  const token = route.query.token
  
  if (!token) {
    verifying.value = false
    errorMessage.value = "No verification token provided"
    return
  }

  await verifyEmail(token)
})

async function verifyEmail(token) {
  verifying.value = true
  
  try {
    const res = await apiFetch("/auth/verify-email", {
      method: "POST",
      body: JSON.stringify({ token })
    })

    if (res.ok) {
      success.value = true
    } else {
      const data = await res.json()
      errorMessage.value = data.detail || "Failed to verify email"
    }
  } catch (err) {
    console.error("Verification error:", err)
    errorMessage.value = "Something went wrong. Please try again."
  } finally {
    verifying.value = false
  }
}

async function resendEmail() {
  resending.value = true
  
  try {
    const res = await apiFetch("/auth/resend-verification", {
      method: "POST"
    })

    if (res.ok) {
      errorMessage.value = "Verification email sent! Please check your inbox."
    } else {
      const data = await res.json()
      errorMessage.value = data.detail || "Failed to send verification email"
    }
  } catch (err) {
    console.error("Resend error:", err)
    errorMessage.value = "Failed to send email. Please try again later."
  } finally {
    resending.value = false
  }
}
</script>