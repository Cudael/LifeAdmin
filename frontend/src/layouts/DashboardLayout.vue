<script setup>
import { ref, onMounted, computed } from "vue"
import { useRouter, useRoute } from "vue-router"
import AppSidebar from "../components/layout/AppSidebar.vue"
import DashboardTopBar from "../components/layout/DashboardTopBar.vue"
import EmailVerificationBanner from "../components/EmailVerificationBanner.vue"
import { useAuthStore } from "../stores/auth"
import { clearTokens } from "../utils/auth"
import { error } from "../utils/logger"
import { Sparkles, Menu, X, Plus, LayoutDashboard, Package, Calendar, User, Settings, CreditCard, LogOut } from "lucide-vue-next"

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const props = defineProps({
  pageTitle: { type: String, default: "Dashboard" },
  pageSubtitle: { type: String, default: "" }
})

// UI State
const mobileMenuOpen = ref(false)

// Computed values from store
const userName = computed(() => {
  const u = authStore.user
  return u?.full_name || u?.username || u?.name || "User"
})
const userEmail = computed(() => authStore.user?.email || "")
const userAvatar = computed(() => authStore.user?.profile_picture || null)
const loading = ref(true)

// User initials for avatar fallback
const initials = computed(() => {
  const names = userName.value.split(" ")
  if (names.length >= 2) {
    return (names[0][0] + names[names.length - 1][0]).toUpperCase()
  }
  return userName.value.charAt(0).toUpperCase() + (userName.value.charAt(1) || '').toUpperCase()
})

// Check if it's the dashboard page
const isDashboard = computed(() => props.pageTitle === "Dashboard")

