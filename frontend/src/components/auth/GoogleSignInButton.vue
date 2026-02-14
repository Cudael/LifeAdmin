<template>
  <button
    @click="handleClick"
    :disabled="disabled"
    type="button"
    class="w-full flex items-center justify-center gap-3 px-6 py-4 bg-white border-2 border-gray-300 rounded-xl font-semibold text-gray-700 hover:bg-gray-50 hover:border-gray-400 hover:shadow-md transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed group"
  >
    <img 
      src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" 
      alt="Google" 
      class="w-6 h-6"
    />
    <span>Continue with Google</span>
  </button>
</template>

<script setup>
const props = defineProps({
  disabled: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['click'])

function handleClick() {
  emit('click')
}
</script>
