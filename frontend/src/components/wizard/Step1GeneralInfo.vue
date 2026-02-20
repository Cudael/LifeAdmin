<template>
  <div class="space-y-8">
    
    <!-- CATEGORY -->
    <div class="space-y-3">
      <label class="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
        <FolderOpen :size="14" class="text-teal-400" />
        Vault Category
        <span class="text-rose-400">*</span>
      </label>
      
      <div class="relative group/select">
        <select
          :value="category"
          @input="$emit('update:category', $event.target.value)"
          class="w-full bg-slate-950/50 border border-white/10 text-white rounded-xl pl-4 pr-10 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300 appearance-none cursor-pointer hover:border-white/20 font-medium"
          required
          :disabled="loading"
        >
          <option value="" disabled class="bg-slate-900 text-slate-500">Select classification...</option>
          <option v-for="cat in categories" :key="cat" :value="cat" class="bg-slate-900 text-white font-medium">
            {{ cat }}
          </option>
        </select>
        <!-- Custom Chevron -->
        <div class="absolute inset-y-0 right-4 flex items-center pointer-events-none text-slate-500 group-hover/select:text-white transition-colors">
          <ChevronDown :size="16" />
        </div>
      </div>
    </div>

    <!-- ITEM TYPE -->
    <div class="space-y-3">
      <label class="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
        <FileType :size="14" class="text-teal-400" />
        Asset Type
        <span class="text-rose-400">*</span>
      </label>
      
      <div v-if="!category" class="w-full flex items-center justify-center p-8 border border-dashed border-white/10 rounded-2xl bg-white/[0.01]">
        <p class="text-sm font-medium text-slate-500">Select a category to view available asset types.</p>
      </div>
      
      <div v-else-if="itemTypes.length === 0" class="w-full flex items-center justify-center p-8 border border-dashed border-rose-500/20 rounded-2xl bg-rose-500/5">
        <p class="text-sm font-medium text-rose-400">No asset types registered for this category.</p>
      </div>
      
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <button
          v-for="type in itemTypes"
          :key="type.id"
          type="button"
          @click="$emit('update:itemTypeName', type.name)"
          class="relative flex items-start gap-4 p-5 rounded-2xl border text-left transition-all duration-300 overflow-hidden group"
          :class="[
            itemTypeName === type.name
              ? 'border-teal-500 bg-teal-500/10 shadow-[0_0_20px_rgba(45,212,191,0.15)]'
              : 'border-white/5 bg-slate-950/50 hover:border-white/15 hover:bg-slate-900'
          ]"
          :disabled="loading"
        >
          <!-- Active Glow Background -->
          <div v-if="itemTypeName === type.name" class="absolute top-0 right-0 w-24 h-24 bg-teal-500/20 blur-xl rounded-full pointer-events-none"></div>

          <div class="w-10 h-10 rounded-xl bg-slate-800 border border-white/5 flex items-center justify-center text-xl shrink-0 group-hover:scale-110 transition-transform shadow-inner">
            {{ type.icon || '📄' }}
          </div>
          
          <div class="flex-1 min-w-0 pr-6">
            <h4 class="font-bold text-slate-200 group-hover:text-white transition-colors truncate">{{ type.name }}</h4>
            <p class="text-xs text-slate-500 mt-1 font-medium line-clamp-2 leading-relaxed">{{ type.description }}</p>
          </div>

          <!-- Selection Indicator -->
          <div class="absolute top-5 right-5">
            <div 
              class="w-5 h-5 rounded-full border transition-all flex items-center justify-center"
              :class="itemTypeName === type.name ? 'bg-teal-500 border-teal-500 shadow-[0_0_10px_rgba(45,212,191,0.5)]' : 'border-slate-700'"
            >
              <Check v-if="itemTypeName === type.name" :size="12" class="text-slate-950 stroke-[3]" />
            </div>
          </div>
        </button>
      </div>
    </div>

    <!-- ITEM NAME -->
    <div class="space-y-3">
      <div class="flex items-center justify-between">
        <label class="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
          <Edit3 :size="14" class="text-teal-400" />
          Asset Name
          <span class="text-rose-400">*</span>
        </label>
        <span class="text-[10px] font-bold text-slate-600">{{ name.length }}/200</span>
      </div>
      
      <input
        type="text"
        :value="name"
        @input="$emit('update:name', $event.target.value)"
        class="w-full bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl px-4 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300 hover:border-white/20 font-medium"
        placeholder="e.g., Personal Passport, Netflix Subscription"
        required
        :disabled="loading"
        maxlength="200"
      />
    </div>

  </div>
</template>

<script setup>
import { FolderOpen, FileType, Edit3, ChevronDown, Check } from "lucide-vue-next"

defineProps({
  category: String,
  itemTypeName: String,
  name: String,
  categories: Array,
  itemTypes: Array,
  loading: Boolean
})

defineEmits(['update:category', 'update:itemTypeName', 'update:name'])
</script>