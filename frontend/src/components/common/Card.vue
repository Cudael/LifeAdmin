<template>
  <div class="bg-white rounded-2xl shadow-lg border border-gray-100">
    <!-- Header slot or title -->
    <div v-if="title || $slots.header" :class="['border-b border-gray-200', noPadding ? '' : 'p-6']">
      <slot name="header">
        <h3 class="text-xl font-bold text-gray-900">{{ title }}</h3>
      </slot>
    </div>

    <!-- Main content -->
    <div :class="[noPadding ? '' : 'p-6']">
      <slot />
    </div>

    <!-- Footer slot -->
    <div v-if="$slots.footer" :class="['border-t border-gray-200', noPadding ? '' : 'p-6']">
      <slot name="footer" />
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    default: ''
  },
  noPadding: {
    type: Boolean,
    default: false
  }
})
</script>
