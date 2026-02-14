<template>
  <DashboardLayout pageTitle="Dashboard">

    <!-- PAGE ACTION BUTTONS -->
    <template #actions>
      <div class="flex gap-3">
        <RouterLink
          to="/add-item"
          class="group px-5 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg shadow-teal-500/30 hover:shadow-xl hover:shadow-teal-500/40 hover:scale-105 transition-all duration-200 flex items-center gap-2"
        >
          <PlusCircle :size="18" class="group-hover:rotate-90 transition-transform duration-200" />
          Add Item
        </RouterLink>
      </div>
    </template>

    <!-- SUMMARY CARDS - Compact Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4 mb-8">
      
      <SummaryCard
        label="Total Items"
        :icon="Package"
        iconColor="stroke-teal-500"
        subtitle="All items"
        :value="stats.total"
        bgGradient="from-teal-50 to-cyan-50"
        class="hover:scale-105 transition-transform duration-200"
        @click="navigateToItems('all')"
      />

      <SummaryCard
        label="Expiring Soon"
        :icon="Clock"
        iconColor="stroke-orange-500"
        subtitle="Within 30 days"
        :value="stats.soon"
        bgGradient="from-orange-50 to-red-50"
        class="hover:scale-105 transition-transform duration-200"
        @click="navigateToItems('soon')"
      />

      <SummaryCard
        label="This Week"
        :icon="Calendar"
        iconColor="stroke-amber-500"
        subtitle="Next 7 days"
        :value="stats.week"
        bgGradient="from-amber-50 to-yellow-50"
        class="hover:scale-105 transition-transform duration-200"
        @click="navigateToItems('week')"
      />

      <SummaryCard
        label="Expired"
        :icon="AlertTriangle"
        iconColor="stroke-red-500"
        subtitle="Needs attention"
        :value="stats.expired"
        bgGradient="from-red-50 to-pink-50"
        class="hover:scale-105 transition-transform duration-200"
        @click="navigateToItems('expired')"
      />

      <SummaryCard
        label="Documents"
        :icon="FileText"
        iconColor="stroke-green-500"
        subtitle="Uploaded files"
        :value="stats.documents"
        bgGradient="from-green-50 to-emerald-50"
        class="hover:scale-105 transition-transform duration-200"
        @click="navigateToItems('documents')"
      />

      <SummaryCard
        label="Subscriptions"
        :icon="CreditCard"
        iconColor="stroke-purple-500"
        subtitle="Recurring items"
        :value="stats.subscriptions"
        bgGradient="from-purple-50 to-violet-50"
        class="hover:scale-105 transition-transform duration-200"
        @click="navigateToItems('subscriptions')"
      />

    </div>

    <!-- WIDGETS LAYOUT - Enhanced with better styling -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

      <!-- RECENTLY ADDED (2 columns wide) - Enhanced -->
      <div class="lg:col-span-2 bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-xl font-bold text-gray-900 flex items-center gap-2">
            <Clock :size="24" class="text-teal-500" />
            Recently Added
          </h3>
          <RouterLink to="/items" class="text-teal-600 text-sm font-medium hover:text-teal-700 hover:underline">
            View All →
          </RouterLink>
        </div>

        <div v-if="recentItems.length === 0" class="text-center py-12">
          <Package :size="48" class="text-gray-300 mx-auto mb-3" />
          <p class="text-gray-500 text-sm">No recent items yet</p>
          <RouterLink to="/add-document" class="text-teal-600 text-sm font-medium hover:underline mt-2 inline-block">
            Add your first item
          </RouterLink>
        </div>

        <ul v-else class="space-y-3">
          <li
            v-for="item in recentItems"
            :key="item.id"
            class="group flex justify-between items-center p-4 rounded-xl hover:bg-gradient-to-r hover:from-teal-50 hover:to-cyan-50 transition-all duration-200 border border-transparent hover:border-teal-200"
          >
            <div class="flex items-start gap-3">
              <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center flex-shrink-0 shadow-md">
                <FileText :size="20" class="text-white" />
              </div>
              <div>
                <p class="font-semibold text-gray-900 group-hover:text-teal-700 transition-colors">
                  {{ item.name }}
                </p>
                <p class="text-xs text-gray-500 mt-1">
                  Added {{ formatDate(item.created_at) }}
                </p>
              </div>
            </div>
            <RouterLink
              :to="`/items/${item.id}`"
              class="px-4 py-2 bg-teal-500 text-white text-sm font-medium rounded-lg hover:bg-teal-600 transition-colors shadow-sm opacity-0 group-hover:opacity-100 duration-200"
            >
              View
            </RouterLink>
          </li>
        </ul>
      </div>

      <!-- RECOMMENDED ACTIONS (1 column wide) - Enhanced -->
      <div class="bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl shadow-lg p-6 text-white hover:shadow-xl transition-shadow duration-300">
        <h3 class="text-xl font-bold mb-6 flex items-center gap-2">
          <AlertTriangle :size="24" />
          Action Items
        </h3>

        <div v-if="recommended.length === 0" class="text-center py-8">
          <div class="w-16 h-16 rounded-full bg-white/20 flex items-center justify-center mx-auto mb-3">
            <span class="text-3xl">✨</span>
          </div>
          <p class="text-white/90 font-medium">You're all caught up!</p>
          <p class="text-white/70 text-sm mt-1">Great job staying organized</p>
        </div>

        <ul v-else class="space-y-4">
          <li
            v-for="action in recommended"
            :key="action.id"
            class="bg-white/10 backdrop-blur-sm rounded-xl p-4 border border-white/20 hover:bg-white/20 transition-colors duration-200"
          >
            <div class="flex items-start gap-3">
              <div class="w-2 h-2 rounded-full bg-white mt-2 flex-shrink-0"></div>
              <div class="flex-1">
                <p class="font-medium text-white mb-2">{{ action.text }}</p>
                <RouterLink
                  v-if="action.link"
                  :to="action.link"
                  class="inline-flex items-center gap-1 text-sm font-medium text-white/90 hover:text-white underline-offset-2 hover:underline"
                >
                  {{ action.cta }} →
                </RouterLink>
              </div>
            </div>
          </li>
        </ul>
      </div>

    </div>

    <!-- NEW ROW: MINI CALENDAR + CATEGORIES -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-6">
      
      <!-- Mini Calendar Widget -->
      <MiniCalendar :items="itemsStore.items" />

      <!-- Categories Overview (2 columns) -->
      <div class="lg:col-span-2 bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
        <div class="flex items-center justify-between mb-6">
          <h3 class="text-xl font-bold text-gray-900 flex items-center gap-2">
            <FileText :size="24" class="text-teal-500" />
            Categories Overview
          </h3>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 gap-4">
          <div
            v-for="category in categoryStats"
            :key="category.name"
            class="p-4 bg-gradient-to-br from-teal-50 to-cyan-50 rounded-xl border border-teal-200/50 hover:shadow-md transition-all hover:scale-105 duration-200 cursor-pointer"
          >
            <div class="text-3xl mb-2">{{ category.icon }}</div>
            <p class="text-sm text-gray-600 mb-1">{{ category.name }}</p>
            <p class="text-2xl font-bold text-gray-900">{{ category.count }}</p>
          </div>
        </div>
      </div>

    </div>

    <!-- UPCOMING EXPIRATIONS (full width) - Enhanced -->
    <div class="mt-6 bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
      <div class="flex items-center justify-between mb-6">
        <h3 class="text-xl font-bold text-gray-900 flex items-center gap-2">
          <AlertTriangle :size="24" class="text-orange-500" />
          Upcoming Expirations
        </h3>
        <span class="px-3 py-1 bg-orange-100 text-orange-700 text-xs font-semibold rounded-full">
          {{ upcoming.length }} items
        </span>
      </div>

      <div v-if="upcoming.length === 0" class="text-center py-12">
        <Calendar :size="48" class="text-gray-300 mx-auto mb-3" />
        <p class="text-gray-500 text-sm">Nothing expiring soon</p>
        <p class="text-gray-400 text-xs mt-1">You're all set! 🎉</p>
      </div>

      <ul v-else class="space-y-3">
        <li
          v-for="item in upcoming"
          :key="item.id"
          class="group flex justify-between items-center p-4 rounded-xl hover:bg-orange-50 transition-all duration-200 border border-transparent hover:border-orange-200"
        >
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-orange-400 to-red-400 flex items-center justify-center flex-shrink-0 shadow-md">
              <Clock :size="20" class="text-white" />
            </div>
            <div>
              <p class="font-semibold text-gray-900">{{ item.name }}</p>
              <p class="text-xs text-gray-500 mt-1 flex items-center gap-2">
                <span>Expires {{ formatDate(item.expiration_date) }}</span>
                <span class="px-2 py-0.5 bg-orange-100 text-orange-700 rounded-full font-medium">
                  {{ daysLeft(item.expiration_date) }} days
                </span>
              </p>
            </div>
          </div>
          <RouterLink
            :to="`/items/${item.id}`"
            class="px-4 py-2 bg-orange-500 text-white text-sm font-medium rounded-lg hover:bg-orange-600 transition-colors shadow-sm opacity-0 group-hover:opacity-100 duration-200"
          >
            Review
          </RouterLink>
        </li>
      </ul>
    </div>

    <!-- TIMELINE (full width) - Enhanced -->
    <div class="mt-6 bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
      <div class="flex items-center justify-between mb-6">
        <h3 class="text-xl font-bold text-gray-900 flex items-center gap-2">
          <Calendar :size="24" class="text-teal-500" />
          Next Deadlines
        </h3>
      </div>

      <div v-if="timeline.length === 0" class="text-center py-12">
        <Calendar :size="48" class="text-gray-300 mx-auto mb-3" />
        <p class="text-gray-500 text-sm">No upcoming deadlines</p>
      </div>

      <div v-else class="relative pl-8 space-y-6">
        <!-- Timeline line -->
        <div class="absolute left-2 top-3 bottom-3 w-0.5 bg-gradient-to-b from-teal-400 to-cyan-400"></div>

        <div
          v-for="(item, index) in timeline"
          :key="item.id"
          class="relative"
        >
          <!-- Timeline dot -->
          <div class="absolute -left-6 w-4 h-4 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 shadow-lg border-2 border-white"></div>

          <div class="bg-gradient-to-r from-teal-50 to-cyan-50 rounded-xl p-4 border border-teal-200/50 hover:shadow-md transition-shadow duration-200">
            <p class="font-semibold text-gray-900 mb-1">{{ item.name }}</p>
            <div class="flex items-center gap-3 text-xs text-gray-600">
              <span class="flex items-center gap-1">
                <Calendar :size="14" />
                {{ formatDate(item.expiration_date) }}
              </span>
              <span class="px-2 py-1 bg-teal-100 text-teal-700 rounded-full font-medium">
                {{ daysLeft(item.expiration_date) }} days left
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

  </DashboardLayout>
