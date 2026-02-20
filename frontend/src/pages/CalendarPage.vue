<template>
  <DashboardLayout pageTitle="Timeline">
    
    <!-- Ambient Background Mesh -->
    <div class="fixed inset-0 z-0 bg-[linear-gradient(to_right,#80808008_1px,transparent_1px),linear-gradient(to_bottom,#80808008_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none"></div>
    <div class="fixed top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-indigo-500/5 blur-[150px] rounded-full pointer-events-none z-0 mix-blend-screen"></div>

    <div class="relative z-10 max-w-[1600px] mx-auto pb-12 space-y-6">

      <!-- PAGE HEADER -->
      <div class="flex flex-col md:flex-row justify-between items-center gap-6 bg-slate-900/60 backdrop-blur-xl p-4 sm:p-6 rounded-[2rem] border border-white/5 shadow-lg animate-fade-in-up">
        
        <!-- Month Navigation -->
        <div class="flex items-center gap-4 w-full md:w-auto justify-between md:justify-start">
          <button
            @click="previousMonth"
            class="p-2.5 bg-slate-800 hover:bg-slate-700 border border-white/5 rounded-xl text-slate-400 hover:text-white transition-all shadow-inner group"
          >
            <ChevronLeft :size="20" class="group-hover:-translate-x-0.5 transition-transform" />
          </button>
          
          <div class="text-center min-w-[180px]">
            <h2 class="text-2xl font-extrabold text-white tracking-tight">{{ currentMonthYear }}</h2>
            <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mt-1">
              <span class="text-indigo-400">{{ itemsThisMonth }}</span> items this month
            </p>
          </div>
          
          <button
            @click="nextMonth"
            class="p-2.5 bg-slate-800 hover:bg-slate-700 border border-white/5 rounded-xl text-slate-400 hover:text-white transition-all shadow-inner group"
          >
            <ChevronRight :size="20" class="group-hover:translate-x-0.5 transition-transform" />
          </button>
        </div>

        <!-- Legend -->
        <div class="hidden xl:flex items-center gap-6 px-6 py-2.5 bg-slate-950/50 rounded-xl border border-white/5">
          <div class="flex items-center gap-2">
            <div class="w-2 h-2 rounded-full bg-rose-500 shadow-[0_0_8px_rgba(225,29,72,0.6)]"></div>
            <span class="text-xs font-semibold text-slate-400">&lt; 7 Days</span>
          </div>
          <div class="flex items-center gap-2">
            <div class="w-2 h-2 rounded-full bg-amber-400 shadow-[0_0_8px_rgba(251,191,36,0.6)]"></div>
            <span class="text-xs font-semibold text-slate-400">&lt; 30 Days</span>
          </div>
          <div class="flex items-center gap-2">
            <div class="w-2 h-2 rounded-full bg-teal-400 shadow-[0_0_8px_rgba(45,212,191,0.6)]"></div>
            <span class="text-xs font-semibold text-slate-400">Future</span>
          </div>
        </div>

        <!-- View Controls -->
        <div class="flex items-center gap-3 w-full md:w-auto justify-end">
          <button
            @click="goToToday"
            class="px-5 py-2.5 bg-white/5 hover:bg-white/10 border border-white/10 text-white rounded-xl font-bold transition-all shadow-inner text-sm"
          >
            Today
          </button>
          
          <div class="flex items-center p-1 bg-slate-950/50 border border-white/5 rounded-xl">
            <button
              @click="viewMode = 'month'"
              class="p-2 rounded-lg transition-all duration-200"
              :class="viewMode === 'month' ? 'bg-indigo-500/20 text-indigo-400 shadow-sm' : 'text-slate-500 hover:text-slate-300 hover:bg-white/5'"
            >
              <LayoutGrid :size="18" />
            </button>
            <button
              @click="viewMode = 'list'"
              class="p-2 rounded-lg transition-all duration-200"
              :class="viewMode === 'list' ? 'bg-indigo-500/20 text-indigo-400 shadow-sm' : 'text-slate-500 hover:text-slate-300 hover:bg-white/5'"
            >
              <List :size="18" />
            </button>
          </div>
        </div>

      </div>

      <!-- Loading State -->
      <div v-if="loading" class="flex flex-col items-center justify-center py-32 animate-fade-in-up">
        <div class="w-16 h-16 bg-indigo-500/10 rounded-2xl flex items-center justify-center mb-4 border border-indigo-500/20 shadow-inner">
          <Loader2 :size="32" class="animate-spin text-indigo-400" />
        </div>
        <p class="text-slate-400 font-medium">Syncing timeline...</p>
      </div>

      <!-- CALENDAR VIEW -->
      <div v-else-if="viewMode === 'month'" class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 shadow-2xl overflow-hidden animate-fade-in-up animation-delay-100 flex flex-col">
        
        <!-- Day Headers -->
        <div class="grid grid-cols-7 bg-slate-950/50 border-b border-white/5">
          <div
            v-for="day in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']"
            :key="day"
            class="py-4 text-center text-[10px] font-bold uppercase tracking-widest text-slate-500"
          >
            {{ day }}
          </div>
        </div>

        <!-- Hairline Grid Container -->
        <div class="grid grid-cols-7 gap-[1px] bg-white/5 flex-1">
          <div
            v-for="(day, index) in calendarDays"
            :key="index"
            class="bg-slate-900 min-h-[120px] sm:min-h-[140px] p-2 sm:p-3 transition-colors duration-200 group relative flex flex-col"
            :class="[
              !day.isCurrentMonth ? 'opacity-40 hover:opacity-60 bg-slate-900/50' : 'hover:bg-slate-800/80 cursor-pointer'
            ]"
            @click="openDayModal(day)"
          >
            <!-- Date Number -->
            <div class="flex items-center justify-between mb-2">
              <span
                class="flex items-center justify-center text-sm font-bold w-8 h-8 rounded-full transition-all"
                :class="[
                  day.isToday 
                    ? 'bg-indigo-500 text-white shadow-[0_0_15px_rgba(99,102,241,0.5)]' 
                    : 'text-slate-400 group-hover:text-white',
                ]"
              >
                {{ day.date.getDate() }}
              </span>
              
              <!-- Daily Counter Badge -->
              <span
                v-if="day.items.length > 0"
                class="hidden sm:flex px-2 py-0.5 bg-slate-950 border border-white/5 text-slate-300 text-[10px] font-bold rounded-full shadow-inner"
              >
                {{ day.items.length }}
              </span>
            </div>

            <!-- Items Container -->
            <div class="flex-1 space-y-1.5 overflow-hidden">
              <div
                v-for="item in day.items.slice(0, 3)"
                :key="item.id"
                class="text-[10px] sm:text-xs px-2 py-1.5 rounded-lg truncate font-bold border backdrop-blur-md transition-all duration-200"
                :class="getItemPillClasses(item)"
                :title="item.name"
              >
                {{ item.name }}
              </div>
              
              <!-- More indicator -->
              <div
                v-if="day.items.length > 3"
                class="text-[10px] text-slate-500 font-bold px-2 pt-1 uppercase tracking-wider"
              >
                +{{ day.items.length - 3 }} more
              </div>
            </div>
            
            <!-- Hover Expand Hint -->
            <div v-if="day.items.length > 0" class="absolute bottom-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity text-slate-500">
              <ArrowUpRight :size="14" />
            </div>
          </div>
        </div>
      </div>

      <!-- LIST VIEW -->
      <div v-else class="space-y-6 animate-fade-in-up animation-delay-100">
        
        <div v-if="groupedItems.length === 0" class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 shadow-2xl p-16 text-center">
          <div class="w-20 h-20 bg-slate-950 rounded-3xl border border-white/5 flex items-center justify-center mx-auto mb-6 shadow-inner">
            <CalendarOff :size="32" class="text-slate-600" />
          </div>
          <h3 class="text-2xl font-extrabold text-white tracking-tight mb-2">No items this month</h3>
          <p class="text-slate-400 font-medium mb-8">Add items to see them plotted on your timeline.</p>
          <button
            @click="$router.push('/add-item')"
            class="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.3)] hover:shadow-[0_0_30px_rgba(45,212,191,0.5)] transition-all duration-300 hover:-translate-y-0.5"
          >
            <Plus :size="18" />
            New Item
          </button>
        </div>

        <div
          v-for="group in groupedItems"
          :key="group.date"
          class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 shadow-xl p-6 sm:p-8"
        >
          <div class="flex items-center justify-between mb-6 pb-4 border-b border-white/5">
            <h3 class="text-xl font-extrabold text-white flex items-center gap-3 tracking-tight">
              <div class="w-10 h-10 rounded-xl bg-indigo-500/10 flex items-center justify-center text-indigo-400 border border-indigo-500/20">
                <Calendar :size="18" />
              </div>
              {{ formatDateHeader(group.date) }}
            </h3>
            <span class="px-3 py-1 bg-slate-950 border border-white/10 text-slate-400 text-xs font-bold uppercase tracking-wider rounded-lg shadow-inner">
              {{ group.items.length }} items
            </span>
          </div>

          <div class="space-y-3">
            <div
              v-for="item in group.items"
              :key="item.id"
              class="group flex flex-col sm:flex-row sm:items-center gap-4 p-4 bg-slate-950/50 border border-white/5 rounded-2xl hover:border-white/10 hover:bg-slate-800/80 transition-all duration-300 cursor-pointer"
              @click="openItemDetails(item)"
            >
              <div class="flex items-center gap-4 flex-1 min-w-0">
                <div :class="['w-12 h-12 rounded-xl flex items-center justify-center border shrink-0 shadow-inner', getItemIconClasses(item)]">
                  <component :is="item.type === 'subscription' ? Repeat : FileText" :size="20" />
                </div>
                
                <div class="min-w-0">
                  <p class="font-bold text-slate-200 text-lg truncate group-hover:text-white transition-colors">{{ item.name }}</p>
                  <p class="text-xs font-semibold text-slate-500 uppercase tracking-widest mt-0.5">{{ item.category || 'Uncategorized' }}</p>
                </div>
              </div>

              <div class="flex items-center justify-between sm:justify-end gap-6 sm:pl-4 sm:border-l border-white/5 mt-4 sm:mt-0">
                <div class="text-left sm:text-right">
                  <p class="text-sm font-bold text-slate-300">{{ formatDate(item.expiration_date) }}</p>
                  <p :class="['text-[10px] font-bold uppercase tracking-widest mt-1', getDaysUntilColor(item)]">
                    {{ getDaysUntilText(item) }}
                  </p>
                </div>
                <div class="w-8 h-8 rounded-full bg-white/5 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity sm:block hidden">
                  <ArrowUpRight :size="16" class="text-slate-400 group-hover:text-white" />
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- DAY MODAL (Cinematic Glassmorphic) -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 backdrop-blur-none"
      enter-to-class="opacity-100 backdrop-blur-md"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 backdrop-blur-md"
      leave-to-class="opacity-0 backdrop-blur-none"
    >
      <div
        v-if="selectedDay"
        class="fixed inset-0 bg-slate-950/80 z-[100] flex items-center justify-center p-4 sm:p-6"
        @click.self="selectedDay = null"
      >
        <Transition
          appear
          enter-active-class="transition-all duration-400 cubic-bezier(0.16, 1, 0.3, 1)"
          enter-from-class="opacity-0 scale-95 translate-y-8"
          enter-to-class="opacity-100 scale-100 translate-y-0"
          leave-active-class="transition-all duration-200 ease-in"
          leave-from-class="opacity-100 scale-100 translate-y-0"
          leave-to-class="opacity-0 scale-95 translate-y-8"
        >
          <div class="bg-slate-900 rounded-[2rem] border border-white/10 shadow-[0_20px_60px_rgba(0,0,0,0.6)] max-w-2xl w-full max-h-[85vh] flex flex-col relative overflow-hidden">
            
            <!-- Ambient Modal Glow -->
            <div class="absolute top-0 left-0 w-full h-32 bg-indigo-500/10 blur-[50px] pointer-events-none"></div>

            <div class="px-8 py-6 border-b border-white/5 flex items-center justify-between relative z-10 bg-white/[0.02]">
              <div>
                <h3 class="text-2xl font-extrabold text-white tracking-tight">{{ formatDateHeader(selectedDay.date) }}</h3>
                <p class="text-xs font-bold uppercase tracking-widest text-slate-500 mt-1">
                  <span class="text-indigo-400">{{ selectedDay.items.length }}</span> items on this day
                </p>
              </div>
              <button
                @click="selectedDay = null"
                class="w-10 h-10 bg-slate-800 hover:bg-slate-700 rounded-xl flex items-center justify-center text-slate-400 hover:text-white transition-colors border border-white/5 shadow-inner"
              >
                <X :size="20" />
              </button>
            </div>

            <div class="p-8 overflow-y-auto custom-scrollbar relative z-10 flex-1">
              <div class="space-y-3">
                <div
                  v-for="item in selectedDay.items"
                  :key="item.id"
                  class="group flex items-center gap-4 p-4 bg-slate-950/50 border border-white/5 rounded-2xl hover:border-white/10 hover:bg-slate-800 transition-all duration-300 cursor-pointer"
                  @click="openItemDetails(item)"
                >
                  <div :class="['w-10 h-10 rounded-xl flex items-center justify-center border shrink-0', getItemIconClasses(item)]">
                    <component :is="item.type === 'subscription' ? Repeat : FileText" :size="16" />
                  </div>
                  
                  <div class="flex-1 min-w-0">
                    <p class="font-bold text-slate-200 text-lg truncate group-hover:text-white">{{ item.name }}</p>
                    <div class="flex items-center gap-3 mt-1">
                      <p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">{{ item.category || 'Uncategorized' }}</p>
                      <div class="w-1 h-1 rounded-full bg-slate-700"></div>
                      <p :class="['text-[10px] font-bold uppercase tracking-widest', getDaysUntilColor(item)]">
                        {{ getDaysUntilText(item) }}
                      </p>
                    </div>
                  </div>

                  <div class="w-8 h-8 rounded-full bg-white/5 flex items-center justify-center group-hover:bg-white/10 transition-colors shrink-0">
                    <ArrowUpRight :size="16" class="text-slate-400 group-hover:text-white" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Transition>
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
  X,
  FileText,
  Repeat,
  ArrowUpRight,
  Plus
} from "lucide-vue-next"

