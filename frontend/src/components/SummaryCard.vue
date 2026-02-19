<template>
  <div
    class="group relative overflow-hidden rounded-2xl border cursor-pointer
           transition-all duration-300 select-none"
    :class="[
      'bg-gradient-to-br from-gray-900 to-gray-900/80 backdrop-blur-xl',
      active
        ? `shadow-xl scale-[1.02] ${accent.borderActive} ring-1 ${accent.ringActive}`
        : `border-gray-800/50 hover:border-gray-700 hover:shadow-xl hover:shadow-${accentColor}-500/10 hover:scale-[1.01]`
    ]"
    @click="$emit('click')"
  >
    <!-- Premium ambient glow -->
    <div
      class="absolute -top-12 -right-12 w-32 h-32 rounded-full blur-3xl
             opacity-0 group-hover:opacity-20 transition-opacity duration-500"
      :class="accent.glowBg"
    />

    <!-- Inner content with glassmorphism inset -->
    <div class="relative p-5">

      <!-- Top: Icon badge -->
      <div
        class="w-10 h-10 rounded-xl flex items-center justify-center mb-4
               ring-1 ring-white/5 shadow-inner"
        :class="accent.iconBg"
      >
        <component :is="icon" class="w-5 h-5" :class="accent.iconColor" />
      </div>

      <!-- Value with animated counter feel -->
      <p class="text-3xl font-bold text-white tracking-tight mb-1 tabular-nums">
        {{ formattedValue }}
      </p>

      <!-- Label -->
      <p class="text-sm font-medium text-gray-400 mb-3">{{ label }}</p>

      <!-- Activity sparkline / summary -->
      <div v-if="activitySummary" class="flex items-center gap-1.5">
        <div class="w-1.5 h-1.5 rounded-full animate-pulse" :class="accent.dotColor" />
        <p class="text-xs font-medium" :class="accent.activityColor">
          {{ activitySummary }}
        </p>
      </div>
    </div>

    <!-- Bottom accent bar -->
    <div
      class="h-0.5 w-full opacity-0 group-hover:opacity-100 transition-opacity duration-300"
      :class="accent.barGradient"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { MoreVertical } from 'lucide-vue-next'

const ACCENT_MAP = {
  teal: {
    hover: 'bg-teal-900/20',
    borderActive: 'border-teal-500',
    borderHover: 'border-teal-700',
    ringActive: 'ring-teal-900/50',
    iconBg: 'bg-gray-800',
    activityColor: 'text-teal-400',
  },
  orange: {
    hover: 'bg-orange-900/20',
    borderActive: 'border-orange-500',
    borderHover: 'border-orange-700',
    ringActive: 'ring-orange-900/50',
    iconBg: 'bg-gray-800',
    activityColor: 'text-orange-400',
  },
  red: {
    hover: 'bg-red-900/20',
    borderActive: 'border-red-500',
    borderHover: 'border-red-700',
    ringActive: 'ring-red-900/50',
    iconBg: 'bg-gray-800',
    activityColor: 'text-red-400',
  },
  amber: {
    hover: 'bg-amber-900/20',
    borderActive: 'border-amber-500',
    borderHover: 'border-amber-700',
    ringActive: 'ring-amber-900/50',
    iconBg: 'bg-gray-800',
    activityColor: 'text-amber-400',
  },
  green: {
    hover: 'bg-green-900/20',
    borderActive: 'border-green-500',
    borderHover: 'border-green-700',
    ringActive: 'ring-green-900/50',
    iconBg: 'bg-gray-800',
    activityColor: 'text-green-400',
  },
  purple: {
    hover: 'bg-purple-900/20',
    borderActive: 'border-purple-500',
    borderHover: 'border-purple-700',
    ringActive: 'ring-purple-900/50',
    iconBg: 'bg-gray-800',
    activityColor: 'text-purple-400',
  },
}

const props = defineProps({
  label: { type: String, required: true },
  value: { type: [Number, String], required: true },
  subtitle: { type: String, default: "" },
  activitySummary: { type: String, default: "" },
  active: { type: Boolean, default: false },
  clickable: { type: Boolean, default: true },
  accentColor: {
    type: String,
    default: 'teal',
    validator: (v) => ['teal', 'orange', 'red', 'amber', 'green', 'purple'].includes(v)
  },

  icon: {
    type: [Object, Function],
    required: true
  },

  iconBgColor: { type: String, default: "" }
})

defineEmits(['click'])

const formattedValue = computed(() => {
  if (typeof props.value === 'number') {
    return props.value.toLocaleString()
  }
  return props.value
})

const accent = computed(() => ACCENT_MAP[props.accentColor] || ACCENT_MAP.teal)
const computedHoverBg = computed(() => accent.value.hover)
const computedBorderActive = computed(() => accent.value.borderActive)
const computedBorderHover = computed(() => accent.value.borderHover)
const computedRingActive = computed(() => accent.value.ringActive)
const computedIconBg = computed(() => props.iconBgColor || accent.value.iconBg)
const computedActivityColor = computed(() => accent.value.activityColor)
</script>
