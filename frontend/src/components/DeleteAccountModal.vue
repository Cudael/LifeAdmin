<template>
  <Transition
    enter-active-class="transition-opacity duration-300"
    enter-from-class="opacity-0"
    enter-to-class="opacity-100"
    leave-active-class="transition-opacity duration-200"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div
      v-if="show"
      class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
      @click.self="$emit('cancel')"
    >
      <div
        class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-8 animate-scale-in"
        @click.stop
      >
        
        <!-- Header -->
        <div class="text-center mb-6">
          <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <AlertTriangle :size="32" class="text-red-600" />
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">Delete Account?</h3>
          <p class="text-gray-600">This action cannot be undone!</p>
        </div>

        <!-- Warning List -->
        <div class="bg-red-50 border-2 border-red-200 rounded-xl p-4 mb-6">
          <p class="text-sm font-semibold text-red-900 mb-3">This will permanently delete:</p>
          <ul class="space-y-2 text-sm text-red-800">
            <li class="flex items-center gap-2">
              <div class="w-1.5 h-1.5 rounded-full bg-red-600"></div>
              Your account and profile
            </li>
            <li class="flex items-center gap-2">
              <div class="w-1.5 h-1.5 rounded-full bg-red-600"></div>
              All your items and documents
            </li>
            <li class="flex items-center gap-2">
              <div class="w-1.5 h-1.5 rounded-full bg-red-600"></div>
              All uploaded files
            </li>
            <li class="flex items-center gap-2">
              <div class="w-1.5 h-1.5 rounded-full bg-red-600"></div>
              All settings and preferences
            </li>
          </ul>
        </div>

        <!-- Password Confirmation -->
        <div class="mb-6">
          <label class="block text-sm font-semibold text-gray-700 mb-2">
            Enter your password to confirm
          </label>
          <div class="relative">
            <Lock :size="20" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
            <input
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="Your password"
              class="w-full pl-12 pr-12 py-3 border-2 border-gray-300 rounded-xl focus:border-red-500 focus:outline-none transition-colors"
              :disabled="loading"
              @keyup.enter="handleConfirm"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
            >
              <Eye v-if="!showPassword" :size="20" />
              <EyeOff v-else :size="20" />
            </button>
          </div>
        </div>

        <!-- Error Message -->
        <div v-if="error" class="mb-6 p-3 bg-red-50 border border-red-200 rounded-xl">
          <p class="text-sm text-red-800 text-center">{{ error }}</p>
        </div>

        <!-- Checkbox Confirmation -->
        <label class="flex items-start gap-3 mb-6 cursor-pointer">
          <input
            v-model="confirmed"
            type="checkbox"
            class="w-5 h-5 mt-0.5 text-red-600 border-gray-300 rounded focus:ring-red-500"
          />
          <span class="text-sm text-gray-700">
            I understand this action is permanent and cannot be undone
          </span>
        </label>

        <!-- Buttons -->
        <div class="flex gap-3">
          <button
            @click="$emit('cancel')"
            :disabled="loading"
            class="flex-1 px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-colors disabled:opacity-50"
          >
            Cancel
          </button>
          <button
            @click="handleConfirm"
            :disabled="!canDelete || loading"
            class="flex-1 px-6 py-3 bg-red-600 text-white rounded-xl font-semibold hover:bg-red-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            <Loader2 v-if="loading" :size="20" class="animate-spin" />
            <Trash2 v-else :size="20" />
            <span>{{ loading ? 'Deleting...' : 'Delete Forever' }}</span>
          </button>
        </div>

      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, computed, watch } from "vue"
import {
  AlertTriangle,
  Lock,
  Eye,
  EyeOff,
  Trash2,
  Loader2
} from "lucide-vue-next"

const props = defineProps({
  show: Boolean,
  loading: Boolean,
  error: String
})

const emit = defineEmits(['cancel', 'confirm'])

const password = ref("")
const confirmed = ref(false)
const showPassword = ref(false)

const canDelete = computed(() => {
  return password.value.length >= 8 && confirmed.value
})

function handleConfirm() {
  if (canDelete.value) {
    emit('confirm', password.value)
  }
}

// Reset when modal closes
watch(() => props.show, (newVal) => {
  if (!newVal) {
    password.value = ""
    confirmed.value = false
    showPassword.value = false
  }
})
</script>

<style scoped>
@keyframes scale-in {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-scale-in {
  animation: scale-in 0.2s ease-out;
}
</style>