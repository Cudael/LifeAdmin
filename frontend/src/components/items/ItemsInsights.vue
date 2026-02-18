<script setup>
import { TrendingUp, Clock, AlertTriangle, Upload, Calendar } from "lucide-vue-next"

const props = defineProps({
  insights: {
    type: Object,
    required: true
  },
  totalItems: {
    type: Number,
    required: true
  },
  documentsCount: {
    type: Number,
    required: true
  },
  subscriptionsCount: {
    type: Number,
    required: true
  },
  isPremium: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['filter'])

function handleFilter(filter) {
  emit('filter', filter)
}
</script>

<template>
  <div class="mb-6 bg-gradient-to-br from-purple-50 via-pink-50 to-orange-50 rounded-2xl p-6 border-2 border-purple-200/50 shadow-lg">
    <div class="flex items-center gap-2 mb-4">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center shadow-md">
        <TrendingUp :size="20" class="text-white" />
      </div>
      <h3 class="text-lg font-bold text-white">Insights</h3>
    </div>

    <!-- Stats Grid - Top Row (4 insights) -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 mb-3">
      
      <!-- Expiring This Month -->
      <div class="bg-orange-900/20 backdrop-blur-sm rounded-xl p-3 border border-orange-800 hover:shadow-md transition-shadow">
        <div class="flex items-center gap-2 mb-1">
          <Clock :size="14" class="text-orange-500" />
          <p class="text-xs text-gray-300 font-medium">Expiring This Month</p>
        </div>
        <p class="text-2xl font-bold text-orange-400">
          {{ insights.expiringThisMonth }}
        </p>
        <button
          v-if="insights.expiringThisMonth > 0"
          @click="handleFilter('soon')"
          class="mt-1 text-xs text-orange-400 hover:text-orange-500 font-medium hover:underline"
        >
          View items →
        </button>
      </div>

      <!-- Needs Attention -->
      <div class="bg-red-900/20 backdrop-blur-sm rounded-xl p-3 border border-red-800 hover:shadow-md transition-shadow">
        <div class="flex items-center gap-2 mb-1">
          <AlertTriangle :size="14" class="text-red-500" />
          <p class="text-xs text-gray-300 font-medium">Needs Attention</p>
        </div>
        <p class="text-2xl font-bold text-red-400">
          {{ insights.needsAttention }}
        </p>
        <button
          v-if="insights.needsAttention > 0"
          @click="handleFilter('expired')"
          class="mt-1 text-xs text-red-400 hover:text-red-500 font-medium hover:underline"
        >
          View expired →
        </button>
      </div>

      <!-- Files Uploaded -->
      <div class="bg-teal-900/20 backdrop-blur-sm rounded-xl p-3 border border-teal-800 hover:shadow-md transition-shadow">
        <div class="flex items-center gap-2 mb-1">
          <Upload :size="14" class="text-teal-400" />
          <p class="text-xs text-gray-300 font-medium">Files Uploaded</p>
        </div>
        <p class="text-2xl font-bold text-teal-400">
          {{ insights.filesUploaded }}
        </p>
        <p class="mt-1 text-xs text-gray-400">
          {{ totalItems > 0 
            ? Math.round((insights.filesUploaded / totalItems) * 100) 
            : 0 
          }}% of items
        </p>
      </div>

      <!-- Added This Week -->
      <div class="bg-gray-800/50 backdrop-blur-sm rounded-xl p-3 border border-gray-800 hover:shadow-md transition-shadow">
        <div class="flex items-center gap-2 mb-1">
          <Calendar :size="14" class="text-blue-500" />
          <p class="text-xs text-gray-300 font-medium">Added This Week</p>
        </div>
        <p class="text-2xl font-bold text-blue-600">
          {{ insights.addedThisWeek }}
        </p>
        <p class="mt-1 text-xs text-gray-400">
          Last 7 days
        </p>
      </div>

    </div>

    <!-- Stats Grid - Bottom Row (3 quick stats) -->
    <div class="grid grid-cols-2 lg:grid-cols-3 gap-3">
      
      <div class="bg-gray-800/50 backdrop-blur-sm rounded-xl p-3 border border-gray-800 hover:shadow-md transition-shadow">
        <p class="text-xs text-gray-400 mb-1">Total Items</p>
        <p class="text-2xl font-bold text-white">
          {{ isPremium ? totalItems : `${totalItems}/20` }}
        </p>
        <p v-if="!isPremium" class="text-xs text-gray-400 mt-1">
          Free plan limit
        </p>
        <p v-else class="text-xs text-teal-600 mt-1">
          Unlimited
        </p>
      </div>

      <div class="bg-teal-900/20 backdrop-blur-sm rounded-xl p-3 border border-gray-800 hover:shadow-md transition-shadow">
        <p class="text-xs text-gray-400 mb-1">Documents</p>
        <p class="text-2xl font-bold text-teal-600">
          {{ documentsCount }}
        </p>
      </div>

      <div class="bg-gray-800/50 backdrop-blur-sm rounded-xl p-3 border border-gray-800 hover:shadow-md transition-shadow">
        <p class="text-xs text-gray-400 mb-1">Subscriptions</p>
        <p class="text-2xl font-bold text-purple-600">
          {{ subscriptionsCount }}
        </p>
      </div>

    </div>
  </div>
</template>
