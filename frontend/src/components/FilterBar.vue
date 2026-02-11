<template>
  <div class="relative">
    
    <!-- Desktop Filter Bar -->
    <div class="hidden lg:flex items-center gap-3 mb-6 overflow-x-auto pb-2 scrollbar-hide">
      
      <!-- Filter Label -->
      <div class="flex items-center gap-2 mr-2 flex-shrink-0">
        <Filter :size="18" class="text-gray-500" />
        <span class="text-sm font-medium text-gray-700">Filter:</span>
      </div>

      <!-- Filter Buttons -->
      <button
        v-for="category in categories"
        :key="category.value"
        @click="$emit('change', category.value)"
        class="group relative px-5 py-2.5 rounded-full text-sm font-medium transition-all duration-200 flex items-center gap-2 flex-shrink-0"
        :class="category.value === activeCategory
          ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white shadow-lg shadow-teal-200 scale-105'
          : 'bg-white text-gray-700 border-2 border-gray-200 hover:border-teal-300 hover:shadow-md hover:scale-102'"
      >
        <!-- Icon -->
        <component
          v-if="category.icon"
          :is="category.icon"
          :size="16"
          :class="category.value === activeCategory ? 'text-white' : 'text-gray-500 group-hover:text-teal-600'"
        />
        
        <!-- Label -->
        <span>{{ category.label }}</span>
        
        <!-- Count Badge -->
        <span
          v-if="category.count !== undefined"
          class="px-2 py-0.5 rounded-full text-xs font-semibold transition-colors"
          :class="category.value === activeCategory
            ? 'bg-white/20 text-white'
            : 'bg-gray-100 text-gray-600 group-hover:bg-teal-100 group-hover:text-teal-700'"
        >
          {{ category.count }}
        </span>

        <!-- Active Indicator -->
        <div
          v-if="category.value === activeCategory"
          class="absolute -bottom-1 left-1/2 -translate-x-1/2 w-1.5 h-1.5 bg-white rounded-full"
        ></div>
      </button>

      <!-- Clear All Button -->
      <Transition
        enter-active-class="transition-all duration-200 ease-out"
        enter-from-class="opacity-0 scale-75"
        enter-to-class="opacity-100 scale-100"
        leave-active-class="transition-all duration-150 ease-in"
        leave-from-class="opacity-100 scale-100"
        leave-to-class="opacity-0 scale-75"
      >
        <button
          v-if="activeCategory !== 'all' && showClearButton"
          @click="$emit('change', 'all')"
          class="ml-2 px-4 py-2 text-sm font-medium text-gray-600 hover:text-gray-900 underline decoration-dotted underline-offset-4 flex-shrink-0"
        >
          Clear filters
        </button>
      </Transition>
    </div>

    <!-- Mobile/Tablet Dropdown Filter -->
    <div class="lg:hidden mb-6">
      <div class="relative">
        <button
          @click="showMobileDropdown = !showMobileDropdown"
          class="w-full flex items-center justify-between px-4 py-3 bg-white border-2 border-gray-200 rounded-xl text-sm font-medium text-gray-700 hover:border-teal-300 transition-colors"
        >
          <div class="flex items-center gap-2">
            <Filter :size="18" class="text-gray-500" />
            <span>{{ activeLabel }}</span>
            <span
              v-if="activeCategoryData?.count !== undefined"
              class="px-2 py-0.5 bg-teal-100 text-teal-700 rounded-full text-xs font-semibold"
            >
              {{ activeCategoryData.count }}
            </span>
          </div>
          <ChevronDown
            :size="20"
            class="text-gray-400 transition-transform duration-200"
            :class="{ 'rotate-180': showMobileDropdown }"
          />
        </button>

        <!-- Dropdown Menu -->
        <Transition
          enter-active-class="transition-all duration-200 ease-out"
          enter-from-class="opacity-0 -translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition-all duration-150 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 -translate-y-2"
        >
          <div
            v-if="showMobileDropdown"
            v-click-outside="closeMobileDropdown"
            class="absolute top-full left-0 right-0 mt-2 bg-white border-2 border-gray-200 rounded-xl shadow-xl z-50 py-2 max-h-96 overflow-y-auto"
          >
            <button
              v-for="category in categories"
              :key="category.value"
              @click="selectCategory(category.value)"
              class="w-full flex items-center justify-between px-4 py-3 text-left hover:bg-gray-50 transition-colors"
              :class="{ 'bg-teal-50': category.value === activeCategory }"
            >
              <div class="flex items-center gap-3">
                <component
                  v-if="category.icon"
                  :is="category.icon"
                  :size="18"
                  :class="category.value === activeCategory ? 'text-teal-600' : 'text-gray-500'"
                />
                <span
                  class="font-medium"
                  :class="category.value === activeCategory ? 'text-teal-900' : 'text-gray-700'"
                >
                  {{ category.label }}
                </span>
              </div>
              <div class="flex items-center gap-2">
                <span
                  v-if="category.count !== undefined"
                  class="px-2 py-0.5 rounded-full text-xs font-semibold"
                  :class="category.value === activeCategory
                    ? 'bg-teal-100 text-teal-700'
                    : 'bg-gray-100 text-gray-600'"
                >
                  {{ category.count }}
                </span>
                <Check
                  v-if="category.value === activeCategory"
                  :size="18"
                  class="text-teal-600"
                />
              </div>
            </button>
          </div>
        </Transition>
      </div>
    </div>

    <!-- Active Filters Summary (optional) -->
    <Transition
      enter-active-class="transition-all duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div
        v-if="activeCategory !== 'all' && showSummary"
        class="mb-4 p-3 bg-teal-50 border border-teal-200 rounded-xl flex items-center justify-between"
      >
        <div class="flex items-center gap-2 text-sm">
          <Info :size="16" class="text-teal-600" />
          <span class="text-teal-900">
            Showing <strong>{{ activeCategoryData?.count || 0 }}</strong> items in <strong>{{ activeLabel }}</strong>
          </span>
        </div>
        <button
          @click="$emit('change', 'all')"
          class="text-teal-600 hover:text-teal-700 font-medium text-sm"
        >
          Clear
        </button>
      </div>
    </Transition>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import {
  Filter,
  ChevronDown,
  Check,
  Info,
  Layers,
  Heart,
  Wallet,
  Briefcase,
  User,
  Plane,
  Repeat
} from 'lucide-vue-next'

