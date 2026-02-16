<template>
  <div class="relative min-h-screen flex items-center justify-center px-4 py-12 overflow-hidden bg-gradient-to-br from-gray-50 via-teal-50/30 to-cyan-50/30">
    
    <!-- Decorative background elements -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-20 left-10 w-72 h-72 bg-teal-200 rounded-full opacity-20 blur-3xl animate-pulse-slow"></div>
      <div class="absolute bottom-20 right-10 w-96 h-96 bg-cyan-200 rounded-full opacity-20 blur-3xl animate-pulse-slower"></div>
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-blue-200 rounded-full opacity-10 blur-3xl"></div>
    </div>

    <!-- Register Card -->
    <div class="relative z-10 w-full max-w-md">
      
      <!-- Logo/Brand -->
      <div class="text-center mb-8 animate-fade-in-down">
        <RouterLink to="/" class="inline-block">
          <div class="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl flex items-center justify-center shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110">
            <UserPlus :size="32" class="text-white" />
          </div>
          <h1 class="text-2xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
            Remindes
          </h1>
        </RouterLink>
      </div>

      <!-- Main Card -->
      <div class="bg-white/80 backdrop-blur-xl p-8 md:p-10 rounded-3xl shadow-2xl border-2 border-white/50 animate-fade-in-up">
        
        <div class="text-center mb-8">
          <h2 class="text-3xl font-bold text-gray-900 mb-2">Create Your Account</h2>
          <p class="text-gray-600">Join thousands of organized users today</p>
        </div>

        <!-- Error Message -->
        <div
          v-if="errorMessage"
          class="mb-6 p-4 bg-red-50 border-2 border-red-200 rounded-xl flex items-start gap-3 animate-shake"
        >
          <AlertCircle :size="20" class="text-red-500 flex-shrink-0 mt-0.5" />
          <p class="text-sm text-red-700">{{ errorMessage }}</p>
        </div>

        <!-- Success Message -->
        <div
          v-if="successMessage"
          class="mb-6 p-4 bg-green-50 border-2 border-green-200 rounded-xl flex items-start gap-3 animate-bounce-in"
        >
          <CheckCircle2 :size="20" class="text-green-500 flex-shrink-0 mt-0.5" />
          <div>
            <p class="text-sm font-semibold text-green-700">{{ successMessage }}</p>
            <p class="text-xs text-green-600 mt-1">Redirecting to login...</p>
          </div>
        </div>

        <!-- Register Form -->
        <form @submit.prevent="handleRegister" class="space-y-5">

          <!-- Full Name -->
          <div class="space-y-2">
            <label class="block text-sm font-semibold text-gray-700 items-center gap-2">
              <User :size="16" class="text-teal-600" />
              Full Name
            </label>
            <div class="relative">
              <input
                v-model="fullName"
                type="text"
                class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 backdrop-blur-sm"
                placeholder="John Doe"
                required
                :disabled="loading"
                minlength="2"
              />
            </div>
          </div>

          <!-- Email -->
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

          <!-- Password -->
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
                minlength="8"
                @input="validatePassword"
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
            
            <!-- Password Strength Indicator -->
            <div v-if="password" class="space-y-2 mt-3">
              <div class="flex gap-1">
                <div
                  v-for="i in 4"
                  :key="i"
                  :class="[
                    'h-1 flex-1 rounded-full transition-all duration-300',
                    passwordStrength >= i ? getStrengthColor(passwordStrength) : 'bg-gray-200'
                  ]"
                ></div>
              </div>
              <p :class="['text-xs font-medium', getStrengthTextColor(passwordStrength)]">
                {{ getStrengthText(passwordStrength) }}
              </p>
            </div>
          </div>

          <!-- Confirm Password -->
          <div class="space-y-2">
            <label class="block text-sm font-semibold text-gray-700 items-center gap-2">
              <ShieldCheck :size="16" class="text-teal-600" />
              Confirm Password
            </label>
            <div class="relative">
              <input
                v-model="confirmPassword"
                :type="showConfirmPassword ? 'text' : 'password'"
                class="w-full px-4 py-3 pr-12 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 backdrop-blur-sm"
                placeholder="••••••••"
                required
                :disabled="loading"
              />
              <button
                type="button"
                @click="showConfirmPassword = !showConfirmPassword"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 transition-colors"
                tabindex="-1"
              >
                <Eye v-if="!showConfirmPassword" :size="20" />
                <EyeOff v-if="showConfirmPassword" :size="20" />
              </button>
            </div>
            
            <!-- Password Match Indicator -->
            <div v-if="confirmPassword" class="flex items-center gap-2 text-xs font-medium">
              <CheckCircle2 v-if="password === confirmPassword" :size="14" class="text-green-500" />
              <XCircle v-else :size="14" class="text-red-500" />
              <span :class="password === confirmPassword ? 'text-green-600' : 'text-red-600'">
                {{ password === confirmPassword ? 'Passwords match' : 'Passwords do not match' }}
              </span>
            </div>
          </div>

          <!-- Terms and Conditions -->
          <div class="flex items-start gap-3 p-4 bg-teal-50/50 border border-teal-200 rounded-xl">
            <input
              type="checkbox"
              v-model="agreeToTerms"
              id="terms"
              class="w-4 h-4 mt-0.5 text-teal-600 border-gray-300 rounded focus:ring-teal-500 cursor-pointer"
              required
            />
            <label for="terms" class="text-xs text-gray-700 cursor-pointer leading-relaxed">
              I agree to the
              <RouterLink to="/terms" class="text-teal-600 font-semibold hover:underline">Terms of Service</RouterLink>
              and
              <RouterLink to="/privacy" class="text-teal-600 font-semibold hover:underline">Privacy Policy</RouterLink>
            </label>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading || !agreeToTerms || (password && confirmPassword && password !== confirmPassword)"
            class="group relative w-full bg-gradient-to-r from-teal-500 to-cyan-500 text-white py-4 rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            <span v-if="!loading" class="flex items-center gap-2">
              Create Account
              <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
            </span>
            <span v-else class="flex items-center gap-3">
              <Loader2 :size="20" class="animate-spin" />
              Creating your account...
            </span>
          </button>

        </form>

        <!-- Divider -->
        <div class="relative my-8">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-200"></div>
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-4 bg-white/80 text-gray-500 font-medium">Or sign up with</span>
          </div>
        </div>

        <!-- Social Sign Up -->
        <div class="grid grid-cols-2 gap-4">
          <button
            type="button"
            class="flex items-center justify-center gap-2 px-4 py-3 border-2 border-gray-200 rounded-xl hover:border-gray-300 hover:bg-gray-50 transition-all duration-200 font-medium text-gray-700"
          >
            <svg class="w-5 h-5" viewBox="0 0 24 24">
              <path fill="currentColor" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
              <path fill="currentColor" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
              <path fill="currentColor" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
              <path fill="currentColor" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
            </svg>
            Google
          </button>

          <button
            type="button"
            class="flex items-center justify-center gap-2 px-4 py-3 border-2 border-gray-200 rounded-xl hover:border-gray-300 hover:bg-gray-50 transition-all duration-200 font-medium text-gray-700"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.17 6.839 9.49.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.463-1.11-1.463-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.167 22 16.418 22 12c0-5.523-4.477-10-10-10z"/>
            </svg>
            GitHub
          </button>
        </div>

        <!-- Login Link -->
        <p class="text-center text-sm text-gray-600 mt-8">
          Already have an account?
          <RouterLink
            to="/login"
            class="text-teal-600 hover:text-teal-700 font-semibold hover:underline transition-colors"
          >
            Sign in
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
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import { apiFetch } from "../utils/api"
import {
  UserPlus,
  User,
  Mail,
  Lock,
  Eye,
  EyeOff,
  ArrowRight,
  ArrowLeft,
  Loader2,
  AlertCircle,
  CheckCircle2,
  XCircle,
  ShieldCheck
} from "lucide-vue-next"