const router = useRouter()

const items = ref([])
const loading = ref(true)
const currentDate = ref(new Date())
const viewMode = ref('month')
const selectedDay = ref(null)

const currentMonthYear = computed(() => {
  return currentDate.value.toLocaleDateString('en-US', { month: 'long', year: 'numeric' })
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
  
  const firstDay = new Date(year, month, 1)
  const lastDay = new Date(year, month + 1, 0)
  
  const startDate = new Date(firstDay)
  startDate.setDate(startDate.getDate() - firstDay.getDay())
  
  const endDate = new Date(lastDay)
  endDate.setDate(endDate.getDate() + (6 - lastDay.getDay()))
  
  const days = []
  const currentDay = new Date(startDate)
  
  while (currentDay <= endDate) {
    const checkDate = new Date(currentDay)
    checkDate.setHours(0, 0, 0, 0)
    
    const dayItems = items.value.filter(item => {
      if (!item.expiration_date) return false
      const itemDate = new Date(item.expiration_date)
      itemDate.setHours(0, 0, 0, 0)
      return itemDate.getTime() === checkDate.getTime()
    })
    
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    
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
  
  const groups = {}
  filtered.forEach(item => {
    const dateObj = new Date(item.expiration_date)
    dateObj.setHours(0, 0, 0, 0)
    const dateKey = dateObj.getTime()
    
    if (!groups[dateKey]) {
      groups[dateKey] = { date: dateObj, items: [] }
    }
    groups[dateKey].items.push(item)
  })
  
  return Object.values(groups)
    .sort((a, b) => a.date - b.date)
    .map(group => {
      group.items.sort((a, b) => a.name.localeCompare(b.name))
      return group
    })
})

onMounted(async () => {
  await loadItems()
})

async function loadItems() {
  loading.value = true
  try {
    const res = await apiFetch('/items')
    if (res.ok) {
      const data = await res.json()
      items.value = data.items || data
    }
  } catch (err) {
    console.error('Failed to load items:', err)
  } finally {
    loading.value = false
  }
}

function previousMonth() { currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() - 1, 1) }
function nextMonth() { currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() + 1, 1) }
function goToToday() { currentDate.value = new Date() }

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
  if (days < 0) return `Overdue by ${Math.abs(days)} days`
  if (days === 0) return 'Expires today'
  if (days === 1) return 'Expires tomorrow'
  return `In ${days} days`
}

