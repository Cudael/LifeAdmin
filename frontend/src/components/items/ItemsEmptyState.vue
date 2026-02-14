<script setup>
import { Package } from "lucide-vue-next"

const props = defineProps({
  hasActiveFilters: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['clearFilters'])

function clearFilters() {
  emit('clearFilters')
}
</script>

<template>
  <div class="text-center py-20">
    <Package :size="64" class="text-gray-300 mx-auto mb-4" />
    <h3 class="text-xl font-bold text-gray-900 mb-2">No items found</h3>
    <p class="text-gray-600 mb-6">
      {{ hasActiveFilters
        ? 'Try adjusting your filters or search'
        : 'Get started by adding your first item'
      }}
    </p>
    <div class="flex items-center justify-center gap-3">
      <button
        v-if="hasActiveFilters"
        @click="clearFilters"
        class="px-6 py-3 bg-white text-gray-700 rounded-xl font-medium border-2 border-gray-200 hover:border-gray-300 transition-colors"
      >
        Clear Filters
      </button>
      <RouterLink
        to="/add-item"
        class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl transition-all"
      >
        Add Your First Item
      </RouterLink>
    </div>
  </div>
</template>
