<script setup>
import { ref, computed, onMounted } from "vue"
import { apiFetch } from "../utils/api"
import {
  Mail,
  X,
  CheckCircle2,
  AlertCircle,
  Loader2
} from "lucide-vue-next"

const props = defineProps({
  user: {
    type: Object,
    required: true
  }
})

const isVerified = computed(() => props.user?.email_verified || false)
const isUserReady = computed(() => {
  return props.user && 'email_verified' in props.user
})

// ✅ Check dismissal status IMMEDIATELY (not in onMounted)
const checkDismissalStatus = () => {
  const dismissedUntil = localStorage.getItem('verification_banner_dismissed_until')
  
  if (dismissedUntil) {
    const dismissTime = new Date(dismissedUntil)
    const now = new Date()
    
    // If still within the dismissed period, keep it hidden
    if (now < dismissTime) {
      const minutesLeft = Math.round((dismissTime - now) / 1000 / 60)
      console.log(`🔕 Verification banner dismissed for ${minutesLeft} more minutes`)
      return true
    } else {
      // Time expired, remove the storage item
      localStorage.removeItem('verification_banner_dismissed_until')
      return false
    }
  }
  
  return false
}

// ✅ Initialize immediately (before component renders)
const isDismissed = ref(checkDismissalStatus())

const resending = ref(false)
const justSent = ref(false)
const successMessage = ref("")
const errorMessage = ref("")

// ✅ Dismiss for 1 hour
function dismiss() {
  isDismissed.value = true
  
  // Set dismissal to expire in 1 hour
  const dismissUntil = new Date()
  dismissUntil.setHours(dismissUntil.getHours() + 1)
  
  localStorage.setItem('verification_banner_dismissed_until', dismissUntil.toISOString())
  
  console.log(`✅ Banner dismissed until: ${dismissUntil.toLocaleString()}`)
}

async function resendVerification() {
  resending.value = true
  successMessage.value = ""
  errorMessage.value = ""
  
  try {
    const res = await apiFetch("/auth/resend-verification", {
      method: "POST"
    })

    if (res.ok) {
      justSent.value = true
      successMessage.value = "✅ Verification email sent! Please check your inbox (and spam folder)."
      
      // Reset after 5 seconds
      setTimeout(() => {
        justSent.value = false
        successMessage.value = ""
      }, 5000)
    } else {
      const data = await res.json()
      errorMessage.value = data.detail || "Failed to send verification email"
      
      setTimeout(() => {
        errorMessage.value = ""
      }, 5000)
    }
  } catch (err) {
    console.error("Resend verification error:", err)
    errorMessage.value = "Something went wrong. Please try again."
    
    setTimeout(() => {
      errorMessage.value = ""
    }, 5000)
  } finally {
    resending.value = false
  }
}
</script>

<template>
  <Transition
    enter-active-class="transition-all duration-300 ease-out"
    enter-from-class="opacity-0 -translate-y-4"
    enter-to-class="opacity-100 translate-y-0"
    leave-active-class="transition-all duration-200 ease-in"
    leave-from-class="opacity-100 translate-y-0"
    leave-to-class="opacity-0 -translate-y-4"
  >
    <div
      v-if="isUserReady && !isVerified && !isDismissed"
      class="bg-gradient-to-r from-orange-500 to-amber-500 text-white shadow-lg"
    >
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <div class="flex items-center justify-between gap-4">
          
          <!-- Icon & Message -->
          <div class="flex items-center gap-3 flex-1">
            <div class="flex-shrink-0">
              <div class="w-10 h-10 bg-white/20 rounded-full flex items-center justify-center">
                <Mail :size="20" class="text-white" />
              </div>
            </div>
            
            <div class="flex-1">
              <p class="font-semibold text-white mb-1">
                📧 Verify Your Email Address
              </p>
              <p class="text-sm text-white/90">
                Please verify your email to unlock all features and ensure you receive important notifications.
              </p>
            </div>
          </div>

          <!-- Actions -->
          <div class="flex items-center gap-3">
            
            <!-- Resend Button -->
            <button
              @click="resendVerification"
              :disabled="resending || justSent"
              class="px-4 py-2 bg-white text-orange-600 rounded-lg font-semibold hover:bg-white/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2 text-sm"
            >
              <Loader2 v-if="resending" :size="16" class="animate-spin" />
              <CheckCircle2 v-else-if="justSent" :size="16" />
              <Mail v-else :size="16" />
              <span v-if="justSent">Sent!</span>
              <span v-else-if="resending">Sending...</span>
              <span v-else>Resend Email</span>
            </button>

            <!-- Dismiss Button -->
            <button
              @click="dismiss"
              class="p-2 hover:bg-white/10 rounded-lg transition-colors"
              title="Dismiss for 1 hour"
            >
              <X :size="20" class="text-white" />
            </button>
          </div>

        </div>

        <!-- Success Message -->
        <Transition
          enter-active-class="transition-all duration-200 ease-out"
          enter-from-class="opacity-0 translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition-all duration-150 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 translate-y-2"
        >
          <div v-if="successMessage" class="mt-3 p-3 bg-white/20 backdrop-blur-sm rounded-lg flex items-center gap-2">
            <CheckCircle2 :size="16" class="text-white flex-shrink-0" />
            <p class="text-sm text-white">{{ successMessage }}</p>
          </div>
        </Transition>

        <!-- Error Message -->
        <Transition
          enter-active-class="transition-all duration-200 ease-out"
          enter-from-class="opacity-0 translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition-all duration-150 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 translate-y-2"
        >
          <div v-if="errorMessage" class="mt-3 p-3 bg-red-500/20 backdrop-blur-sm rounded-lg flex items-center gap-2">
            <AlertCircle :size="16" class="text-white flex-shrink-0" />
            <p class="text-sm text-white">{{ errorMessage }}</p>
          </div>
        </Transition>

      </div>
    </div>
  </Transition>
</template>