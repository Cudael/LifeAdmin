<template>
  <div
    class="group relative p-5 rounded-2xl border cursor-pointer transition-all duration-300 select-none
           bg-gray-900 overflow-hidden"
    :class="[
      active
        ? `shadow-xl scale-[1.02] ${computedBorderActive} ring-1 ${computedRingActive}`
        : 'border-gray-800 hover:border-gray-700 hover:shadow-lg hover:scale-[1.01]'
    ]"
    @click="$emit('click')"
  >

    <!-- Subtle hover background tint -->
    <div
      class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"
      :class="computedHoverBg"
    ></div>

    <!-- Accent bottom bar -->
    <div
      class="absolute bottom-0 left-0 right-0 h-0.5 transition-all duration-300"
      :class="[computedAccentBar, active ? 'opacity-100' : 'opacity-40 group-hover:opacity-100']"
    ></div>

    <!-- Content -->
    <div class="relative">

      <!-- TOP ROW: Label + Icon -->
      <div class="flex items-start justify-between mb-4">
        <h3 class="text-xs font-semibold tracking-widest uppercase text-gray-500 group-hover:text-gray-400 transition-colors leading-tight pt-0.5">
          {{ label }}
        </h3>
        <!-- Icon: small, subtle, top-right -->
        <div
          class="flex items-center justify-center w-8 h-8 rounded-lg flex-shrink-0 ml-2"
          :class="computedIconBg"
        >
          <component
            :is="icon"
            class="w-4 h-4"
            :class="iconColor || computedIconColor"
          />
        </div>
      </div>

      <!-- VALUE (Large) -->
      <p class="text-4xl font-bold text-white tracking-tight leading-none mb-3">
        {{ formattedValue }}
      </p>

      <!-- BOTTOM ROW: Subtitle + Trend Badge -->
      <div class="flex items-center justify-between">
        <p class="text-xs text-gray-500">{{ subtitle }}</p>
        <div
          v-if="trend"
          class="flex items-center gap-0.5 px-2 py-0.5 rounded-full text-xs font-semibold ml-2"
          :class="trendUp
            ? 'bg-green-900/40 text-green-400'
            : trendDown
            ? 'bg-red-900/40 text-red-400'
            : 'bg-gray-800 text-gray-300'"
        >
          <TrendingUp v-if="trendUp" :size="10" />
          <TrendingDown v-if="trendDown" :size="10" />
          <span>{{ trend }}</span>
        </div>
      </div>

      <!-- PROGRESS BAR (optional) -->
      <div v-if="percent !== null" class="mt-3 space-y-1">
        <div class="flex items-center justify-between text-xs">
          <span class="text-gray-400 font-medium">Progress</span>
          <span class="text-white font-bold">{{ percent }}%</span>
        </div>
        <div class="w-full bg-gray-800 h-1 rounded-full overflow-hidden">
          <div
            class="h-1 rounded-full transition-all duration-500 ease-out"
            :class="progressColor || computedProgressColor"
            :style="{ width: percent + '%' }"
          ></div>
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { computed } from 'vue'
import { TrendingUp, TrendingDown } from 'lucide-vue-next'

const ACCENT_MAP = {
  teal: {
    bar: 'bg-gradient-to-r from-teal-500 to-cyan-500',
    hover: 'bg-teal-900/20',
    borderActive: 'border-teal-500',
    ringActive: 'ring-teal-900/50',
    iconBg: 'bg-teal-900/40',
    iconColor: 'stroke-teal-400',
    progress: 'bg-gradient-to-r from-teal-500 to-cyan-500',
  },
  orange: {
    bar: 'bg-gradient-to-r from-orange-500 to-amber-500',
    hover: 'bg-orange-900/20',
    borderActive: 'border-orange-500',
    ringActive: 'ring-orange-900/50',
    iconBg: 'bg-orange-900/40',
    iconColor: 'stroke-orange-400',
    progress: 'bg-gradient-to-r from-orange-500 to-amber-500',
  },
  red: {
    bar: 'bg-gradient-to-r from-red-500 to-orange-500',
    hover: 'bg-red-900/20',
    borderActive: 'border-red-500',
    ringActive: 'ring-red-900/50',
    iconBg: 'bg-red-900/40',
    iconColor: 'stroke-red-400',
    progress: 'bg-gradient-to-r from-red-500 to-orange-500',
  },
  amber: {
    bar: 'bg-gradient-to-r from-amber-500 to-yellow-500',
    hover: 'bg-amber-900/20',
    borderActive: 'border-amber-500',
    ringActive: 'ring-amber-900/50',
    iconBg: 'bg-amber-900/40',
    iconColor: 'stroke-amber-400',
    progress: 'bg-gradient-to-r from-amber-500 to-yellow-500',
  },
  green: {
    bar: 'bg-gradient-to-r from-green-500 to-emerald-500',
    hover: 'bg-green-900/20',
    borderActive: 'border-green-500',
    ringActive: 'ring-green-900/50',
    iconBg: 'bg-green-900/40',
    iconColor: 'stroke-green-400',
    progress: 'bg-gradient-to-r from-green-500 to-emerald-500',
  },
  purple: {
    bar: 'bg-gradient-to-r from-purple-500 to-violet-500',
    hover: 'bg-purple-900/20',
    borderActive: 'border-purple-500',
    ringActive: 'ring-purple-900/50',
    iconBg: 'bg-purple-900/40',
    iconColor: 'stroke-purple-400',
    progress: 'bg-gradient-to-r from-purple-500 to-violet-500',
  },
}

const props = defineProps({
  label: { type: String, required: true },
  value: { type: [Number, String], required: true },
  subtitle: { type: String, default: "" },
  trend: { type: String, default: "" },
  trendUp: { type: Boolean, default: false },
  trendDown: { type: Boolean, default: false },
  percent: { type: Number, default: null },
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

  iconBgColor: { type: String, default: "" },
  iconColor: { type: String, default: "" },
  bgGradient: { type: String, default: "" },
  progressColor: { type: String, default: "" }
})

defineEmits(['click'])

const formattedValue = computed(() => {
  if (typeof props.value === 'number') {
    return props.value.toLocaleString()
  }
  return props.value
})

const accent = computed(() => ACCENT_MAP[props.accentColor] || ACCENT_MAP.teal)
const computedAccentBar = computed(() => props.bgGradient || accent.value.bar)
const computedHoverBg = computed(() => accent.value.hover)
const computedBorderActive = computed(() => accent.value.borderActive)
const computedRingActive = computed(() => accent.value.ringActive)
const computedIconBg = computed(() => props.iconBgColor || accent.value.iconBg)
const computedIconColor = computed(() => accent.value.iconColor)
const computedProgressColor = computed(() => accent.value.progress)
</script>