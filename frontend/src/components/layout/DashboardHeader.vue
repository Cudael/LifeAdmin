<template>
  <!-- Fixed Header (Deep Slate & Frosted Glass) -->
  <header class="fixed top-0 left-0 right-0 h-16 bg-slate-950/80 backdrop-blur-xl shadow-sm z-50 border-b border-white/5">
    <div class="max-w-7xl mx-auto px-6 h-full flex items-center justify-between">

      <!-- LEFT: LOGO + NAV -->
      <div class="flex items-center gap-8">
        
        <!-- Logo -->
        <RouterLink to="/dashboard" class="flex items-center gap-3 group w-max">
          <div class="w-8 h-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-lg flex items-center justify-center shadow-[0_0_15px_rgba(45,212,191,0.2)] group-hover:scale-105 transition-transform duration-300">
            <Sparkles :size="16" class="text-slate-950" />
          </div>
          <span class="text-xl font-extrabold text-white tracking-tight">
            Life<span class="text-slate-500">Admin</span>
          </span>
        </RouterLink>

        <!-- Navigation (Hidden on mobile) -->
        <nav class="hidden md:flex items-center gap-2">
          
          <RouterLink
            to="/dashboard"
            class="nav-link"
            :class="{ 'nav-link-active': $route.path === '/dashboard' }"
          >
            <LayoutDashboard :size="16" />
            Dashboard
          </RouterLink>

          <RouterLink
            to="/items"
            class="nav-link"
            :class="{ 'nav-link-active': $route.path.startsWith('/items') }"
          >
            <Package :size="16" />
            Items
          </RouterLink>

          <router-link
            to="/calendar"
            class="nav-link"
            :class="{ 'nav-link-active': $route.path === '/calendar' }"
          >
            <Calendar :size="16" />
            Calendar
          </router-link>

          <div class="w-px h-4 bg-white/10 mx-2"></div>

          <RouterLink
            to="/settings"
            class="nav-link text-slate-400"
            :class="{ 'nav-link-active': $route.path === '/settings' }"
          >
            <Settings :size="16" />
          </RouterLink>

          <RouterLink
            to="/subscription"
            class="nav-link text-slate-400"
            :class="{ 'nav-link-active': $route.path === '/subscription' }"
          >
            <CreditCard :size="16" />
          </RouterLink>
          
        </nav>
      </div>

      <!-- RIGHT: QUICK ADD + NOTIFICATIONS + USER MENU -->
      <div class="flex items-center gap-3">

        <!-- Quick Add Dropdown -->
        <div class="relative">
          <button
            @click="quickAddOpen = !quickAddOpen"
            class="group inline-flex items-center gap-2 px-4 py-2 bg-slate-50 hover:bg-white text-slate-950 rounded-xl font-bold shadow-[0_0_15px_rgba(255,255,255,0.1)] transition-all duration-300"
            @blur="closeQuickAdd"
          >
            <Plus :size="16" class="text-teal-600 group-hover:rotate-90 transition-transform duration-300" />
            <span class="hidden sm:inline">New</span>
            <ChevronDown :size="14" :class="{ 'rotate-180': quickAddOpen }" class="transition-transform duration-200 text-slate-400" />
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
              class="absolute right-0 mt-3 w-56 bg-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.5)] p-1.5 z-[60]"
            >
              <RouterLink
                to="/add-item"
                @click="quickAddOpen = false"
                class="dropdown-item group"
              >
                <div class="w-8 h-8 rounded-lg bg-teal-500/10 border border-teal-500/20 flex items-center justify-center text-teal-400 shrink-0">
                  <Plus :size="16" />
                </div>
                <div>
                  <p class="font-bold text-slate-200 group-hover:text-white">Add Item</p>
                  <p class="text-[10px] text-slate-500">Documents & subscriptions</p>
                </div>
              </RouterLink>
            </div>
          </Transition>
        </div>

        <!-- NOTIFICATION BELL -->
        <div class="relative">
          <button
            @click.stop="toggleNotifications"
            class="relative w-9 h-9 rounded-xl bg-slate-900 border border-white/5 flex items-center justify-center hover:bg-slate-800 transition-colors shadow-inner group"
          >
            <Bell :size="18" class="text-slate-400 group-hover:text-slate-200 transition-colors" />
            
            <!-- Glowing Red Badge -->
            <span
              v-if="unreadCount > 0"
              class="absolute -top-1 -right-1 w-4 h-4 bg-rose-500 text-white text-[9px] font-bold rounded-full flex items-center justify-center shadow-[0_0_10px_rgba(225,29,72,0.6)] animate-pulse"
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
              @click.stop
              class="absolute right-0 mt-3 w-80 sm:w-96 bg-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.5)] z-[60] overflow-hidden flex flex-col max-h-[80vh]"
            >
              <!-- Header -->
              <div class="px-4 py-3 border-b border-white/5 flex items-center justify-between bg-white/[0.02]">
                <h3 class="font-bold text-white text-sm">Notifications</h3>
                <button
                  v-if="unreadCount > 0"
                  @click.stop="handleMarkAllAsRead"
                  class="text-xs text-teal-400 hover:text-teal-300 font-bold tracking-wide"
                >
                  Mark all read
                </button>
              </div>

              <!-- Notifications List -->
              <div class="overflow-y-auto custom-scrollbar flex-1">
                <!-- Empty State -->
                <div v-if="notifications.length === 0" class="px-4 py-10 text-center flex flex-col items-center">
                  <div class="w-12 h-12 rounded-full bg-white/5 flex items-center justify-center mb-3">
                    <Bell :size="20" class="text-slate-600" />
                  </div>
                  <p class="text-sm font-medium text-slate-400">All caught up!</p>
                </div>

                <div v-else>
                  <!-- Unread Section -->
                  <div v-if="unreadNotifications.length > 0">
                    <div class="px-4 py-1.5 bg-slate-950/50 border-b border-white/5">
                      <p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">New</p>
                    </div>
                    <button
                      v-for="notification in unreadNotifications"
                      :key="notification.id"
                      @click.stop="handleNotificationClick(notification)"
                      class="w-full px-4 py-3 hover:bg-white/5 transition-colors border-b border-white/5 text-left bg-teal-500/[0.02] relative"
                    >
                      <div class="absolute left-0 top-0 h-full w-0.5 bg-teal-400"></div>
                      <div class="flex items-start gap-3">
                        <div class="flex-1 min-w-0">
                          <p class="text-sm font-bold text-slate-200 mb-0.5 truncate">
                            {{ notification.title }}
                          </p>
                          <p class="text-xs text-slate-400 line-clamp-2">
                            {{ notification.message }}
                          </p>
                          <p class="text-[10px] text-slate-500 mt-1.5 font-medium">
                            {{ formatTime(notification.created_at) }}
                          </p>
                        </div>
                      </div>
                    </button>
                  </div>

                  <!-- Read Section -->
                  <div v-if="readNotifications.length > 0">
                    <div class="px-4 py-1.5 bg-slate-950/50 border-b border-white/5">
                      <p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Earlier</p>
                    </div>
                    <button
                      v-for="notification in readNotifications"
                      :key="notification.id"
                      @click.stop="handleNotificationClick(notification)"
                      class="w-full px-4 py-3 hover:bg-white/5 transition-colors border-b border-white/5 last:border-b-0 text-left opacity-60 hover:opacity-100"
                    >
                      <div class="flex items-start gap-3">
                        <div class="flex-1 min-w-0">
                          <p class="text-sm font-semibold text-slate-300 mb-0.5 truncate">
                            {{ notification.title }}
                          </p>
                          <p class="text-xs text-slate-500 line-clamp-2">
                            {{ notification.message }}
                          </p>
                          <p class="text-[10px] text-slate-600 mt-1.5 font-medium">
                            {{ formatTime(notification.created_at) }}
                          </p>
                        </div>
                      </div>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </Transition>
        </div>

        <!-- User Menu -->
        <div class="relative">
          <button
            @click="menuOpen = !menuOpen"
            class="w-9 h-9 rounded-xl flex items-center justify-center transition-all duration-200 shadow-md hover:shadow-lg overflow-hidden group border border-white/10 hover:border-teal-500/50"
            @blur="closeUserMenu"
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
              <span class="font-bold text-slate-300 text-xs">
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
              class="absolute right-0 mt-3 w-56 bg-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl shadow-[0_10px_40px_rgba(0,0,0,0.5)] p-1.5 z-[60]"
            >
              <!-- User Info -->
              <div class="px-3 py-3 border-b border-white/5 mb-1.5">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full overflow-hidden flex-shrink-0 border border-white/10">
                    <img
                      v-if="userAvatar"
                      :src="userAvatar"
                      :alt="userName"
                      class="w-full h-full object-cover"
                    />
                    <div v-else class="w-full h-full bg-slate-800 flex items-center justify-center">
                      <span class="font-bold text-white text-sm">{{ initials }}</span>
                    </div>
                  </div>
                  <div class="flex-1 min-w-0">
                    <p class="font-bold text-slate-200 text-sm truncate">{{ userName }}</p>
                    <p class="text-[10px] text-slate-500 font-medium truncate">{{ userEmail || 'user@example.com' }}</p>
                  </div>
                </div>
              </div>

              <!-- Menu Items -->
              <RouterLink to="/profile" @click="menuOpen = false" class="dropdown-item group">
                <User :size="16" class="text-slate-500 group-hover:text-teal-400 transition-colors" />
                <span>Profile</span>
              </RouterLink>

              <RouterLink to="/settings" @click="menuOpen = false" class="dropdown-item group">
                <Settings :size="16" class="text-slate-500 group-hover:text-teal-400 transition-colors" />
                <span>Settings</span>
              </RouterLink>

              <RouterLink to="/subscription" @click="menuOpen = false" class="dropdown-item group">
                <CreditCard :size="16" class="text-slate-500 group-hover:text-teal-400 transition-colors" />
                <span>Billing</span>
              </RouterLink>

              <div class="h-px bg-white/5 my-1.5"></div>

              <button @click="logout" class="dropdown-item group text-rose-400 hover:bg-rose-500/10">
                <LogOut :size="16" class="text-rose-500/70 group-hover:text-rose-400 transition-colors" />
                <span>Sign out</span>
              </button>
            </div>
          </Transition>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="md:hidden w-9 h-9 rounded-xl bg-slate-900 border border-white/5 flex items-center justify-center hover:bg-slate-800 transition-colors text-slate-400"
        >
          <Menu v-if="!mobileMenuOpen" :size="20" />
          <X v-else :size="20" />
        </button>

      </div>

    </div>
  </header>

  <!-- Mobile Navigation (Deep Dark Mode) -->
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
      class="fixed top-16 left-0 right-0 z-40 md:hidden border-b border-white/10 bg-slate-950/95 backdrop-blur-xl shadow-2xl"
    >
      <nav class="px-6 py-4 space-y-1">
        <!-- Mobile User Info Card -->
        <div class="mb-4 p-3 bg-slate-900 border border-white/5 rounded-2xl">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-full overflow-hidden border border-white/10 flex-shrink-0">
              <img v-if="userAvatar" :src="userAvatar" :alt="userName" class="w-full h-full object-cover"/>
              <div v-else class="w-full h-full bg-slate-800 flex items-center justify-center">
                <span class="font-bold text-white text-sm">{{ initials }}</span>
              </div>
            </div>
            <div class="flex-1 min-w-0">
              <p class="font-bold text-white truncate">{{ userName }}</p>
              <p class="text-xs text-slate-500 font-medium truncate">{{ userEmail }}</p>
            </div>
          </div>
        </div>

        <RouterLink to="/dashboard" @click="mobileMenuOpen = false" class="mobile-nav-link" :class="{ 'mobile-nav-link-active': $route.path === '/dashboard' }">
          <LayoutDashboard :size="18" /> Dashboard
        </RouterLink>
        <RouterLink to="/items" @click="mobileMenuOpen = false" class="mobile-nav-link" :class="{ 'mobile-nav-link-active': $route.path.startsWith('/items') }">
          <Package :size="18" /> Vault Items
        </RouterLink>
        <RouterLink to="/calendar" @click="mobileMenuOpen = false" class="mobile-nav-link" :class="{ 'mobile-nav-link-active': $route.path === '/calendar' }">
          <Calendar :size="18" /> Timeline
        </RouterLink>
        <RouterLink to="/settings" @click="mobileMenuOpen = false" class="mobile-nav-link" :class="{ 'mobile-nav-link-active': $route.path === '/settings' }">
          <Settings :size="18" /> Settings
        </RouterLink>
        <div class="h-px bg-white/5 my-3"></div>
        <RouterLink to="/add-item" @click="mobileMenuOpen = false" class="mobile-nav-link text-teal-400">
          <Plus :size="18" /> Add New Item
        </RouterLink>
      </nav>
    </div>
  </Transition>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from "vue"
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
  Bell,
  CreditCard,
  Calendar
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

