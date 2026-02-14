<template>
  <div
    v-if="message"
    class="mb-6 p-4 bg-red-50 border-2 border-red-200 rounded-xl flex items-start gap-3 animate-shake"
  >
    <AlertCircle :size="20" class="text-red-500 flex-shrink-0 mt-0.5" />
    <p class="text-sm text-red-700">{{ message }}</p>
  </div>
</template>

<script setup>
import { AlertCircle } from "lucide-vue-next"

defineProps({
  message: {
    type: String,
    default: ""
  }
})
</script>

<style scoped>
@keyframes shake {
  0%, 100% {
    transform: translateX(0);
  }
  10%, 30%, 50%, 70%, 90% {
    transform: translateX(-5px);
  }
  20%, 40%, 60%, 80% {
    transform: translateX(5px);
  }
}

.animate-shake {
  animation: shake 0.5s ease-in-out;
}
</style>