</template>

<script setup>
import { computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import { useItemsStore } from "../stores/items"
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
  PlusCircle
} from "lucide-vue-next"

const itemsStore = useItemsStore()
const router = useRouter()

function navigateToItems(filter) {
  router.push({ path: '/items', query: { filter } })
}

function getStatus(date) {
  if (!date) return "valid"
  const today = new Date()
  const exp = new Date(date)
  const diff = (exp - today) / (1000 * 60 * 60 * 24)

  if (diff < 0) return "expired"
  if (diff < 7) return "week"
  if (diff < 30) return "soon"
  return "valid"
}

function formatDate(date) {
  return new Date(date).toLocaleDateString()
}

function daysLeft(date) {
  const diff = (new Date(date) - new Date()) / (1000 * 60 * 60 * 24)
  return Math.ceil(diff)
}

const stats = computed(() => ({
  total: itemsStore.items.length,
  expired: itemsStore.items.filter(i => getStatus(i.expiration_date) === "expired").length,
  week: itemsStore.items.filter(i => getStatus(i.expiration_date) === "week").length,
  soon: itemsStore.items.filter(i => getStatus(i.expiration_date) === "soon").length,
  documents: itemsStore.items.filter(i => i.type === "document").length,
  subscriptions: itemsStore.items.filter(i => i.type === "subscription").length,
  missingDocs: itemsStore.items.filter(i => !i.file_path).length,
  recent: itemsStore.items.filter(i => {
    const diff = (new Date() - new Date(i.created_at)) / (1000 * 60 * 60 * 24)
    return diff <= 30
  }).length
}))

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