const unreadNotifications = computed(() => notifications.value.filter(n => !n.is_read))
const readNotifications = computed(() => notifications.value.filter(n => n.is_read))

const vClickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = function(event) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event)
      }
    }
    setTimeout(() => {
      document.body.addEventListener('click', el.clickOutsideEvent)
    }, 100)
  },
  unmounted(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent)
  }
}

async function fetchNotifications() {
  try {
    const res = await apiFetch('/notifications/')
    if (res.ok) {
      const data = await res.json()
      notifications.value = data
    }
  } catch (error) {
    console.error('Failed to fetch notifications:', error)
  }
}

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

async function toggleNotifications(event) {
  event.stopPropagation()
  if (notificationsOpen.value) {
    notificationsOpen.value = false
  } else {
    notificationsOpen.value = true
    await nextTick()
    await fetchNotifications()
    await fetchUnreadCount()
  }
}

function closeNotifications() {
  notificationsOpen.value = false
}

async function markAsRead(notificationId) {
  try {
    const res = await apiFetch(`/notifications/${notificationId}/read`, { method: 'POST' })
    if (res.ok) {
      const notification = notifications.value.find(n => n.id === notificationId)
      if (notification && !notification.is_read) {
        notification.is_read = true
        unreadCount.value = Math.max(0, unreadCount.value - 1)
      }
      return true
    }
    return false
  } catch (error) {
    return false
  }
}

