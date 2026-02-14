<template>
  <div class="relative mb-6">
    <div class="absolute inset-0 flex items-center">
      <div class="w-full border-t border-gray-200"></div>
    </div>
    <div class="relative flex justify-center text-sm">
      <span class="px-4 bg-white/80 text-gray-500 font-medium">{{ text }}</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  text: {
    type: String,
    default: "Or continue with email"
  }
})
</script>
