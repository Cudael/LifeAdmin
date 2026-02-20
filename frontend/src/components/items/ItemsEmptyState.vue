<template>
  <div class="w-full flex flex-col items-center justify-center py-24 px-6 bg-slate-900/40 backdrop-blur-xl border border-dashed border-white/10 rounded-[2rem] shadow-inner">
    <div class="w-20 h-20 rounded-3xl bg-slate-800/50 border border-white/5 flex items-center justify-center mb-6 shadow-xl">
      <Package :size="32" class="text-slate-500" />
    </div>
    
    <h3 class="text-2xl font-extrabold text-white tracking-tight mb-2">No items found</h3>
    <p class="text-slate-400 font-medium mb-8 max-w-sm text-center leading-relaxed">
      {{ hasActiveFilters
        ? 'No items match your current filter criteria. Try clearing them to see all items.'
        : 'Your vault is currently empty. Get started by securely adding your first document or subscription.'
      }}
    </p>
    
    <div class="flex items-center gap-4">
      <button
        v-if="hasActiveFilters"
        @click="$emit('clearFilters')"
        class="px-6 py-3 bg-slate-800 hover:bg-slate-700 text-white rounded-xl font-bold transition-colors"
      >
        Clear Filters
      </button>
      <RouterLink
        v-else
        to="/add-item"
        class="relative group inline-flex items-center justify-center gap-2 px-6 py-3 bg-slate-50 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(255,255,255,0.1)] hover:bg-white hover:shadow-[0_0_25px_rgba(255,255,255,0.2)] transition-all duration-300"
      >
        <Plus :size="18" class="text-teal-600 group-hover:rotate-90 transition-transform" />
        <span>Add First Item</span>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { Package, Plus } from "lucide-vue-next"
defineProps({ hasActiveFilters: Boolean })
defineEmits(['clearFilters'])
</script>