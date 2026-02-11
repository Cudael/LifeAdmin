<template>
  <div class="relative w-full md:w-96 group">
    <!-- Search Icon -->
    <div class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 transition-colors duration-200"
         :class="{ 'text-teal-500': isFocused || modelValue }">
      <Search :size="20" />
    </div>

    <!-- Input Field -->
    <input
      ref="inputRef"
      :value="modelValue"
      @input="handleInput"
      @focus="isFocused = true"
      @blur="isFocused = false"
      @keydown.esc="clearSearch"
      @keydown.enter="$emit('search', modelValue)"
      type="text"
      :placeholder="placeholder"
      class="w-full pl-12 pr-24 py-3.5 
             bg-white border-2 border-gray-200 
             rounded-xl
             text-gray-900 placeholder-gray-400
             transition-all duration-200
             focus:outline-none focus:border-teal-500 focus:ring-4 focus:ring-teal-100
             hover:border-gray-300
             group-hover:shadow-md"
    />

    <!-- Right Side: Clear Button + Keyboard Shortcut -->
    <div class="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-2">
      
      <!-- Clear Button (shows when there's text) -->
      <Transition
        enter-active-class="transition-all duration-200 ease-out"
        enter-from-class="opacity-0 scale-75"
        enter-to-class="opacity-100 scale-100"
        leave-active-class="transition-all duration-150 ease-in"
        leave-from-class="opacity-100 scale-100"
        leave-to-class="opacity-0 scale-75"
      >
        <button
          v-if="modelValue"
          @click="clearSearch"
          class="p-1.5 rounded-lg text-gray-400 hover:text-gray-600 hover:bg-gray-100 transition-colors duration-200"
          title="Clear search (Esc)"
        >
          <X :size="16" />
        </button>
      </Transition>

      <!-- Keyboard Shortcut Hint (shows when empty and not focused) -->
      <Transition
        enter-active-class="transition-all duration-200 ease-out"
        enter-from-class="opacity-0 scale-75"
        enter-to-class="opacity-100 scale-100"
        leave-active-class="transition-all duration-150 ease-in"
        leave-from-class="opacity-100 scale-100"
        leave-to-class="opacity-0 scale-75"
      >
        <kbd
          v-if="!modelValue && !isFocused && showShortcut"
          class="hidden sm:flex items-center gap-1 px-2 py-1 bg-gray-100 border border-gray-200 rounded text-xs font-mono text-gray-500"
        >
          <Command :size="12" />
          K
        </kbd>
      </Transition>

      <!-- Search Button (optional, shows when there's text) -->
      <Transition
        enter-active-class="transition-all duration-200 ease-out"
        enter-from-class="opacity-0 scale-75"
        enter-to-class="opacity-100 scale-100"
        leave-active-class="transition-all duration-150 ease-in"
        leave-from-class="opacity-100 scale-100"
        leave-to-class="opacity-0 scale-75"
      >
        <button
          v-if="modelValue && showSearchButton"
          @click="$emit('search', modelValue)"
          class="px-3 py-1.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-lg text-sm font-medium hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 shadow-sm hover:shadow-md"
          title="Search (Enter)"
        >
          Search
        </button>
      </Transition>
    </div>

    <!-- Loading Indicator -->
    <Transition
      enter-active-class="transition-opacity duration-200"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-opacity duration-150"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="loading"
        class="absolute right-4 top-1/2 -translate-y-1/2"
      >
        <Loader2 :size="18" class="text-teal-500 animate-spin" />
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { Search, X, Command, Loader2 } from 'lucide-vue-next'

const props = defineProps({
  modelValue: { type: String, default: '' },
  placeholder: { type: String, default: 'Search documents, subscriptions...' },
  loading: { type: Boolean, default: false },
  showShortcut: { type: Boolean, default: true },
  showSearchButton: { type: Boolean, default: false },
  shortcutKey: { type: String, default: 'k' }
})

const emit = defineEmits(['update:modelValue', 'search', 'clear'])

const inputRef = ref(null)
const isFocused = ref(false)

function handleInput(event) {
  emit('update:modelValue', event.target.value)
}

function clearSearch() {
  emit('update:modelValue', '')
  emit('clear')
  inputRef.value?.focus()
}

function focusSearch() {
  inputRef.value?.focus()
}

// Keyboard shortcut (Cmd+K or Ctrl+K)
function handleKeyboardShortcut(e) {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === props.shortcutKey) {
    e.preventDefault()
    focusSearch()
  }
}

onMounted(() => {
  if (props.showShortcut) {
    window.addEventListener('keydown', handleKeyboardShortcut)
  }
})

onUnmounted(() => {
  if (props.showShortcut) {
    window.removeEventListener('keydown', handleKeyboardShortcut)
  }
})

// Expose focus method to parent
defineExpose({
  focus: focusSearch,
  clear: clearSearch
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