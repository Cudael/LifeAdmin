<template>
  <div class="mb-6">
    <!-- Header Toggle -->
    <button
      @click="$emit('update:showInsights', !showInsights)"
      class="w-full flex items-center justify-between p-4 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 hover:border-white/10 transition-colors group"
    >
      <div class="flex items-center gap-4 px-2">
        <div class="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400 shadow-inner">
          <BarChart3 :size="20" />
        </div>
        <div class="text-left">
          <h3 class="text-white font-bold tracking-tight">Vault Insights</h3>
          <p class="text-slate-500 text-xs font-medium mt-0.5">Key metrics and distribution</p>
        </div>
      </div>
      <div class="flex items-center gap-2 px-2">
        <span class="text-xs font-bold uppercase tracking-wider text-slate-500 group-hover:text-slate-400">{{ showInsights ? 'Hide' : 'View' }}</span>
        <component :is="showInsights ? ChevronUp : ChevronDown" :size="18" class="text-slate-500 group-hover:text-slate-400" />
      </div>
    </button>

    <!-- Content -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-4 max-h-0"
      enter-to-class="opacity-100 translate-y-0 max-h-[800px]"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0 max-h-[800px]"
      leave-to-class="opacity-0 -translate-y-4 max-h-0"
    >
      <div v-if="showInsights" class="mt-4 overflow-hidden">
        <div class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] p-8 border border-white/5 shadow-2xl">
          
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
            
            <!-- Needs Attention -->
            <button @click="$emit('filter', 'expired')" class="p-6 bg-slate-950/50 rounded-2xl border border-rose-500/10 hover:border-rose-500/30 hover:bg-rose-500/5 transition-all text-left group relative overflow-hidden">
              <div class="absolute top-0 right-0 w-24 h-24 bg-rose-500/10 blur-2xl rounded-full"></div>
              <AlertTriangle :size="20" class="text-rose-400 mb-4 group-hover:scale-110 transition-transform" />
              <p class="text-4xl font-extrabold text-white mb-1">{{ insights.needsAttention }}</p>
              <p class="text-xs font-bold uppercase tracking-wider text-slate-500">Needs Attention</p>
            </button>

            <!-- Expiring Soon -->
            <button @click="$emit('filter', 'soon')" class="p-6 bg-slate-950/50 rounded-2xl border border-orange-500/10 hover:border-orange-500/30 hover:bg-orange-500/5 transition-all text-left group relative overflow-hidden">
              <div class="absolute top-0 right-0 w-24 h-24 bg-orange-500/10 blur-2xl rounded-full"></div>
              <Clock :size="20" class="text-orange-400 mb-4 group-hover:scale-110 transition-transform" />
              <p class="text-4xl font-extrabold text-white mb-1">{{ insights.expiringThisMonth }}</p>
              <p class="text-xs font-bold uppercase tracking-wider text-slate-500">Expiring Soon</p>
            </button>

            <!-- Documents -->
            <button @click="$emit('filter', 'documents')" class="p-6 bg-slate-950/50 rounded-2xl border border-teal-500/10 hover:border-teal-500/30 hover:bg-teal-500/5 transition-all text-left group relative overflow-hidden">
              <div class="absolute top-0 right-0 w-24 h-24 bg-teal-500/10 blur-2xl rounded-full"></div>
              <FileText :size="20" class="text-teal-400 mb-4 group-hover:scale-110 transition-transform" />
              <p class="text-4xl font-extrabold text-white mb-1">{{ documentsCount }}</p>
              <p class="text-xs font-bold uppercase tracking-wider text-slate-500">Documents</p>
            </button>

            <!-- Subscriptions -->
            <button @click="$emit('filter', 'subscriptions')" class="p-6 bg-slate-950/50 rounded-2xl border border-indigo-500/10 hover:border-indigo-500/30 hover:bg-indigo-500/5 transition-all text-left group relative overflow-hidden">
              <div class="absolute top-0 right-0 w-24 h-24 bg-indigo-500/10 blur-2xl rounded-full"></div>
              <Repeat :size="20" class="text-indigo-400 mb-4 group-hover:scale-110 transition-transform" />
              <p class="text-4xl font-extrabold text-white mb-1">{{ subscriptionsCount }}</p>
              <p class="text-xs font-bold uppercase tracking-wider text-slate-500">Subscriptions</p>
            </button>

          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { AlertTriangle, FileText, Repeat, ChevronDown, ChevronUp, BarChart3, Clock } from 'lucide-vue-next'

defineProps({
  showInsights: Boolean,
  insights: Object,
  totalItems: Number,
  documentsCount: Number,
  subscriptionsCount: Number,
  isPremium: Boolean
})
defineEmits(['filter', 'update:showInsights'])
</script>