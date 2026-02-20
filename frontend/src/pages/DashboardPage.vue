<template>
  <DashboardLayout pageTitle="Command Center">

    <!-- Ambient Dashboard Background Mesh -->
    <div class="fixed inset-0 z-0 bg-[linear-gradient(to_right,#80808008_1px,transparent_1px),linear-gradient(to_bottom,#80808008_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none"></div>
    <div class="fixed top-0 left-1/4 w-[600px] h-[400px] bg-teal-500/5 blur-[120px] rounded-full pointer-events-none z-0 mix-blend-screen"></div>
    <div class="fixed bottom-0 right-1/4 w-[500px] h-[400px] bg-cyan-500/5 blur-[120px] rounded-full pointer-events-none z-0 mix-blend-screen"></div>

    <div class="relative z-10 w-full max-w-[1600px] mx-auto space-y-6 pb-12">

      <!-- Dynamic Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
        <div>
          <h1 class="text-3xl font-extrabold text-white tracking-tight">{{ greeting }}, Admin.</h1>
          <p class="text-slate-400 text-sm mt-1">Here is the latest intelligence on your vault.</p>
        </div>
        <RouterLink 
          to="/add-item" 
          class="group relative inline-flex items-center justify-center gap-2 px-6 py-3 bg-slate-900 text-white rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.15)] border border-teal-500/30 hover:bg-slate-800 transition-all duration-300 w-full sm:w-auto"
        >
          <div class="absolute inset-0 bg-gradient-to-r from-teal-500/20 to-cyan-500/20 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity blur-md"></div>
          <Plus :size="18" class="text-teal-400" />
          <span>Add New Item</span>
        </RouterLink>
      </div>

      <!-- 12-COLUMN BENTO BOX GRID -->
      <div class="grid grid-cols-12 gap-6">

        <!-- METRICS ROW (Span 2 cols each on large, 4 on medium, 6 on mobile) -->
        <template v-if="loading">
          <div v-for="i in 6" :key="i" class="col-span-6 md:col-span-4 xl:col-span-2 rounded-3xl bg-slate-800/30 border border-white/5 animate-pulse h-44"></div>
        </template>
        
        <template v-else>
          <SummaryCard class="col-span-6 md:col-span-4 xl:col-span-2" label="Total Items" :icon="Package" accentColor="teal" :value="stats.total" :activitySummary="activitySummaries.totalItems" @click="navigateToItems('all')" />
          <SummaryCard class="col-span-6 md:col-span-4 xl:col-span-2" label="Expiring Soon" :icon="Clock" accentColor="orange" :value="stats.soon" :activitySummary="activitySummaries.expiringSoon" @click="navigateToItems('soon')" />
          <SummaryCard class="col-span-6 md:col-span-4 xl:col-span-2" label="This Week" :icon="Calendar" accentColor="amber" :value="stats.week" :activitySummary="activitySummaries.thisWeek" @click="navigateToItems('week')" />
          <SummaryCard class="col-span-6 md:col-span-4 xl:col-span-2" label="Expired" :icon="AlertTriangle" accentColor="rose" isAlert :value="stats.expired" :activitySummary="activitySummaries.expired" @click="navigateToItems('expired')" />
          <SummaryCard class="col-span-6 md:col-span-4 xl:col-span-2" label="Documents" :icon="FileText" accentColor="emerald" :value="stats.documents" :activitySummary="activitySummaries.documents" @click="navigateToItems('documents')" />
          <SummaryCard class="col-span-6 md:col-span-4 xl:col-span-2" label="Subscriptions" :icon="CreditCard" accentColor="indigo" :value="stats.subscriptions" :activitySummary="activitySummaries.subscriptions" @click="navigateToItems('subscriptions')" />
        </template>


        <!-- ROW 2 -->
        <!-- RECENTLY ADDED (Span 8) -->
        <div class="col-span-12 lg:col-span-8 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 p-8 shadow-[0_8px_30px_rgba(0,0,0,0.12)] flex flex-col h-full animate-fade-in-up">
          <div class="flex items-center justify-between mb-8">
            <h3 class="text-lg font-bold text-white flex items-center gap-3">
              <div class="w-8 h-8 rounded-lg bg-white/5 flex items-center justify-center text-teal-400 border border-white/5">
                <History :size="16" />
              </div>
              Recently Added
            </h3>
            <RouterLink to="/items" class="text-xs font-bold uppercase tracking-wider text-slate-500 hover:text-teal-400 transition-colors flex items-center gap-1 group">
              View Database <ChevronRight :size="14" class="group-hover:translate-x-0.5 transition-transform" />
            </RouterLink>
          </div>

          <div v-if="recentItems.length === 0" class="flex-1 flex flex-col items-center justify-center text-center py-12 border border-dashed border-white/10 rounded-2xl bg-white/[0.01]">
            <Package :size="32" class="text-slate-600 mb-3" />
            <p class="text-slate-400 text-sm">Your vault is currently empty.</p>
          </div>

          <div v-else class="flex-1 -mx-2">
            <!-- Sleek Table/List -->
            <div 
              v-for="item in recentItems.slice(0, 4)" 
              :key="item.id"
              @click="router.push(`/items/${item.id}`)"
              class="group grid grid-cols-[auto_1fr_auto] items-center gap-4 p-3 rounded-2xl hover:bg-white/[0.03] transition-colors cursor-pointer border border-transparent hover:border-white/5"
            >
              <div class="w-12 h-12 rounded-xl bg-slate-800 border border-white/5 flex items-center justify-center text-slate-400 group-hover:text-teal-400 transition-colors">
                <FileText :size="20" />
              </div>
              <div class="min-w-0">
                <p class="text-sm font-bold text-slate-200 truncate group-hover:text-white transition-colors">{{ item.name }}</p>
                <div class="flex items-center gap-2 mt-1">
                  <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-widest bg-slate-800 text-slate-400">
                    {{ item.category || 'Uncategorized' }}
                  </span>
                  <span class="text-xs text-slate-500 truncate">Added {{ formatDate(item.created_at) }}</span>
                </div>
              </div>
              <div class="pr-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <ArrowUpRight :size="18" class="text-teal-400" />
              </div>
            </div>
          </div>
        </div>

        <!-- ACTION REQUIRED (Span 4) -->
        <div class="col-span-12 lg:col-span-4 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 p-8 shadow-[0_8px_30px_rgba(0,0,0,0.12)] flex flex-col h-full relative overflow-hidden animate-fade-in-up animation-delay-100">
          <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-rose-500 via-orange-500 to-amber-500 opacity-50"></div>
          
          <h3 class="text-lg font-bold text-white flex items-center gap-3 mb-8">
            <div class="w-8 h-8 rounded-lg bg-rose-500/10 flex items-center justify-center text-rose-400 border border-rose-500/20">
              <Zap :size="16" />
            </div>
            Action Required
          </h3>

          <div v-if="recommended.length === 0" class="flex-1 flex flex-col items-center justify-center text-center">
            <div class="w-16 h-16 rounded-full bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center mb-4">
              <CheckCircle2 :size="28" class="text-emerald-400" />
            </div>
            <p class="text-white font-medium">All clear.</p>
            <p class="text-slate-400 text-sm mt-1">No pending actions required.</p>
          </div>

          <div v-else class="space-y-3 flex-1">
            <RouterLink
              v-for="action in recommended"
              :key="action.id"
              :to="action.link"
              class="group block bg-slate-950/50 rounded-2xl p-4 border transition-colors duration-300"
              :class="{
                'border-rose-500/30 hover:border-rose-500/50': action.severity === 'error',
                'border-orange-500/30 hover:border-orange-500/50': action.severity === 'warning' && action.priority === 'high',
                'border-amber-500/30 hover:border-amber-500/50': action.severity === 'warning' && action.priority === 'medium',
                'border-white/5 hover:border-teal-500/30': action.severity === 'info'
              }"
            >
              <div class="flex items-start gap-3">
                <div 
                  class="w-2 h-2 rounded-full mt-1.5 shrink-0 shadow-lg"
                  :class="{
                    'bg-rose-400 shadow-rose-500/50 animate-pulse': action.severity === 'error',
                    'bg-orange-400 shadow-orange-500/50': action.severity === 'warning' && action.priority === 'high',
                    'bg-amber-400 shadow-amber-500/50': action.severity === 'warning' && action.priority === 'medium',
                    'bg-teal-400 shadow-teal-500/50': action.severity === 'info'
                  }"
                ></div>
                <div>
                  <p class="font-medium text-slate-200 text-sm leading-relaxed mb-2">{{ action.text }}</p>
                  <span class="text-xs font-bold uppercase tracking-wider text-slate-500 group-hover:text-white transition-colors flex items-center gap-1">
                    {{ action.cta }} <ArrowUpRight :size="12" />
                  </span>
                </div>
              </div>
            </RouterLink>
          </div>
        </div>

        <!-- ROW 3 -->
        <!-- CATEGORY DISTRIBUTION (Span 4) -->
        <div class="col-span-12 lg:col-span-4 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 p-8 shadow-[0_8px_30px_rgba(0,0,0,0.12)] animate-fade-in-up animation-delay-200">
          <h3 class="text-lg font-bold text-white flex items-center gap-3 mb-8">
            <div class="w-8 h-8 rounded-lg bg-indigo-500/10 flex items-center justify-center text-indigo-400 border border-indigo-500/20">
              <LayoutGrid :size="16" />
            </div>
            Vault Distribution
          </h3>

          <div class="space-y-5">
            <div 
              v-for="category in categoryStats" 
              :key="category.name"
              class="group cursor-pointer"
              @click="navigateToItems(category.key)"
            >
              <div class="flex justify-between text-sm mb-2">
                <span class="text-slate-300 font-medium flex items-center gap-2">
                  <span>{{ category.icon }}</span> {{ category.name }}
                </span>
                <span class="text-slate-500 font-bold">{{ category.count }}</span>
              </div>
              <div class="h-1.5 w-full bg-slate-800 rounded-full overflow-hidden">
                <div 
                  class="h-full rounded-full transition-all duration-1000 ease-out"
                  :class="category.count > 0 ? 'bg-gradient-to-r from-indigo-500 to-purple-500' : 'bg-transparent'"
                  :style="{ width: `${maxCategoryCount > 0 ? (category.count / maxCategoryCount) * 100 : 0}%` }"
                ></div>
              </div>
            </div>
          </div>
        </div>

        <!-- MINI CALENDAR (Span 4) -->
        <div class="col-span-12 lg:col-span-4 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 p-8 shadow-[0_8px_30px_rgba(0,0,0,0.12)] animate-fade-in-up animation-delay-300">
          <MiniCalendar :items="itemsStore.items" />
        </div>

        <!-- TIMELINE (Span 4) -->
        <div class="col-span-12 lg:col-span-4 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 p-8 shadow-[0_8px_30px_rgba(0,0,0,0.12)] animate-fade-in-up animation-delay-400">
          <div class="flex items-center justify-between mb-8">
            <h3 class="text-lg font-bold text-white flex items-center gap-3">
              <div class="w-8 h-8 rounded-lg bg-teal-500/10 flex items-center justify-center text-teal-400 border border-teal-500/20">
                <GitCommit :size="16" />
              </div>
              Upcoming Timeline
            </h3>
          </div>

          <div v-if="timeline.length === 0" class="text-center py-10 border border-dashed border-white/10 rounded-2xl bg-white/[0.01]">
            <Calendar :size="32" class="text-slate-600 mx-auto mb-3" />
            <p class="text-slate-400 text-sm">No upcoming deadlines</p>
          </div>

          <div v-else class="relative pl-6 space-y-6">
            <!-- The glowing laser line -->
            <div class="absolute left-[7px] top-2 bottom-4 w-px bg-gradient-to-b from-teal-400 via-cyan-500 to-transparent opacity-30"></div>

            <div
              v-for="(item, index) in timeline"
              :key="item.id"
              class="relative"
            >
              <!-- Glowing Dot -->
              <div class="absolute -left-[29px] top-1.5 w-3 h-3 rounded-full bg-slate-900 border-2 border-teal-400 shadow-[0_0_10px_rgba(45,212,191,0.5)] z-10"></div>

              <div class="pl-4">
                <p class="font-bold text-slate-200 mb-1 text-sm truncate pr-2">{{ item.name }}</p>
                <div class="flex items-center gap-3 mt-1.5">
                  <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-widest bg-slate-800 text-slate-300">
                    {{ formatDate(item.expiration_date) }}
                  </span>
                  <span 
                    class="text-[10px] font-bold uppercase tracking-widest flex items-center gap-1"
                    :class="getTimelineBadgeTextClasses(item.expiration_date)"
                  >
                    <Clock :size="10" />
                    {{ getTimelineBadgeText(item.expiration_date) }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { computed, onMounted, ref } from "vue"
import { useRouter } from "vue-router"
import { useItemsStore } from "../stores/items"
import { useItemStatus } from "../composables/useItemStatus"
import { apiFetch } from "../utils/api"

import DashboardLayout from "../layouts/DashboardLayout.vue"
import SummaryCard from "../components/SummaryCard.vue"
import MiniCalendar from "../components/MiniCalendar.vue"

import {
  Package,
  Clock,
  Calendar,
  AlertTriangle,
  FileText,
  CreditCard,
  Zap,
  History,
  LayoutGrid,
  ChevronRight,
  ArrowUpRight,
  CheckCircle2,
  GitCommit,
  Plus
} from "lucide-vue-next"

const itemsStore = useItemsStore()
const router = useRouter()
const { getStatus, daysLeft } = useItemStatus()

const apiStats = ref(null)
const loading = ref(true)

// Generate dynamic greeting
const greeting = computed(() => {
  const hour = new Date().getHours()
  if (hour < 12) return 'Good morning'
  if (hour < 18) return 'Good afternoon'
  return 'Good evening'
})

function navigateToItems(filter) {
  router.push({ path: '/items', query: { filter } })
}

function formatDate(date) {
  return new Date(date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

function getTimelineBadgeTextClasses(expirationDate) {
  const days = daysLeft(expirationDate)
  if (days === null) return 'text-slate-500'
  
  if (days <= 0) {
    return 'text-rose-400'
  } else if (days <= 7) {
    return 'text-rose-400'
  } else if (days <= 30) {
    return 'text-orange-400'
  } else {
    return 'text-teal-400'
  }
}

function getTimelineBadgeText(expirationDate) {
  const days = daysLeft(expirationDate)
  if (days === null) return 'No expiration'
  
  if (days < 0) {
    return 'Expired'
  } else if (days === 0) {
    return 'Expires today'
  } else {
    return `In ${days} days`
  }
}

const stats = computed(() => ({
  total: itemsStore.items.length,
  expired: itemsStore.items.filter(i => getStatus(i.expiration_date).key === "expired").length,
  week: itemsStore.items.filter(i => getStatus(i.expiration_date).key === "week").length,
  soon: itemsStore.items.filter(i => getStatus(i.expiration_date).key === "soon").length,
  documents: itemsStore.items.filter(i => i.type === "document").length,
  subscriptions: itemsStore.items.filter(i => i.type === "subscription").length,
  missingDocs: itemsStore.items.filter(i => !i.file_path).length,
  recent: itemsStore.items.filter(i => {
    const diff = (new Date() - new Date(i.created_at)) / (1000 * 60 * 60 * 24)
    return diff <= 30
  }).length
}))

const activitySummaries = computed(() => {
  if (!apiStats.value?.activity_summaries) {
    return {
      totalItems: "Loading...",
      expiringSoon: "Loading...",
      thisWeek: "Loading...",
      expired: "Loading...",
      documents: "Loading...",
      subscriptions: "Loading..."
    }
  }
  const summaries = apiStats.value.activity_summaries
  return {
    totalItems: `${summaries.items_added_this_month} added in last 30 days`,
    expiringSoon: `${summaries.items_expiring_this_month} expiring this month`,
    thisWeek: `${summaries.items_expiring_this_week} expiring this week`,
    expired: `${summaries.expired_items} items need review`,
    documents: `${summaries.documents_total} securely stored`,
    subscriptions: `${summaries.subscriptions_renewing_week} renewing in 7 days`
  }
})

const categoryStats = computed(() => {
  const categories = [
    { name: 'Passport', icon: '🛂', key: 'passport' },
    { name: 'License', icon: '🪪', key: 'license' },
    { name: 'Insurance', icon: '🏥', key: 'insurance' },
    { name: 'Banking', icon: '🏦', key: 'banking' },
    { name: 'Subscriptions', icon: '💳', key: 'subscription' },
    { name: 'Other', icon: '📄', key: 'other' }
  ]

  return categories.map(cat => ({
    ...cat,
    count: itemsStore.items.filter(item => 
      item.category?.toLowerCase() === cat.key ||
      item.type?.toLowerCase() === cat.key
    ).length
  }))
})

// Used to calculate the percentage width of the category progress bars
const maxCategoryCount = computed(() => {
  const max = Math.max(...categoryStats.value.map(c => c.count))
  return max > 0 ? max : 1
})

const recentItems = computed(() =>
  [...itemsStore.items]
    .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
    .slice(0, 5)
)

const timeline = computed(() =>
  itemsStore.items
    .filter(i => i.expiration_date && daysLeft(i.expiration_date) >= 0)
    .sort((a, b) => new Date(a.expiration_date) - new Date(b.expiration_date))
    .slice(0, 5)
)

const recommended = computed(() => {
  const actions = []

  if (stats.value.expired > 0) {
    actions.push({
      id: 1,
      severity: 'error',
      priority: 'high',
      text: `${stats.value.expired} items have expired and need review.`,
      link: "/items?filter=expired",
      cta: "Review Now"
    })
  }

  if (stats.value.soon > 0) {
    actions.push({
      id: 2,
      severity: 'warning',
      priority: 'high',
      text: `${stats.value.soon} items are expiring in the next 30 days.`,
      link: "/items?filter=soon",
      cta: "View Items"
    })
  }

  if (stats.value.missingDocs > 0) {
    actions.push({
      id: 3,
      severity: 'warning',
      priority: 'medium',
      text: `${stats.value.missingDocs} items are missing attached documents.`,
      link: "/items?filter=missingDocs",
      cta: "Fix Now"
    })
  }

  if (stats.value.recent === 0) {
    actions.push({
      id: 4,
      severity: 'info',
      priority: 'low',
      text: "Your vault is empty. Add your first item to get started.",
      link: "/add-item",
      cta: "Add Item"
    })
  }

  return actions.slice(0, 4)
})

onMounted(async () => {
  try {
    const itemsRes = await apiFetch("/items")
    const itemsData = await itemsRes.json()
    itemsStore.setItems(itemsData.items || itemsData)
  } catch (error) {
    console.error("Failed to fetch items:", error)
  }
  
  try {
    const statsRes = await apiFetch("/items/stats")
    apiStats.value = await statsRes.json()
  } catch (error) {
    console.error("Failed to fetch stats:", error)
  }
  
  loading.value = false
})
</script>

<style scoped>
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in-up {
  animation: fade-in-up 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.animation-delay-100 { animation-delay: 0.1s; }
.animation-delay-200 { animation-delay: 0.2s; }
.animation-delay-300 { animation-delay: 0.3s; }
.animation-delay-400 { animation-delay: 0.4s; }
</style>