<template>
  <main class="min-h-screen flex bg-slate-950 text-slate-300 font-sans selection:bg-teal-500/30 selection:text-teal-200">
    
    <!-- LEFT PANE: Form Area (Scrollable if screen is short) -->
    <div class="w-full lg:w-[50%] h-screen overflow-y-auto flex flex-col px-8 sm:px-12 md:px-16 lg:px-24 relative z-10 custom-scrollbar py-12">
      
      <!-- Logo -->
      <RouterLink to="/" class="flex items-center gap-3 group w-max mb-12">
        <div class="w-8 h-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-lg flex items-center justify-center shadow-[0_0_15px_rgba(45,212,191,0.2)] group-hover:scale-105 transition-transform">
          <Sparkles :size="16" class="text-slate-950" />
        </div>
        <span class="text-xl font-extrabold text-white tracking-tight">
          Life<span class="text-slate-500">Admin</span>
        </span>
      </RouterLink>

      <div class="w-full max-w-md mx-auto flex-1 flex flex-col justify-center">
        <h1 class="text-3xl font-extrabold text-white tracking-tight mb-2">Create your account</h1>
        <p class="text-slate-400 mb-8">Join thousands of organized users today.</p>

        <!-- Error Message -->
        <div v-if="errorMessage" class="mb-6 p-4 bg-rose-500/10 border border-rose-500/20 rounded-xl flex items-start gap-3 animate-shake">
          <AlertCircle :size="20" class="text-rose-400 shrink-0 mt-0.5" />
          <p class="text-sm text-rose-300 font-medium">{{ errorMessage }}</p>
        </div>

        <!-- Success Message -->
        <div v-if="successMessage" class="mb-6 p-4 bg-emerald-500/10 border border-emerald-500/20 rounded-xl flex items-start gap-3 animate-fade-in-up">
          <CheckCircle2 :size="20" class="text-emerald-400 shrink-0 mt-0.5" />
          <div>
            <p class="text-sm font-semibold text-emerald-300">{{ successMessage }}</p>
            <p class="text-xs text-emerald-400/70 mt-1">Redirecting to login...</p>
          </div>
        </div>

        <!-- Register Form -->
        <form @submit.prevent="handleRegister" class="space-y-5">

          <!-- Full Name -->
          <div class="space-y-1.5">
            <label class="text-sm font-medium text-slate-300">Full Name</label>
            <div class="relative group/input">
              <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <User :size="18" class="text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
              </div>
              <input
                v-model="fullName"
                type="text"
                required
                :disabled="loading"
                placeholder="John Doe"
                class="w-full bg-slate-900/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl pl-11 pr-4 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
              />
            </div>
          </div>

          <!-- Email -->
          <div class="space-y-1.5">
            <label class="text-sm font-medium text-slate-300">Email address</label>
            <div class="relative group/input">
              <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <Mail :size="18" class="text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
              </div>
              <input
                v-model="email"
                type="email"
                required
                :disabled="loading"
                placeholder="you@example.com"
                class="w-full bg-slate-900/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl pl-11 pr-4 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
              />
            </div>
          </div>

          <!-- Password Layout: Grid for Desktop to save vertical space -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
            
            <!-- Password -->
            <div class="space-y-1.5">
              <label class="text-sm font-medium text-slate-300">Password</label>
              <div class="relative group/input">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <Lock :size="18" class="text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
                </div>
                <input
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  :disabled="loading"
                  @input="validatePassword"
                  placeholder="••••••••"
                  class="w-full bg-slate-900/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl pl-11 pr-10 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
                />
                <button
                  type="button"
                  @click="showPassword = !showPassword"
                  class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300 transition-colors"
                >
                  <Eye v-if="!showPassword" :size="18" />
                  <EyeOff v-else :size="18" />
                </button>
              </div>
            </div>

            <!-- Confirm Password -->
            <div class="space-y-1.5">
              <label class="text-sm font-medium text-slate-300">Confirm Password</label>
              <div class="relative group/input">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <ShieldCheck :size="18" class="text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
                </div>
                <input
                  v-model="confirmPassword"
                  :type="showConfirmPassword ? 'text' : 'password'"
                  required
                  :disabled="loading"
                  placeholder="••••••••"
                  class="w-full bg-slate-900/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl pl-11 pr-10 py-3 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
                />
                <button
                  type="button"
                  @click="showConfirmPassword = !showConfirmPassword"
                  class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300 transition-colors"
                >
                  <Eye v-if="!showConfirmPassword" :size="18" />
                  <EyeOff v-else :size="18" />
                </button>
              </div>
            </div>

          </div>

          <!-- Dynamic Password HUD -->
          <div v-if="password" class="bg-slate-900/50 border border-white/5 p-3 rounded-xl space-y-2">
            <!-- Strength Indicator -->
            <div class="flex gap-1.5">
              <div
                v-for="i in 4"
                :key="i"
                :class="[
                  'h-1.5 flex-1 rounded-full transition-all duration-500',
                  passwordStrength >= i ? getStrengthColor(passwordStrength) : 'bg-slate-800'
                ]"
              ></div>
            </div>
            <div class="flex justify-between items-center text-xs font-medium">
              <span :class="getStrengthTextColor(passwordStrength)">{{ getStrengthText(passwordStrength) }}</span>
              <!-- Match Indicator -->
              <span v-if="confirmPassword" class="flex items-center gap-1">
                <CheckCircle2 v-if="password === confirmPassword" :size="12" class="text-emerald-400" />
                <XCircle v-else :size="12" class="text-rose-400" />
                <span :class="password === confirmPassword ? 'text-emerald-400' : 'text-rose-400'">
                  {{ password === confirmPassword ? 'Matched' : 'Mismatch' }}
                </span>
              </span>
            </div>
          </div>

          <!-- Terms and Conditions -->
          <div class="flex items-start gap-3 pt-2">
            <input
              type="checkbox"
              v-model="agreeToTerms"
              id="terms"
              class="w-4 h-4 mt-0.5 rounded border-white/20 bg-slate-900 accent-teal-500 cursor-pointer focus:ring-teal-500/50 focus:ring-offset-slate-950"
              required
            />
            <label for="terms" class="text-xs text-slate-400 cursor-pointer leading-relaxed">
              I agree to the
              <RouterLink to="/terms" class="text-teal-400 font-semibold hover:text-teal-300">Terms of Service</RouterLink>
              and
              <RouterLink to="/privacy" class="text-teal-400 font-semibold hover:text-teal-300">Privacy Policy</RouterLink>.
            </label>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading || !agreeToTerms || (password && confirmPassword && password !== confirmPassword)"
            class="relative group/btn w-full mt-2"
          >
            <div class="absolute -inset-0.5 bg-gradient-to-r from-teal-500 to-cyan-500 rounded-xl blur opacity-50 group-hover/btn:opacity-100 transition duration-300 disabled:opacity-0"></div>
            <div class="relative w-full flex items-center justify-center gap-2 px-4 py-3.5 bg-slate-900 text-white font-bold rounded-xl border border-white/10 transition-all duration-300 disabled:opacity-80">
              <span v-if="!loading" class="flex items-center gap-2">
                Create Account
                <ArrowRight :size="18" class="text-teal-400 group-hover/btn:translate-x-1 transition-transform" />
              </span>
              <span v-else class="flex items-center gap-2">
                <Loader2 :size="18" class="animate-spin text-teal-400" />
                Creating vault...
              </span>
            </div>
          </button>

        </form>

        <!-- Divider -->
        <div class="flex items-center gap-4 my-8">
          <div class="h-px bg-white/10 flex-1"></div>
          <span class="text-xs text-slate-500 font-medium uppercase tracking-wider">Or continue with</span>
          <div class="h-px bg-white/10 flex-1"></div>
        </div>

        <!-- Social Sign Up -->
        <div class="grid grid-cols-2 gap-4">
          <button type="button" class="flex items-center justify-center gap-2 px-4 py-3 bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 rounded-xl transition-all duration-200 font-medium text-white text-sm">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
              <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
              <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
              <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 15.01 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
            </svg>
            Google
          </button>

          <button type="button" class="flex items-center justify-center gap-2 px-4 py-3 bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 rounded-xl transition-all duration-200 font-medium text-white text-sm">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
              <path d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.17 6.839 9.49.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.463-1.11-1.463-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.167 22 16.418 22 12c0-5.523-4.477-10-10-10z"/>
            </svg>
            GitHub
          </button>
        </div>

        <p class="text-center text-sm text-slate-500 mt-8">
          Already have an account?
          <RouterLink to="/login" class="text-teal-400 hover:text-teal-300 font-bold transition-colors ml-1">
            Sign in
          </RouterLink>
        </p>
      </div>

    </div>

    <!-- RIGHT PANE: Visual Showcase (Hidden on Mobile) -->
    <div class="hidden lg:flex flex-1 relative bg-slate-900 border-l border-white/5 overflow-hidden items-center justify-center p-12">
      
      <!-- Decorative Background Grid -->
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:32px_32px] [mask-image:radial-gradient(ellipse_80%_80%_at_50%_50%,#000_40%,transparent_100%)] pointer-events-none"></div>
      
      <!-- Glowing Orbs -->
      <div class="absolute top-1/3 right-1/3 w-80 h-80 bg-teal-500/20 blur-[100px] rounded-full pointer-events-none mix-blend-screen animate-pulse-slow"></div>
      <div class="absolute bottom-1/3 left-1/3 w-80 h-80 bg-cyan-500/20 blur-[100px] rounded-full pointer-events-none mix-blend-screen animate-pulse-slower"></div>

      <!-- Abstract Registration Graphic -->
      <div class="relative z-10 w-full max-w-md">
        <!-- Background decorative card -->
        <div class="absolute inset-0 bg-slate-800/50 rounded-3xl transform rotate-6 scale-95 border border-white/5"></div>
        <div class="absolute inset-0 bg-slate-800/80 rounded-3xl transform -rotate-3 scale-100 border border-white/5"></div>
        
        <!-- Main Foreground Card -->
        <div class="relative bg-slate-900/80 backdrop-blur-xl border border-white/10 rounded-3xl p-10 shadow-[0_0_50px_rgba(0,0,0,0.4)]">
          <div class="flex justify-between items-start mb-12">
            <div class="w-14 h-14 bg-teal-500/10 border border-teal-500/20 rounded-2xl flex items-center justify-center shadow-inner">
              <ShieldCheck :size="28" class="text-teal-400 drop-shadow-[0_0_8px_rgba(45,212,191,0.5)]" />
            </div>
            <!-- Mock encrypted status -->
            <div class="flex items-center gap-2 px-3 py-1.5 bg-emerald-500/10 border border-emerald-500/20 rounded-full">
              <div class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></div>
              <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">AES-256</span>
            </div>
          </div>
          
          <h3 class="text-2xl font-bold text-white mb-2 tracking-tight">
            Your personal vault awaits.
          </h3>
          <p class="text-slate-400 text-sm leading-relaxed mb-8">
            All your data is encrypted at rest and in transit. We never sell your data, and only you hold the keys.
          </p>
          
          <!-- Mock loading UI indicating processing -->
          <div class="space-y-4">
            <div class="h-2 w-full bg-slate-800 rounded-full overflow-hidden">
              <div class="h-full bg-gradient-to-r from-teal-500 to-cyan-500 w-[65%] rounded-full"></div>
            </div>
            <div class="flex justify-between text-xs font-semibold text-slate-500">
              <span>Establishing secure connection...</span>
              <span class="text-teal-400">65%</span>
            </div>
          </div>
        </div>
      </div>

    </div>
  </main>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import { apiFetch } from "../utils/api"
import {
  Sparkles,
  User,
  Mail,
  Lock,
  Eye,
  EyeOff,
  ArrowRight,
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
  if (strength <= 1) return 'bg-rose-500 shadow-[0_0_10px_rgba(225,29,72,0.5)]'
  if (strength === 2) return 'bg-amber-500 shadow-[0_0_10px_rgba(245,158,11,0.5)]'
  if (strength === 3) return 'bg-blue-500 shadow-[0_0_10px_rgba(59,130,246,0.5)]'
  return 'bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.5)]'
}

function getStrengthTextColor(strength) {
  if (strength <= 1) return 'text-rose-400'
  if (strength === 2) return 'text-amber-400'
  if (strength === 3) return 'text-blue-400'
  return 'text-emerald-400'
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
@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-4px); }
  20%, 40%, 60%, 80% { transform: translateX(4px); }
}

.animate-fade-in-up {
  animation: fade-in-up 0.4s ease-out forwards;
}

.animate-shake {
  animation: shake 0.4s ease-in-out;
}

@keyframes pulse-slow {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 0.8; }
}

@keyframes pulse-slower {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.6; }
}

.animate-pulse-slow {
  animation: pulse-slow 6s ease-in-out infinite;
}

.animate-pulse-slower {
  animation: pulse-slower 8s ease-in-out infinite;
}

/* Hide scrollbar for the form column but keep functionality */
.custom-scrollbar::-webkit-scrollbar {
  display: none;
}
.custom-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>