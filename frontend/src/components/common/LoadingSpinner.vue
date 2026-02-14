<template>
  <div class="flex items-center justify-center">
    <div
      :class="[
        'rounded-full border-4 border-t-transparent spinner-rotate',
        sizeClasses,
        colorClasses
      ]"
      role="status"
      aria-label="Loading"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  size: {
    type: String,
    default: 'md',
    validator: (value) => ['sm', 'md', 'lg'].includes(value)
  },
  color: {
    type: String,
    default: 'teal'
  }
})

const sizeClasses = computed(() => {
  const sizes = {
    sm: 'w-4 h-4',
    md: 'w-8 h-8',
    lg: 'w-12 h-12'
  }
  return sizes[props.size]
})

const colorClasses = computed(() => {
  const colors = {
    teal: 'border-teal-500',
    gray: 'border-gray-500',
    white: 'border-white',
    red: 'border-red-500',
    blue: 'border-blue-500'
  }
  return colors[props.color] || colors.teal
})
</script>

<style scoped>
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.spinner-rotate {
  animation: spin 0.8s linear infinite;
}
</style>
