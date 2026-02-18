<template>
  <div
    class="group relative p-5 rounded-2xl border cursor-pointer transition-all duration-300 select-none
           bg-gray-900 overflow-hidden"
    :class="[
      active
        ? `shadow-xl scale-[1.02] ${computedBorderActive} ring-1 ${computedRingActive}`
        : `border-gray-800 hover:${computedBorderHover} hover:shadow-lg hover:scale-[1.02]`
    ]"
    @click="$emit('click')"
  >

    <!-- Subtle hover background tint -->
    <div
      class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"
      :class="computedHoverBg"
    ></div>

    <!-- Content -->
    <div class="relative">

      <!-- TOP ROW: Icon + Label + 3-dot Menu -->
      <div class="flex items-center justify-between mb-4">
        <div class="flex items-center gap-2">
          <!-- Icon: small, subtle, left side -->
          <div
            class="flex items-center justify-center w-8 h-8 rounded-lg flex-shrink-0"
            :class="computedIconBg"
          >
            <component
              :is="icon"
              class="w-4 h-4 text-gray-200"
            />
          </div>
          <h3 class="text-xs font-semibold tracking-widest uppercase text-gray-500 group-hover:text-gray-400 transition-colors leading-tight">
            {{ label }}
          </h3>
        </div>
        <!-- 3-dot menu icon -->
        <MoreVertical :size="16" class="text-gray-600 group-hover:text-gray-400 transition-colors flex-shrink-0" />
      </div>

      <!-- VALUE (Large) -->
      <p class="text-4xl font-bold text-white tracking-tight leading-none mb-2">
        {{ formattedValue }}
      </p>

      <!-- Subtitle -->
      <p class="text-xs text-gray-500 mb-3">{{ subtitle }}</p>

      <!-- Activity Summary (at bottom with accent color) -->
      <p 
        v-if="activitySummary"
        class="text-xs font-medium transition-colors"
        :class="computedActivityColor"
      >
        {{ activitySummary }}
      </p>

    </div>

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