const router = useRouter()

const fullName = ref("")
const email = ref("")
const password = ref("")
const confirmPassword = ref("")
const agreeToTerms = ref(false)

const showPassword = ref(false)
const showConfirmPassword = ref(false)
const loading = ref(false)
const errorMessage = ref("")
const successMessage = ref("")

const passwordStrength = ref(0)

// Password strength calculator
function validatePassword() {
  let strength = 0
  const pwd = password.value

  if (pwd.length >= 8) strength++
  if (pwd.length >= 12) strength++
  if (/[a-z]/.test(pwd) && /[A-Z]/.test(pwd)) strength++
  if (/\d/.test(pwd)) strength++
  if (/[^a-zA-Z0-9]/.test(pwd)) strength++

  passwordStrength.value = Math.min(strength, 4)
}

function getStrengthColor(strength) {
  if (strength <= 1) return 'bg-red-500'
  if (strength === 2) return 'bg-yellow-500'
  if (strength === 3) return 'bg-blue-500'
  return 'bg-green-500'
}

function getStrengthTextColor(strength) {
  if (strength <= 1) return 'text-red-600'
  if (strength === 2) return 'text-yellow-600'
  if (strength === 3) return 'text-blue-600'
  return 'text-green-600'
}

function getStrengthText(strength) {
  if (strength === 0) return 'Very Weak'
  if (strength === 1) return 'Weak'
  if (strength === 2) return 'Fair'
  if (strength === 3) return 'Good'
  return 'Strong'
}

async function handleRegister() {
  errorMessage.value = ""
  successMessage.value = ""
  loading.value = true

  // Validation
  if (password.value !== confirmPassword.value) {
    errorMessage.value = "Passwords do not match"
    loading.value = false
    return
  }

  if (password.value.length < 8) {
    errorMessage.value = "Password must be at least 8 characters long"
    loading.value = false
    return
  }

  if (!agreeToTerms.value) {
    errorMessage.value = "You must agree to the Terms of Service"
    loading.value = false
    return
  }

  try {
    const res = await apiFetch("/auth/register", {
      method: "POST",
      body: JSON.stringify({
        full_name: fullName.value,
        email: email.value,
        password: password.value
      })
    })

    if (!res.ok) {
      const data = await res.json()
      errorMessage.value = data.detail || "Registration failed. Please try again."
      loading.value = false
      return
    }

    successMessage.value = "Account created successfully! 🎉"

    // Redirect after 2 seconds
    setTimeout(() => {
      router.push("/login")
    }, 2000)

  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong. Please try again."
    loading.value = false
  }
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

@keyframes bounce-in {
  0% {
    opacity: 0;
    transform: scale(0.9);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    opacity: 1;
    transform: scale(1);
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

.animate-bounce-in {
  animation: bounce-in 0.5s ease-out;
}
</style>