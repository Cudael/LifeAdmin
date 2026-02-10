<script setup>
import { ref, onMounted } from "vue"
import DashboardHeader from "../components/layout/DashboardHeader.vue"

const props = defineProps({
  pageTitle: { type: String, default: "Dashboard" }
})

// Holds the user's name from backend
const userName = ref("User")

// Fetch user profile on load
onMounted(async () => {
  try {
    const res = await fetch("http://localhost:8000/auth/me", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`
      }
    })

    if (!res.ok) {
      console.error("Failed to fetch user profile")
      return
    }

    const data = await res.json()
    userName.value = data.full_name || data.name || "User"

  } catch (err) {
    console.error("Error fetching user:", err)
  }
})
</script>

<template>
  <div class="min-h-screen flex flex-col bg-gray-100">

    <!-- TOP NAVIGATION BAR -->
    <DashboardHeader />

    <!-- MAIN CONTENT AREA -->
    <main class="flex-1 p-4 overflow-y-auto">
      <div class="max-w-7xl mx-auto">

        <!-- PAGE HEADER -->
        <div class="flex items-center justify-between mb-12 mt-6">

          <div>
            <!-- DASHBOARD WELCOME BLOCK -->
            <template v-if="pageTitle === 'Dashboard'">
              <h1 class="text-3xl font-semibold text-gray-900 leading-tight">
                Welcome back, {{ userName }}! 👋
              </h1>
              <p class="text-lg text-gray-600 mt-1">
                Here's your overview for today
              </p>
            </template>

            <!-- NORMAL PAGE TITLE -->
            <template v-else>
              <h1 class="text-3xl font-semibold text-gray-900 leading-tight">
                {{ pageTitle }}
              </h1>
            </template>
          </div>

          <!-- ACTION BUTTONS -->
          <div class="flex items-center gap-3">
            <slot name="actions" />
          </div>

        </div>

        <!-- PAGE CONTENT -->
        <slot />

      </div>
    </main>

  </div>
</template>