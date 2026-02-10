<template>
  <div
    class="p-5 rounded-xl border cursor-pointer transition-all duration-200 select-none
           flex flex-col gap-3 bg-white
           hover:shadow-md hover:scale-[1.02]"
    :class="active
      ? 'shadow-xl scale-[1.03] border-gray-300 ring-2 ring-gray-200'
      : 'border-gray-200'"
    @click="$emit('click')"
  >
    <!-- ICON + LABEL -->
    <div class="flex items-center justify-between">
      <div class="flex flex-col">
        <span class="text-sm opacity-70">{{ label }}</span>
        <span class="text-3xl font-bold leading-tight">{{ value }}</span>
      </div>

      <div
        class="flex items-center justify-center rounded-lg"
        :class="[
          'w-12 h-12',
          iconBgColor,
        ]"
      >
        <component
          :is="icon"
          class="w-6 h-6"
          :class="iconColor"
        />
      </div>
    </div>

    <!-- SUBTITLE -->
    <div v-if="subtitle" class="text-xs opacity-60">
      {{ subtitle }}
    </div>

    <!-- TREND -->
    <div v-if="trend" class="text-xs font-medium opacity-70">
      {{ trend }}
    </div>

    <!-- PROGRESS BAR -->
    <div v-if="percent !== null" class="w-full bg-gray-200 h-1 rounded mt-2">
      <div
        class="h-1 rounded bg-gray-700 transition-all duration-300"
        :style="{ width: percent + '%' }"
      ></div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  label: String,
  value: Number,
  subtitle: { type: String, default: "" },
  trend: { type: String, default: "" },
  percent: { type: Number, default: null },
  active: Boolean,

  icon: {
    type: [Object, Function],
    required: true
  },

  iconBgColor: { type: String, default: "bg-transparent" },
  iconColor: { type: String, default: "stroke-gray-600" }
})
</script>