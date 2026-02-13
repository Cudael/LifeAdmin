<template>
  <div class="relative">
    <input
      v-model="inputValue"
      @input="onInput"
      @focus="showSuggestions = true"
      @blur="onBlur"
      @keydown.down.prevent="navigateDown"
      @keydown.up.prevent="navigateUp"
      @keydown.enter.prevent="selectCurrent"
      @keydown.escape="showSuggestions = false"
      class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl transition-all duration-200 bg-white/50"
      :class="focusClasses"
      :placeholder="placeholder"
      :required="required"
      :disabled="disabled"
    />
    
    <Transition name="dropdown">
      <div
        v-if="showSuggestions && filteredSuggestions.length"
        class="absolute z-50 w-full mt-2 bg-white border-2 border-gray-200 rounded-xl shadow-xl max-h-60 overflow-y-auto"
      >
        <button
          v-for="(suggestion, index) in filteredSuggestions"
          :key="suggestion.value"
          @mousedown.prevent="selectSuggestion(suggestion)"
          @mouseenter="selectedIndex = index"
          :class="['w-full px-4 py-3 text-left transition-colors flex items-center gap-3', 
                   selectedIndex === index ? hoverClasses : '']"
        >
          <span class="text-2xl">{{ suggestion.icon }}</span>
          <div>
            <p class="font-semibold text-gray-900">{{ suggestion.label }}</p>
            <p class="text-xs text-gray-500">{{ suggestion.description }}</p>
          </div>
        </button>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue"

const props = defineProps({
  modelValue: {
    type: String,
    default: ""
  },
  suggestions: {
    type: Array,
    default: () => []
  },
  placeholder: {
    type: String,
    default: ""
  },
  required: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  color: {
    type: String,
    default: "teal",
    validator: (value) => ["teal", "purple"].includes(value)
  }
})

const emit = defineEmits(["update:modelValue"])

const BLUR_DELAY = 200 // Delay in milliseconds to allow click events on suggestions to fire
const inputValue = ref(props.modelValue)
const showSuggestions = ref(false)
const selectedIndex = ref(0)

// Watch for external changes to modelValue
watch(() => props.modelValue, (newValue) => {
  inputValue.value = newValue
})

// Filtered suggestions based on input
const filteredSuggestions = computed(() => {
  if (!inputValue.value) {
    return props.suggestions
  }
  
  const searchTerm = inputValue.value.toLowerCase()
  return props.suggestions.filter(suggestion => 
    suggestion.label.toLowerCase().includes(searchTerm) ||
    suggestion.value.toLowerCase().includes(searchTerm) ||
    suggestion.description.toLowerCase().includes(searchTerm)
  )
})

// Dynamic focus classes based on color prop
const focusClasses = computed(() => {
  if (props.color === "teal") {
    return "focus:ring-2 focus:ring-teal-500 focus:border-teal-500"
  } else if (props.color === "purple") {
    return "focus:ring-2 focus:ring-purple-500 focus:border-purple-500"
  }
  return ""
})

// Dynamic hover classes based on color prop
const hoverClasses = computed(() => {
  if (props.color === "teal") {
    return "bg-gradient-to-r from-teal-50 to-cyan-50"
  } else if (props.color === "purple") {
    return "bg-gradient-to-r from-purple-50 to-pink-50"
  }
  return ""
})

// Handle input changes
function onInput() {
  emit("update:modelValue", inputValue.value)
  showSuggestions.value = true
  selectedIndex.value = 0
}

// Select a suggestion
function selectSuggestion(suggestion) {
  inputValue.value = suggestion.value
  emit("update:modelValue", suggestion.value)
  showSuggestions.value = false
}

// Handle blur event
function onBlur() {
  // Delay to allow click events on suggestions to fire first
  setTimeout(() => {
    showSuggestions.value = false
  }, BLUR_DELAY)
}

// Navigate down in suggestions
function navigateDown() {
  if (selectedIndex.value < filteredSuggestions.value.length - 1) {
    selectedIndex.value++
  }
}

// Navigate up in suggestions
function navigateUp() {
  if (selectedIndex.value > 0) {
    selectedIndex.value--
  }
}

// Select currently highlighted suggestion
function selectCurrent() {
  if (filteredSuggestions.value.length > 0 && showSuggestions.value) {
    selectSuggestion(filteredSuggestions.value[selectedIndex.value])
  }
}
</script>

<style scoped>
/* Dropdown transition */
.dropdown-enter-active {
  transition: all 0.3s ease-out;
}

.dropdown-leave-active {
  transition: all 0.2s ease-in;
}

.dropdown-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}

.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
