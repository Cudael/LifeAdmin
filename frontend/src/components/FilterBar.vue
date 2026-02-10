<template>
  <div class="flex flex-wrap gap-2 mb-6">
    <button
      v-for="cat in categories"
      :key="cat"
      @click="$emit('change', cat)"
      class="px-4 py-2 rounded-full text-sm transition"
      :class="cat === activeCategory
        ? 'bg-blue-600 text-white shadow-sm'
        : 'bg-gray-100 text-gray-700 hover:bg-gray-200'"
    >
      {{ cat }}
    </button>
  </div>
</template>

<script setup>
defineProps({
  activeCategory: String
})

const categories = [
  "All",
  "Health",
  "Finance",
  "Work",
  "Personal",
  "Travel",
  "Subscriptions"
]
</script>