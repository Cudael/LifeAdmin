<template>
  <div class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] p-6 sm:p-8 border border-white/5 shadow-2xl w-full">
    
    <div class="flex items-center justify-between mb-8">
      <h3 class="text-lg font-bold text-white flex items-center gap-2 tracking-tight">
        <Filter :size="18" class="text-teal-400" /> Advanced Filters
      </h3>
      <button
        v-if="hasActiveFilters"
        @click="$emit('clearFilters')"
        class="text-[10px] font-bold uppercase tracking-widest text-rose-400 hover:text-rose-300 transition-colors px-3 py-1.5 rounded-lg hover:bg-rose-500/10"
      >
        Clear All
      </button>
    </div>
    
    <!-- Status Grid -->
    <div class="mb-8">
      <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-3">Item Status</p>
      <div class="flex flex-wrap gap-2">
        <button
          v-for="filter in statusFilters"
          :key="filter.value"
          @click="$emit('update:activeStatFilter', filter.value)"
          class="px-4 py-2 rounded-xl text-sm font-bold transition-all duration-200 flex items-center gap-2 border"
          :class="activeStatFilter === filter.value
            ? 'bg-teal-500/10 text-teal-400 border-teal-500/30 shadow-[0_0_15px_rgba(45,212,191,0.15)]'
            : 'bg-slate-950/50 text-slate-400 border-white/5 hover:border-white/10 hover:text-slate-200'"
        >
          <component :is="filter.icon" :size="16" />
          {{ filter.label }}
        </button>
      </div>
    </div>

    <!-- Category Grid -->
    <div>
      <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-3">Vault Categories</p>
      <div class="flex flex-wrap gap-2">
        <button
          v-for="cat in categoryFilters"
          :key="cat.value"
          @click="$emit('update:activeCategory', cat.value)"
          class="px-4 py-2 rounded-xl text-sm font-bold transition-all duration-200 flex items-center gap-2 border"
          :class="activeCategory === cat.value
            ? 'bg-indigo-500/10 text-indigo-400 border-indigo-500/30 shadow-[0_0_15px_rgba(99,102,241,0.15)]'
            : 'bg-slate-950/50 text-slate-400 border-white/5 hover:border-white/10 hover:text-slate-200'"
        >
          <component :is="cat.icon" :size="16" />
          {{ cat.label }}
          <span 
            class="ml-1 px-1.5 py-0.5 rounded text-[10px] bg-slate-950"
            :class="activeCategory === cat.value ? 'text-indigo-400' : 'text-slate-500'"
          >
            {{ cat.count }}
          </span>
        </button>
      </div>
    </div>

  </div>
</template>

<script setup>
import { Filter, Layers, AlertTriangle, FileText, Repeat } from 'lucide-vue-next'

defineProps({
  activeCategory: String,
  activeStatFilter: String,
  categoryFilters: Array,
  hasActiveFilters: Boolean
})

defineEmits(['update:activeCategory', 'update:activeStatFilter', 'clearFilters'])

const statusFilters = [
  { label: 'All Items', value: 'all', icon: Layers },
  { label: 'Expiring Soon', value: 'soon', icon: AlertTriangle },
  { label: 'This Week', value: 'week', icon: AlertTriangle },
  { label: 'Expired', value: 'expired', icon: AlertTriangle },
  { label: 'Documents', value: 'documents', icon: FileText },
  { label: 'Subscriptions', value: 'subscriptions', icon: Repeat },
  { label: 'Missing Docs', value: 'missingDocs', icon: FileText },
]
</script>