const props = defineProps({
  activeCategory: { type: String, default: 'all' },
  categories: {
    type: Array,
    default: () => [
      { label: 'All', value: 'all', icon: Layers, count: 45 },
      { label: 'Health', value: 'health', icon: Heart, count: 8 },
      { label: 'Finance', value: 'finance', icon: Wallet, count: 12 },
      { label: 'Work', value: 'work', icon: Briefcase, count: 6 },
      { label: 'Personal', value: 'personal', icon: User, count: 10 },
      { label: 'Travel', value: 'travel', icon: Plane, count: 4 },
      { label: 'Subscriptions', value: 'subscriptions', icon: Repeat, count: 5 }
    ]
  },
  showClearButton: { type: Boolean, default: true },
  showSummary: { type: Boolean, default: true }
})

defineEmits(['change'])

const showMobileDropdown = ref(false)

const activeCategoryData = computed(() => {
  return props.categories.find(cat => cat.value === props.activeCategory)
})

const activeLabel = computed(() => {
  return activeCategoryData.value?.label || 'All'
})

function selectCategory(category) {
  props.$emit('change', category)
  showMobileDropdown.value = false
}

function closeMobileDropdown() {
  showMobileDropdown.value = false
}

// Click outside directive
const vClickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = function(event) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value()
      }
    }
    document.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted(el) {
    document.removeEventListener('click', el.clickOutsideEvent)
  }
}
</script>

<style scoped>
/* Hide scrollbar but keep functionality */
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

/* Smooth scale */
.scale-102 {
  transform: scale(1.02);
}
</style>