<template>
  <input
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
    type="text"
    placeholder="Search..."
    class="w-full md:w-80 p-3 border rounded-lg focus:ring-blue-500 focus:border-blue-500"
  />
</template>

<script setup>
defineProps({
  modelValue: String
})
</script>