<template>
  <header
    :class="[
      'fixed top-0 left-0 w-full z-50 transition-all duration-500 border-b',
      scrolled 
        ? 'backdrop-blur-2xl bg-slate-950/60 shadow-2xl shadow-black/50 border-white/5 py-3' 
        : 'bg-transparent border-transparent py-6'
    ]"
  >
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex items-center justify-between">

        <!-- LOGO -->
        <RouterLink to="/" class="flex items-center gap-3 group">
          <div class="w-10 h-10 bg-gradient-to-br from-teal-400 to-cyan-500 rounded-xl flex items-center justify-center shadow-lg shadow-teal-500/20 group-hover:shadow-teal-500/40 transition-all duration-300 group-hover:scale-105 ring-1 ring-white/20 inset-0">
            <Sparkles :size="20" class="text-slate-950 drop-shadow-sm" />
          </div>
          <span class="text-xl font-extrabold text-white tracking-tight">
            Life<span class="text-slate-500">Admin</span>
          </span>
        </RouterLink>

        <!-- DESKTOP NAV -->
        <nav class="hidden md:flex items-center gap-1 bg-slate-900/50 p-1.5 rounded-full ring-1 ring-white/10 backdrop-blur-md">
          <RouterLink 
            to="/" 
            class="nav-link"
            :class="{ 'bg-white/10 text-white shadow-sm': $route.path === '/' }"
            @click="scrollToTop"
          >
            Home
          </RouterLink>

          <a href="/#features" class="nav-link" @click="smoothScroll">Features</a>
          <a href="/#pricing" class="nav-link" @click="smoothScroll">Pricing</a>
          <a href="/#faq" class="nav-link" @click="smoothScroll">FAQ</a>
        </nav>

        <!-- DESKTOP AUTH BUTTONS -->
        <div class="hidden md:flex items-center gap-4">
          <template v-if="!isLoggedIn">
            <RouterLink
              to="/login"
              class="px-5 py-2.5 text-sm font-semibold text-slate-300 hover:text-white transition-colors flex items-center gap-2"
            >
              Sign in
            </RouterLink>

            <RouterLink
              to="/register"
              class="group relative px-6 py-2.5 bg-white text-slate-950 rounded-full text-sm font-bold shadow-lg shadow-white/10 hover:shadow-white/20 hover:scale-[1.02] transition-all duration-300 flex items-center gap-2"
            >
              Get Started
              <ArrowRight :size="16" class="group-hover:translate-x-1 transition-transform text-slate-900" />
            </RouterLink>
          </template>

          <template v-else>
            <RouterLink
              to="/dashboard"
              class="group px-6 py-2.5 bg-gradient-to-r from-teal-400 to-cyan-400 text-slate-950 rounded-full text-sm font-bold shadow-lg shadow-teal-500/20 hover:shadow-teal-500/40 hover:scale-[1.02] transition-all duration-300 flex items-center gap-2"
            >
              <LayoutDashboard :size="16" />
              Dashboard
            </RouterLink>
            <button @click="logout" class="p-2.5 text-slate-400 hover:text-rose-400 bg-white/5 hover:bg-rose-500/10 rounded-full transition-all duration-200">
              <LogOut :size="18" />
            </button>
          </template>
        </div>

        <!-- MOBILE MENU BUTTON -->
        <button class="md:hidden p-2 rounded-full bg-white/5 ring-1 ring-white/10 text-slate-300 hover:text-white transition-colors" @click="mobileOpen = true">
          <Menu :size="20" />
        </button>
      </div>
    </div>

    <!-- Mobile Menu Overlay & Drawer (Simplified for brevity, uses same slick UI) -->
    <!-- (Retains your existing mobile logic, styled to match the new dark mode) -->
    <Transition enter-active-class="transition-opacity duration-300" enter-from-class="opacity-0" enter-to-class="opacity-100" leave-active-class="transition-opacity duration-200" leave-from-class="opacity-100" leave-to-class="opacity-0">
      <div v-if="mobileOpen" class="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-40 md:hidden" @click="mobileOpen = false"></div>
    </Transition>

    <Transition enter-active-class="transition-transform duration-300 ease-out" enter-from-class="translate-x-full" enter-to-class="translate-x-0" leave-active-class="transition-transform duration-200 ease-in" leave-from-class="translate-x-0" leave-to-class="translate-x-full">
      <div v-if="mobileOpen" class="fixed top-0 right-0 w-80 h-screen bg-slate-900 ring-1 ring-white/10 shadow-2xl z-50 md:hidden overflow-y-auto flex flex-col">
        <div class="flex items-center justify-between p-6 border-b border-white/5">
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 bg-gradient-to-br from-teal-400 to-cyan-500 rounded-lg flex items-center justify-center shadow-md">
              <Sparkles :size="16" class="text-slate-950" />
            </div>
            <span class="text-lg font-extrabold text-white tracking-tight">LifeAdmin</span>
          </div>
          <button @click="mobileOpen = false" class="p-2 rounded-full bg-white/5 text-slate-400 hover:text-white transition-colors">
            <X :size="20" />
          </button>
        </div>
        <nav class="p-6 space-y-2 flex-1">
          <RouterLink to="/" @click="closeMobile" class="mobile-nav-link" :class="{ 'bg-white/10 text-white': $route.path === '/' }"><Home :size="18" /> Home</RouterLink>
          <a href="/#features" @click="smoothScrollMobile" class="mobile-nav-link"><Sparkles :size="18" /> Features</a>
          <a href="/#pricing" @click="smoothScrollMobile" class="mobile-nav-link"><DollarSign :size="18" /> Pricing</a>
          <a href="/#faq" @click="smoothScrollMobile" class="mobile-nav-link"><HelpCircle :size="18" /> FAQ</a>
        </nav>
      </div>
    </Transition>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue"
