<template>
  <DashboardLayout pageTitle="Calendar">
    <div class="p-6">

      <!-- Header -->
      <div class="mb-6">
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Calendar</h1>
        <p class="text-gray-600">View all your items by expiration date</p>
      </div>

      <!-- Calendar Controls -->
      <div class="bg-white rounded-2xl shadow-lg p-6 mb-6">
        <div class="flex items-center justify-between mb-6">
          
          <!-- Month Navigation -->
          <div class="flex items-center gap-4">
            <button
              @click="previousMonth"
              class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <ChevronLeft :size="24" class="text-gray-600" />
            </button>
            
            <div class="text-center">
              <h2 class="text-2xl font-bold text-gray-900">{{ currentMonthYear }}</h2>
              <p class="text-sm text-gray-500">{{ itemsThisMonth }} items this month</p>
            </div>
            
            <button
              @click="nextMonth"
              class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <ChevronRight :size="24" class="text-gray-600" />
            </button>
          </div>

          <!-- View Toggle & Actions -->
          <div class="flex items-center gap-3">
            <button
              @click="goToToday"
              class="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg font-medium transition-colors"
            >
              Today
            </button>
            
            <button
              @click="toggleView"
              class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
              :title="viewMode === 'month' ? 'Switch to List View' : 'Switch to Calendar View'"
            >
              <LayoutGrid v-if="viewMode === 'list'" :size="20" class="text-gray-600" />
              <List v-else :size="20" class="text-gray-600" />
            </button>
          </div>

        </div>

        <!-- Legend -->
        <div class="flex flex-wrap items-center gap-4 text-sm">
          <div class="flex items-center gap-2">
            <div class="w-3 h-3 rounded-full bg-red-500"></div>
            <span class="text-gray-600">Expiring soon (within 7 days)</span>
          </div>
          <div class="flex items-center gap-2">
            <div class="w-3 h-3 rounded-full bg-orange-500"></div>
            <span class="text-gray-600">Expiring this month</span>
          </div>
          <div class="flex items-center gap-2">
            <div class="w-3 h-3 rounded-full bg-blue-500"></div>
            <span class="text-gray-600">Future</span>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex items-center justify-center py-20">
        <Loader2 :size="40" class="animate-spin text-teal-500" />
      </div>

      <!-- Calendar View -->
      <div v-else-if="viewMode === 'month'" class="bg-white rounded-2xl shadow-lg overflow-hidden">
        
        <!-- Day Headers -->
        <div class="grid grid-cols-7 border-b border-gray-200 bg-gray-50">
          <div
            v-for="day in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']"
            :key="day"
            class="p-4 text-center text-sm font-semibold text-gray-600"
          >
            {{ day }}
          </div>
        </div>

        <!-- Calendar Grid -->
        <div class="grid grid-cols-7">
          <div
            v-for="(day, index) in calendarDays"
            :key="index"
            :class="[
              'min-h-32 border-b border-r border-gray-200 p-3 hover:bg-gray-50 transition-colors cursor-pointer',
              day.isToday ? 'bg-teal-50' : '',
              !day.isCurrentMonth ? 'bg-gray-50 opacity-50' : '',
              index % 7 === 6 ? 'border-r-0' : ''
            ]"
            @click="openDayModal(day)"
          >
            <!-- Date Number -->
            <div class="flex items-center justify-between mb-2">
              <span
                :class="[
                  'text-sm font-semibold',
                  day.isToday ? 'w-7 h-7 flex items-center justify-center bg-teal-500 text-white rounded-full' : 'text-gray-700',
                  !day.isCurrentMonth ? 'text-gray-400' : ''
                ]"
              >
                {{ day.date.getDate() }}
              </span>
              
              <!-- Item Count Badge -->
              <span
                v-if="day.items.length > 0"
                class="px-2 py-0.5 bg-teal-100 text-teal-700 text-xs font-semibold rounded-full"
              >
                {{ day.items.length }}
              </span>
            </div>

            <!-- Items on this day -->
            <div class="space-y-1">
              <div
                v-for="item in day.items.slice(0, 3)"
                :key="item.id"
                :class="[
                  'text-xs px-2 py-1 rounded truncate font-medium',
                  getItemColor(item)
                ]"
                :title="item.name"
              >
                {{ item.name }}
              </div>
              
              <!-- Show more indicator -->
              <div
                v-if="day.items.length > 3"
                class="text-xs text-gray-500 font-medium px-2"
              >
                +{{ day.items.length - 3 }} more
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- List View -->
      <div v-else class="space-y-4">
        <div
          v-for="group in groupedItems"
          :key="group.date"
          class="bg-white rounded-xl shadow-lg p-6"
        >
          <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
            <Calendar :size="20" class="text-teal-500" />
            {{ formatDateHeader(group.date) }}
            <span class="text-sm font-normal text-gray-500">({{ group.items.length }} items)</span>
          </h3>

          <div class="space-y-3">
            <div
              v-for="item in group.items"
              :key="item.id"
              class="flex items-center gap-4 p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors cursor-pointer"
              @click="openItemDetails(item)"
            >
              <div :class="['w-2 h-2 rounded-full', getItemDotColor(item)]"></div>
              
              <div class="flex-1">
                <p class="font-semibold text-gray-900">{{ item.name }}</p>
                <p class="text-sm text-gray-600">{{ item.category }}</p>
              </div>

              <div class="text-right">
                <p class="text-sm font-medium text-gray-700">{{ formatDate(item.expiration_date) }}</p>
                <p :class="['text-xs font-semibold', getDaysUntilColor(item)]">
                  {{ getDaysUntilText(item) }}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- No items -->
        <div v-if="groupedItems.length === 0" class="bg-white rounded-xl shadow-lg p-12 text-center">
          <CalendarOff :size="48" class="mx-auto text-gray-400 mb-4" />
          <h3 class="text-xl font-bold text-gray-900 mb-2">No items this month</h3>
          <p class="text-gray-600 mb-6">Add items to see them on your calendar</p>
          <button
            @click="$router.push('/items/new')"
            class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold hover:shadow-lg transition-all"
          >
            Add Your First Item
          </button>
        </div>
      </div>

    </div>

    <!-- Day Modal -->
    <Transition
      enter-active-class="transition-all duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-150 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="selectedDay"
        class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
        @click.self="selectedDay = null"
      >
        <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[80vh] overflow-y-auto p-6">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h3 class="text-2xl font-bold text-gray-900">{{ formatDateHeader(selectedDay.date) }}</h3>
              <p class="text-sm text-gray-600 mt-1">{{ selectedDay.items.length }} items expiring</p>
            </div>
            <button
              @click="selectedDay = null"
              class="p-2 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <X :size="24" class="text-gray-600" />
            </button>
          </div>

          <div class="space-y-3">
            <div
              v-for="item in selectedDay.items"
              :key="item.id"
              class="flex items-center gap-4 p-4 bg-gray-50 rounded-xl hover:bg-gray-100 transition-colors cursor-pointer"
              @click="openItemDetails(item)"
            >
              <div :class="['w-3 h-3 rounded-full', getItemDotColor(item)]"></div>
              
              <div class="flex-1">
                <p class="font-semibold text-gray-900">{{ item.name }}</p>
                <p class="text-sm text-gray-600">{{ item.category }}</p>
              </div>

              <ChevronRight :size="20" class="text-gray-400" />
            </div>
          </div>
        </div>
      </div>
    </Transition>

  </DashboardLayout>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import { apiFetch } from "../utils/api"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import {
  Calendar,
  CalendarOff,
  ChevronLeft,
  ChevronRight,
  LayoutGrid,
  List,
  Loader2,
  X
} from "lucide-vue-next"

