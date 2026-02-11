<template>
  <Teleport to="body">
    <Transition
      enter-active-class="transition-all duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-150 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="show"
        class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4"
        @click.self="handleBackdropClick"
      >
        <Transition
          enter-active-class="transition-all duration-200 ease-out"
          enter-from-class="opacity-0 scale-95 translate-y-4"
          enter-to-class="opacity-100 scale-100 translate-y-0"
          leave-active-class="transition-all duration-150 ease-in"
          leave-from-class="opacity-100 scale-100 translate-y-0"
          leave-to-class="opacity-0 scale-95 translate-y-4"
        >
          <div
            v-if="show"
            class="bg-white rounded-2xl shadow-2xl w-full max-w-md"
            role="dialog"
            aria-modal="true"
            :aria-labelledby="titleId"
          >
            <!-- Header -->
            <div class="p-6 pb-4">
              <div class="flex items-start gap-4">
                <!-- Icon -->
                <div
                  class="flex-shrink-0 w-12 h-12 rounded-full flex items-center justify-center"
                  :class="iconBgColor"
                >
                  <component
                    :is="icon"
                    :size="24"
                    :class="iconColor"
                  />
                </div>

                <!-- Content -->
                <div class="flex-1">
                  <h3
                    :id="titleId"
                    class="text-xl font-bold text-gray-900 mb-1"
                  >
                    {{ title }}
                  </h3>
                  <p class="text-sm text-gray-600">
                    {{ message }}
                  </p>
                </div>

                <!-- Close Button -->
                <button
                  v-if="showCloseButton"
                  @click="handleCancel"
                  class="flex-shrink-0 p-1 text-gray-400 hover:text-gray-600 rounded-lg hover:bg-gray-100 transition-colors"
                  aria-label="Close"
                >
                  <X :size="20" />
                </button>
              </div>
            </div>

            <!-- Item Details (Optional) -->
            <div
              v-if="itemName || $slots.details"
              class="px-6 pb-4"
            >
              <div class="p-4 bg-gray-50 rounded-xl">
                <slot name="details">
                  <div class="flex items-center gap-3">
                    <div
                      v-if="itemIcon"
                      class="w-10 h-10 rounded-lg bg-white border border-gray-200 flex items-center justify-center flex-shrink-0"
                    >
                      <component :is="itemIcon" :size="20" class="text-gray-600" />
                    </div>
                    <div class="flex-1 min-w-0">
                      <p class="font-semibold text-gray-900 truncate">{{ itemName }}</p>
                      <p v-if="itemDescription" class="text-sm text-gray-600 truncate">{{ itemDescription }}</p>
                    </div>
                  </div>
                </slot>
              </div>
            </div>

            <!-- Warning Message -->
            <div
              v-if="warningMessage || permanent"
              class="px-6 pb-4"
            >
              <div class="flex items-start gap-2 p-3 bg-red-50 border border-red-200 rounded-xl">
                <AlertTriangle :size="16" class="text-red-600 flex-shrink-0 mt-0.5" />
                <div class="text-sm text-red-800">
                  <p v-if="warningMessage">{{ warningMessage }}</p>
                  <p v-else-if="permanent">
                    <strong>This action cannot be undone.</strong> All data will be permanently deleted.
                  </p>
                </div>
              </div>
            </div>

            <!-- Confirmation Input -->
            <div
              v-if="requireConfirmation"
              class="px-6 pb-4"
            >
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Type <span class="font-mono font-bold text-red-600">{{ confirmationText }}</span> to confirm:
              </label>
              <input
                ref="confirmInputRef"
                v-model="confirmationInput"
                type="text"
                class="w-full px-4 py-2 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-red-500 focus:border-transparent"
                :placeholder="`Type ${confirmationText}`"
                @keydown.enter="handleConfirmWithEnter"
                @keydown.esc="handleCancel"
              />
            </div>

            <!-- Actions -->
            <div class="px-6 pb-6">
              <div class="flex gap-3">
                <button
                  @click="handleCancel"
                  :disabled="loading"
                  class="flex-1 px-4 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {{ cancelText }}
                </button>

                <button
                  @click="handleConfirm"
                  :disabled="!canConfirm || loading"
                  class="flex-1 px-4 py-3 text-white rounded-xl font-semibold transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                  :class="[
                    danger 
                      ? 'bg-red-600 hover:bg-red-700 shadow-lg shadow-red-200' 
                      : 'bg-teal-600 hover:bg-teal-700 shadow-lg shadow-teal-200'
                  ]"
                >
                  <Loader2 v-if="loading" :size="18" class="animate-spin" />
                  <component v-else-if="confirmIcon" :is="confirmIcon" :size="18" />
                  <span>{{ loading ? loadingText : confirmText }}</span>
                </button>
              </div>
            </div>

          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup>
import { ref, computed, watch, nextTick } from 'vue'
import { AlertTriangle, Trash2, X, Loader2 } from 'lucide-vue-next'

const props = defineProps({
  show: { type: Boolean, default: false },
  title: { type: String, default: 'Delete Item?' },
  message: { type: String, default: 'Are you sure you want to delete this item? This action cannot be undone.' },
  
  // Item details
  itemName: { type: String, default: '' },
  itemDescription: { type: String, default: '' },
  itemIcon: { type: [Object, Function], default: null },
  
  // Appearance
  icon: { type: [Object, Function], default: () => AlertTriangle },
  iconBgColor: { type: String, default: 'bg-red-100' },
  iconColor: { type: String, default: 'text-red-600' },
  danger: { type: Boolean, default: true },
  
  // Button text
  confirmText: { type: String, default: 'Delete' },
  cancelText: { type: String, default: 'Cancel' },
  loadingText: { type: String, default: 'Deleting...' },
  
  // Icons
  confirmIcon: { type: [Object, Function], default: () => Trash2 },
  
  // Behavior
  permanent: { type: Boolean, default: true },
  warningMessage: { type: String, default: '' },
  requireConfirmation: { type: Boolean, default: false },
  confirmationText: { type: String, default: 'DELETE' },
  closeOnBackdrop: { type: Boolean, default: true },
  showCloseButton: { type: Boolean, default: true },
  loading: { type: Boolean, default: false }
})

const emit = defineEmits(['confirm', 'cancel', 'close'])

const confirmationInput = ref('')
const confirmInputRef = ref(null)
const titleId = `modal-title-${Math.random().toString(36).substr(2, 9)}`

const canConfirm = computed(() => {
  if (props.loading) return false
  if (props.requireConfirmation) {
    return confirmationInput.value === props.confirmationText
  }
  return true
})

function handleConfirm() {
  if (!canConfirm.value) return
  emit('confirm')
}

function handleConfirmWithEnter() {
  if (canConfirm.value) {
    handleConfirm()
  }
}

function handleCancel() {
  if (props.loading) return
  confirmationInput.value = ''
  emit('cancel')
  emit('close')
}

function handleBackdropClick() {
  if (props.closeOnBackdrop && !props.loading) {
    handleCancel()
  }
}

// Focus confirmation input when modal opens
watch(() => props.show, async (newVal) => {
  if (newVal && props.requireConfirmation) {
    await nextTick()
    confirmInputRef.value?.focus()
  }
  
  // Reset confirmation input when modal closes
  if (!newVal) {
    confirmationInput.value = ''
  }
})

// Prevent body scroll when modal is open
watch(() => props.show, (newVal) => {
  if (newVal) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
})
</script>

<style scoped>
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>