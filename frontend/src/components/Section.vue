<template>
  <div class="mb-10">
    <h2 class="text-xl font-semibold mb-4">{{ title }}</h2>
    <slot />
  </div>
</template>

<script setup>
defineProps({ title: String })
</script>