function getDaysUntilColor(item) {
  const days = getDaysUntil(item)
  if (days === null) return 'text-slate-500'
  if (days <= 7) return 'text-rose-400'
  if (days <= 30) return 'text-amber-400'
  return 'text-teal-400'
}

function getItemPillClasses(item) {
  const days = getDaysUntil(item)
  if (days === null) return 'bg-slate-800 border-white/5 text-slate-400'
  if (days <= 7) return 'bg-rose-500/10 border-rose-500/20 text-rose-400'
  if (days <= 30) return 'bg-amber-500/10 border-amber-500/20 text-amber-400'
  return 'bg-teal-500/10 border-teal-500/20 text-teal-400'
}

function getItemIconClasses(item) {
  const days = getDaysUntil(item)
  if (days === null) return 'bg-slate-800 border-white/5 text-slate-400'
  if (days <= 7) return 'bg-rose-500/10 border-rose-500/20 text-rose-400'
  if (days <= 30) return 'bg-amber-500/10 border-amber-500/20 text-amber-400'
  return 'bg-teal-500/10 border-teal-500/20 text-teal-400'
}

function formatDate(dateString) {
  if (!dateString) return 'N/A'
  return new Date(dateString).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

function formatDateHeader(date) {
  return date.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' })
}

function openDayModal(day) {
  if (day.items.length > 0) selectedDay.value = day
}

function openItemDetails(item) {
  selectedDay.value = null
  router.push(`/items/${item.id}`)
}
</script>

<style scoped>
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in-up {
  animation: fade-in-up 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.animation-delay-100 { animation-delay: 0.1s; }

.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  @apply bg-slate-800 rounded-full;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  @apply bg-slate-700;
}
</style>