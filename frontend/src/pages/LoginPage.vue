<script setup>
import { ref, onMounted } from "vue"
import { useRouter, useRoute } from "vue-router"
import { apiFetch, BASE_URL } from "../utils/api"
import { setTokens } from "../utils/auth"
import { 
  Sparkles, 
  AlertCircle, 
  ArrowRight, 
  ShieldCheck, 
  Mail, 
  Lock 
} from "lucide-vue-next"

const router = useRouter()
const route = useRoute()

const email = ref("")
const password = ref("")
const rememberMe = ref(false)
const loading = ref(false)
const errorMessage = ref("")

onMounted(() => {
  if (route.query.error === 'oauth_failed') {
    errorMessage.value = 'Google sign-in failed. Please try again.'
  }
})

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

    setTimeout(() => {
      router.push("/dashboard")
    }, 300)

  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong. Please try again."
    loading.value = false
  }
}

function signInWithGoogle() {
  loading.value = true
  errorMessage.value = ""
  window.location.href = `${BASE_URL}/auth/google`
}
</script>

<template>
  <main class="min-h-screen flex bg-slate-950 text-slate-300 font-sans selection:bg-teal-500/30 selection:text-teal-200">
    
    <!-- LEFT PANE: Form Area -->
    <div class="w-full lg:w-[45%] flex flex-col justify-center px-8 sm:px-12 md:px-16 lg:px-24 relative z-10">
      
      <!-- Logo -->
      <RouterLink to="/" class="absolute top-8 left-8 sm:left-12 flex items-center gap-3 group">
        <div class="w-8 h-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-lg flex items-center justify-center shadow-[0_0_15px_rgba(45,212,191,0.2)] group-hover:scale-105 transition-transform">
          <Sparkles :size="16" class="text-slate-950" />
        </div>
        <span class="text-xl font-extrabold text-white tracking-tight">
          Life<span class="text-slate-500">Admin</span>
        </span>
      </RouterLink>

      <div class="w-full max-w-sm mx-auto mt-16 lg:mt-0">
        <h1 class="text-3xl font-extrabold text-white tracking-tight mb-2">Welcome back</h1>
        <p class="text-slate-400 mb-8">Sign in to your account to continue</p>

        <!-- Error Alert -->
        <div v-if="errorMessage" class="mb-6 p-4 bg-rose-500/10 border border-rose-500/20 rounded-xl flex items-start gap-3 animate-fade-in">
          <AlertCircle :size="20" class="text-rose-400 shrink-0 mt-0.5" />
          <p class="text-sm text-rose-300 font-medium">{{ errorMessage }}</p>
        </div>

        <!-- Google OAuth Button -->
        <button 
          @click="signInWithGoogle"
          :disabled="loading"
          class="w-full flex items-center justify-center gap-3 px-4 py-3.5 bg-white/5 border border-white/10 hover:bg-white/10 hover:border-white/20 text-white font-semibold rounded-xl transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
            <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
            <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
            <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 15.01 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
          </svg>
          Continue with Google
        </button>

        <!-- Divider -->
        <div class="flex items-center gap-4 my-8">
          <div class="h-px bg-white/10 flex-1"></div>
          <span class="text-sm text-slate-500 font-medium uppercase tracking-wider">Or email</span>
          <div class="h-px bg-white/10 flex-1"></div>
        </div>

        <!-- Form -->
        <form @submit.prevent="handleLogin" class="space-y-5">
          
          <!-- Email Input -->
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
                placeholder="you@example.com"
                class="w-full bg-slate-900/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl pl-11 pr-4 py-3.5 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
              />
            </div>
          </div>

          <!-- Password Input -->
          <div class="space-y-1.5">
            <div class="flex items-center justify-between">
              <label class="text-sm font-medium text-slate-300">Password</label>
              <RouterLink to="/forgot-password" class="text-xs text-teal-400 hover:text-teal-300 font-medium transition-colors">
                Forgot password?
              </RouterLink>
            </div>
            <div class="relative group/input">
              <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <Lock :size="18" class="text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
              </div>
              <input 
                v-model="password" 
                type="password" 
                required
                placeholder="••••••••"
                class="w-full bg-slate-900/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl pl-11 pr-4 py-3.5 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
              />
            </div>
          </div>

          <!-- Remember Me -->
          <div class="flex items-center gap-3 pt-2">
            <input 
              v-model="rememberMe"
              id="remember" 
              type="checkbox" 
              class="w-4 h-4 rounded border-white/20 bg-slate-900 accent-teal-500 cursor-pointer focus:ring-teal-500/50 focus:ring-offset-slate-950"
            />
            <label for="remember" class="text-sm text-slate-400 cursor-pointer select-none">
              Remember me for 30 days
            </label>
          </div>

          <!-- Submit Button -->
          <button 
            type="submit" 
            :disabled="loading"
            class="relative group/btn w-full mt-4"
          >
            <div class="absolute -inset-0.5 bg-gradient-to-r from-teal-500 to-cyan-500 rounded-xl blur opacity-50 group-hover/btn:opacity-100 transition duration-300 disabled:opacity-0"></div>
            <div class="relative w-full flex items-center justify-center gap-2 px-4 py-3.5 bg-slate-900 text-white font-bold rounded-xl border border-white/10 transition-all duration-300">
              <span v-if="loading" class="flex items-center gap-2">
                <svg class="animate-spin h-5 w-5 text-teal-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                Signing in...
              </span>
              <span v-else class="flex items-center gap-2">
                Sign In
                <ArrowRight :size="18" class="text-teal-400 group-hover/btn:translate-x-1 transition-transform" />
              </span>
            </div>
          </button>

        </form>

        <p class="text-center text-sm text-slate-500 mt-10">
          Don't have an account?
          <RouterLink to="/register" class="text-teal-400 hover:text-teal-300 font-bold transition-colors ml-1">
            Create an account
          </RouterLink>
        </p>

      </div>
    </div>

    <!-- RIGHT PANE: Visual Showcase (Hidden on Mobile) -->
    <div class="hidden lg:flex flex-1 relative bg-slate-900 border-l border-white/5 overflow-hidden items-center justify-center p-12">
      
      <!-- Decorative Background Grid -->
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:32px_32px] [mask-image:radial-gradient(ellipse_80%_80%_at_50%_50%,#000_40%,transparent_100%)] pointer-events-none"></div>
      
      <!-- Glowing Orbs -->
      <div class="absolute top-1/4 right-1/4 w-96 h-96 bg-teal-500/20 blur-[120px] rounded-full pointer-events-none mix-blend-screen animate-pulse-slow"></div>
      <div class="absolute bottom-1/4 left-1/4 w-96 h-96 bg-blue-500/20 blur-[120px] rounded-full pointer-events-none mix-blend-screen animate-pulse-slower"></div>

      <!-- Floating Glass Card (Testimonial/Feature) -->
      <div class="relative z-10 w-full max-w-lg bg-slate-900/40 backdrop-blur-xl border border-white/10 rounded-3xl p-10 shadow-[0_0_50px_rgba(0,0,0,0.3)]">
        <div class="w-14 h-14 bg-emerald-500/10 border border-emerald-500/20 rounded-2xl flex items-center justify-center mb-8 shadow-inner">
          <ShieldCheck :size="28" class="text-emerald-400 drop-shadow-[0_0_8px_rgba(16,185,129,0.5)]" />
        </div>
        
        <h3 class="text-3xl font-bold text-white mb-4 tracking-tight leading-snug">
          "LifeAdmin completely eliminated the mental load of keeping track of my documents."
        </h3>
        
        <div class="flex items-center gap-4 mt-8 pt-8 border-t border-white/10">
          <div class="w-10 h-10 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 p-[2px]">
            <div class="w-full h-full bg-slate-900 rounded-full flex items-center justify-center">
              <span class="text-xs font-bold text-white">MW</span>
            </div>
          </div>
          <div>
            <p class="text-white font-bold text-sm">Marcus W.</p>
            <p class="text-slate-500 text-xs font-medium uppercase tracking-wider">Premium Member</p>
          </div>
        </div>
      </div>

    </div>

  </main>
</template>

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
</style>