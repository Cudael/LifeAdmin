<template>
  <!-- Fixed Header (always h-16) -->
  <header class="fixed top-0 left-0 right-0 h-16 bg-white/90 backdrop-blur-xl shadow-sm z-50 border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-6 h-full flex items-center justify-between">

      <!-- LEFT: LOGO + NAV -->
      <div class="flex items-center gap-8">
        
        <!-- Logo -->
        <RouterLink to="/dashboard" class="flex items-center gap-3 group">
          <div class="w-9 h-9 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-xl flex items-center justify-center shadow-md group-hover:shadow-lg transition-all duration-300 group-hover:scale-110">
            <Sparkles :size="18" class="text-white" />
          </div>
          <span class="text-xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
            LifeAdmin
          </span>
        </RouterLink>

        <!-- Navigation -->
        <nav class="hidden md:flex items-center gap-1">
          
          <RouterLink
            to="/dashboard"
            class="nav-link"
            :class="{ 'nav-link-active': $route.path === '/dashboard' }"
          >
            <LayoutDashboard :size="18" />
            Dashboard
          </RouterLink>

          <RouterLink
            to="/items"
            class="nav-link"
            :class="{ 'nav-link-active': $route.path.startsWith('/items') }"
          >
            <Package :size="18" />
            Items
          </RouterLink>

          <RouterLink
            to="/settings"
            class="nav-link"
            :class="{ 'nav-link-active': $route.path === '/settings' }"
          >
            <Settings :size="18" />
            Settings
          </RouterLink>
          
        </nav>
      </div>

      <!-- RIGHT: QUICK ADD + NOTIFICATIONS + USER MENU -->
      <div class="flex items-center gap-3">

        <!-- Quick Add Dropdown -->
        <div class="relative">
          <button
            @click="quickAddOpen = !quickAddOpen"
            class="group inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300"
            @blur="closeQuickAdd"
          >
            <Plus :size="18" class="group-hover:rotate-90 transition-transform duration-300" />
            <span class="hidden sm:inline">Quick Add</span>
            <ChevronDown :size="16" :class="{ 'rotate-180': quickAddOpen }" class="transition-transform duration-200" />
          </button>

          <!-- Dropdown Menu -->
          <Transition
            enter-active-class="transition-all duration-200 ease-out"
            enter-from-class="opacity-0 scale-95 -translate-y-2"
            enter-to-class="opacity-100 scale-100 translate-y-0"
            leave-active-class="transition-all duration-150 ease-in"
            leave-from-class="opacity-100 scale-100 translate-y-0"
            leave-to-class="opacity-0 scale-95 -translate-y-2"
          >
            <div
              v-if="quickAddOpen"
              class="absolute right-0 mt-2 w-56 bg-white border-2 border-gray-200 rounded-2xl shadow-2xl py-2 z-[60]"
            >
              <RouterLink
                to="/add-document"
                @click="quickAddOpen = false"
                class="dropdown-item"
              >
                <FileText :size="18" />
                <div>
                  <p class="font-semibold">Add Document</p>
                  <p class="text-xs text-gray-500">Passport, ID, Insurance...</p>
                </div>
              </RouterLink>

              <RouterLink
                to="/add-subscription"
                @click="quickAddOpen = false"
                class="dropdown-item"
              >
                <Repeat :size="18" />
                <div>
                  <p class="font-semibold">Add Subscription</p>
                  <p class="text-xs text-gray-500">Netflix, Spotify, Gym...</p>
                </div>
              </RouterLink>
            </div>
          </Transition>
        </div>

        <!-- NOTIFICATION BELL -->
        <div class="relative">
          <button
            @click="toggleNotifications"
            class="relative w-10 h-10 rounded-xl bg-gray-100 flex items-center justify-center hover:bg-gray-200 transition-colors"
          >
            <Bell :size="20" class="text-gray-700" />
            
            <!-- Badge -->
            <span
              v-if="unreadCount > 0"
              class="absolute -top-1 -right-1 w-5 h-5 bg-red-500 text-white text-xs font-bold rounded-full flex items-center justify-center animate-pulse"
            >
              {{ unreadCount > 9 ? '9+' : unreadCount }}
            </span>
          </button>

          <!-- Notifications Dropdown -->
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
              v-click-outside="closeNotifications"
              class="absolute right-0 mt-2 w-96 max-h-[500px] bg-white border-2 border-gray-200 rounded-2xl shadow-2xl z-[60] overflow-hidden"
            >
              <!-- Header -->
              <div class="px-4 py-3 border-b border-gray-200 flex items-center justify-between bg-gradient-to-r from-teal-50 to-cyan-50">
                <h3 class="font-semibold text-gray-900">Notifications</h3>
                <button
                  v-if="unreadCount > 0"
                  @click.stop="handleMarkAllAsRead"
                  class="text-xs text-teal-600 hover:text-teal-700 font-medium"
                >
                  Mark all read
                </button>
              </div>

              <!-- Notifications List -->
              <div class="overflow-y-auto max-h-[400px]">
                <div v-if="notifications.length === 0" class="px-4 py-8 text-center text-gray-500">
                  <Bell :size="32" class="mx-auto mb-2 text-gray-300" />
                  <p class="text-sm">No notifications yet</p>
                </div>

                <button
                  v-for="notification in notifications"
                  :key="notification.id"
                  @click.stop="handleNotificationClick(notification)"
                  class="w-full px-4 py-3 hover:bg-gray-50 transition-colors border-b border-gray-100 last:border-b-0 text-left"
                  :class="{ 'bg-teal-50/50': !notification.is_read }"
                >
                  <div class="flex items-start gap-3">
                    <div class="flex-shrink-0 mt-1">
                      <div
                        class="w-2 h-2 rounded-full"
                        :class="notification.is_read ? 'bg-gray-300' : 'bg-teal-500'"
                      ></div>
                    </div>
                    <div class="flex-1 min-w-0">
                      <p class="text-sm font-semibold text-gray-900 mb-1">
                        {{ notification.title }}
                      </p>
                      <p class="text-xs text-gray-600">
                        {{ notification.message }}
                      </p>
                      <p class="text-xs text-gray-400 mt-1">
                        {{ formatTime(notification.created_at) }}
                      </p>
                    </div>
                  </div>
                </button>
              </div>
            </div>
          </Transition>
        </div>

        <!-- User Menu -->
        <div class="relative">
          <button
            @click="menuOpen = !menuOpen"
            class="w-10 h-10 rounded-xl flex items-center justify-center hover:ring-2 hover:ring-teal-500 transition-all duration-200 shadow-md hover:shadow-lg overflow-hidden group"
            @blur="closeUserMenu"
          >
            <!-- Profile Picture or Initials -->
            <img
              v-if="userAvatar"
              :src="userAvatar"
              :alt="userName"
              class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
            />
            <div
              v-else
              class="w-full h-full bg-gradient-to-br from-teal-500 to-cyan-500 flex items-center justify-center group-hover:from-teal-600 group-hover:to-cyan-600 transition-all duration-200"
            >
              <span class="font-bold text-white text-sm">
                {{ initials }}
              </span>
            </div>
          </button>

          <!-- User Dropdown -->
          <Transition
            enter-active-class="transition-all duration-200 ease-out"
            enter-from-class="opacity-0 scale-95 -translate-y-2"
            enter-to-class="opacity-100 scale-100 translate-y-0"
            leave-active-class="transition-all duration-150 ease-in"
            leave-from-class="opacity-100 scale-100 translate-y-0"
            leave-to-class="opacity-0 scale-95 -translate-y-2"
          >
            <div
              v-if="menuOpen"
              class="absolute right-0 mt-2 w-64 bg-white border-2 border-gray-200 rounded-2xl shadow-2xl py-2 z-[60]"
            >
              <!-- User Info -->
              <div class="px-4 py-3 border-b border-gray-100">
                <div class="flex items-center gap-3">
                  <div class="w-12 h-12 rounded-full overflow-hidden ring-2 ring-teal-200 flex-shrink-0">
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
                      <span class="font-bold text-white text-lg">
                        {{ initials }}
                      </span>
                    </div>
                  </div>
                  <div class="flex-1 min-w-0">
                    <p class="font-semibold text-gray-900 truncate">{{ userName }}</p>
                    <p class="text-xs text-gray-500 mt-0.5 truncate">{{ userEmail || 'user@example.com' }}</p>
                  </div>
                </div>
              </div>

              <!-- Menu Items -->
              <RouterLink
                to="/profile"
                @click="menuOpen = false"
                class="dropdown-item"
              >
                <User :size="18" />
                <span>Profile</span>
              </RouterLink>

              <RouterLink
                to="/settings"
                @click="menuOpen = false"
                class="dropdown-item"
              >
                <Settings :size="18" />
                <span>Settings</span>
              </RouterLink>

              <div class="border-t border-gray-100 my-2"></div>

              <button
                @click="logout"
                class="dropdown-item text-red-600 hover:bg-red-50 w-full text-left"
              >
                <LogOut :size="18" />
                <span>Logout</span>
              </button>
            </div>
          </Transition>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="md:hidden w-10 h-10 rounded-xl bg-gray-100 flex items-center justify-center hover:bg-gray-200 transition-colors"
        >
          <Menu v-if="!mobileMenuOpen" :size="20" />
          <X v-else :size="20" />
        </button>

      </div>

    </div>
  </header>

  <!-- Mobile Navigation -->
  <Transition
    enter-active-class="transition-all duration-300 ease-out"
    enter-from-class="opacity-0 -translate-y-4"
    enter-to-class="opacity-100 translate-y-0"
    leave-active-class="transition-all duration-200 ease-in"
    leave-from-class="opacity-100 translate-y-0"
    leave-to-class="opacity-0 -translate-y-4"
  >
    <div
      v-if="mobileMenuOpen"
      class="fixed top-16 left-0 right-0 z-40 md:hidden border-b border-gray-200 bg-white/95 backdrop-blur-xl shadow-lg"
    >
      <nav class="px-6 py-4 space-y-2">
        <!-- Mobile User Info Card -->
        <div class="mb-4 p-3 bg-gradient-to-br from-teal-50 to-cyan-50 rounded-xl border border-teal-200">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-full overflow-hidden ring-2 ring-teal-300 flex-shrink-0">
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
                <span class="font-bold text-white text-lg">
                  {{ initials }}
                </span>
              </div>
            </div>
            <div class="flex-1 min-w-0">
              <p class="font-semibold text-gray-900 truncate">{{ userName }}</p>
              <p class="text-xs text-gray-600 truncate">{{ userEmail }}</p>
            </div>
          </div>
        </div>

        <RouterLink
          to="/dashboard"
          @click="mobileMenuOpen = false"
          class="mobile-nav-link"
          :class="{ 'mobile-nav-link-active': $route.path === '/dashboard' }"
        >
          <LayoutDashboard :size="18" />
          Dashboard
        </RouterLink>

        <RouterLink
          to="/items"
          @click="mobileMenuOpen = false"
          class="mobile-nav-link"
          :class="{ 'mobile-nav-link-active': $route.path.startsWith('/items') }"
        >
          <Package :size="18" />
          Items
        </RouterLink>

        <RouterLink
          to="/settings"
          @click="mobileMenuOpen = false"
          class="mobile-nav-link"
          :class="{ 'mobile-nav-link-active': $route.path === '/settings' }"
        >
          <Settings :size="18" />
          Settings
        </RouterLink>

        <div class="border-t border-gray-200 my-2"></div>

        <RouterLink
          to="/add-document"
          @click="mobileMenuOpen = false"
          class="mobile-nav-link"
        >
          <FileText :size="18" />
          Add Document
        </RouterLink>

        <RouterLink
          to="/add-subscription"
          @click="mobileMenuOpen = false"
          class="mobile-nav-link"
        >
          <Repeat :size="18" />
          Add Subscription
        </RouterLink>
      </nav>
    </div>
  </Transition>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue"
