<template>
  <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
    
    <!-- Header -->
    <div class="flex items-center justify-between mb-4">
      <h3 class="text-lg font-bold text-gray-900 flex items-center gap-2">
        <Calendar :size="20" class="text-teal-500" />
        {{ currentMonth }}
      </h3>
      <div class="flex items-center gap-2">
        <button
          @click="previousMonth"
          class="p-1.5 hover:bg-gray-100 rounded-lg transition-colors"
          aria-label="Previous month"
        >
          <ChevronLeft :size="16" class="text-gray-600" />
        </button>
        <button
          @click="nextMonth"
          class="p-1.5 hover:bg-gray-100 rounded-lg transition-colors"
          aria-label="Next month"
        >
          <ChevronRight :size="16" class="text-gray-600" />
        </button>
      </div>
    </div>

    <!-- Day headers -->
    <div class="grid grid-cols-7 gap-1 mb-2">
      <div
        v-for="(day, index) in DAY_NAMES"
        :key="`day-${index}`"
        class="text-center text-xs font-semibold text-gray-500 py-1"
      >
        {{ day.charAt(0) }}
      </div>
    </div>

    <!-- Calendar grid -->
    <div class="grid grid-cols-7 gap-1">
      <button
        v-for="(day, index) in calendarDays"
        :key="index"
        @click="handleDayClick(day)"
        :class="[
          'aspect-square flex items-center justify-center text-sm rounded-lg transition-all duration-200 relative',
          day.isCurrentMonth ? 'text-gray-900 hover:bg-teal-50' : 'text-gray-300',
          day.isToday ? 'bg-teal-500 text-white font-bold hover:bg-teal-600' : '',
          day.hasItems && !day.isToday ? 'font-semibold' : '',
          !day.isCurrentMonth ? 'cursor-default' : 'cursor-pointer'
        ]"
        :disabled="!day.isCurrentMonth"
      >
        <span>{{ day.date.getDate() }}</span>
        
        <!-- Item indicator dots -->
        <div v-if="day.hasItems && !day.isToday" class="absolute bottom-1 left-1/2 -translate-x-1/2 flex gap-0.5">
          <div
            v-for="i in Math.min(day.itemCount, 3)"
            :key="i"
            :class="[
              'w-1 h-1 rounded-full',
              getItemDotColor(day)
            ]"
          ></div>
        </div>
      </button>
    </div>

    <!-- Footer - Quick stats -->
    <div class="mt-4 pt-4 border-t border-gray-200">
      <div class="flex items-center justify-between text-xs">
        <div class="flex items-center gap-2">
          <div class="w-2 h-2 rounded-full bg-red-500"></div>
          <span class="text-gray-600">{{ expiringSoonCount }} expiring soon</span>
        </div>
        <RouterLink
          to="/calendar"
          class="text-teal-600 font-medium hover:text-teal-700 hover:underline"
        >
          View Calendar →
        </RouterLink>
      </div>
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
  ChevronRight
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
    const dayItems = props.items.filter(item => {
      if (!item.expiration_date) return false
      return item.expiration_date.split('T')[0] === dateStr
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
  if (!day.items.length) return 'bg-gray-400'
  
  // Find the most urgent item
  const minDays = Math.min(...day.items.map(item => getDaysUntil(item.expiration_date)))
  
  if (minDays < 0) return 'bg-gray-400'
  if (minDays <= 7) return 'bg-red-500'
  if (minDays <= 30) return 'bg-orange-500'
  return 'bg-blue-500'
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