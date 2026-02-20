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

        <!-- Success State -->
        <div v-if="emailSent" class="text-center animate-fade-in">
          <div class="w-16 h-16 bg-emerald-500/10 border border-emerald-500/20 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-inner">
            <Mail :size="32" class="text-emerald-400 drop-shadow-[0_0_8px_rgba(16,185,129,0.5)]" />
          </div>
          <h3 class="text-2xl font-bold text-white mb-3 tracking-tight">Check your inbox</h3>
          <p class="text-slate-400 mb-6 leading-relaxed">
            We've sent password reset instructions to:<br>
            <strong class="text-white font-semibold mt-1 inline-block">{{ email }}</strong>
          </p>
          <div class="p-4 bg-white/5 border border-white/10 rounded-xl mb-8">
            <p class="text-sm text-slate-400">
              Didn't receive it? Check your spam folder or
              <button @click="resetForm" class="text-teal-400 font-semibold hover:text-teal-300 transition-colors">try again</button>.
            </p>
          </div>
          <RouterLink
            to="/login"
            class="inline-flex items-center gap-2 text-slate-300 font-medium hover:text-white transition-colors"
          >
            <ArrowLeft :size="18" />
            Back to sign in
          </RouterLink>
        </div>

        <!-- Form State -->
        <div v-else class="animate-fade-in">
          
          <!-- Header -->
          <div class="text-center mb-8">
            <div class="w-16 h-16 bg-teal-500/10 border border-teal-500/20 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-[0_0_15px_rgba(45,212,191,0.15)]">
              <KeyRound :size="32" class="text-teal-400" />
            </div>
            <h1 class="text-2xl font-bold text-white mb-2 tracking-tight">Forgot Password?</h1>
            <p class="text-slate-400 text-sm">No worries. We'll send you reset instructions.</p>
          </div>

          <!-- Error Message -->
          <div v-if="error" class="mb-6 p-4 bg-rose-500/10 border border-rose-500/20 rounded-xl flex items-start gap-3 animate-shake">
            <AlertCircle :size="20" class="text-rose-400 shrink-0 mt-0.5" />
            <p class="text-sm text-rose-300 font-medium">{{ error }}</p>
          </div>

          <form @submit.prevent="handleSubmit" class="space-y-5">
            
            <!-- Email Input -->
            <div class="space-y-1.5">
              <label class="block text-sm font-medium text-slate-300">Email Address</label>
              <div class="relative group/input">
                <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                  <Mail :size="18" class="text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
                </div>
                <input
                  v-model="email"
                  type="email"
                  required
                  placeholder="you@example.com"
                  class="w-full bg-slate-900/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl pl-11 pr-4 py-3.5 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
                  :disabled="loading"
                />
              </div>
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
                <span v-else>Send Reset Link</span>
              </div>
            </button>

            <!-- Back to Login -->
            <div class="mt-6 text-center pt-4">
              <RouterLink
                to="/login"
                class="inline-flex items-center gap-2 text-slate-400 hover:text-white font-medium transition-colors group"
              >
                <ArrowLeft :size="16" class="group-hover:-translate-x-1 transition-transform" />
                Back to sign in
              </RouterLink>
            </div>

          </form>
        </div>

      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue"
import { apiFetch } from "../utils/api"
import {
  Sparkles,
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

<style scoped>
@keyframes fade-in {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
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