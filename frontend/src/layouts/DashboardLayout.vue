<script setup>
import { ref, onMounted, computed } from "vue"
import { useRouter } from "vue-router"
import DashboardHeader from "../components/layout/DashboardHeader.vue"
import EmailVerificationBanner from "../components/EmailVerificationBanner.vue"  // ✅ Import
import { apiFetch } from "../utils/api"
import { clearTokens } from "../utils/auth"
import { Sparkles, TrendingUp } from "lucide-vue-next"

const router = useRouter()

const props = defineProps({
  pageTitle: { type: String, default: "Dashboard" }
})

// User info
const user = ref(null)  // ✅ Changed to full user object
const userName = ref("User")
const userEmail = ref("")
const userAvatar = ref(null)
const loading = ref(true)

// Check if it's the dashboard page
const isDashboard = computed(() => props.pageTitle === "Dashboard")

// Get greeting based on time
const greeting = computed(() => {
  const hour = new Date().getHours()
  if (hour < 12) return "Good morning"
  if (hour < 18) return "Good afternoon"
  return "Good evening"
})

// Fetch user profile on load
onMounted(async () => {
  try {
    const res = await apiFetch("/auth/me")

    // If unauthorized, clear tokens and redirect to login
    if (res.status === 401) {
      console.error("Unauthorized - redirecting to login")
      clearTokens()
      router.push("/login")
      return
    }

    if (!res.ok) {
      console.error("Failed to fetch user profile")
      loading.value = false
      return
    }

    const data = await res.json()
    user.value = data  // ✅ Store full user object
    userName.value = data.full_name || data.username || data.name || "User"
    userEmail.value = data.email || ""
    userAvatar.value = data.profile_picture || null
    loading.value = false

  } catch (err) {
    console.error("Error fetching user:", err)
    loading.value = false
  }
})
</script>

<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-br from-gray-50 via-gray-100 to-gray-50 pt-16">

    <!-- TOP NAVIGATION BAR -->
    <DashboardHeader 
      :userName="userName" 
      :userEmail="userEmail"
      :userAvatar="userAvatar"
    />

    <!-- ✅ EMAIL VERIFICATION BANNER (Below header, above content) -->
    <EmailVerificationBanner v-if="user && !loading" :user="user" />

    <!-- MAIN CONTENT AREA (with top padding for fixed header) -->
    <main class="flex-1 p-4 md:p-6 lg:p-8 pt-20 overflow-y-auto">
      <div class="max-w-7xl mx-auto">

        <!-- ONLY SHOW SPECIAL HEADER FOR DASHBOARD -->
        <template v-if="isDashboard">
          <div class="mb-8">
            <div class="relative overflow-hidden bg-gradient-to-br from-teal-500 to-cyan-500 rounded-3xl shadow-xl p-8 md:p-10 text-white">
              
              <!-- Decorative elements -->
              <div class="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
              <div class="absolute bottom-0 left-0 w-48 h-48 bg-white/10 rounded-full translate-y-1/2 -translate-x-1/2"></div>
              
              <div class="relative z-10">
                <div class="flex items-center gap-2 mb-3">
                  <Sparkles :size="24" class="text-white/90" />
                  <span class="text-white/90 font-medium">{{ greeting }}</span>
                </div>
                
                <h1 class="text-3xl md:text-4xl font-bold mb-2 flex items-center gap-3">
                  <span v-if="!loading">Welcome back, {{ userName }}!</span>
                  <span v-else>Welcome back!</span>
                  <span class="text-3xl">👋</span>
                </h1>
                
                <p class="text-white/90 text-lg mb-6">
                  Here's your overview for today
                </p>

                <!-- Quick Stats -->
                <div class="flex flex-wrap gap-6 mt-6">
                  <div class="flex items-center gap-2">
                    <div class="w-2 h-2 rounded-full bg-white/50"></div>
                    <span class="text-white/80 text-sm">All systems operational</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <TrendingUp :size="16" class="text-white/80" />
                    <span class="text-white/80 text-sm">Stay organized</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </template>

        <!-- ACTION BUTTONS SLOT (for page-specific actions) -->
        <div v-if="$slots.actions" class="mb-6">
          <slot name="actions" />
        </div>

        <!-- PAGE CONTENT -->
        <div class="animate-fade-in">
          <slot />
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