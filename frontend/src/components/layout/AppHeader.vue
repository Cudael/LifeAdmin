<template>
  <header
    :class="[
      'fixed top-0 left-0 w-full z-50 transition-all duration-500',
      scrolled 
        ? 'backdrop-blur-xl bg-slate-950/70 shadow-[0_10px_30px_rgba(0,0,0,0.3)] border-b border-white/5 py-3' 
        : 'bg-transparent border-b border-transparent py-5'
    ]"
  >
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex items-center justify-between">

        <!-- LOGO -->
        <RouterLink to="/" class="flex items-center gap-3 group">
          <div class="w-10 h-10 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-xl flex items-center justify-center shadow-[0_0_15px_rgba(45,212,191,0.3)] group-hover:shadow-[0_0_25px_rgba(45,212,191,0.5)] transition-all duration-300 group-hover:scale-105">
            <Sparkles :size="20" class="text-slate-950 drop-shadow-sm" />
          </div>
          <span class="text-xl font-extrabold text-white tracking-tight">
            Life<span class="text-slate-500">Admin</span>
          </span>
        </RouterLink>

        <!-- DESKTOP NAV -->
        <nav class="hidden md:flex items-center gap-8">

          <RouterLink 
            to="/" 
            class="nav-link group"
            :class="{ 'text-teal-400 font-semibold': $route.path === '/' }"
            @click="scrollToTop"
          >
            <span class="relative">
              Home
              <span class="absolute -bottom-1 left-0 h-[2px] bg-gradient-to-r from-teal-400 to-cyan-400 transition-all duration-300"
                    :class="$route.path === '/' ? 'w-full' : 'w-0 group-hover:w-full'"></span>
            </span>
          </RouterLink>

          <a 
            href="/#features" 
            class="nav-link group"
            @click="smoothScroll"
          >
            <span class="relative">
              Features
              <span class="absolute -bottom-1 left-0 w-0 h-[2px] bg-gradient-to-r from-teal-400 to-cyan-400 group-hover:w-full transition-all duration-300"></span>
            </span>
          </a>

          <a 
            href="/#pricing" 
            class="nav-link group"
            @click="smoothScroll"
          >
            <span class="relative">
              Pricing
              <span class="absolute -bottom-1 left-0 w-0 h-[2px] bg-gradient-to-r from-teal-400 to-cyan-400 group-hover:w-full transition-all duration-300"></span>
            </span>
          </a>

          <a 
            href="/#faq" 
            class="nav-link group"
            @click="smoothScroll"
          >
            <span class="relative">
              FAQ
              <span class="absolute -bottom-1 left-0 w-0 h-[2px] bg-gradient-to-r from-teal-400 to-cyan-400 group-hover:w-full transition-all duration-300"></span>
            </span>
          </a>

        </nav>

        <!-- DESKTOP AUTH BUTTONS -->
        <div class="hidden md:flex items-center gap-4">

          <!-- Logged OUT -->
          <template v-if="!isLoggedIn">
            <RouterLink
              to="/login"
              class="px-5 py-2.5 rounded-full text-slate-300 font-medium hover:text-white hover:bg-white/5 transition-all duration-200 flex items-center gap-2"
            >
              <LogIn :size="18" />
              Sign in
            </RouterLink>

            <RouterLink
              to="/register"
              class="group relative px-6 py-2.5 bg-slate-50 text-slate-950 rounded-full font-bold shadow-[0_0_15px_rgba(255,255,255,0.1)] hover:shadow-[0_0_25px_rgba(255,255,255,0.2)] hover:bg-white transition-all duration-300 flex items-center gap-2"
            >
              Get Started Free
              <ArrowRight :size="18" class="group-hover:translate-x-1 transition-transform text-teal-600" />
            </RouterLink>
          </template>

          <!-- Logged IN -->
          <template v-else>
            <RouterLink
              to="/dashboard"
              class="group px-6 py-2.5 bg-gradient-to-r from-teal-400 to-cyan-400 text-slate-950 rounded-full font-bold shadow-[0_0_15px_rgba(45,212,191,0.2)] hover:shadow-[0_0_25px_rgba(45,212,191,0.4)] hover:from-teal-300 hover:to-cyan-300 transition-all duration-300 flex items-center gap-2"
            >
              <LayoutDashboard :size="18" />
              Dashboard
              <ArrowRight :size="18" class="group-hover:translate-x-1 transition-transform" />
            </RouterLink>

            <button
              @click="logout"
              class="p-2.5 text-slate-400 hover:text-rose-400 hover:bg-rose-500/10 rounded-full transition-all duration-200"
              title="Logout"
            >
              <LogOut :size="20" />
            </button>
          </template>

        </div>

        <!-- MOBILE MENU BUTTON -->
        <button
          class="md:hidden p-2 rounded-xl text-slate-300 hover:text-white hover:bg-white/5 transition-colors"
          @click="mobileOpen = true"
        >
          <Menu :size="24" />
        </button>
      </div>
    </div>

    <!-- MOBILE OVERLAY -->
    <Transition
      enter-active-class="transition-opacity duration-300"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-opacity duration-200"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="mobileOpen"
        class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-40 md:hidden"
        @click="mobileOpen = false"
      ></div>
    </Transition>

    <!-- MOBILE DRAWER -->
    <Transition
      enter-active-class="transition-transform duration-300 ease-out"
      enter-from-class="translate-x-full"
      enter-to-class="translate-x-0"
      leave-active-class="transition-transform duration-200 ease-in"
      leave-from-class="translate-x-0"
      leave-to-class="translate-x-full"
    >
      <!-- Ensure the mobile drawer sits in the fixed viewport with a high z-index -->
      <div
        v-if="mobileOpen"
        class="fixed top-0 right-0 w-80 h-screen bg-slate-950 border-l border-white/10 shadow-[0_0_40px_rgba(0,0,0,0.5)] z-50 md:hidden overflow-y-auto flex flex-col"
      >
        <!-- Mobile Header -->
        <div class="flex items-center justify-between p-6 border-b border-white/5">
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-lg flex items-center justify-center shadow-md">
              <Sparkles :size="16" class="text-slate-950" />
            </div>
            <span class="text-lg font-extrabold text-white tracking-tight">
              Life<span class="text-slate-500">Admin</span>
            </span>
          </div>
          <button
            @click="mobileOpen = false"
            class="p-2 rounded-xl text-slate-400 hover:text-white hover:bg-white/5 transition-colors"
          >
            <X :size="24" />
          </button>
        </div>

        <!-- Mobile Navigation -->
        <nav class="p-6 space-y-2 flex-1">

          <RouterLink 
            to="/" 
            @click="closeMobile" 
            class="mobile-nav-link"
            :class="{ 'bg-teal-500/10 text-teal-400 font-semibold border-teal-500/20': $route.path === '/' }"
          >
            <Home :size="20" />
            Home
          </RouterLink>

          <a 
            href="/#features" 
            @click="smoothScrollMobile" 
            class="mobile-nav-link"
          >
            <Sparkles :size="20" />
            Features
          </a>

          <a 
            href="/#pricing" 
            @click="smoothScrollMobile" 
            class="mobile-nav-link"
          >
            <DollarSign :size="20" />
            Pricing
          </a>

          <a 
            href="/#faq" 
            @click="smoothScrollMobile" 
            class="mobile-nav-link"
          >
            <HelpCircle :size="20" />
            FAQ
          </a>

        </nav>

        <!-- Mobile Auth Section -->
        <div class="p-6 border-t border-white/5 space-y-3 pb-8">

          <!-- Logged OUT -->
          <template v-if="!isLoggedIn">
            <RouterLink
              to="/login"
              @click="closeMobile"
              class="flex items-center justify-center gap-2 w-full px-5 py-3.5 rounded-xl text-slate-300 font-medium bg-white/5 border border-white/10 hover:bg-white/10 hover:text-white transition-all duration-200"
            >
              <LogIn :size="20" />
              Sign in
            </RouterLink>

            <RouterLink
              to="/register"
              @click="closeMobile"
              class="flex items-center justify-center gap-2 w-full px-5 py-3.5 bg-slate-50 text-slate-950 rounded-xl font-bold shadow-[0_0_15px_rgba(255,255,255,0.1)] hover:bg-white transition-all duration-300"
            >
              Get Started Free
              <ArrowRight :size="20" class="text-teal-600" />
            </RouterLink>
          </template>

          <!-- Logged IN -->
          <template v-else>
            <!-- User Info Card -->
            <div class="p-4 bg-slate-900/50 rounded-xl border border-white/10 mb-4 flex items-center gap-4">
              <div class="w-12 h-12 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center text-slate-950 font-bold text-lg shadow-[0_0_15px_rgba(45,212,191,0.3)]">
                {{ userInitials }}
              </div>
              <div>
                <p class="font-bold text-slate-100">Welcome back!</p>
                <p class="text-sm text-slate-400">Access your vault</p>
              </div>
            </div>

            <RouterLink
              to="/dashboard"
              @click="closeMobile"
              class="flex items-center justify-center gap-2 w-full px-5 py-3.5 bg-gradient-to-r from-teal-400 to-cyan-400 text-slate-950 rounded-xl font-bold shadow-[0_0_15px_rgba(45,212,191,0.2)] transition-all duration-300"
            >
              <LayoutDashboard :size="20" />
              Open Dashboard
            </RouterLink>

            <button
              @click="logout"
              class="flex items-center justify-center gap-2 w-full px-5 py-3.5 text-rose-400 font-medium bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/20 rounded-xl transition-all duration-200"
            >
              <LogOut :size="20" />
              Sign Out
            </button>
          </template>

        </div>

      </div>
    </Transition>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue"
