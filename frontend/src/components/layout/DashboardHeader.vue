<template>
  <header class="bg-white/80 backdrop-blur-md shadow-sm z-50 relative">
    <div class="max-w-7xl mx-auto px-6 h-14 flex items-center justify-between">

      <!-- LEFT: LOGO + NAV -->
      <div class="flex items-center gap-10">
        <RouterLink to="/" class="text-lg font-semibold tracking-tight text-gray-900">
          LifeAdmin
        </RouterLink>

        <nav class="flex items-center gap-1 text-gray-600">
          <RouterLink
            to="/dashboard"
            class="px-3 py-2 rounded-md text-sm hover:bg-gray-100 transition"
            active-class="bg-gray-100 text-gray-900 font-medium"
          >
            Dashboard
          </RouterLink>

          <RouterLink
            to="/add-document"
            class="px-3 py-2 rounded-md text-sm hover:bg-gray-100 transition"
            active-class="bg-gray-100 text-gray-900 font-medium"
          >
            Documents
          </RouterLink>

          <RouterLink
            to="/add-subscription"
            class="px-3 py-2 rounded-md text-sm hover:bg-gray-100 transition"
            active-class="bg-gray-100 text-gray-900 font-medium"
          >
            Subscriptions
          </RouterLink>

          <RouterLink
            to="/settings"
            class="px-3 py-2 rounded-md text-sm hover:bg-gray-100 transition"
            active-class="bg-gray-100 text-gray-900 font-medium"
          >
            Settings
          </RouterLink>

        </nav>
      </div>

      <!-- RIGHT: USER MENU -->
      <div class="relative">
        <button
          @click="menuOpen = !menuOpen"
          class="w-9 h-9 rounded-full bg-gray-100 flex items-center justify-center hover:bg-gray-200 transition"
        >
          <span class="font-semibold text-gray-700 text-sm">
            {{ initials }}
          </span>
        </button>

        <div
          v-if="menuOpen"
          class="absolute right-0 mt-2 w-40 bg-white border border-gray-200 rounded-lg shadow-lg py-2 z-50"
        >
          <button
            @click="logout"
            class="w-full text-left px-4 py-2 hover:bg-gray-100 text-sm"
          >
            Logout
          </button>
        </div>
      </div>

    </div>
  </header>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"

const props = defineProps({
  userName: { type: String, default: "User" }
})

const router = useRouter()
const menuOpen = ref(false)

const initials = props.userName
  .split(" ")
  .map(n => n[0])
  .join("")
  .toUpperCase()

function logout() {
  localStorage.removeItem("token")
  router.push("/login")
}
</script>