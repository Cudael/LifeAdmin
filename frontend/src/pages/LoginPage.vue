<template>
  <div class="relative min-h-screen flex items-center justify-center px-4 overflow-hidden bg-gradient-to-br from-gray-50 via-teal-50/30 to-cyan-50/30">
    
    <!-- Decorative background elements -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-20 left-10 w-72 h-72 bg-teal-200 rounded-full opacity-20 blur-3xl animate-pulse-slow"></div>
      <div class="absolute bottom-20 right-10 w-96 h-96 bg-cyan-200 rounded-full opacity-20 blur-3xl animate-pulse-slower"></div>
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-blue-200 rounded-full opacity-10 blur-3xl"></div>
    </div>

    <!-- Login Card -->
    <div class="relative z-10 w-full max-w-md">
      
      <!-- Logo/Brand (optional) -->
      <div class="text-center mb-8 animate-fade-in-down">
        <RouterLink to="/" class="inline-block">
          <div class="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl flex items-center justify-center shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110">
            <Lock :size="32" class="text-white" />
          </div>
          <h1 class="text-2xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
            LifeAdmin
          </h1>
        </RouterLink>
      </div>

      <!-- Main Card -->
      <div class="bg-white/80 backdrop-blur-xl p-8 md:p-10 rounded-3xl shadow-2xl border-2 border-white/50 animate-fade-in-up">
        
        <div class="text-center mb-8">
          <h2 class="text-3xl font-bold text-gray-900 mb-2">Welcome Back</h2>
          <p class="text-gray-600">Sign in to your account to continue</p>
        </div>

        <!-- Error Message -->
        <div
          v-if="errorMessage"
          class="mb-6 p-4 bg-red-50 border-2 border-red-200 rounded-xl flex items-start gap-3 animate-shake"
        >
          <AlertCircle :size="20" class="text-red-500 flex-shrink-0 mt-0.5" />
          <p class="text-sm text-red-700">{{ errorMessage }}</p>
        </div>

        <!-- Google Sign In Button (NEW - FEATURED) -->
        <button
          @click="signInWithGoogle"
          :disabled="loading"
          type="button"
          class="w-full flex items-center justify-center gap-3 px-6 py-4 bg-white border-2 border-gray-300 rounded-xl font-semibold text-gray-700 hover:bg-gray-50 hover:border-gray-400 hover:shadow-md transition-all duration-200 mb-6 disabled:opacity-50 disabled:cursor-not-allowed group"
        >
          <img 
            src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" 
            alt="Google" 
            class="w-6 h-6"
          />
          <span>Continue with Google</span>
        </button>

        <!-- Divider -->
        <div class="relative mb-6">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-200"></div>
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-4 bg-white/80 text-gray-500 font-medium">Or continue with email</span>
          </div>
        </div>

        <!-- Login Form -->
        <form @submit.prevent="handleLogin" class="space-y-6">

          <!-- EMAIL -->
          <div class="space-y-2">
            <label class="block text-sm font-semibold text-gray-700 items-center gap-2">
              <Mail :size="16" class="text-teal-600" />
              Email Address
            </label>
            <div class="relative">
              <input
                v-model="email"
                type="email"
                class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 backdrop-blur-sm"
                placeholder="you@example.com"
                required
                :disabled="loading"
              />
            </div>
          </div>

          <!-- PASSWORD -->
          <div class="space-y-2">
            <label class="block text-sm font-semibold text-gray-700 items-center gap-2">
              <Lock :size="16" class="text-teal-600" />
              Password
            </label>
            <div class="relative">
              <input
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                class="w-full px-4 py-3 pr-12 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 backdrop-blur-sm"
                placeholder="••••••••"
                required
                :disabled="loading"
              />
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 transition-colors"
                tabindex="-1"
              >
                <Eye v-if="!showPassword" :size="20" />
                <EyeOff v-if="showPassword" :size="20" />
              </button>
            </div>
          </div>

          <!-- Remember Me & Forgot Password -->
          <div class="flex items-center justify-between text-sm">
            <label class="flex items-center gap-2 cursor-pointer group">
              <input
                type="checkbox"
                v-model="rememberMe"
                class="w-4 h-4 text-teal-600 border-gray-300 rounded focus:ring-teal-500 cursor-pointer"
              />
              <span class="text-gray-600 group-hover:text-gray-900 transition-colors">Remember me</span>
            </label>
            <RouterLink
              to="/forgot-password"
              class="text-teal-600 hover:text-teal-700 font-medium hover:underline transition-colors"
            >
              Forgot password?
            </RouterLink>
          </div>

          <!-- SUBMIT BUTTON -->
          <button
            type="submit"
            :disabled="loading"
            class="group relative w-full bg-gradient-to-r from-teal-500 to-cyan-500 text-white py-4 rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            <span v-if="!loading" class="flex items-center gap-2">
              Sign In
              <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
            </span>
            <span v-else class="flex items-center gap-3">
              <Loader2 :size="20" class="animate-spin" />
              Signing in...
            </span>
          </button>

        </form>

        <!-- Register Link -->
        <p class="text-center text-sm text-gray-600 mt-8">
          Don't have an account?
          <RouterLink
            to="/register"
            class="text-teal-600 hover:text-teal-700 font-semibold hover:underline transition-colors"
          >
            Create an account
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
import { ref, onMounted } from "vue"
import { useRouter, useRoute } from "vue-router"
import { apiFetch } from "../utils/api"
import { setTokens } from "../utils/auth"
import {
  Lock,
  Mail,
  Eye,
  EyeOff,
  ArrowRight,
  ArrowLeft,
  Loader2,
  AlertCircle
} from "lucide-vue-next"

const router = useRouter()
const route = useRoute()

const email = ref("")
const password = ref("")
const rememberMe = ref(false)
const showPassword = ref(false)
const loading = ref(false)
const errorMessage = ref("")

// Check for OAuth error in URL
onMounted(() => {
  if (route.query.error === 'oauth_failed') {
    errorMessage.value = 'Google sign-in failed. Please try again.'
  }
})

// Regular email/password login
async function handleLogin() {
  loading.value = true
  errorMessage.value = ""

  try {
    const res = await apiFetch("/auth/login", {
      method: "POST",
      body: JSON.stringify({
        email: email.value,
        password: password.value,
        remember_me: rememberMe.value
      })
    })

    if (!res.ok) {
      const data = await res.json()
      errorMessage.value = data.detail || "Invalid email or password"
      loading.value = false
      return
    }

    const data = await res.json()
    setTokens(data.access_token, data.refresh_token)

    // Success animation before redirect
    setTimeout(() => {
      router.push("/dashboard")
    }, 300)

  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong. Please try again."
    loading.value = false
  }
}

// Google OAuth login
function signInWithGoogle() {
  loading.value = true
  errorMessage.value = ""
  
  // Redirect to backend Google OAuth endpoint
  window.location.href = 'http://localhost:8000/auth/google'
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

@keyframes shake {
  0%, 100% {
    transform: translateX(0);
  }
  10%, 30%, 50%, 70%, 90% {
    transform: translateX(-5px);
  }
  20%, 40%, 60%, 80% {
    transform: translateX(5px);
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

.animate-pulse-slow {
  animation: pulse-slow 4s ease-in-out infinite;
}

.animate-pulse-slower {
  animation: pulse-slower 6s ease-in-out infinite;
}

.animate-shake {
  animation: shake 0.5s ease-in-out;
}
</style>