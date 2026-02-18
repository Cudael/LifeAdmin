<script setup>
import { ref, onMounted, computed } from "vue"
import { useRouter, useRoute } from "vue-router"
import AppSidebar from "../components/layout/AppSidebar.vue"
import EmailVerificationBanner from "../components/EmailVerificationBanner.vue"
import { useAuthStore } from "../stores/auth"
import { clearTokens } from "../utils/auth"
import { error } from "../utils/logger"

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const props = defineProps({
  pageTitle: { type: String, default: "Dashboard" }
})

// Computed values from store
const userName = computed(() => {
  const u = authStore.user
  return u?.full_name || u?.username || u?.name || "User"
})
const loading = ref(true)

// Check if it's the dashboard page
const isDashboard = computed(() => props.pageTitle === "Dashboard")

// Get current date formatted
const currentDate = computed(() => {
  const options = { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' }
  return new Date().toLocaleDateString('en-US', options)
})

// Get page subtitle based on route
const pageSubtitle = computed(() => {
  switch(props.pageTitle) {
    case "Dashboard":
      return "Welcome back! Here's your overview"
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
  <div class="min-h-screen flex bg-gradient-to-br from-gray-50 via-gray-100 to-gray-50">

    <!-- SIDEBAR (Fixed left) -->
    <AppSidebar />

    <!-- MAIN CONTENT AREA (with left margin for sidebar on desktop) -->
    <main class="flex-1 ml-0 lg:ml-64 overflow-y-auto">
      
      <!-- EMAIL VERIFICATION BANNER -->
      <EmailVerificationBanner v-if="authStore.user && !loading" :user="authStore.user" />

      <!-- PAGE CONTENT WRAPPER -->
      <div class="p-4 md:p-6 lg:p-8">
        <div class="max-w-7xl mx-auto">

          <!-- SIMPLE PAGE TITLE HEADER -->
          <div class="mb-8">
            <div class="flex items-center justify-between">
              <div>
                <h1 class="text-2xl md:text-3xl font-bold text-gray-900">{{ pageTitle }}</h1>
                <p v-if="pageSubtitle" class="text-gray-500 mt-1">{{ pageSubtitle }}</p>
              </div>
              <!-- Show current date on dashboard -->
              <div v-if="isDashboard" class="hidden md:block">
                <p class="text-sm text-gray-500">{{ currentDate }}</p>
              </div>
            </div>
          </div>

          <!-- ACTION BUTTONS SLOT (for page-specific actions - optional) -->
          <div v-if="$slots.actions" class="mb-6">
            <slot name="actions" />
          </div>

          <!-- PAGE CONTENT -->
          <div class="animate-fade-in">
            <slot />
          </div>

        </div>
      </div>
    </main>

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
</style>