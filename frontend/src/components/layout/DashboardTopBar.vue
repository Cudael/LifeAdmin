<template>
  <div class="sticky top-0 z-40 h-12 bg-gray-900 border-b border-gray-800 flex items-center justify-between px-6">
    
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
    if (!item.expiry_date) return false
    const expiryDate = new Date(item.expiry_date)
    return expiryDate <= thirtyDaysFromNow
  })
})

// Functions
function toggleDropdown() {
  dropdownOpen.value = !dropdownOpen.value
}

function closeDropdown() {
  dropdownOpen.value = false
}

function handleUpgrade() {
  router.push("/subscription")
}

function handleNotifications() {
  // Navigate to items page with filter for expiring/expired
  router.push("/items?filter=soon")
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
}

onMounted(() => {
  document.addEventListener("click", handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener("click", handleClickOutside)
})
</script>
