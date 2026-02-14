<template>
  <div class="flex flex-col items-center justify-center py-12 px-4 text-center">
    <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-teal-100 to-cyan-100 flex items-center justify-center mb-6">
      <component
        v-if="icon"
        :is="icon"
        :size="32"
        class="text-teal-600"
      />
    </div>

    <h3 class="text-xl font-bold text-gray-900 mb-2">
      {{ title }}
    </h3>

    <p class="text-gray-600 mb-6 max-w-md">
      {{ message }}
    </p>

    <div v-if="actionText || $slots.actions">
      <slot name="actions">
        <button
          v-if="actionText"
          @click="handleAction"
          class="inline-flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-200"
        >
          {{ actionText }}
        </button>
      </slot>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  icon: {
    type: [Object, Function],
    default: null
  },
  title: {
    type: String,
    default: 'No items found'
  },
  message: {
    type: String,
    default: 'Get started by adding your first item.'
  },
  actionText: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['action'])

function handleAction() {
  emit('action')
}
</script>
