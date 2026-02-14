<template>
  <Transition
    enter-active-class="transition-all duration-200 ease-out"
    enter-from-class="opacity-0 translate-y-2"
    enter-to-class="opacity-100 translate-y-0"
    leave-active-class="transition-all duration-150 ease-in"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div
      v-if="visible"
      :class="[
        'flex items-start gap-3 p-4 rounded-xl border',
        typeClasses
      ]"
      role="alert"
    >
      <component
        :is="icon"
        :size="20"
        class="flex-shrink-0 mt-0.5"
      />
      
      <div class="flex-1 min-w-0">
        <p class="text-sm font-medium">{{ message }}</p>
      </div>

      <button
        v-if="dismissible"
        @click="handleDismiss"
        class="flex-shrink-0 p-1 rounded-lg hover:bg-black/5 transition-colors"
        aria-label="Dismiss"
      >
        <X :size="16" />
      </button>
    </div>
  </Transition>
</template>

<script setup>
import { ref, computed } from 'vue'
import { CheckCircle, XCircle, AlertTriangle, Info, X } from 'lucide-vue-next'

const props = defineProps({
  type: {
    type: String,
    default: 'info',
    validator: (value) => ['success', 'error', 'warning', 'info'].includes(value)
  },
  message: {
    type: String,
    required: true
  },
  dismissible: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['dismiss'])

const visible = ref(true)

const typeConfig = {
  success: {
    icon: CheckCircle,
    classes: 'bg-green-50 border-green-200 text-green-800'
  },
  error: {
    icon: XCircle,
    classes: 'bg-red-50 border-red-200 text-red-800'
  },
  warning: {
    icon: AlertTriangle,
    classes: 'bg-orange-50 border-orange-200 text-orange-800'
  },
  info: {
    icon: Info,
    classes: 'bg-blue-50 border-blue-200 text-blue-800'
  }
}

const icon = computed(() => typeConfig[props.type].icon)
const typeClasses = computed(() => typeConfig[props.type].classes)

function handleDismiss() {
  visible.value = false
  emit('dismiss')
}
</script>