async function handleNotificationClick(notification) {
  await markAsRead(notification.id)
  notificationsOpen.value = false
  router.push(`/items/${notification.item_id}`)
}

async function handleMarkAllAsRead() {
  try {
    const res = await apiFetch('/notifications/mark-all-read', { method: 'POST' })
    if (res.ok) {
      notifications.value.forEach(n => { n.is_read = true })
      unreadCount.value = 0
    }
  } catch (error) {}
}

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
  setTimeout(() => { menuOpen.value = false }, 200)
}

function closeQuickAdd() {
  setTimeout(() => { quickAddOpen.value = false }, 200)
}

onMounted(() => {
  fetchNotifications()
  fetchUnreadCount()
  pollInterval = setInterval(() => { fetchUnreadCount() }, 30000)
})

onUnmounted(() => {
  if (pollInterval) clearInterval(pollInterval)
})
</script>

<style scoped>
.nav-link {
  @apply flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm font-medium text-slate-400 hover:text-slate-200 hover:bg-white/5 transition-all duration-200;
}
.nav-link-active {
  @apply bg-white/5 text-white shadow-[inset_0_-2px_0_0_rgba(45,212,191,1)];
}
.mobile-nav-link {
  @apply flex items-center gap-3 px-4 py-3 rounded-xl text-sm font-bold text-slate-400 hover:bg-white/5 hover:text-white transition-all duration-200;
}
.mobile-nav-link-active {
  @apply bg-teal-500/10 text-teal-400 border border-teal-500/20;
}
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