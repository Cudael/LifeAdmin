<script setup>
import { PlusCircle } from "lucide-vue-next"

defineProps({
  pageTitle: {
    type: String,
    default: "Items"
  }
})
</script>

<template>
  <RouterLink
    to="/add-item"
    class="group px-5 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg shadow-teal-500/30 hover:shadow-xl hover:shadow-teal-500/40 hover:scale-105 transition-all duration-200 flex items-center gap-2"
  >
    <PlusCircle :size="18" class="group-hover:rotate-90 transition-transform duration-200" />
    Add Item
  </RouterLink>
</template>