import { useRouter } from "vue-router"
import { accessToken, clearTokens } from "../../utils/auth"
import { Sparkles, Menu, X, Home, LogIn, LogOut, ArrowRight, LayoutDashboard, DollarSign, HelpCircle } from "lucide-vue-next"

const router = useRouter()
const mobileOpen = ref(false)
const scrolled = ref(false)

const isLoggedIn = computed(() => !!accessToken.value)

function handleScroll() { scrolled.value = window.scrollY > 20 }
function smoothScroll(event) {
  const href = event.currentTarget.getAttribute('href')
  if (href.startsWith('/#')) {
    event.preventDefault()
    const id = href.replace('/#', '')
    const element = document.getElementById(id)
    if (element) {
      window.scrollTo({ top: element.getBoundingClientRect().top + window.pageYOffset - 80, behavior: 'smooth' })
    }
  }
}
function scrollToTop(event) {
  if (router.currentRoute.value.path === '/') {
    event.preventDefault(); window.scrollTo({ top: 0, behavior: 'smooth' })
  }
}
function logout() { clearTokens(); mobileOpen.value = false; router.push("/") }
function closeMobile() { mobileOpen.value = false }
function smoothScrollMobile(event) { closeMobile(); setTimeout(() => { smoothScroll(event) }, 300) }

onMounted(() => { window.addEventListener('scroll', handleScroll); handleScroll() })
onUnmounted(() => { window.removeEventListener('scroll', handleScroll) })
</script>

<style scoped>
.nav-link {
  @apply px-4 py-2 rounded-full text-sm font-medium text-slate-400 hover:text-white hover:bg-white/5 transition-all duration-200 cursor-pointer;
}
.mobile-nav-link {
  @apply flex items-center gap-3 w-full px-4 py-3 rounded-xl text-slate-300 text-sm font-medium hover:bg-white/5 hover:text-white transition-all duration-200;
}
</style>