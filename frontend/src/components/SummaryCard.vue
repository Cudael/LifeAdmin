<template>
  <div
    class="group relative p-4 rounded-xl border cursor-pointer transition-all duration-300 select-none
           flex flex-col gap-3 bg-white overflow-hidden"
    :class="[
      active
        ? 'shadow-xl scale-[1.02] border-teal-200 ring-2 ring-teal-100'
        : 'border-gray-200 hover:border-gray-300 hover:shadow-lg hover:scale-[1.01]'
    ]"
    @click="$emit('click')"
  >
    
    <!-- Background Gradient Decoration -->
    <div 
      class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"
      :class="bgGradient || 'bg-gradient-to-br from-teal-50/50 to-cyan-50/50'"
    ></div>

    <!-- Content (relative to stay above gradient) -->
    <div class="relative">
      
      <!-- TOP ROW: Icon + Trend Badge -->
      <div class="flex items-start justify-between mb-2">
        <!-- Icon -->
        <div
          class="flex items-center justify-center rounded-lg transition-all duration-300 shadow-sm"
          :class="[
            'w-10 h-10',
            iconBgColor || 'bg-gradient-to-br from-teal-100 to-cyan-100',
            active ? 'scale-110 shadow-md' : 'group-hover:scale-105'
          ]"
        >
          <component
            :is="icon"
            class="w-5 h-5 transition-transform duration-300"
            :class="[
              iconColor || 'stroke-teal-600',
              active ? 'scale-110' : 'group-hover:scale-110'
            ]"
          />
        </div>

        <!-- Trend Badge (if exists) -->
        <div 
          v-if="trend"
          class="flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold"
          :class="trendUp 
            ? 'bg-green-100 text-green-700' 
            : trendDown
            ? 'bg-red-100 text-red-700'
            : 'bg-gray-100 text-gray-700'"
        >
          <TrendingUp v-if="trendUp" :size="10" />
          <TrendingDown v-if="trendDown" :size="10" />
          <span>{{ trend }}</span>
        </div>
      </div>

      <!-- LABEL -->
      <div class="mb-1">
        <h3 class="text-xs font-medium text-gray-600 group-hover:text-gray-700 transition-colors">
          {{ label }}
        </h3>
      </div>

      <!-- VALUE -->
      <div class="mb-1">
        <p class="text-2xl font-bold text-gray-900 tracking-tight">
          {{ formattedValue }}
        </p>
      </div>

      <!-- SUBTITLE -->
      <div v-if="subtitle" class="text-xs text-gray-500 mb-2">
        {{ subtitle }}
      </div>

      <!-- PROGRESS BAR -->
      <div v-if="percent !== null" class="space-y-1">
        <div class="flex items-center justify-between text-xs">
          <span class="text-gray-600 font-medium">Progress</span>
          <span class="text-gray-900 font-bold">{{ percent }}%</span>
        </div>
        <div class="w-full bg-gray-200 h-1.5 rounded-full overflow-hidden">
          <div
            class="h-1.5 rounded-full transition-all duration-500 ease-out"
            :class="progressColor || 'bg-gradient-to-r from-teal-500 to-cyan-500'"
            :style="{ width: percent + '%' }"
          ></div>
        </div>
      </div>

      <!-- ACTION HINT -->
      <div 
        v-if="clickable !== false"
        class="flex items-center gap-1 text-xs font-medium text-teal-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300 mt-2"
      >
        <span>View details</span>
        <ArrowRight :size="12" />
      </div>

    </div>

    <!-- Active Indicator -->
    <div 
      v-if="active"
      class="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-teal-500 to-cyan-500"
    ></div>

  </div>
</template>

<script setup>
import { computed } from 'vue'
import { TrendingUp, TrendingDown, ArrowRight } from 'lucide-vue-next'

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
    // Add comma formatting for large numbers
    return props.value.toLocaleString()
  }
  return props.value
})
</script>