import { useRouter } from "vue-router"
import { clearTokens } from "../../utils/auth"
import { apiFetch } from "../../utils/api"
import {
  Sparkles,
  LayoutDashboard,
  Package,
  Settings,
  Plus,
  FileText,
  Repeat,
  User,
  LogOut,
  Menu,
  X,
  ChevronDown,
  Bell
} from "lucide-vue-next"

const props = defineProps({
  userName: { type: String, default: "User" },
  userEmail: { type: String, default: "" },
  userAvatar: { type: String, default: null }
})

const router = useRouter()
const menuOpen = ref(false)
const quickAddOpen = ref(false)
const mobileMenuOpen = ref(false)
const notificationsOpen = ref(false)

// Notifications
const notifications = ref([])
const unreadCount = ref(0)
let pollInterval = null

const initials = computed(() => {
  const names = props.userName.split(" ")
  if (names.length >= 2) {
    return (names[0][0] + names[names.length - 1][0]).toUpperCase()
  }
  return props.userName.charAt(0).toUpperCase() + (props.userName.charAt(1) || '').toUpperCase()
})

// Click outside directive
const vClickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = function(event) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event)
      }
    }
    document.body.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent)
  }
}

// Fetch notifications
async function fetchNotifications() {
  try {
    const res = await apiFetch('/notifications/')
    if (res.ok) {
      const data = await res.json()
      notifications.value = data
      console.log('Fetched notifications:', data.length)
    }
  } catch (error) {
    console.error('Failed to fetch notifications:', error)
  }
}

