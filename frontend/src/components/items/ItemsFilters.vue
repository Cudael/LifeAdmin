<script setup>
import { Filter } from "lucide-vue-next"
import FilterBar from "../FilterBar.vue"

const props = defineProps({
  activeCategory: {
    type: String,
    required: true
  },
  activeStatFilter: {
    type: String,
    required: true
  },
  categoryFilters: {
    type: Array,
    required: true
  },
  showFilters: {
    type: Boolean,
    required: true
  },
  hasActiveFilters: {
    type: Boolean,
    required: true
  },
  search: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['update:showFilters', 'update:activeCategory', 'update:activeStatFilter', 'update:search', 'clearFilters'])

function toggleFilters() {
  emit('update:showFilters', !props.showFilters)
}

function setCategory(cat) {
  emit('update:activeCategory', cat)
}

function setFilter(filter) {
  emit('update:activeStatFilter', filter)
}

function clearFilters() {
  emit('clearFilters')
}

function clearSearch() {
  emit('update:search', '')
}
</script>

<template>
  <div>
    <!-- Filters Button -->
    <button
      @click="toggleFilters"
      class="relative px-4 py-2 bg-gray-800 border-2 border-gray-700 text-gray-300 rounded-xl font-semibold hover:border-teal-300 hover:shadow-md transition-all duration-200 flex items-center gap-2"
    >
      <Filter :size="18" />
      <span class="hidden md:inline">Filters</span>
      
      <!-- Active indicator dot -->
      <span 
        v-if="hasActiveFilters"
        class="absolute -top-1 -right-1 w-3 h-3 bg-teal-500 rounded-full border-2 border-gray-950"
      ></span>
    </button>

    <!-- ACTIVE FILTERS CHIPS -->
    <div 
      v-if="hasActiveFilters"
      class="mt-4 flex items-center gap-2 flex-wrap"
    >
      <span class="text-xs text-gray-400 font-medium">Active:</span>
      
      <button
        v-if="activeStatFilter !== 'all'"
        @click="setFilter('all')"
        class="px-3 py-1 bg-teal-900/40 text-teal-400 text-xs rounded-full font-medium hover:bg-teal-900/60 transition-colors flex items-center gap-1"
      >
        {{ activeStatFilter }}
        <span class="text-teal-400">×</span>
      </button>
      
      <button
        v-if="activeCategory !== 'All'"
        @click="setCategory('All')"
        class="px-3 py-1 bg-cyan-100 text-cyan-700 text-xs rounded-full font-medium hover:bg-cyan-200 transition-colors flex items-center gap-1"
      >
        {{ activeCategory }}
        <span class="text-cyan-600">×</span>
      </button>
      
      <button
        v-if="search"
        @click="clearSearch"
        class="px-3 py-1 bg-blue-100 text-blue-700 text-xs rounded-full font-medium hover:bg-blue-200 transition-colors flex items-center gap-1"
      >
        "{{ search }}"
        <span class="text-blue-600">×</span>
      </button>

      <button
        @click="clearFilters"
        class="text-xs text-gray-400 hover:text-gray-300 font-medium underline"
      >
        Clear all
      </button>
    </div>

    <!-- COLLAPSIBLE FILTERS -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-4 max-h-0"
      enter-to-class="opacity-100 translate-y-0 max-h-[1000px]"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0 max-h-[1000px]"
      leave-to-class="opacity-0 -translate-y-4 max-h-0"
    >
      <div v-show="showFilters" class="mt-4 overflow-hidden">
        <div class="bg-gray-900 rounded-2xl shadow-lg border border-gray-800 p-6 space-y-6">
          
          <!-- Status Filters -->
          <div>
            <h3 class="text-sm font-semibold text-gray-300 mb-3">Status</h3>
            <div class="flex flex-wrap gap-2">
              <button
                v-for="filter in ['all', 'expired', 'week', 'soon', 'missingDocs']"
                :key="filter"
                @click="setFilter(filter)"
                :class="[
                  'px-4 py-2 rounded-lg text-sm font-medium transition-all',
                  activeStatFilter === filter
                    ? 'bg-teal-500 text-white shadow-md'
                    : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
                ]"
              >
                {{ filter === 'all' ? 'All' : filter === 'week' ? 'This Week' : filter === 'missingDocs' ? 'Missing Docs' : filter.charAt(0).toUpperCase() + filter.slice(1) }}
              </button>
            </div>
          </div>

          <!-- Category Filters -->
          <div>
            <h3 class="text-sm font-semibold text-gray-300 mb-3">Categories</h3>
            <FilterBar 
              :activeCategory="activeCategory" 
              :categories="categoryFilters"
              :show-clear-button="false"
              :show-summary="false"
              @change="setCategory" 
            />
          </div>

        </div>
      </div>
    </Transition>
  </div>
</template>