// Get current date formatted
const currentDate = computed(() => {
  const options = { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' }
  return new Date().toLocaleDateString('en-US', options)
})

// Get page subtitle based on route
const pageSubtitleComputed = computed(() => {
  // If prop is provided, use it
  if (props.pageSubtitle) {
    return props.pageSubtitle
  }
  
  // Otherwise, compute based on page title
  switch(props.pageTitle) {
    case "Dashboard": {
      // Time-aware greeting with first name
      const hour = new Date().getHours()
      const firstName = userName.value.split(' ')[0].trim()
      const displayName = firstName || userName.value || 'there'
      let greeting = 'Good morning'
      if (hour >= 12 && hour < 17) {
        greeting = 'Good afternoon'
      } else if (hour >= 17) {
        greeting = 'Good evening'
      }
      return `${greeting}, ${displayName}! Here's your overview`
    }
    case "Items":
      return "Manage all your documents and subscriptions"
    case "Calendar":
      return "View upcoming deadlines and expirations"
    case "Profile":
      return "Manage your personal information"
    case "Settings":
      return "Configure your preferences"
    case "Subscription":
      return "Manage your subscription plan"
    default:
      return ""
  }
})

// Logout function
function logout() {
  clearTokens()
  mobileMenuOpen.value = false
  router.push("/login")
}

// Fetch user profile on load
onMounted(async () => {
  try {
    await authStore.fetchUser()
    loading.value = false
  } catch (err) {
    error("Error fetching user:", err)
    loading.value = false
  }
})
</script>

<template>
  <!-- FLEX ROW LAYOUT: Sidebar + Main Content -->
  <div class="min-h-screen flex bg-gray-950">

    <!-- SIDEBAR (Fixed left, hidden on mobile) -->
    <AppSidebar />

    <!-- MOBILE HEADER (visible only on mobile) -->
    <header class="lg:hidden fixed top-0 left-0 right-0 h-16 bg-gray-900/90 backdrop-blur-xl shadow-sm z-50 border-b border-gray-800">
      <div class="px-4 h-full flex items-center justify-between">
        <!-- Logo -->
        <RouterLink to="/dashboard" class="flex items-center gap-2">
          <div class="w-8 h-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-lg flex items-center justify-center shadow-md">
            <Sparkles :size="16" class="text-white" />
          </div>
          <span class="text-lg font-bold text-white">
            Remindes
          </span>
        </RouterLink>

        <!-- Mobile menu button -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="w-10 h-10 rounded-lg bg-gray-800 flex items-center justify-center hover:bg-gray-700 transition-colors text-gray-300"
        >
          <Menu v-if="!mobileMenuOpen" :size="20" />
          <X v-else :size="20" />
        </button>
      </div>
    </header>

    <!-- MOBILE NAVIGATION DRAWER -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-x-full"
      enter-to-class="opacity-100 translate-x-0"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-x-0"
      leave-to-class="opacity-0 -translate-x-full"
    >
      <div
        v-if="mobileMenuOpen"
        class="lg:hidden fixed inset-0 z-50 bg-black/50"
        @click="mobileMenuOpen = false"
      >
        <aside
          @click.stop
          class="w-64 h-full bg-gray-900 flex flex-col border-r border-gray-800"
        >
          <!-- Mobile nav content (same as sidebar) -->
          <div class="p-6 border-b border-gray-800 flex items-center justify-between">
            <RouterLink to="/dashboard" class="flex items-center gap-3" @click="mobileMenuOpen = false">
              <div class="w-9 h-9 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-xl flex items-center justify-center shadow-lg">
                <Sparkles :size="18" class="text-white" />
              </div>
              <span class="text-xl font-bold text-white">Remindes</span>
            </RouterLink>
            <button @click="mobileMenuOpen = false" class="text-gray-400 hover:text-white">
              <X :size="20" />
            </button>
          </div>

          <!-- Quick Add Button -->
          <div class="px-4 pt-4 pb-2">
            <RouterLink
              to="/add-item"
              @click="mobileMenuOpen = false"
              class="w-full px-4 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 hover:from-teal-600 hover:to-cyan-600 text-white rounded-lg flex items-center justify-center gap-2 font-semibold shadow-lg hover:shadow-xl transition-all duration-300"
            >
              <Plus :size="18" />
              <span>Add Item</span>
            </RouterLink>
          </div>

          <!-- Mobile Navigation Links -->
          <nav class="flex-1 px-4 py-2 overflow-y-auto">
            <div class="mb-6">
              <p class="px-3 mb-2 text-xs font-semibold uppercase tracking-widest text-gray-500">General</p>
              <div class="space-y-1">
                <RouterLink
                  to="/dashboard"
                  @click="mobileMenuOpen = false"
                  class="nav-item"
                  :class="{ 'nav-item-active': $route.path === '/dashboard' }"
                >
                  <LayoutDashboard :size="18" />
                  <span>Overview</span>
                </RouterLink>
                <RouterLink
                  to="/items"
                  @click="mobileMenuOpen = false"
                  class="nav-item"
                  :class="{ 'nav-item-active': $route.path.startsWith('/items') }"
                >
                  <Package :size="18" />
                  <span>Items</span>
                </RouterLink>
                <RouterLink
                  to="/calendar"
                  @click="mobileMenuOpen = false"
                  class="nav-item"
                  :class="{ 'nav-item-active': $route.path === '/calendar' }"
                >
                  <Calendar :size="18" />
                  <span>Calendar</span>
                </RouterLink>
              </div>
            </div>

            <div>
              <p class="px-3 mb-2 text-xs font-semibold uppercase tracking-widest text-gray-500">Account</p>
              <div class="space-y-1">
                <RouterLink
                  to="/profile"
                  @click="mobileMenuOpen = false"
                  class="nav-item"
                  :class="{ 'nav-item-active': $route.path === '/profile' }"
                >
                  <User :size="18" />
                  <span>Profile</span>
                </RouterLink>
                <RouterLink
                  to="/settings"
                  @click="mobileMenuOpen = false"
                  class="nav-item"
                  :class="{ 'nav-item-active': $route.path === '/settings' }"
                >
                  <Settings :size="18" />
                  <span>Settings</span>
                </RouterLink>
                <RouterLink
                  to="/subscription"
                  @click="mobileMenuOpen = false"
                  class="nav-item"
                  :class="{ 'nav-item-active': $route.path === '/subscription' }"
                >
                  <CreditCard :size="18" />
                  <span>Subscription</span>
                </RouterLink>
              </div>
            </div>
          </nav>

          <!-- Mobile User Section -->
          <div class="p-4 border-t border-gray-800">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full overflow-hidden flex-shrink-0 ring-2 ring-gray-700">
                <img
                  v-if="userAvatar"
                  :src="userAvatar"
                  :alt="userName"
                  class="w-full h-full object-cover"
                />
                <div
                  v-else
                  class="w-full h-full bg-gradient-to-br from-teal-500 to-cyan-500 flex items-center justify-center"
                >
                  <span class="font-bold text-white text-sm">{{ initials }}</span>
                </div>
              </div>
              <div class="flex-1 min-w-0">
                <p class="text-sm font-semibold text-white truncate">{{ userName }}</p>
                <p class="text-xs text-gray-400 truncate">{{ userEmail }}</p>
              </div>
              <button
                @click="logout"
                class="w-8 h-8 rounded-lg bg-gray-800 hover:bg-red-600 flex items-center justify-center text-gray-400 hover:text-white transition-colors duration-200"
                title="Logout"
              >
                <LogOut :size="16" />
              </button>
            </div>
          </div>
        </aside>
      </div>
    </Transition>

    <!-- MAIN CONTENT AREA (with left margin for sidebar on desktop, top margin on mobile) -->
    <div class="flex-1 ml-0 lg:ml-64 pt-16 lg:pt-0 flex flex-col min-h-screen bg-gray-950">
      
      <!-- TOP BAR -->
      <DashboardTopBar :pageTitle="pageTitle" />
      
      <!-- EMAIL VERIFICATION BANNER -->
      <EmailVerificationBanner v-if="authStore.user && !loading" :user="authStore.user" />

      <!-- PAGE TITLE SECTION -->
      <div class="px-6 py-4 border-b border-gray-800 bg-gray-900">
        <div class="flex items-center justify-between">
          <div>
            <h1 class="text-2xl md:text-3xl font-bold text-white">{{ pageTitle }}</h1>
            <p v-if="pageSubtitleComputed" class="text-gray-400 mt-1">{{ pageSubtitleComputed }}</p>
          </div>
          <!-- Show current date on dashboard -->
          <div v-if="isDashboard" class="block">
            <p class="text-sm text-gray-400">{{ currentDate }}</p>
          </div>
        </div>
      </div>

      <!-- ACTION BUTTONS SLOT (for page-specific actions - optional) -->
      <div v-if="$slots.actions" class="px-6 py-4 bg-gray-950">
        <slot name="actions" />
      </div>

      <!-- MAIN CONTENT -->
      <main class="flex-1 p-4 md:p-6 lg:p-8 overflow-y-auto">
        <div class="max-w-7xl mx-auto">
          <div class="animate-fade-in">
            <slot />
          </div>
        </div>
      </main>
    </div>

  </div>
</template>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 0.4s ease-out;
}

/* Nav item styles (for mobile drawer) */
.nav-item {
  @apply flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium text-gray-300 hover:text-white hover:bg-gray-800 transition-all duration-200;
}

.nav-item-active {
  @apply bg-teal-500/20 text-teal-400 border-l-2 border-teal-400 pl-[10px];
}

/* Ensure smooth scrolling */
main {
  scroll-behavior: smooth;
}

/* Custom scrollbar */
main::-webkit-scrollbar {
  width: 8px;
}

main::-webkit-scrollbar-track {
  background: transparent;
}

main::-webkit-scrollbar-thumb {
  background: linear-gradient(to bottom, #14b8a6, #06b6d4);
  border-radius: 4px;
}

main::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(to bottom, #0d9488, #0891b2);
}

button:focus-visible,
a:focus-visible {
  outline: 2px solid #14b8a6;
  outline-offset: 2px;
  border-radius: 6px;
}
</style>