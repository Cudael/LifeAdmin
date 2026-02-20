<template>
  <div class="sticky top-0 z-40 h-16 bg-slate-950/80 backdrop-blur-xl border-b border-white/5 flex items-center justify-between px-8 transition-all duration-300">
    
    <!-- LEFT: Page Title & Breadcrumb -->
    <div class="flex items-center gap-3">
      <!-- Optional: Add a subtle logo or home icon here if you want it next to the title -->
      <h2 class="text-white font-bold text-lg tracking-tight">
        {{ pageTitle }}
      </h2>
    </div>

    <!-- RIGHT: Actions -->
    <div class="flex items-center gap-4">
      
      <!-- UPGRADE BUTTON (sleek pill) -->
      <button
        v-if="!isPremium"
        @click="handleUpgrade"
        class="hidden sm:flex items-center gap-2 px-3 py-1.5 bg-gradient-to-r from-teal-500/10 to-cyan-500/10 border border-teal-500/20 text-teal-400 text-xs font-bold uppercase tracking-wider rounded-full hover:bg-teal-500/20 transition-all duration-300"
      >
        <Sparkles :size="12" />
        <span>Upgrade</span>
      </button>

      <div class="h-6 w-px bg-white/10 hidden sm:block"></div>

      <!-- NOTIFICATION BELL -->
      <div class="relative" ref="notificationsRef">
        <button
          @click="handleNotifications"
          class="relative w-9 h-9 rounded-xl flex items-center justify-center text-slate-400 hover:text-white hover:bg-white/5 transition-all duration-200"
          title="Notifications"
        >
          <Bell :size="18" />
          
          <!-- Pulsing Red Dot for Alerts -->
          <span
            v-if="hasNotifications"
            class="absolute top-1.5 right-2 w-2 h-2 bg-rose-500 rounded-full shadow-[0_0_10px_rgba(225,29,72,0.8)] animate-pulse"
          ></span>
        </button>

        <!-- NOTIFICATIONS DROPDOWN -->
        <Transition
          enter-active-class="transition-all duration-200 ease-out"
          enter-from-class="opacity-0 scale-95 -translate-y-2"
          enter-to-class="opacity-100 scale-100 translate-y-0"
          leave-active-class="transition-all duration-150 ease-in"
          leave-from-class="opacity-100 scale-100 translate-y-0"
          leave-to-class="opacity-0 scale-95 -translate-y-2"
        >
          <div
            v-if="notificationsOpen"
            class="absolute right-0 top-full mt-2 w-80 bg-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.5)] overflow-hidden z-[60]"
          >
            <!-- Header -->
            <div class="px-4 py-3 border-b border-white/5 bg-white/[0.02]">
              <p class="text-white font-bold text-sm">Action Required</p>
            </div>

            <!-- Notifications list -->
            <div class="overflow-y-auto max-h-80 custom-scrollbar">
              <div v-if="notificationItems.length === 0" class="px-4 py-10 text-center flex flex-col items-center">
                <div class="w-12 h-12 rounded-full bg-emerald-500/10 flex items-center justify-center mb-3 text-emerald-400">
                  <CheckCircle2 :size="24" />
                </div>
                <p class="text-slate-300 font-bold text-sm mb-1">Vault Secure</p>
                <p class="text-slate-500 text-xs font-medium">No expiring items to review.</p>
              </div>

              <div v-else>
                <RouterLink
                  v-for="item in notificationItems"
                  :key="item.id"
                  :to="`/items/${item.id}`"
                  @click="closeNotifications"
                  class="flex items-start gap-3 px-4 py-3 hover:bg-white/5 transition-colors border-b border-white/5 last:border-b-0 group"
                >
                  <div class="flex-1 min-w-0">
                    <p class="text-slate-200 font-bold text-sm truncate group-hover:text-white transition-colors">{{ item.name }}</p>
                    <p class="text-slate-500 text-xs mt-1 font-medium">
                      Expires {{ formatExpiryDate(item.expiration_date) }}
                    </p>
                  </div>
                  <span
                    class="px-2 py-1 rounded text-[10px] font-bold uppercase tracking-widest whitespace-nowrap border"
                    :class="getUrgencyClasses(item.urgency)"
                  >
                    {{ item.urgencyLabel }}
                  </span>
                </RouterLink>
              </div>
            </div>
          </div>
        </Transition>
      </div>

      <!-- USER PROFILE DROPDOWN -->
      <div class="relative" ref="dropdownRef">
        <!-- Avatar Button -->
        <button
          @click.stop="toggleDropdown"
          class="flex items-center gap-2 w-9 h-9 rounded-xl overflow-hidden border border-white/10 hover:border-teal-500/50 transition-colors shadow-inner group"
        >
          <img
            v-if="userAvatar"
            :src="userAvatar"
            :alt="userName"
            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
          />
          <div
            v-else
            class="w-full h-full bg-slate-800 flex items-center justify-center group-hover:bg-slate-700 transition-colors"
          >
            <span class="font-bold text-slate-300 text-xs">{{ initials }}</span>
          </div>
        </button>

        <!-- DROPDOWN MENU -->
        <Transition
          enter-active-class="transition-all duration-200 ease-out"
          enter-from-class="opacity-0 scale-95 -translate-y-2"
          enter-to-class="opacity-100 scale-100 translate-y-0"
          leave-active-class="transition-all duration-150 ease-in"
          leave-from-class="opacity-100 scale-100 translate-y-0"
          leave-to-class="opacity-0 scale-95 -translate-y-2"
        >
          <div
            v-if="dropdownOpen"
            class="absolute right-0 top-full mt-3 w-56 bg-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.5)] p-1.5 z-[60]"
          >
            <!-- Header: User Info -->
            <div class="px-3 py-3 border-b border-white/5 mb-1.5 flex flex-col items-center text-center">
              <div class="w-12 h-12 rounded-full overflow-hidden border border-white/10 mb-2">
                <img v-if="userAvatar" :src="userAvatar" class="w-full h-full object-cover" />
                <div v-else class="w-full h-full bg-slate-800 flex items-center justify-center">
                  <span class="font-bold text-white text-sm">{{ initials }}</span>
                </div>
              </div>
              <p class="text-white font-bold text-sm truncate w-full">{{ userName }}</p>
              <p class="text-slate-500 text-[10px] font-medium uppercase tracking-wider truncate w-full">{{ userEmail }}</p>
            </div>

            <!-- Menu Items -->
            <RouterLink to="/profile" @click="closeDropdown" class="dropdown-item group">
              <User :size="16" class="text-slate-500 group-hover:text-teal-400 transition-colors" />
              <span>Profile Settings</span>
            </RouterLink>

            <RouterLink to="/settings" @click="closeDropdown" class="dropdown-item group">
              <Settings :size="16" class="text-slate-500 group-hover:text-teal-400 transition-colors" />
              <span>App Preferences</span>
            </RouterLink>

            <div class="h-px bg-white/5 my-1.5"></div>

            <button @click="handleLogout" class="dropdown-item group text-rose-400 hover:bg-rose-500/10">
              <LogOut :size="16" class="text-rose-500/70 group-hover:text-rose-400 transition-colors" />
              <span>Secure Sign Out</span>
            </button>
          </div>
        </Transition>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue"