const router = useRouter()

const items = ref([])
const loading = ref(true)
const currentDate = ref(new Date())
const viewMode = ref('month') // 'month' or 'list'
const selectedDay = ref(null)

const currentMonthYear = computed(() => {
  return currentDate.value.toLocaleDateString('en-US', { 
    month: 'long', 
    year: 'numeric' 
  })
})

const itemsThisMonth = computed(() => {
  return items.value.filter(item => {
    if (!item.expiration_date) return false
    const expiryDate = new Date(item.expiration_date)
    return expiryDate.getMonth() === currentDate.value.getMonth() &&
           expiryDate.getFullYear() === currentDate.value.getFullYear()
  }).length
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
    const dayItems = items.value.filter(item => {
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
      isCurrentMonth: currentDay.getMonth() === month,
      isToday: checkDate.getTime() === today.getTime()
    })
    
    currentDay.setDate(currentDay.getDate() + 1)
  }
  
  return days
})

const groupedItems = computed(() => {
  const filtered = items.value.filter(item => {
    if (!item.expiration_date) return false
    const expiryDate = new Date(item.expiration_date)
    return expiryDate.getMonth() === currentDate.value.getMonth() &&
           expiryDate.getFullYear() === currentDate.value.getFullYear()
  })
  
  // Group by date
  const groups = {}
  filtered.forEach(item => {
    const date = item.expiration_date.split('T')[0]
    if (!groups[date]) {
      groups[date] = []
    }
    groups[date].push(item)
  })
  
  // Convert to array and sort
  return Object.keys(groups)
    .sort()
    .map(date => ({
      date: new Date(date),
      items: groups[date].sort((a, b) => a.name.localeCompare(b.name))
    }))
})