const recentItems = computed(() =>
  [...itemsStore.items]
    .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
    .slice(0, 5)
)

const upcoming = computed(() =>
  itemsStore.items
    .filter(i => getStatus(i.expiration_date) === "soon" || getStatus(i.expiration_date) === "week")
    .sort((a, b) => new Date(a.expiration_date) - new Date(b.expiration_date))
    .slice(0, 5)
)

const timeline = computed(() =>
  itemsStore.items
    .filter(i => i.expiration_date)
    .sort((a, b) => new Date(a.expiration_date) - new Date(b.expiration_date))
    .slice(0, 5)
)

const recommended = computed(() => {
  const actions = []

  if (stats.value.expired > 0) {
    actions.push({
      id: 1,
      text: `${stats.value.expired} items have expired — review them`,
      link: "/items?filter=expired",
      cta: "Review Now"
    })
  }

  if (stats.value.soon > 0) {
    actions.push({
      id: 2,
      text: `${stats.value.soon} items are expiring soon`,
      link: "/items?filter=soon",
      cta: "View Items"
    })
  }

  if (stats.value.missingDocs > 0) {
    actions.push({
      id: 3,
      text: `${stats.value.missingDocs} items are missing documents`,
      link: "/items?filter=missingDocs",
      cta: "Fix Now"
    })
  }

  if (stats.value.recent === 0) {
    actions.push({
      id: 4,
      text: "Add your first item to get started",
      link: "/add-document",
      cta: "Add Item"
    })
  }

  return actions.slice(0, 4)
})

onMounted(async () => {
  const res = await apiFetch("/items")
  const data = await res.json()
  itemsStore.setItems(data.items || data)
})
</script>