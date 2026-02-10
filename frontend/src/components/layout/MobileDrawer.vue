<template>
  <div
    v-if="open"
    class="fixed top-0 left-0 z-40 w-64 h-screen p-4 bg-white border-r border-gray-200"
  >
    <h2 class="text-xl font-bold mb-4">Life Admin</h2>

    <nav class="space-y-1">
      <RouterLink @click="close" to="/dashboard" class="block px-4 py-2 rounded-lg bg-blue-600 text-white">
        Dashboard
      </RouterLink>

      <RouterLink @click="close" to="/items" class="block px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100">
        Items
      </RouterLink>

      <RouterLink @click="close" to="/add-item" class="block px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100">
        Add Item
      </RouterLink>

      <RouterLink @click="close" to="/settings" class="block px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100">
        Settings
      </RouterLink>

      <button @click="logout" class="block w-full text-left px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100">
        Logout
      </button>
    </nav>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router"

defineProps({
  open: Boolean
})

const emit = defineEmits(["close"])

const router = useRouter()

function close() {
  emit("close")
}

function logout() {
  localStorage.removeItem("token")
  router.push("/login")
}
</script>