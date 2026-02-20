<template>
  <!-- SIDEBAR (Fixed left, Deep Slate Theme) -->
  <aside
    class="hidden lg:flex fixed top-0 left-0 h-screen w-64 bg-slate-950 flex-col border-r border-white/5 z-50 selection:bg-teal-500/30 selection:text-teal-200"
  >
    <!-- Ambient top glow -->
    <div class="absolute top-0 left-0 w-full h-32 bg-teal-500/5 blur-[50px] pointer-events-none"></div>

    <!-- LOGO + BRAND -->
    <div class="px-6 py-6 relative z-10">
      <RouterLink to="/dashboard" class="flex items-center gap-3 group w-max">
        <div class="w-8 h-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-lg flex items-center justify-center shadow-[0_0_15px_rgba(45,212,191,0.2)] group-hover:scale-105 transition-transform duration-300">
          <Sparkles :size="16" class="text-slate-950" />
        </div>
        <span class="text-xl font-extrabold text-white tracking-tight">
          Life<span class="text-slate-500">Admin</span>
        </span>
      </RouterLink>
    </div>

    <!-- SEARCH / COMMAND PALETTE HINT -->
    <div class="px-4 mb-4 relative z-10">
      <button
        class="w-full h-10 bg-slate-900/50 hover:bg-slate-900 border border-white/5 hover:border-white/10 rounded-xl flex items-center justify-between px-3 text-slate-500 hover:text-slate-300 transition-all duration-200 group shadow-inner"
      >
        <div class="flex items-center gap-2.5">
          <Search :size="14" class="group-hover:text-teal-400 transition-colors" />
          <span class="text-sm font-medium">Search vault...</span>
        </div>
        <div class="flex items-center gap-1">
          <kbd class="px-1.5 py-0.5 text-[10px] font-sans font-bold bg-slate-800 rounded text-slate-400 group-hover:text-slate-300">⌘</kbd>
          <kbd class="px-1.5 py-0.5 text-[10px] font-sans font-bold bg-slate-800 rounded text-slate-400 group-hover:text-slate-300">K</kbd>
        </div>
      </button>
    </div>

    <!-- QUICK ADD BUTTON -->
    <div class="px-4 mb-6 relative z-10">
      <RouterLink
        to="/add-item"
        class="group relative w-full h-10 bg-slate-50 hover:bg-white text-slate-950 rounded-xl flex items-center justify-center gap-2 font-bold shadow-[0_0_15px_rgba(255,255,255,0.1)] hover:shadow-[0_0_20px_rgba(255,255,255,0.2)] transition-all duration-300"
      >
        <Plus :size="16" class="text-teal-600 group-hover:scale-110 transition-transform" />
        <span>New Item</span>
      </RouterLink>
    </div>

    <!-- NAVIGATION SECTIONS -->
    <nav class="flex-1 px-3 overflow-y-auto custom-scrollbar relative z-10 space-y-6 pb-4">
      
      <!-- VAULT SECTION -->
      <div>
        <p class="px-3 mb-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
          Your Vault
        </p>
        <div class="space-y-1">
          <RouterLink
            to="/dashboard"
            class="nav-item group"
            :class="{ 'nav-item-active': $route.path === '/dashboard' }"
          >
            <LayoutDashboard :size="18" class="nav-icon" />
            <span>Overview</span>
          </RouterLink>

          <RouterLink
            to="/items"
            class="nav-item group"
            :class="{ 'nav-item-active': $route.path.startsWith('/items') }"
          >
            <Package :size="18" class="nav-icon" />
            <span>All Items</span>
          </RouterLink>

          <RouterLink
            to="/calendar"
            class="nav-item group"
            :class="{ 'nav-item-active': $route.path === '/calendar' }"
          >
            <Calendar :size="18" class="nav-icon" />
            <span>Timeline</span>
          </RouterLink>
        </div>
      </div>

      <!-- PREFERENCES SECTION -->
      <div>
        <p class="px-3 mb-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
          Preferences
        </p>
        <div class="space-y-1">
          <RouterLink
            to="/profile"
            class="nav-item group"
            :class="{ 'nav-item-active': $route.path === '/profile' }"
          >
            <User :size="18" class="nav-icon" />
            <span>Profile</span>
          </RouterLink>

          <RouterLink
            to="/settings"
            class="nav-item group"
            :class="{ 'nav-item-active': $route.path === '/settings' }"
          >
            <Settings :size="18" class="nav-icon" />
            <span>Settings</span>
          </RouterLink>

          <RouterLink
            to="/subscription"
            class="nav-item group"
            :class="{ 'nav-item-active': $route.path === '/subscription' }"
          >
            <CreditCard :size="18" class="nav-icon" />
            <span>Billing</span>
            
            <!-- Premium/Free Badge -->
            <span
              v-if="isPremium"
              class="ml-auto px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider bg-gradient-to-r from-teal-500/20 to-cyan-500/20 text-teal-400 border border-teal-500/20 rounded-md"
            >
              Pro
            </span>
            <span
              v-else
              class="ml-auto px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider bg-slate-800 text-slate-400 rounded-md"
            >
              Free
            </span>
          </RouterLink>
        </div>
      </div>
    </nav>

    <!-- FLOATING USER PROFILE CARD -->
    <div class="p-4 relative z-10">
      <div class="bg-slate-900/80 border border-white/5 rounded-2xl p-2.5 flex items-center gap-3 hover:bg-slate-800/80 transition-colors duration-200 shadow-lg group">
        
        <!-- User Avatar -->
        <div class="w-9 h-9 rounded-xl overflow-hidden flex-shrink-0 border border-white/10 shadow-inner bg-slate-800">
          <img
            v-if="userAvatar"
            :src="userAvatar"
            :alt="userName"
            class="w-full h-full object-cover"
          />
          <div
            v-else
            class="w-full h-full bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center"
          >
            <span class="font-bold text-slate-950 text-xs shadow-sm">
              {{ initials }}
            </span>
          </div>
        </div>

        <!-- User Info -->
        <div class="flex-1 min-w-0 cursor-pointer">
          <p class="text-sm font-bold text-slate-200 truncate group-hover:text-white transition-colors">{{ userName }}</p>
          <p class="text-[10px] text-slate-500 truncate font-medium">{{ userEmail }}</p>
        </div>

        <!-- Logout Button -->
        <button
          @click="logout"
          class="w-8 h-8 rounded-lg flex items-center justify-center text-slate-500 hover:bg-rose-500/10 hover:text-rose-400 transition-colors duration-200"
          title="Sign out"
        >
          <LogOut :size="16" />
        </button>
      </div>
    </div>

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
/* Base Nav Item Styles */
.nav-item {
  @apply relative flex items-center gap-3 px-3 py-2 rounded-xl text-sm font-medium text-slate-400 hover:text-slate-200 hover:bg-white/5 transition-all duration-200;
}

/* Icon base styles to handle transition */
.nav-icon {
  @apply text-slate-500 group-hover:text-slate-300 transition-colors duration-200;
}

/* ACTIVE STATE STYLES */
/* This creates the beautiful glowing left-border marker and highlights the text/icon */
.nav-item-active {
  @apply text-white bg-teal-500/10 hover:bg-teal-500/10;
}

.nav-item-active .nav-icon {
  @apply text-teal-400 drop-shadow-[0_0_8px_rgba(45,212,191,0.5)];
}

/* The Glowing Left Pill Marker */
.nav-item-active::before {
  content: '';
  @apply absolute left-0 top-1/2 -translate-y-1/2 h-1/2 w-1 bg-teal-400 rounded-r-full shadow-[0_0_10px_rgba(45,212,191,1)];
}

/* Stealthy custom scrollbar for navigation */
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  @apply bg-slate-800 rounded-full;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  @apply bg-slate-700;
}
</style>