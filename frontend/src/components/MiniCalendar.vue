<template>
  <div class="flex flex-col h-full">
    
    <!-- Header: Month & Navigation -->
    <div class="flex items-center justify-between mb-6">
      <h3 class="text-lg font-bold text-white flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-teal-500/10 flex items-center justify-center text-teal-400 border border-teal-500/20">
          <Calendar :size="16" />
        </div>
        {{ currentMonth }}
      </h3>
      <div class="flex items-center gap-1 bg-slate-900/50 rounded-lg border border-white/5 p-1 shadow-inner">
        <button
          @click="previousMonth"
          class="p-1.5 hover:bg-slate-800 rounded-md text-slate-400 hover:text-white transition-colors"
          aria-label="Previous month"
        >
          <ChevronLeft :size="14" />
        </button>
        <div class="w-px h-4 bg-white/10"></div>
        <button
          @click="nextMonth"
          class="p-1.5 hover:bg-slate-800 rounded-md text-slate-400 hover:text-white transition-colors"
          aria-label="Next month"
        >
          <ChevronRight :size="14" />
        </button>
      </div>
    </div>

    <!-- Calendar Matrix -->
    <div class="flex-1 flex flex-col">
      <!-- Day headers (M, T, W, T, F, S, S) -->
      <div class="grid grid-cols-7 gap-1 mb-3">
        <div
          v-for="(day, index) in DAY_NAMES"
          :key="`day-${index}`"
          class="text-center text-[10px] font-bold text-slate-500 uppercase tracking-widest py-1"
        >
          {{ day.charAt(0) }}
        </div>
      </div>

      <!-- Calendar grid -->
      <div class="grid grid-cols-7 gap-1 flex-1">
        <button
          v-for="(day, index) in calendarDays"
          :key="index"
          @click="handleDayClick(day)"
          class="relative aspect-square flex flex-col items-center justify-center rounded-full transition-all duration-200 group"
          :class="[
            !day.isCurrentMonth ? 'text-slate-700 cursor-default opacity-40' : 'cursor-pointer hover:bg-white/5',
            day.isToday ? 'bg-teal-500/10 text-teal-400 font-bold ring-1 ring-teal-500 shadow-[0_0_15px_rgba(45,212,191,0.2)]' : 'text-slate-300 font-medium',
            day.hasItems && !day.isToday ? 'text-white' : ''
          ]"
          :disabled="!day.isCurrentMonth"
        >
          <span class="text-[13px] leading-none mt-0.5">{{ day.date.getDate() }}</span>
          
          <!-- Item indicator dots (Data Heatmap) -->
          <div v-if="day.hasItems" class="absolute bottom-1.5 flex gap-[3px]">
            <div
              v-for="i in Math.min(day.itemCount, 3)"
              :key="i"
              class="w-1 h-1 rounded-full shadow-sm"
              :class="getItemDotColor(day)"
            ></div>
          </div>
        </button>
      </div>
    </div>

    <!-- Footer: Quick Stats & CTA -->
    <div class="mt-6 pt-5 border-t border-white/5 flex items-center justify-between">
      <div class="flex items-center gap-2 px-2.5 py-1 bg-amber-500/10 border border-amber-500/20 rounded-full">
        <div class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse shadow-[0_0_8px_rgba(251,191,36,0.6)]"></div>
        <span class="text-[10px] font-bold text-amber-400 uppercase tracking-wider">{{ expiringSoonCount }} Action Items</span>
      </div>
      
      <RouterLink
        to="/calendar"
        class="text-xs font-bold uppercase tracking-wider text-slate-500 hover:text-teal-400 transition-colors flex items-center gap-1 group"
      >
        Full Timeline <ArrowUpRight :size="12" class="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
      </RouterLink>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import { useItemStatus } from "../composables/useItemStatus"
import {
  Calendar,
  ChevronLeft,
  ChevronRight,
  ArrowUpRight
} from "lucide-vue-next"

const props = defineProps({
  items: {
    type: Array,
    default: () => []
  }
})

const router = useRouter()
const currentDate = ref(new Date())
const { daysLeft } = useItemStatus()

const DAY_NAMES = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

const currentMonth = computed(() => {
  return currentDate.value.toLocaleDateString('en-US', { 
    month: 'long', 
    year: 'numeric' 
  })
})

const calendarDays = computed(() => {
  const year = currentDate.value.getFullYear()
  const month = currentDate.value.getMonth()
  
  // First day of month
  const firstDay = new Date(year, month, 1)
  const lastDay = new Date(year, month + 1, 0)
  
  // Start from Sunday before first day
  const startDate = new Date(firstDay)
  startDate.setDate(startDate.getDate() - firstDay.getDay())
  
  // End on Saturday after last day
  const endDate = new Date(lastDay)
  endDate.setDate(endDate.getDate() + (6 - lastDay.getDay()))
  
  const days = []
  const currentDay = new Date(startDate)
  
  while (currentDay <= endDate) {
    const dateStr = currentDay.toISOString().split('T')[0]
    // Account for timezone offsets to ensure correct date mapping
    const dayItems = props.items.filter(item => {
      if (!item.expiration_date) return false
      // Extract just the YYYY-MM-DD part from the ISO string to avoid TZ issues
      const itemDateStr = item.expiration_date.split('T')[0]
      return itemDateStr === dateStr
    })
    
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    const checkDate = new Date(currentDay)
    checkDate.setHours(0, 0, 0, 0)
    
    days.push({
      date: new Date(currentDay),
      items: dayItems,
      itemCount: dayItems.length,
      hasItems: dayItems.length > 0,
      isCurrentMonth: currentDay.getMonth() === month,
      isToday: checkDate.getTime() === today.getTime()
    })
    
    currentDay.setDate(currentDay.getDate() + 1)
  }
  
  return days
})

const expiringSoonCount = computed(() => {
  return props.items.filter(item => {
    if (!item.expiration_date) return false
    const days = daysLeft(item.expiration_date)
    return days !== null && days >= 0 && days <= 30
  }).length
})

function getDaysUntil(dateString) {
  return daysLeft(dateString)
}

function getItemDotColor(day) {
  if (!day.items.length) return 'bg-slate-600'
  
  // Find the most urgent item to color the dots
  const minDays = Math.min(...day.items.map(item => getDaysUntil(item.expiration_date)))
  
  if (minDays < 0) return 'bg-rose-500 shadow-rose-500/50' // Expired
  if (minDays <= 7) return 'bg-rose-400 shadow-rose-500/50' // < 1 week
  if (minDays <= 30) return 'bg-amber-400 shadow-amber-500/50' // < 1 month
  return 'bg-teal-400 shadow-teal-500/50' // standard upcoming
}

function previousMonth() {
  currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() - 1, 1)
}

function nextMonth() {
  currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() + 1, 1)
}

function handleDayClick(day) {
  if (day.isCurrentMonth) {
    router.push('/calendar')
  }
}
</script>