import { useRouter } from "vue-router"
import { accessToken, clearTokens } from "../../utils/auth"
import {
  Sparkles,
  Menu,
  X,
  Home,
  LogIn,
  LogOut,
  ArrowRight,
  LayoutDashboard,
  DollarSign,
  HelpCircle
} from "lucide-vue-next"

const router = useRouter()
const mobileOpen = ref(false)
const scrolled = ref(false)

// Reactive login state
const isLoggedIn = computed(() => !!accessToken.value)

// User initials (you can enhance this later with actual user data)
const userInitials = computed(() => {
  // You can fetch user name from store/API later
  return "U"
})

// Handle scroll effect
function handleScroll() {
  scrolled.value = window.scrollY > 20
}

// Smooth scroll for anchor links
function smoothScroll(event) {
  const href = event.currentTarget.getAttribute('href')
  if (href.startsWith('/#')) {
    event.preventDefault()
    const id = href.replace('/#', '')
    const element = document.getElementById(id)
    if (element) {
      const headerOffset = 80 // Account for fixed header
      const elementPosition = element.getBoundingClientRect().top
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset
      
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      })
    }
  }
}

function scrollToTop(event) {
  // Only scroll to top if already on landing page
  if (router.currentRoute.value.path === '/') {
    event.preventDefault()
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    })
  }
}

function logout() {
  clearTokens()
  mobileOpen.value = false
  router.push("/")
}

function closeMobile() {
  mobileOpen.value = false
}

function smoothScrollMobile(event) {
  closeMobile()
  setTimeout(() => {
    smoothScroll(event)
  }, 300) // Wait for mobile menu to close
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  handleScroll() // Check initial state
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.nav-link {
  @apply text-slate-300 font-medium hover:text-white transition-colors duration-200 cursor-pointer;
}

.mobile-nav-link {
  @apply flex items-center gap-3 w-full px-4 py-3.5 rounded-xl border border-transparent text-slate-300 font-medium hover:bg-white/5 hover:border-white/5 hover:text-white transition-all duration-200;
}
</style>