// Fetch unread count
async function fetchUnreadCount() {
  try {
    const res = await apiFetch('/notifications/unread-count')
    if (res.ok) {
      const data = await res.json()
      unreadCount.value = data.count
    }
  } catch (error) {
    console.error('Failed to fetch unread count:', error)
  }
}

// Toggle notifications dropdown
async function toggleNotifications() {
  notificationsOpen.value = !notificationsOpen.value
  if (notificationsOpen.value) {
    await fetchNotifications()
    await fetchUnreadCount()
  }
}

// Close notifications
function closeNotifications() {
  notificationsOpen.value = false
}

// Mark notification as read
async function markAsRead(notificationId) {
  try {
    console.log('Marking notification as read:', notificationId)
    
    const res = await apiFetch(`/notifications/${notificationId}/read`, {
      method: 'POST'
    })
    
    if (res.ok) {
      console.log('Successfully marked as read')
      
      // Update local state
      const notification = notifications.value.find(n => n.id === notificationId)
      if (notification && !notification.is_read) {
        notification.is_read = true
        unreadCount.value = Math.max(0, unreadCount.value - 1)
        console.log('Updated local state. New unread count:', unreadCount.value)
      }
      
      return true
    } else {
      console.error('Failed to mark as read. Status:', res.status)
      return false
    }
  } catch (error) {
    console.error('Error marking notification as read:', error)
    return false
  }
}

