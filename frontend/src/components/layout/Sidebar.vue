<template>
  <aside class="w-64 h-screen bg-white border-r flex flex-col justify-between p-6">

    <!-- TOP: APP TITLE -->
    <div>
      <h1 class="text-2xl font-bold mb-8 tracking-tight">Life Admin</h1>

      <!-- NAVIGATION -->
      <nav class="space-y-3 mb-10">
        <RouterLink
          to="/dashboard"
          class="flex items-center gap-3 text-gray-700 hover:text-purple-600 transition"
          :class="{ 'text-purple-600 font-semibold': isActive('/dashboard') }"
        >
          🏠 Dashboard
        </RouterLink>

        <RouterLink
          to="/documents"
          class="flex items-center gap-3 text-gray-700 hover:text-purple-600 transition"
          :class="{ 'text-purple-600 font-semibold': isActive('/documents') }"
        >
          📄 Documents
        </RouterLink>

        <RouterLink
          to="/subscriptions"
          class="flex items-center gap-3 text-gray-700 hover:text-purple-600 transition"
          :class="{ 'text-purple-600 font-semibold': isActive('/subscriptions') }"
        >
          💳 Subscriptions
        </RouterLink>
      </nav>

      <!-- QUICK STATS -->
      <div>
        <h2 class="text-xs font-semibold text-gray-500 uppercase mb-3">Quick Stats</h2>

        <div class="space-y-2 text-sm">
          <div class="flex justify-between">
            <span>💰 Monthly Cost</span>
            <span class="font-semibold">{{ monthlyCost }} €</span>
          </div>

          <div class="flex justify-between">
            <span>⏳ Renewals Soon</span>
            <span class="font-semibold">{{ renewalsSoon }}</span>
          </div>

          <div class="flex justify-between">
            <span>📄 Expiring Soon</span>
            <span class="font-semibold">{{ expiringSoon }}</span>
          </div>

          <div class="flex justify-between">
            <span>📦 Total Items</span>
            <span class="font-semibold">{{ items.length }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- FOOTER -->
    <div class="pt-6 border-t">
      <RouterLink
        to="/settings"
        class="flex items-center gap-3 text-gray-600 hover:text-purple-600 transition"
      >
        ⚙️ Settings
      </RouterLink>

      <div class="mt-4 flex items-center gap-3">
        <div class="w-10 h-10 bg-purple-200 rounded-full flex items-center justify-center font-bold text-purple-700">
          {{ userInitial }}
        </div>
        <div>
          <p class="font-semibold">{{ userName }}</p>
          <p class="text-xs text-gray-500">Logged in</p>
        </div>
      </div>
    </div>

  </aside>
</template>

<script setup>
import { computed } from "vue"
import { useRoute } from "vue-router"
import { useItemsStore } from "../../stores/items"

const route = useRoute()
const itemsStore = useItemsStore()
const items = computed(() => itemsStore.items)

// Active route helper
function isActive(path) {
  return route.path === path
}

// User info (placeholder)
const userName = "Elvis"
const userInitial = userName.charAt(0).toUpperCase()

// Monthly cost
const monthlyCost = computed(() => {
  return items.value
    .filter(i => i.type === "subscription" && i.price)
    .reduce((sum, i) => sum + Number(i.price), 0)
    .toFixed(2)
})

// Renewals soon (next 30 days)
const renewalsSoon = computed(() => {
  const today = new Date()
  return items.value.filter(i => {
    if (i.type !== "subscription" || !i.renewal_date) return false
    const diff = (new Date(i.renewal_date) - today) / (1000 * 60 * 60 * 24)
    return diff >= 0 && diff <= 30
  }).length
})

// Expiring soon (documents + subscriptions with expiration)
const expiringSoon = computed(() => {
  const today = new Date()
  return items.value.filter(i => {
    if (!i.expiration_date) return false
    const diff = (new Date(i.expiration_date) - today) / (1000 * 60 * 60 * 24)
    return diff >= 0 && diff <= 30
  }).length
})
</script>

<style scoped>
aside {
  min-width: 16rem;
}
</style>