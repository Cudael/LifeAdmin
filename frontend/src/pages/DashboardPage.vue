<template>
  <DashboardLayout pageTitle="Dashboard">

    <!-- PAGE ACTION BUTTONS -->
    <template #actions>
      <div class="flex gap-3">
        <RouterLink
          to="/add-document"
          class="px-4 py-2 bg-gradient-to-r from-teal-400 to-cyan-400 text-black rounded-lg font-semibold shadow hover:from-teal-300 hover:to-cyan-300 transition"
        >
          + Add Document
        </RouterLink>

        <RouterLink
          to="/add-subscription"
          class="px-4 py-2 bg-white/10 backdrop-blur border border-white/20 text-white rounded-lg font-semibold hover:bg-white/20 transition"
        >
          + Add Subscription
        </RouterLink>
      </div>
    </template>

    <!-- SUMMARY CARDS ROW 1 -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">

      <SummaryCard
        label="Total Items"
        :icon="Package"
        iconColor="stroke-teal-500"
        subtitle="All stored items"
        :value="stats.total"
      />

      <SummaryCard
        label="Expiring Soon"
        :icon="Clock"
        iconColor="stroke-red-500"
        subtitle="Within 30 days"
        :value="stats.soon"
      />

      <SummaryCard
        label="This Week"
        :icon="Calendar"
        iconColor="stroke-yellow-500"
        subtitle="Next 7 days"
        :value="stats.week"
      />

      <SummaryCard
        label="Expired"
        :icon="AlertTriangle"
        iconColor="stroke-red-600"
        subtitle="Needs attention"
        :value="stats.expired"
      />

    </div>

    <!-- SUMMARY CARDS ROW 2 -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">

      <SummaryCard
        label="Documents"
        :icon="FileText"
        iconColor="stroke-green-600"
        subtitle="Uploaded files"
        :value="stats.documents"
      />

      <SummaryCard
        label="Subscriptions"
        :icon="CreditCard"
        iconColor="stroke-purple-600"
        subtitle="Recurring items"
        :value="stats.subscriptions"
      />

      <SummaryCard
        label="Recently Added"
        :icon="PlusCircle"
        iconColor="stroke-teal-600"
        subtitle="Last 30 days"
        :value="stats.recent"
      />

      <SummaryCard
        label="Missing Documents"
        :icon="AlertTriangle"
        iconColor="stroke-blue-600"
        subtitle="No file uploaded"
        :value="stats.missingDocs"
      />

    </div>

    <!-- WIDGETS LAYOUT -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">

      <!-- RECENTLY ADDED (2 columns wide) -->
      <div class="lg:col-span-2 bg-white rounded-3xl shadow p-6 border border-teal-100">
        <h3 class="text-xl font-semibold mb-4 text-gray-900">Recently Added</h3>

        <div v-if="recentItems.length === 0" class="text-gray-500 text-sm">
          No recent items.
        </div>

        <ul v-else class="space-y-4">
          <li
            v-for="item in recentItems"
            :key="item.id"
            class="flex justify-between items-center"
          >
            <div>
              <p class="font-medium text-gray-900">{{ item.name }}</p>
              <p class="text-xs text-gray-500">
                Added {{ formatDate(item.created_at) }}
              </p>
            </div>
            <RouterLink
              :to="`/items/${item.id}`"
              class="text-teal-600 text-sm font-medium hover:underline"
            >
              View
            </RouterLink>
          </li>
        </ul>
      </div>

      <!-- RECOMMENDED ACTIONS (1 column wide) -->
      <div class="bg-white rounded-3xl shadow p-6 border border-teal-100">
        <h3 class="text-xl font-semibold mb-4 text-gray-900">Recommended Actions</h3>

        <div v-if="recommended.length === 0" class="text-gray-500 text-sm">
          You're all caught up.
        </div>

        <ul v-else class="space-y-4">
          <li
            v-for="action in recommended"
            :key="action.id"
            class="flex items-start gap-3"
          >
            <div class="w-2 h-2 rounded-full bg-teal-500 mt-2"></div>

            <div>
              <p class="font-medium text-gray-900">{{ action.text }}</p>

              <RouterLink
                v-if="action.link"
                :to="action.link"
                class="text-teal-600 text-sm font-medium hover:underline"
              >
                {{ action.cta }}
              </RouterLink>
            </div>
          </li>
        </ul>
      </div>

    </div>

    <!-- UPCOMING EXPIRATIONS (full width) -->
    <div class="mt-8 bg-white rounded-3xl shadow p-6 border border-teal-100">
      <h3 class="text-xl font-semibold mb-4 text-gray-900">Upcoming Expirations</h3>

      <div v-if="upcoming.length === 0" class="text-gray-500 text-sm">
        Nothing expiring soon.
      </div>

      <ul v-else class="space-y-4">
        <li
          v-for="item in upcoming"
          :key="item.id"
          class="flex justify-between items-center"
        >
          <div>
            <p class="font-medium text-gray-900">{{ item.name }}</p>
            <p class="text-xs text-gray-500">
              Expires {{ formatDate(item.expiration_date) }}
            </p>
          </div>
          <RouterLink
            :to="`/items/${item.id}`"
            class="text-red-600 text-sm font-medium hover:underline"
          >
            Review
          </RouterLink>
        </li>
      </ul>
    </div>

    <!-- TIMELINE (full width) -->
    <div class="mt-8 bg-white rounded-3xl shadow p-6 border border-teal-100">
      <h3 class="text-xl font-semibold mb-4 text-gray-900">Next Deadlines</h3>

      <div v-if="timeline.length === 0" class="text-gray-500 text-sm">
        No upcoming deadlines.
      </div>

      <div v-else class="space-y-6">
        <div
          v-for="item in timeline"
          :key="item.id"
          class="flex items-start gap-3"
        >
          <div class="w-2 h-2 rounded-full bg-teal-500 mt-2"></div>

          <div>
            <p class="font-medium text-gray-900">{{ item.name }}</p>
            <p class="text-xs text-gray-500">
              {{ formatDate(item.expiration_date) }} • {{ daysLeft(item.expiration_date) }} days left
            </p>
          </div>
        </div>
      </div>
    </div>

  </DashboardLayout>
</template>

<script setup>
import { computed, onMounted } from "vue"
import { useItemsStore } from "../stores/items"
import { apiFetch } from "../utils/api"

import DashboardLayout from "../layouts/DashboardLayout.vue"
import SummaryCard from "../components/SummaryCard.vue"

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
      cta: "Review"
    })
  }

  if (stats.value.soon > 0) {
    actions.push({
      id: 2,
      text: `${stats.value.soon} items are expiring soon`,
      link: "/items?filter=soon",
      cta: "View"
    })
  }

  if (stats.value.missingDocs > 0) {
    actions.push({
      id: 3,
      text: `${stats.value.missingDocs} items are missing documents`,
      link: "/items?filter=missingDocs",
      cta: "Fix"
    })
  }

  if (stats.value.recent === 0) {
    actions.push({
      id: 4,
      text: "Add your first item to get started",
      link: "/add-item",
      cta: "Add Item"
    })
  }

  return actions.slice(0, 4)
})

onMounted(async () => {
  const res = await apiFetch("/items")
  const data = await res.json()
  itemsStore.setItems(data)
})
</script>