<template>
  <header
    :class="[
      'fixed top-0 left-0 w-full z-50 transition-all duration-300',
      scrolled 
        ? 'backdrop-blur-xl bg-white/90 shadow-lg border-b border-gray-200' 
        : 'backdrop-blur-md bg-white/70 border-b border-white/20'
    ]"
  >
    <div class="max-w-7xl mx-auto px-6 py-4">
      <div class="flex items-center justify-between">

        <!-- LOGO -->
        <RouterLink to="/" class="flex items-center gap-3 group">
          <div class="w-10 h-10 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-xl flex items-center justify-center shadow-md group-hover:shadow-lg transition-all duration-300 group-hover:scale-110">
            <Sparkles :size="20" class="text-white" />
          </div>
          <span class="text-xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
            Remindes
          </span>
        </RouterLink>

        <!-- DESKTOP NAV -->
        <nav class="hidden md:flex items-center gap-8">

          <RouterLink 
            to="/" 
            class="nav-link group"
            :class="{ 'text-teal-600 font-semibold': $route.path === '/' }"
            @click="scrollToTop"
          >
            <span class="relative">
              Home
              <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-teal-500 to-cyan-500 group-hover:w-full transition-all duration-300"></span>
            </span>
          </RouterLink>

          <a 
            href="/#features" 
            class="nav-link group"
            @click="smoothScroll"
          >
            <span class="relative">
              Features
              <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-teal-500 to-cyan-500 group-hover:w-full transition-all duration-300"></span>
            </span>
          </a>

          <a 
            href="/#pricing" 
            class="nav-link group"
            @click="smoothScroll"
          >
            <span class="relative">
              Pricing
              <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-teal-500 to-cyan-500 group-hover:w-full transition-all duration-300"></span>
            </span>
          </a>

          <a 
            href="/#faq" 
            class="nav-link group"
            @click="smoothScroll"
          >
            <span class="relative">
              FAQ
              <span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-gradient-to-r from-teal-500 to-cyan-500 group-hover:w-full transition-all duration-300"></span>
            </span>
          </a>

        </nav>

        <!-- DESKTOP AUTH BUTTONS -->
        <div class="hidden md:flex items-center gap-3">

          <!-- Logged OUT -->
          <template v-if="!isLoggedIn">
            <RouterLink
              to="/login"
              class="px-5 py-2.5 rounded-xl text-gray-700 font-medium hover:bg-gray-100 transition-all duration-200 flex items-center gap-2"
            >
              <LogIn :size="18" />
              Login
            </RouterLink>

            <RouterLink
              to="/register"
              class="group px-5 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 flex items-center gap-2"
            >
              Get Started
              <ArrowRight :size="18" class="group-hover:translate-x-1 transition-transform" />
            </RouterLink>
          </template>

          <!-- Logged IN -->
          <template v-else>
            <RouterLink
              to="/dashboard"
              class="group px-5 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 flex items-center gap-2"
            >
              <LayoutDashboard :size="18" />
              Dashboard
              <ArrowRight :size="18" class="group-hover:translate-x-1 transition-transform" />
            </RouterLink>

            <button
              @click="logout"
              class="px-5 py-2.5 text-gray-700 font-medium hover:bg-red-50 hover:text-red-600 rounded-xl transition-all duration-200 flex items-center gap-2"
            >
              <LogOut :size="18" />
              Logout
            </button>
          </template>

        </div>

        <!-- MOBILE MENU BUTTON -->
        <button
          class="md:hidden p-2 rounded-xl hover:bg-gray-100 transition-colors"
          @click="mobileOpen = true"
        >
          <Menu :size="24" class="text-gray-700" />
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
        class="fixed inset-0 bg-black/50 backdrop-blur-sm z-40 md:hidden"
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
      <div
        v-if="mobileOpen"
        class="fixed top-0 right-0 w-80 h-full bg-white shadow-2xl z-50 md:hidden overflow-y-auto"
      >
        <!-- Mobile Header -->
        <div class="flex items-center justify-between p-6 border-b border-gray-200">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-xl flex items-center justify-center shadow-md">
              <Sparkles :size="20" class="text-white" />
            </div>
            <span class="text-xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
              Remindes
            </span>
          </div>
          <button
            @click="mobileOpen = false"
            class="p-2 rounded-xl hover:bg-gray-100 transition-colors"
          >
            <X :size="24" class="text-gray-700" />
          </button>
        </div>

        <!-- Mobile Navigation -->
        <nav class="p-6 space-y-2">

          <RouterLink 
            to="/" 
            @click="closeMobile" 
            class="mobile-nav-link"
            :class="{ 'bg-teal-50 text-teal-600 font-semibold': $route.path === '/' }"
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
        <div class="p-6 border-t border-gray-200 space-y-3">

          <!-- Logged OUT -->
          <template v-if="!isLoggedIn">
            <RouterLink
              to="/login"
              @click="closeMobile"
              class="flex items-center justify-center gap-2 w-full px-5 py-3 rounded-xl text-gray-700 font-medium bg-gray-100 hover:bg-gray-200 transition-all duration-200"
            >
              <LogIn :size="20" />
              Login
            </RouterLink>

            <RouterLink
              to="/register"
              @click="closeMobile"
              class="flex items-center justify-center gap-2 w-full px-5 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl transition-all duration-300"
            >
              Get Started
              <ArrowRight :size="20" />
            </RouterLink>
          </template>

          <!-- Logged IN -->
          <template v-else>
            <!-- User Info Card -->
            <div class="p-4 bg-gradient-to-br from-teal-50 to-cyan-50 rounded-xl border border-teal-200 mb-4">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-br from-teal-500 to-cyan-500 flex items-center justify-center text-white font-bold text-lg shadow-md">
                  {{ userInitials }}
                </div>
                <div>
                  <p class="font-semibold text-gray-900">Welcome back!</p>
                  <p class="text-sm text-gray-600">Manage your items</p>
                </div>
              </div>
            </div>

            <RouterLink
              to="/dashboard"
              @click="closeMobile"
              class="flex items-center justify-center gap-2 w-full px-5 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl transition-all duration-300"
            >
              <LayoutDashboard :size="20" />
              Dashboard
            </RouterLink>

            <button
              @click="logout"
              class="flex items-center justify-center gap-2 w-full px-5 py-3 text-red-600 font-medium bg-red-50 hover:bg-red-100 rounded-xl transition-all duration-200"
            >
              <LogOut :size="20" />
              Logout
            </button>
          </template>

        </div>

        <!-- Mobile Footer -->
        <div class="p-6 border-t border-gray-200 text-center text-sm text-gray-500">
          <p>© 2026 Remindes</p>
          <p class="mt-1">All rights reserved</p>
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
  @apply text-gray-700 font-medium hover:text-teal-600 transition-colors duration-200 cursor-pointer;
}

.mobile-nav-link {
  @apply flex items-center gap-3 w-full px-4 py-3 rounded-xl text-gray-700 font-medium hover:bg-gray-100 transition-all duration-200;
}

/* Ensure header doesn't overlap content */
:deep(main) {
  @apply pt-20;
}
</style>