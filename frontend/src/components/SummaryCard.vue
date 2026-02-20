<template>
  <div
    @click="clickable ? $emit('click') : null"
    class="group relative h-full rounded-3xl transition-all duration-500 z-10"
    :class="[clickable ? 'cursor-pointer hover:-translate-y-1' : '']"
  >
    <!-- Deep Base Layer -->
    <div class="absolute inset-0 bg-slate-900/80 rounded-3xl shadow-lg border border-white/5 group-hover:border-white/10 transition-colors duration-500"></div>

    <!-- Hover Ambient Radial Glow -->
    <div 
      class="absolute inset-0 rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-700 blur-[40px] pointer-events-none" 
      :class="accent.glowBg"
    ></div>

    <!-- Top Hardware Edge Highlight -->
    <div class="absolute top-0 left-0 right-0 h-px z-20 flex justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-500">
      <div 
        class="h-full w-1/2 group-hover:w-3/4 transition-all duration-700 ease-out"
        :class="accent.topLine"
      ></div>
    </div>

    <!-- Active/Alert State Permanent Glow -->
    <div 
      v-if="isAlert || active" 
      class="absolute -top-10 -right-10 w-32 h-32 rounded-full blur-[50px] pointer-events-none" 
      :class="accent.glowBg"
    ></div>

    <!-- Content -->
    <div class="relative z-20 p-6 flex flex-col h-full justify-between">
      
      <!-- Top Row: Icon & Arrow -->
      <div class="flex justify-between items-start mb-6">
        <div 
          class="w-12 h-12 rounded-2xl border flex items-center justify-center transition-transform duration-500 group-hover:scale-110 shadow-inner"
          :class="[accent.iconBg, accent.iconBorder, accent.iconText]"
        >
          <component :is="icon" :size="22" stroke-width="2" />
        </div>

        <div 
          v-if="clickable"
          class="w-8 h-8 rounded-full bg-white/5 border border-white/10 flex items-center justify-center opacity-0 -translate-y-2 translate-x-2 group-hover:opacity-100 group-hover:translate-y-0 group-hover:translate-x-0 transition-all duration-300 ease-out shadow-lg"
        >
          <ArrowUpRight :size="16" class="text-white/70 group-hover:text-white transition-colors" />
        </div>
      </div>
      
      <!-- Middle Row: Highly Legible Title & Value -->
      <div class="mb-4">
        <!-- The Title is now above the number and highly visible -->
        <h3 class="text-sm font-semibold text-slate-400 group-hover:text-slate-300 transition-colors mb-1.5">
          {{ label }}
        </h3>
        <div class="flex items-baseline gap-2">
          <span class="text-4xl font-extrabold text-white tracking-tight tabular-nums">{{ formattedValue }}</span>
        </div>
      </div>

      <!-- Bottom Row: Status/Activity -->
      <div class="pt-4 border-t border-white/10 flex items-start gap-2.5">
        <div 
          class="w-2 h-2 rounded-full shrink-0 mt-1 shadow-lg" 
          :class="[
            isAlert ? 'animate-pulse' : '',
            accent.statusDot,
            accent.statusShadow
          ]"
        ></div>
        <span 
          class="text-xs font-medium leading-snug line-clamp-2" 
          :class="isAlert ? accent.statusText : 'text-slate-500 group-hover:text-slate-400 transition-colors'"
          :title="activitySummary"
        >
          {{ activitySummary || 'All systems operational' }}
        </span>
      </div>

    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { ArrowUpRight } from 'lucide-vue-next'

const ACCENT_MAP = {
  teal: {
    iconBg: 'bg-teal-500/10',
    iconBorder: 'border-teal-500/20',
    iconText: 'text-teal-400',
    glowBg: 'bg-teal-500/15',
    topLine: 'bg-gradient-to-r from-transparent via-teal-400 to-transparent',
    statusDot: 'bg-teal-500',
    statusShadow: 'shadow-teal-500/50',
    statusText: 'text-teal-400',
  },
  orange: {
    iconBg: 'bg-orange-500/10',
    iconBorder: 'border-orange-500/20',
    iconText: 'text-orange-400',
    glowBg: 'bg-orange-500/15',
    topLine: 'bg-gradient-to-r from-transparent via-orange-400 to-transparent',
    statusDot: 'bg-orange-500',
    statusShadow: 'shadow-orange-500/50',
    statusText: 'text-orange-400',
  },
  amber: {
    iconBg: 'bg-amber-500/10',
    iconBorder: 'border-amber-500/20',
    iconText: 'text-amber-400',
    glowBg: 'bg-amber-500/15',
    topLine: 'bg-gradient-to-r from-transparent via-amber-400 to-transparent',
    statusDot: 'bg-amber-500',
    statusShadow: 'shadow-amber-500/50',
    statusText: 'text-amber-400',
  },
  rose: {
    iconBg: 'bg-rose-500/10',
    iconBorder: 'border-rose-500/20',
    iconText: 'text-rose-400',
    glowBg: 'bg-rose-500/15',
    topLine: 'bg-gradient-to-r from-transparent via-rose-400 to-transparent',
    statusDot: 'bg-rose-500',
    statusShadow: 'shadow-rose-500/50',
    statusText: 'text-rose-400',
  },
  emerald: {
    iconBg: 'bg-emerald-500/10',
    iconBorder: 'border-emerald-500/20',
    iconText: 'text-emerald-400',
    glowBg: 'bg-emerald-500/15',
    topLine: 'bg-gradient-to-r from-transparent via-emerald-400 to-transparent',
    statusDot: 'bg-emerald-500',
    statusShadow: 'shadow-emerald-500/50',
    statusText: 'text-emerald-400',
  },
  indigo: {
    iconBg: 'bg-indigo-500/10',
    iconBorder: 'border-indigo-500/20',
    iconText: 'text-indigo-400',
    glowBg: 'bg-indigo-500/15',
    topLine: 'bg-gradient-to-r from-transparent via-indigo-400 to-transparent',
    statusDot: 'bg-indigo-500',
    statusShadow: 'shadow-indigo-500/50',
    statusText: 'text-indigo-400',
  },
}

const props = defineProps({
  label:           { type: String,           required: true },
  value:           { type: [Number, String], required: true },
  activitySummary: { type: String,           default: "" },
  active:          { type: Boolean,          default: false },
  clickable:       { type: Boolean,          default: true },
  isAlert:         { type: Boolean,          default: false },
  accentColor: {
    type: String,
    default: 'teal',
    validator: (v) => ['teal', 'orange', 'rose', 'amber', 'emerald', 'indigo'].includes(v)
  },
  icon: { type: [Object, Function], required: true },
})

defineEmits(['click'])

const formattedValue = computed(() => {
  if (typeof props.value === 'number') return props.value.toLocaleString()
  return props.value
})

const accent = computed(() => ACCENT_MAP[props.accentColor] ?? ACCENT_MAP.teal)
</script>