onMounted(async () => {
  await loadItems()
})

async function loadItems() {
  loading.value = true
  try {
    const res = await apiFetch('/items')
    if (res.ok) {
      items.value = await res.json()
    }
  } catch (err) {
    console.error('Failed to load items:', err)
  } finally {
    loading.value = false
  }
}

function previousMonth() {
  currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() - 1, 1)
}

function nextMonth() {
  currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() + 1, 1)
}

function goToToday() {
  currentDate.value = new Date()
}

function toggleView() {
  viewMode.value = viewMode.value === 'month' ? 'list' : 'month'
}

function getDaysUntil(item) {
  if (!item.expiration_date) return null
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  const expiryDate = new Date(item.expiration_date)
  expiryDate.setHours(0, 0, 0, 0)
  const diffTime = expiryDate - today
  return Math.ceil(diffTime / (1000 * 60 * 60 * 24))
}

function getDaysUntilText(item) {
  const days = getDaysUntil(item)
  if (days === null) return 'No expiry'
  if (days < 0) return `Expired ${Math.abs(days)} days ago`
  if (days === 0) return 'Expires today'
  if (days === 1) return 'Expires tomorrow'
  return `${days} days until expiry`
}

function getDaysUntilColor(item) {
  const days = getDaysUntil(item)
  if (days === null || days < 0) return 'text-gray-500'
  if (days <= 7) return 'text-red-600'
  if (days <= 30) return 'text-orange-600'
  return 'text-blue-600'
}

function getItemColor(item) {
  const days = getDaysUntil(item)
  if (days === null) return 'bg-gray-100 text-gray-700'
  if (days < 0) return 'bg-gray-200 text-gray-600'
  if (days <= 7) return 'bg-red-100 text-red-700'
  if (days <= 30) return 'bg-orange-100 text-orange-700'
  return 'bg-blue-100 text-blue-700'
}

function getItemDotColor(item) {
  const days = getDaysUntil(item)
  if (days === null || days < 0) return 'bg-gray-400'
  if (days <= 7) return 'bg-red-500'
  if (days <= 30) return 'bg-orange-500'
  return 'bg-blue-500'
}

function formatDate(dateString) {
  if (!dateString) return 'N/A'
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { 
    month: 'short', 
    day: 'numeric', 
    year: 'numeric' 
  })
}

function formatDateHeader(date) {
  return date.toLocaleDateString('en-US', { 
    weekday: 'long',
    month: 'long', 
    day: 'numeric', 
    year: 'numeric' 
  })
}

function openDayModal(day) {
  if (day.items.length > 0) {
    selectedDay.value = day
  }
}

function openItemDetails(item) {
  selectedDay.value = null
  router.push(`/items/${item.id}`)
}
</script>