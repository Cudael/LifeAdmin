<template>
  <div class="relative min-h-screen flex items-center justify-center px-4 overflow-hidden bg-gradient-to-br from-gray-50 via-teal-50/30 to-cyan-50/30">
    
    <!-- Decorative background -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-20 left-10 w-72 h-72 bg-teal-200 rounded-full opacity-20 blur-3xl animate-pulse-slow"></div>
      <div class="absolute bottom-20 right-10 w-96 h-96 bg-cyan-200 rounded-full opacity-20 blur-3xl animate-pulse-slower"></div>
    </div>

    <!-- Card -->
    <div class="relative z-10 w-full max-w-md">
      
      <!-- Logo -->
      <div class="text-center mb-8 animate-fade-in-down">
        <RouterLink to="/" class="inline-block">
          <div class="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl flex items-center justify-center shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110">
            <KeyRound :size="32" class="text-white" />
          </div>
          <h1 class="text-2xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
            LifeAdmin
          </h1>
        </RouterLink>
      </div>

      <!-- Main Card -->
      <div class="bg-white/80 backdrop-blur-xl p-8 md:p-10 rounded-3xl shadow-2xl border-2 border-white/50 animate-fade-in-up">
        
        <div class="text-center mb-8">
          <h2 class="text-3xl font-bold text-gray-900 mb-2">Forgot Password?</h2>
          <p class="text-gray-600">Enter your email to reset your password</p>
        </div>

        <!-- Success Message -->
        <div
          v-if="successMessage"
          class="mb-6 p-4 bg-green-50 border-2 border-green-200 rounded-xl flex items-start gap-3"
        >
          <CheckCircle :size="20" class="text-green-500 flex-shrink-0 mt-0.5" />
          <p class="text-sm text-green-700">{{ successMessage }}</p>
        </div>

        <!-- Error Message -->
        <div
          v-if="errorMessage"
          class="mb-6 p-4 bg-red-50 border-2 border-red-200 rounded-xl flex items-start gap-3"
        >
          <AlertCircle :size="20" class="text-red-500 flex-shrink-0 mt-0.5" />
          <p class="text-sm text-red-700">{{ errorMessage }}</p>
        </div>

        <!-- Form -->
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <div class="space-y-2">
            <label class="block text-sm font-semibold text-gray-700">
              Email Address
            </label>
            <input
              v-model="email"
              type="email"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 backdrop-blur-sm"
              placeholder="you@example.com"
              required
              :disabled="loading"
            />
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="group relative w-full bg-gradient-to-r from-teal-500 to-cyan-500 text-white py-4 rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            <span v-if="!loading" class="flex items-center gap-2">
              Send Reset Link
              <Send :size="20" />
            </span>
            <span v-else class="flex items-center gap-3">
              <Loader2 :size="20" class="animate-spin" />
              Sending...
            </span>
          </button>
        </form>

        <!-- Back to Login -->
        <p class="text-center text-sm text-gray-600 mt-8">
          Remember your password?
          <RouterLink
            to="/login"
            class="text-teal-600 hover:text-teal-700 font-semibold hover:underline transition-colors"
          >
            Back to login
          </RouterLink>
        </p>

      </div>

      <!-- Back to Home -->
      <div class="text-center mt-6 animate-fade-in-up animation-delay-200">
        <RouterLink
          to="/"
          class="inline-flex items-center gap-2 text-gray-600 hover:text-gray-900 transition-colors group"
        >
          <ArrowLeft :size="16" class="group-hover:-translate-x-1 transition-transform" />
          Back to home
        </RouterLink>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { KeyRound, Send, ArrowLeft, Loader2, AlertCircle, CheckCircle } from "lucide-vue-next"

const email = ref("")
const loading = ref(false)
const errorMessage = ref("")
const successMessage = ref("")

async function handleSubmit() {
  loading.value = true
  errorMessage.value = ""
  successMessage.value = ""

  // TODO: Implement password reset API call
  // For now, just show a success message
  setTimeout(() => {
    successMessage.value = "If an account exists with that email, you will receive a password reset link shortly."
    loading.value = false
    email.value = ""
  }, 1000)
}
</script>

<style scoped>
@keyframes fade-in-down {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-down {
  animation: fade-in-down 0.6s ease-out;
}

.animate-fade-in-up {
  animation: fade-in-up 0.6s ease-out;
}

.animation-delay-200 {
  animation-delay: 0.2s;
  opacity: 0;
  animation-fill-mode: forwards;
}

@keyframes pulse-slow {
  0%, 100% {
    opacity: 0.2;
  }
  50% {
    opacity: 0.3;
  }
}

@keyframes pulse-slower {
  0%, 100% {
    opacity: 0.2;
  }
  50% {
    opacity: 0.25;
  }
}

.animate-pulse-slow {
  animation: pulse-slow 4s ease-in-out infinite;
}

.animate-pulse-slower {
  animation: pulse-slower 6s ease-in-out infinite;
}
</style>