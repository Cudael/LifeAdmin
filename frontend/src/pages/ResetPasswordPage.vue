<template>
  <main class="min-h-screen bg-slate-950 flex items-center justify-center p-6 relative overflow-hidden font-sans text-slate-300 selection:bg-teal-500/30 selection:text-teal-200">
    
    <!-- Deep Space Grid Background -->
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:32px_32px] [mask-image:radial-gradient(ellipse_60%_60%_at_50%_50%,#000_60%,transparent_100%)] pointer-events-none"></div>

    <!-- Glowing Orbs -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-xl h-96 bg-teal-500/20 blur-[150px] rounded-full pointer-events-none mix-blend-screen"></div>

    <div class="relative z-10 w-full max-w-md">
      
      <!-- Brand Logo at Top -->
      <RouterLink to="/" class="flex items-center justify-center gap-3 group mb-8">
        <div class="w-8 h-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-lg flex items-center justify-center shadow-[0_0_15px_rgba(45,212,191,0.2)]">
          <Sparkles :size="16" class="text-slate-950" />
        </div>
        <span class="text-xl font-extrabold text-white tracking-tight">
          Life<span class="text-slate-500">Admin</span>
        </span>
      </RouterLink>

      <!-- Glassmorphic Card -->
      <div class="bg-slate-900/60 backdrop-blur-xl border border-white/10 rounded-3xl shadow-[0_0_40px_rgba(0,0,0,0.5)] p-8 sm:p-10 overflow-hidden relative">

        <!-- Loading State -->
        <div v-if="verifying" class="text-center py-8 animate-fade-in">
          <div class="w-16 h-16 bg-teal-500/10 border border-teal-500/20 rounded-2xl flex items-center justify-center mx-auto mb-6">
            <Loader2 :size="32" class="animate-spin text-teal-400" />
          </div>
          <h3 class="text-xl font-bold text-white mb-2">Verifying Link</h3>
          <p class="text-slate-400">Authenticating your secure reset token...</p>
        </div>

        <!-- Invalid Token State -->
        <div v-else-if="!tokenValid" class="text-center py-6 animate-fade-in">
          <div class="w-16 h-16 bg-rose-500/10 border border-rose-500/20 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-inner">
            <AlertCircle :size="32" class="text-rose-400" />
          </div>
          <h3 class="text-2xl font-bold text-white mb-3 tracking-tight">Invalid Reset Link</h3>
          <p class="text-slate-400 mb-8">{{ tokenError }}</p>
          <RouterLink
            to="/forgot-password"
            class="block w-full py-3.5 bg-white/5 hover:bg-white/10 border border-white/10 text-white font-semibold rounded-xl transition-all duration-200"
          >
            Request New Link
          </RouterLink>
        </div>

        <!-- Success State -->
        <div v-else-if="resetSuccess" class="text-center py-6 animate-fade-in">
          <div class="w-16 h-16 bg-emerald-500/10 border border-emerald-500/20 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-inner">
            <CheckCircle2 :size="32" class="text-emerald-400 drop-shadow-[0_0_8px_rgba(16,185,129,0.5)]" />
          </div>
          <h3 class="text-2xl font-bold text-white mb-3 tracking-tight">Password Reset!</h3>
          <p class="text-slate-400 mb-8">
            Your vault has been secured with your new password.
          </p>
          
          <RouterLink
            to="/login"
            class="relative group/btn w-full block"
          >
            <div class="absolute -inset-0.5 bg-gradient-to-r from-emerald-500 to-teal-500 rounded-xl blur opacity-50 group-hover/btn:opacity-100 transition duration-300"></div>
            <div class="relative w-full py-3.5 bg-slate-900 text-white font-bold rounded-xl border border-white/10 transition-all duration-300">
              Go to Login
            </div>
          </RouterLink>
        </div>

        <!-- Reset Form -->
        <div v-else class="animate-fade-in">
          
          <!-- Header -->
          <div class="text-center mb-8">
            <div class="w-16 h-16 bg-teal-500/10 border border-teal-500/20 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-[0_0_15px_rgba(45,212,191,0.15)]">
              <Lock :size="32" class="text-teal-400" />
            </div>
            <h1 class="text-2xl font-bold text-white mb-2 tracking-tight">Secure New Password</h1>
            <p class="text-slate-400 text-sm">Enter your new master password below.</p>
          </div>

          <!-- Form -->
          <form @submit.prevent="handleSubmit" class="space-y-5">
            
            <!-- New Password -->
            <div class="space-y-1.5">
              <label class="block text-sm font-medium text-slate-300">New Password</label>
              <div class="relative group/input">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <Lock :size="18" class="text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
                </div>
                <input
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  minlength="8"
                  placeholder="••••••••"
                  class="w-full bg-slate-900/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl pl-11 pr-12 py-3.5 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
                  :disabled="loading"
                />
                <button
                  type="button"
                  @click="showPassword = !showPassword"
                  class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-500 hover:text-slate-300 transition-colors"
                >
                  <Eye v-if="!showPassword" :size="18" />
                  <EyeOff v-else :size="18" />
                </button>
              </div>
              <p class="text-xs text-slate-500 mt-1.5 font-medium">Must be at least 8 characters</p>
            </div>

            <!-- Confirm Password -->
            <div class="space-y-1.5">
              <label class="block text-sm font-medium text-slate-300">Confirm Password</label>
              <div class="relative group/input">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <ShieldCheck :size="18" class="text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
                </div>
                <input
                  v-model="confirmPassword"
                  :type="showPassword ? 'text' : 'password'"
                  required
                  minlength="8"
                  placeholder="••••••••"
                  class="w-full bg-slate-900/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl pl-11 pr-4 py-3.5 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
                  :disabled="loading"
                />
              </div>
            </div>

            <!-- Error Message -->
            <div v-if="error" class="p-4 bg-rose-500/10 border border-rose-500/20 rounded-xl flex items-start gap-3 animate-shake">
              <AlertCircle :size="20" class="text-rose-400 shrink-0 mt-0.5" />
              <p class="text-sm text-rose-300 font-medium">{{ error }}</p>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="loading"
              class="relative group/btn w-full mt-2"
            >
              <div class="absolute -inset-0.5 bg-gradient-to-r from-teal-500 to-cyan-500 rounded-xl blur opacity-50 group-hover/btn:opacity-100 transition duration-300 disabled:opacity-0"></div>
              <div class="relative w-full flex items-center justify-center gap-2 px-4 py-3.5 bg-slate-900 text-white font-bold rounded-xl border border-white/10 transition-all duration-300 disabled:opacity-80">
                <Loader2 v-if="loading" :size="20" class="animate-spin text-teal-400" />
                <span v-else>Reset Password</span>
              </div>
            </button>

          </form>
        </div>

      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import { apiFetch } from "../utils/api"
import {
  Sparkles,
  Lock,
  Eye,
  EyeOff,
  AlertCircle,
  CheckCircle2,
  Loader2,
  ShieldCheck
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

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 0.4s ease-out forwards;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-4px); }
  20%, 40%, 60%, 80% { transform: translateX(4px); }
}

.animate-shake {
  animation: shake 0.4s ease-in-out;
}
</style>