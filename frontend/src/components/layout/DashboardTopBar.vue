<template>
  <div class="sticky top-0 z-40 h-14 bg-gray-900 border-b border-gray-800 flex items-center justify-between px-6">
    
    <!-- LEFT: Page Title -->
    <div class="text-white font-semibold text-sm">
      {{ pageTitle }}
    </div>

    <!-- RIGHT: Actions (Upgrade + Bell + Profile) -->
    <div class="flex items-center gap-3">
      
      <!-- UPGRADE BUTTON (show only if NOT premium) -->
      <button
        v-if="!isPremium"
        @click="handleUpgrade"
        class="bg-gradient-to-r from-teal-500 to-cyan-500 text-white text-xs font-semibold px-3 py-1.5 rounded-full hover:from-teal-600 hover:to-cyan-600 transition-all flex items-center gap-1.5"
      >
        <span>⭐</span>
        <span>Upgrade</span>
      </button>

      <!-- NOTIFICATION BELL -->
      <div class="relative" ref="notificationsRef">
        <button
          @click="handleNotifications"
          class="relative text-gray-400 hover:text-white transition-colors"
          title="Notifications"
        >
          <Bell :size="18" />
          <!-- Red badge if there are expiring/expired items -->
          <span
            v-if="hasNotifications"
            class="absolute top-0.5 right-0.5 w-2 h-2 bg-red-500 rounded-full"
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
            class="absolute right-0 top-full mt-2 w-80 bg-gray-800 border border-gray-700 rounded-xl shadow-xl overflow-hidden max-h-96"
          >
            <!-- Header -->
            <div class="px-4 py-3 border-b border-gray-700">
              <p class="text-white font-semibold text-sm">Notifications</p>
            </div>

            <!-- Notifications list -->
            <div class="overflow-y-auto max-h-80">
              <div v-if="notificationItems.length === 0" class="px-4 py-8 text-center">
                <p class="text-gray-400 text-sm">All clear! 🎉</p>
              </div>
              <div v-else>
                <RouterLink
                  v-for="item in notificationItems"
                  :key="item.id"
                  :to="`/items/${item.id}`"
                  @click="closeNotifications"
                  class="flex items-start gap-3 px-4 py-3 text-sm hover:bg-gray-700 transition-colors border-b border-gray-700/50 last:border-b-0"
                >
                  <div class="flex-1 min-w-0">
                    <p class="text-white font-medium truncate">{{ item.name }}</p>
                    <p class="text-gray-400 text-xs mt-1">
                      Expires {{ formatExpiryDate(item.expiration_date) }}
                    </p>
                  </div>
                  <span
                    class="px-2 py-1 rounded-full text-xs font-medium whitespace-nowrap"
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
        <!-- Avatar + Name (clickable) -->
        <button
          @click.stop="toggleDropdown"
          class="flex items-center gap-2 hover:opacity-80 transition-opacity"
        >
          <!-- Avatar -->
          <div class="w-8 h-8 rounded-full overflow-hidden flex-shrink-0">
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
              <span class="font-bold text-white text-xs">{{ initials }}</span>
            </div>
          </div>
          <!-- Username (hidden on mobile) -->
          <span class="text-sm font-medium text-gray-300 hidden sm:block">
            {{ userName }}
          </span>
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
            class="absolute right-0 top-full mt-2 w-56 bg-gray-800 border border-gray-700 rounded-xl shadow-xl overflow-hidden"
          >
            <!-- Header: User Info -->
            <div class="px-4 py-3 border-b border-gray-700">
              <p class="text-white font-semibold text-sm truncate">{{ userName }}</p>
              <p class="text-gray-500 text-xs truncate">{{ userEmail }}</p>
            </div>

            <!-- Menu Items -->
            <div class="py-2">
              <!-- Profile -->
              <RouterLink
                to="/profile"
                @click="closeDropdown"
                class="flex items-center gap-3 px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-gray-700 transition-colors"
              >
                <User :size="16" />
                <span>Profile</span>
              </RouterLink>

              <!-- Settings -->
              <RouterLink
                to="/settings"
                @click="closeDropdown"
                class="flex items-center gap-3 px-4 py-2 text-sm text-gray-300 hover:text-white hover:bg-gray-700 transition-colors"
              >
                <Settings :size="16" />
                <span>Settings</span>
              </RouterLink>
            </div>

            <!-- Divider + Logout -->
            <div class="border-t border-gray-700">
              <button
                @click="handleLogout"
                class="w-full flex items-center gap-3 px-4 py-2 text-sm text-gray-300 hover:text-red-400 hover:bg-gray-700 transition-colors"
              >
                <LogOut :size="16" />
                <span>Logout</span>
              </button>
            </div>
          </div>
        </Transition>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue"