// Handle notification click
async function handleNotificationClick(notification) {
  console.log('Notification clicked:', notification.id)
  
  // Mark as read
  const success = await markAsRead(notification.id)
  
  if (success) {
    // Close dropdown
    notificationsOpen.value = false
    
    // Navigate to item
    router.push(`/items/${notification.item_id}`)
  }
}

// Mark all as read
async function handleMarkAllAsRead() {
  try {
    console.log('Marking all as read...')
    
    const res = await apiFetch('/notifications/mark-all-read', {
      method: 'POST'
    })
    
    if (res.ok) {
      // Update local state
      notifications.value.forEach(n => {
        n.is_read = true
      })
      unreadCount.value = 0
      console.log('All notifications marked as read')
    }
  } catch (error) {
    console.error('Failed to mark all as read:', error)
  }
}

// Format notification time
function formatTime(timestamp) {
  const date = new Date(timestamp)
  const now = new Date()
  const diffMs = now - date
  const diffMins = Math.floor(diffMs / 60000)
  const diffHours = Math.floor(diffMs / 3600000)
  const diffDays = Math.floor(diffMs / 86400000)
  
  if (diffMins < 1) return 'Just now'
  if (diffMins < 60) return `${diffMins}m ago`
  if (diffHours < 24) return `${diffHours}h ago`
  if (diffDays < 7) return `${diffDays}d ago`
  
  return date.toLocaleDateString()
}

function logout() {
  clearTokens()
  router.push("/login")
}

function closeUserMenu() {
  setTimeout(() => {
    menuOpen.value = false
  }, 200)
}

function closeQuickAdd() {
  setTimeout(() => {
    quickAddOpen.value = false
  }, 200)
}

// Lifecycle
onMounted(() => {
  fetchNotifications()
  fetchUnreadCount()
  
  // Poll for new notifications every 30 seconds
  pollInterval = setInterval(() => {
    fetchUnreadCount()
  }, 30000)
})

onUnmounted(() => {
  if (pollInterval) {
    clearInterval(pollInterval)
  }
})
</script>

<style scoped>
.nav-link {
  @apply flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-medium text-gray-700 hover:bg-gray-100 hover:text-gray-900 transition-all duration-200;
}

.nav-link-active {
  @apply bg-gradient-to-r from-teal-50 to-cyan-50 text-teal-700 border-2 border-teal-200;
}

.mobile-nav-link {
  @apply flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-medium text-gray-700 hover:bg-gray-100 transition-all duration-200;
}

.mobile-nav-link-active {
  @apply bg-gradient-to-r from-teal-50 to-cyan-50 text-teal-700 border-2 border-teal-200;
}

.dropdown-item {
  @apply flex items-center gap-3 w-full px-4 py-3 text-sm text-gray-700 hover:bg-gray-50 transition-colors duration-150;
}
</style>