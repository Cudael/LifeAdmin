<template>
  <div class="relative">
    
    <!-- Overlay when not verified -->
    <div
      v-if="!isVerified"
      class="absolute inset-0 bg-white/80 backdrop-blur-sm z-10 rounded-xl flex items-center justify-center"
    >
      <div class="text-center p-6 max-w-md">
        <div class="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4">
          <ShieldAlert :size="32" class="text-orange-600" />
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-2">Email Verification Required</h3>
        <p class="text-gray-600 mb-6">
          {{ customMessage || 'Please verify your email address to access this feature.' }}
        </p>
        <button
          @click="resendVerification"
          :disabled="resending"
          class="px-6 py-3 bg-gradient-to-r from-orange-500 to-amber-500 text-white rounded-xl font-semibold hover:shadow-lg transition-all disabled:opacity-50 flex items-center justify-center gap-2 mx-auto"
        >
          <Loader2 v-if="resending" :size="20" class="animate-spin" />
          <Mail v-else :size="20" />
          {{ resending ? 'Sending...' : 'Resend Verification Email' }}
        </button>
      </div>
    </div>

    <!-- Actual content (blurred when not verified) -->
    <div :class="{ 'blur-sm pointer-events-none': !isVerified }">
      <slot />
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from "vue"
import { apiFetch } from "../utils/api"
import {
  ShieldAlert,
  Mail,
  Loader2
} from "lucide-vue-next"

const props = defineProps({
  user: {
    type: Object,
    required: true
  },
  customMessage: {
    type: String,
    default: ""
  }
})

const isVerified = computed(() => props.user?.email_verified || false)
const resending = ref(false)

async function resendVerification() {
  resending.value = true
  
  try {
    const res = await apiFetch("/auth/resend-verification", {
      method: "POST"
    })

    if (res.ok) {
      alert("✅ Verification email sent! Please check your inbox.")
    } else {
      const data = await res.json()
      alert(data.detail || "Failed to send verification email")
    }
  } catch (err) {
    console.error("Resend verification error:", err)
    alert("Something went wrong. Please try again.")
  } finally {
    resending.value = false
  }
}
</script>