import { useRouter } from "vue-router"
import { Bell, User, Settings, LogOut } from "lucide-vue-next"
import { useAuthStore } from "../../stores/auth"
import { useItemsStore } from "../../stores/items"
import { clearTokens } from "../../utils/auth"

const props = defineProps({
  pageTitle: { type: String, default: "Dashboard" }
})

const router = useRouter()
const authStore = useAuthStore()
const itemsStore = useItemsStore()

// Dropdown state
const dropdownOpen = ref(false)
const dropdownRef = ref(null)
const notificationsOpen = ref(false)
const notificationsRef = ref(null)

// Computed values from stores
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

// Check for notifications (expired or soon-expiring items)
const hasNotifications = computed(() => {
  const now = new Date()
  const thirtyDaysFromNow = new Date(now.getTime() + 30 * 24 * 60 * 60 * 1000)
  
  return itemsStore.items.some(item => {
    if (!item.expiration_date) return false
    const expiryDate = new Date(item.expiration_date)
    return expiryDate <= thirtyDaysFromNow
  })
})

// Get notification items
const notificationItems = computed(() => {
  const now = new Date()
  const thirtyDaysFromNow = new Date(now.getTime() + 30 * 24 * 60 * 60 * 1000)
  
  const items = itemsStore.items
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
      } else if (daysUntil <= 7) {
        urgency = 'red'
        urgencyLabel = `${daysUntil} days`
      } else if (daysUntil <= 30) {
        urgency = 'orange'
        urgencyLabel = `${daysUntil} days`
      }
      
      return {
        ...item,
        daysUntil,
        urgency,
        urgencyLabel
      }
    })
    .sort((a, b) => a.daysUntil - b.daysUntil)
    .slice(0, 8)
  
  return items
})

// Functions
function toggleDropdown() {
  dropdownOpen.value = !dropdownOpen.value
}

function closeDropdown() {
  dropdownOpen.value = false
}

function toggleNotifications() {
  notificationsOpen.value = !notificationsOpen.value
}

function closeNotifications() {
  notificationsOpen.value = false
}

function handleUpgrade() {
  router.push("/subscription")
}

function handleNotifications() {
  // Toggle notifications dropdown
  toggleNotifications()
}

function handleLogout() {
  clearTokens()
  closeDropdown()
  router.push("/login")
}

// Close dropdown when clicking outside
function handleClickOutside(event) {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    closeDropdown()
  }
  if (notificationsRef.value && !notificationsRef.value.contains(event.target)) {
    closeNotifications()
  }
}

function formatExpiryDate(dateString) {
  return new Date(dateString).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}

function getUrgencyClasses(urgency) {
  if (urgency === 'red') {
    return 'bg-red-900/40 text-red-400'
  } else if (urgency === 'orange') {
    return 'bg-orange-900/40 text-orange-400'
  } else {
    return 'bg-yellow-900/40 text-yellow-400'
  }
}

onMounted(() => {
  document.addEventListener("click", handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener("click", handleClickOutside)
})
</script>

<style scoped>
button:focus-visible,
a:focus-visible {
  outline: 2px solid #14b8a6;
  outline-offset: 2px;
  border-radius: 6px;
}
</style>
