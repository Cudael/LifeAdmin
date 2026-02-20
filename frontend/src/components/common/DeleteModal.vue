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
        class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center z-50 p-4"
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
            class="relative overflow-hidden bg-rose-950/80 backdrop-blur-xl border border-rose-500/30 rounded-[2rem] shadow-2xl w-full max-w-md"
            role="dialog"
            aria-modal="true"
            :aria-labelledby="titleId"
          >
            <!-- Warning Halo Glow -->
            <div class="absolute -top-24 -right-24 w-64 h-64 bg-rose-500/20 blur-[80px] rounded-full pointer-events-none"></div>

            <!-- Header -->
            <div class="relative z-10 p-6 pb-4">
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
                    class="text-xl font-bold text-white mb-1 tracking-tight"
                  >
                    {{ title }}
                  </h3>
                  <p class="text-sm text-rose-200/70">
                    {{ message }}
                  </p>
                </div>

                <!-- Close Button -->
                <button
                  v-if="showCloseButton"
                  @click="handleCancel"
                  class="flex-shrink-0 p-1 text-rose-400/60 hover:text-rose-300 rounded-lg hover:bg-rose-500/10 transition-colors"
                  aria-label="Close"
                >
                  <X :size="20" />
                </button>
              </div>
            </div>

            <!-- Item Details (Optional) -->
            <div
              v-if="itemName || $slots.details"
              class="relative z-10 px-6 pb-4"
            >
              <div class="p-4 bg-rose-900/20 border border-rose-500/20 rounded-xl">
                <slot name="details">
                  <div class="flex items-center gap-3">
                    <div
                      v-if="itemIcon"
                      class="w-10 h-10 rounded-lg bg-rose-900/40 border border-rose-500/20 flex items-center justify-center flex-shrink-0"
                    >
                      <component :is="itemIcon" :size="20" class="text-rose-300" />
                    </div>
                    <div class="flex-1 min-w-0">
                      <p class="font-semibold text-white truncate">{{ itemName }}</p>
                      <p v-if="itemDescription" class="text-sm text-rose-200/60 truncate">{{ itemDescription }}</p>
                    </div>
                  </div>
                </slot>
              </div>
            </div>

            <!-- Warning Message -->
            <div
              v-if="warningMessage || permanent"
              class="relative z-10 px-6 pb-4"
            >
              <div class="flex items-start gap-2 p-3 bg-rose-900/30 border border-rose-500/30 rounded-xl">
                <AlertTriangle :size="16" class="text-rose-400 flex-shrink-0 mt-0.5" />
                <div class="text-sm text-rose-300">
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
              class="relative z-10 px-6 pb-4"
            >
              <label class="block text-sm font-medium text-rose-300/80 mb-2">
                Type <span class="font-mono font-bold text-rose-400">{{ confirmationText }}</span> to confirm:
              </label>
              <input
                ref="confirmInputRef"
                v-model="confirmationInput"
                type="text"
                class="w-full px-4 py-2 bg-slate-950/50 border border-rose-500/30 text-white placeholder:text-slate-600 rounded-xl focus:ring-1 focus:ring-rose-500/50 focus:border-rose-500/50 shadow-inner"
                :placeholder="`Type ${confirmationText}`"
                @keydown.enter="handleConfirmWithEnter"
                @keydown.esc="handleCancel"
              />
            </div>

            <!-- Actions -->
            <div class="relative z-10 px-6 pb-6">
              <div class="flex gap-3">
                <button
                  @click="handleCancel"
                  :disabled="loading"
                  class="flex-1 px-4 py-3 bg-slate-900/60 border border-white/5 text-slate-300 rounded-xl font-semibold hover:bg-slate-800/60 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {{ cancelText }}
                </button>

                <button
                  @click="handleConfirm"
                  :disabled="!canConfirm || loading"
                  class="flex-1 px-4 py-3 text-white rounded-xl font-semibold transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                  :class="[
                    danger
                      ? 'bg-rose-500/10 hover:bg-rose-500 border border-rose-500/50 hover:border-transparent text-rose-400 hover:text-white shadow-[0_0_20px_rgba(225,29,72,0.1)] hover:shadow-[0_0_30px_rgba(225,29,72,0.5)]'
                      : 'bg-teal-600 hover:bg-teal-700 shadow-lg shadow-teal-900/50'
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
  iconBgColor: { type: String, default: 'bg-rose-500/20' },
  iconColor: { type: String, default: 'text-rose-400' },
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
