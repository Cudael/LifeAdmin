<template>
  <!-- SIDEBAR (Fixed left, dark theme) -->
  <aside
    class="hidden lg:flex fixed top-0 left-0 h-screen w-64 bg-gray-900 flex-col border-r border-gray-800 z-50"
  >
    
    <!-- LOGO + BRAND -->
    <div class="p-6 border-b border-gray-800">
      <RouterLink to="/dashboard" class="flex items-center gap-3 group">
        <div class="w-9 h-9 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-xl flex items-center justify-center shadow-lg group-hover:shadow-xl transition-all duration-300 group-hover:scale-110">
          <Sparkles :size="18" class="text-white" />
        </div>
        <span class="text-xl font-bold text-white">
          Remindes
        </span>
      </RouterLink>
    </div>

    <!-- SEARCH HINT -->
    <div class="px-4 pt-4 pb-2">
      <button
        class="w-full px-4 py-2.5 bg-gray-800 hover:bg-gray-700 rounded-lg flex items-center justify-between text-gray-400 hover:text-gray-300 transition-colors duration-200 group"
      >
        <div class="flex items-center gap-2">
          <Search :size="16" />
          <span class="text-sm">Search</span>
        </div>
        <kbd class="px-2 py-1 text-xs bg-gray-700 group-hover:bg-gray-600 rounded border border-gray-600 text-gray-400">⌘F</kbd>
      </button>
    </div>

    <!-- QUICK ADD BUTTON -->
    <div class="px-4 pt-2 pb-4">
      <RouterLink
        to="/add-item"
        class="w-full px-4 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 hover:from-teal-600 hover:to-cyan-600 text-white rounded-lg flex items-center justify-center gap-2 font-semibold shadow-lg hover:shadow-xl transition-all duration-300 group"
      >
        <Plus :size="18" class="group-hover:rotate-90 transition-transform duration-300" />
        <span>Add Item</span>
      </RouterLink>
    </div>

    <!-- NAVIGATION SECTIONS -->
    <nav class="flex-1 px-4 py-2 overflow-y-auto">
      
      <!-- GENERAL SECTION -->
      <div class="mb-6">
        <p class="px-3 mb-2 text-xs font-semibold uppercase tracking-widest text-gray-500">
          General
        </p>
        <div class="space-y-1">
          <RouterLink
            to="/dashboard"
            class="nav-item"
            :class="{ 'nav-item-active': $route.path === '/dashboard' }"
          >
            <LayoutDashboard :size="18" />
            <span>Overview</span>
          </RouterLink>

          <RouterLink
            to="/items"
            class="nav-item"
            :class="{ 'nav-item-active': $route.path.startsWith('/items') }"
          >
            <Package :size="18" />
            <span>Items</span>
          </RouterLink>

          <RouterLink
            to="/calendar"
            class="nav-item"
            :class="{ 'nav-item-active': $route.path === '/calendar' }"
          >
            <Calendar :size="18" />
            <span>Calendar</span>
          </RouterLink>
        </div>
      </div>

      <!-- ACCOUNT SECTION -->
      <div>
        <p class="px-3 mb-2 text-xs font-semibold uppercase tracking-widest text-gray-500">
          Account
        </p>
        <div class="space-y-1">
          <RouterLink
            to="/profile"
            class="nav-item"
            :class="{ 'nav-item-active': $route.path === '/profile' }"
          >
            <User :size="18" />
            <span>Profile</span>
          </RouterLink>

          <RouterLink
            to="/settings"
            class="nav-item"
            :class="{ 'nav-item-active': $route.path === '/settings' }"
          >
            <Settings :size="18" />
            <span>Settings</span>
          </RouterLink>

          <RouterLink
            to="/subscription"
            class="nav-item"
            :class="{ 'nav-item-active': $route.path === '/subscription' }"
          >
            <CreditCard :size="18" />
            <span>Subscription</span>
            <span
              v-if="isPremium"
              class="ml-auto px-2 py-0.5 text-xs font-semibold bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-full"
            >
              Premium
            </span>
            <span
              v-else
              class="ml-auto px-2 py-0.5 text-xs font-semibold bg-gray-700 text-gray-400 rounded-full"
            >
              Free
            </span>
          </RouterLink>
        </div>
      </div>

    </nav>

    <!-- USER SECTION AT BOTTOM -->
    <div class="p-4 border-t border-gray-800">
      <div class="flex items-center gap-3">
        <!-- User Avatar -->
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
            <span class="font-bold text-white text-sm">
              {{ initials }}
            </span>
          </div>
        </div>

        <!-- User Info -->
        <div class="flex-1 min-w-0">
          <p class="text-sm font-semibold text-white truncate">{{ userName }}</p>
          <p class="text-xs text-gray-400 truncate">{{ userEmail }}</p>
        </div>

        <!-- Logout Button -->
        <button
          @click="logout"
          class="w-8 h-8 rounded-lg bg-gray-800 hover:bg-red-600 flex items-center justify-center text-gray-400 hover:text-white transition-colors duration-200"
          title="Logout"
        >
          <LogOut :size="16" />
        </button>
      </div>
    </div>

    <!-- NOTIFICATION BELL (optional - placed at bottom if needed) -->
    <!-- Uncomment if you want the bell in the sidebar instead of content area
    <div class="px-4 pb-4">
      <button
        class="w-full px-4 py-2 bg-gray-800 hover:bg-gray-700 rounded-lg flex items-center justify-center gap-2 text-gray-400 hover:text-gray-300 transition-colors duration-200 relative"
      >
        <Bell :size="18" />
        <span class="text-sm">Notifications</span>
        <span v-if="unreadCount > 0" class="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
      </button>
    </div>
    -->

  </aside>
</template>

<script setup>
import { computed } from "vue"
import { useRouter } from "vue-router"
import { useAuthStore } from "../../stores/auth"
import { clearTokens } from "../../utils/auth"
import {
  Sparkles,
  Search,
  Plus,
  LayoutDashboard,
  Package,
  Calendar,
  User,
  Settings,
  CreditCard,
  LogOut,
  Bell
} from "lucide-vue-next"

const router = useRouter()
const authStore = useAuthStore()

// Computed values from auth store
const userName = computed(() => {
  const u = authStore.user
  return u?.full_name || u?.username || u?.name || "User"
})

const userEmail = computed(() => authStore.user?.email || "")
const userAvatar = computed(() => authStore.user?.profile_picture || null)
const isPremium = computed(() => authStore.isPremium)

// User initials for avatar fallback
const initials = computed(() => {
  const names = userName.value.split(" ")
  if (names.length >= 2) {
    return (names[0][0] + names[names.length - 1][0]).toUpperCase()
  }
  return userName.value.charAt(0).toUpperCase() + (userName.value.charAt(1) || '').toUpperCase()
})

// Logout function
function logout() {
  clearTokens()
  router.push("/login")
}
</script>

<style scoped>
.nav-item {
  @apply flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium text-gray-300 hover:text-white hover:bg-gray-800 transition-all duration-200;
}

.nav-item-active {
  @apply bg-teal-500/20 text-teal-400 border-l-2 border-teal-400 pl-[10px];
}

/* Custom scrollbar for nav */
nav::-webkit-scrollbar {
  width: 6px;
}

nav::-webkit-scrollbar-track {
  background: transparent;
}

nav::-webkit-scrollbar-thumb {
  background: #374151;
  border-radius: 3px;
}

nav::-webkit-scrollbar-thumb:hover {
  background: #4b5563;
}
</style>
