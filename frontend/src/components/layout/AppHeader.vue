<template>
  <header
    class="fixed top-0 left-0 w-full backdrop-blur-md bg-white/80 border-b border-gray-200 z-30"
  >
    <div class="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">

      <!-- LOGO -->
      <RouterLink to="/" class="text-xl font-semibold tracking-tight text-gray-900">
        LifeAdmin
      </RouterLink>

      <!-- DESKTOP NAV -->
      <nav class="hidden md:flex items-center gap-6">

        <RouterLink to="/" class="nav-link">Home</RouterLink>
        <a href="/#features" class="nav-link">Features</a>
        <a href="/#pricing" class="nav-link">Pricing</a>

        <!-- Logged OUT -->
        <template v-if="!isLoggedIn">
          <RouterLink
            to="/login"
            class="px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100 transition"
          >
            Login
          </RouterLink>

          <RouterLink
            to="/register"
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
          >
            Get Started
          </RouterLink>
        </template>

        <!-- Logged IN -->
        <template v-else>
          <RouterLink
            to="/dashboard"
            class="px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition"
          >
            Dashboard
          </RouterLink>

          <button
            @click="logout"
            class="px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition"
          >
            Logout
          </button>
        </template>

      </nav>

      <!-- MOBILE MENU BUTTON -->
      <button
        class="md:hidden p-2 rounded-lg hover:bg-gray-100 transition"
        @click="mobileOpen = true"
      >
        ☰
      </button>
    </div>

    <!-- MOBILE OVERLAY -->
    <div
      v-if="mobileOpen"
      class="fixed inset-0 bg-black/30 z-40"
      @click="mobileOpen = false"
    ></div>

    <!-- MOBILE DRAWER -->
    <div
      v-if="mobileOpen"
      class="fixed top-0 right-0 w-64 h-full bg-white shadow-xl p-6 z-50"
    >
      <h2 class="text-xl font-semibold mb-6">Menu</h2>

      <nav class="flex flex-col gap-4">

        <RouterLink to="/" @click="closeMobile" class="text-gray-800">Home</RouterLink>
        <a href="/#features" @click="closeMobile" class="text-gray-800">Features</a>
        <a href="/#pricing" @click="closeMobile" class="text-gray-800">Pricing</a>

        <template v-if="!isLoggedIn">
          <RouterLink
            to="/login"
            @click="closeMobile"
            class="px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100 transition"
          >
            Login
          </RouterLink>

          <RouterLink
            to="/register"
            @click="closeMobile"
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
          >
            Get Started
          </RouterLink>
        </template>

        <template v-else>
          <RouterLink
            to="/dashboard"
            @click="closeMobile"
            class="px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition"
          >
            Dashboard
          </RouterLink>

          <button
            @click="logout"
            class="px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-lg transition"
          >
            Logout
          </button>
        </template>

      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import { accessToken, clearTokens } from "../../utils/auth"   // ← Changed clearToken to clearTokens

const router = useRouter()
const mobileOpen = ref(false)

// 🔥 Reactive login state
const isLoggedIn = computed(() => !!accessToken.value)

function logout() {
  clearTokens()  // ← Changed clearToken to clearTokens
  router.push("/")
}

function closeMobile() {
  mobileOpen.value = false
}
</script>

<style lang="postcss" scoped>
.nav-link {
  @apply text-gray-700 hover:text-gray-900 transition;
}
</style>