import { useRouter } from "vue-router"
import { Bell, User, Settings, LogOut, Sparkles, CheckCircle2 } from "lucide-vue-next"
import { useAuthStore } from "../../stores/auth"
import { useItemsStore } from "../../stores/items"
import { clearTokens } from "../../utils/auth"

const props = defineProps({
  pageTitle: { type: String, default: "Dashboard" }
})

const router = useRouter()
const authStore = useAuthStore()
const itemsStore = useItemsStore()

const dropdownOpen = ref(false)
const dropdownRef = ref(null)
const notificationsOpen = ref(false)
const notificationsRef = ref(null)

const userName = computed(() => {
  const u = authStore.user
  return u?.full_name || u?.username || u?.name || "User"
})
const userEmail = computed(() => authStore.user?.email || "")
const userAvatar = computed(() => authStore.user?.profile_picture || null)
const isPremium = computed(() => authStore.isPremium)

const initials = computed(() => {
  const names = userName.value.split(" ")
  if (names.length >= 2) {
    return (names[0][0] + names[names.length - 1][0]).toUpperCase()
  }
  return userName.value.charAt(0).toUpperCase() + (userName.value.charAt(1) || '').toUpperCase()
})

const hasNotifications = computed(() => {
  const now = new Date()
  const thirtyDaysFromNow = new Date(now.getTime() + 30 * 24 * 60 * 60 * 1000)
  return itemsStore.items.some(item => {
    if (!item.expiration_date) return false
    const expiryDate = new Date(item.expiration_date)
    return expiryDate <= thirtyDaysFromNow
  })
})

const notificationItems = computed(() => {
  const now = new Date()
  const thirtyDaysFromNow = new Date(now.getTime() + 30 * 24 * 60 * 60 * 1000)
  
  return itemsStore.items
    .filter(item => {
      if (!item.expiration_date) return false
      const expiryDate = new Date(item.expiration_date)
      return expiryDate <= thirtyDaysFromNow
    })
    .map(item => {
      const expiryDate = new Date(item.expiration_date)
      const daysUntil = Math.ceil((expiryDate - now) / (1000 * 60 * 60 * 24))
      let urgency = 'yellow'
      let urgencyLabel = 'Expiring soon'
      
      if (daysUntil < 0) {
        urgency = 'red'
        urgencyLabel = 'Expired'
      } else if (daysUntil === 0) {
        urgency = 'red'
        urgencyLabel = 'Expires today'
      } else if (daysUntil <= 7) {
        urgency = 'red'
        urgencyLabel = `${daysUntil} days`
      } else if (daysUntil <= 30) {
        urgency = 'orange'
        urgencyLabel = `${daysUntil} days`
      }
      return { ...item, daysUntil, urgency, urgencyLabel }
    })
    .sort((a, b) => a.daysUntil - b.daysUntil)
    .slice(0, 8)
})

function toggleDropdown() { dropdownOpen.value = !dropdownOpen.value }
function closeDropdown() { dropdownOpen.value = false }
function toggleNotifications() { notificationsOpen.value = !notificationsOpen.value }
function closeNotifications() { notificationsOpen.value = false }
function handleUpgrade() { router.push("/subscription") }
function handleNotifications() { toggleNotifications() }

function handleLogout() {
  clearTokens()
  closeDropdown()
  router.push("/login")
}

function handleClickOutside(event) {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) closeDropdown()
  if (notificationsRef.value && !notificationsRef.value.contains(event.target)) closeNotifications()
}

function formatExpiryDate(dateString) {
  return new Date(dateString).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}

function getUrgencyClasses(urgency) {
  if (urgency === 'red') {
    return 'bg-rose-500/10 text-rose-400 border-rose-500/20'
  } else if (urgency === 'orange') {
    return 'bg-orange-500/10 text-orange-400 border-orange-500/20'
  } else {
    return 'bg-amber-500/10 text-amber-400 border-amber-500/20'
  }
}

onMounted(() => document.addEventListener("click", handleClickOutside))
onUnmounted(() => document.removeEventListener("click", handleClickOutside))
</script>

<style scoped>
.dropdown-item {
  @apply flex items-center gap-3 w-full px-3 py-2.5 rounded-xl text-sm font-medium text-slate-300 hover:bg-white/5 hover:text-white transition-colors duration-150;
}
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  @apply bg-slate-800 rounded-full;
}
</style>