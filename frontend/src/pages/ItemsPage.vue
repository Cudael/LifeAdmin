<script setup>
import { ref, computed, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useItemsStore } from "../stores/items"
import { apiFetch } from "../utils/api"

import DashboardLayout from "../layouts/DashboardLayout.vue"
import SearchBar from "../components/SearchBar.vue"
import FilterBar from "../components/FilterBar.vue"
import ItemGrid from "../components/ItemGrid.vue"
import DeleteModal from "../components/DeleteModal.vue"

import { 
  Filter, 
  FileText, 
  Repeat,
  Layers,
  Heart,
  Wallet,
  Briefcase,
  User,
  Plane,
  Home,
  Package,
  TrendingUp,
  Clock,
  AlertTriangle,
  Upload,
  Calendar
} from "lucide-vue-next"

const itemsStore = useItemsStore()
const route = useRoute()
const router = useRouter()

// UI State
const activeCategory = ref("All")
const activeStatFilter = ref("all")
const search = ref("")
const deleteModalOpen = ref(false)
const showFilters = ref(false)
const itemToDelete = ref(null)

// Status helper
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

// Helper to calculate days left
function daysLeft(date) {
  if (!date) return null
  const today = new Date()
  const exp = new Date(date)
  const diff = Math.ceil((exp - today) / (1000 * 60 * 60 * 24))
  return diff
}

// Insights computed properties
const insights = computed(() => {
  const items = itemsStore.items

  // Expiring this month (0-30 days)
  const expiringThisMonth = items.filter(i => {
    const days = daysLeft(i.expiration_date)
    return days !== null && days >= 0 && days <= 30
  }).length

  // Needs attention (expired)
  const needsAttention = items.filter(i => 
    getStatus(i.expiration_date) === 'expired'
  ).length

  // Files uploaded
  const filesUploaded = items.filter(i => i.file_path).length

  // Added this week
  const addedThisWeek = items.filter(i => {
    if (!i.created_at) return false
    const created = new Date(i.created_at)
    const weekAgo = new Date()
    weekAgo.setDate(weekAgo.getDate() - 7)
    return created >= weekAgo
  }).length

  return {
    expiringThisMonth,
    needsAttention,
    filesUploaded,
    addedThisWeek
  }
})

// Dynamic categories
const categoryFilters = computed(() => {
  const items = itemsStore.items
  const categoryCounts = items.reduce((acc, item) => {
    const cat = item.category || 'Uncategorized'
    acc[cat] = (acc[cat] || 0) + 1
    return acc
  }, {})

  const uniqueCategories = [...new Set(items.map(item => item.category || 'Uncategorized'))]
  
  const categoryIcons = {
    'Travel': Plane,
    'Health': Heart,
    'Finance': Wallet,
    'Work': Briefcase,
    'Personal': User,
    'Subscriptions': Repeat,
    'Home': Home,
    'Uncategorized': Layers
  }

  const dynamicCategories = uniqueCategories.map(cat => ({
    label: cat,
    value: cat,
    icon: categoryIcons[cat] || Layers,
    count: categoryCounts[cat] || 0
  }))

  dynamicCategories.sort((a, b) => a.label.localeCompare(b.label))

  return [
    { label: 'All', value: 'All', icon: Layers, count: items.length },
    ...dynamicCategories
  ]
})

// Filtering logic
const filteredItems = computed(() => {
  let list = [...itemsStore.items]

  // Status filter
  switch (activeStatFilter.value) {
    case "soon":
    case "week":
    case "expired":
      list = list.filter(i => getStatus(i.expiration_date) === activeStatFilter.value)
      break
    case "documents":
      list = list.filter(i => i.type === "document")
      break
    case "subscriptions":
      list = list.filter(i => i.type === "subscription")
      break
    case "missingDocs":
      list = list.filter(i => !i.file_path)
      break
  }

  // Category filter
  if (activeCategory.value !== "All") {
    list = list.filter(i => i.category === activeCategory.value)
  }

  // Search filter
  if (search.value.trim()) {
    const q = search.value.toLowerCase()
    list = list.filter(i =>
      i.name.toLowerCase().includes(q) ||
      i.notes?.toLowerCase().includes(q)
    )
  }

  return list
})

const hasActiveFilters = computed(() => {
  return activeStatFilter.value !== 'all' || activeCategory.value !== 'All' || search.value
})

function setCategory(cat) {
  activeCategory.value = cat
}

function setFilter(filter) {
  activeStatFilter.value = filter
}

function clearFilters() {
  activeCategory.value = "All"
  activeStatFilter.value = "all"
  search.value = ""
}

function openDeleteModal(item) {
  itemToDelete.value = item
  deleteModalOpen.value = true
}

async function confirmDelete() {
  if (!itemToDelete.value) return

  try {
    await apiFetch(`/items/${itemToDelete.value.id}`, {
      method: "DELETE"
    })

    itemsStore.setItems(itemsStore.items.filter(i => i.id !== itemToDelete.value.id))
    deleteModalOpen.value = false
    itemToDelete.value = null
  } catch (error) {
    console.error('Failed to delete item:', error)
  }
}

onMounted(async () => {
  const res = await apiFetch("/items")
  const data = await res.json()
  itemsStore.setItems(data.items || data)
  
  // Apply filter from query parameter if present and valid
  const filterParam = route.query.filter
  const validFilters = ['all', 'soon', 'week', 'expired', 'documents', 'subscriptions', 'missingDocs']
  
  if (filterParam && validFilters.includes(filterParam)) {
    activeStatFilter.value = filterParam
    // Auto-open filters panel if filter is applied from URL
    showFilters.value = true
  }
})
</script>

<template>
  <DashboardLayout pageTitle="Items">

    <!-- PAGE HEADER ACTIONS -->
    <template #actions>
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full">
        
        <!-- Search Bar -->
        <div class="flex-1 max-w-xl">
          <SearchBar v-model="search" placeholder="Search items..." />
        </div>

        <!-- Action Buttons -->
        <div class="flex items-center gap-2">
          
          <!-- Filters Button (with indicator) -->
          <button
            @click="showFilters = !showFilters"
            class="relative px-4 py-2 bg-white border-2 border-gray-200 text-gray-700 rounded-xl font-semibold hover:border-teal-300 hover:shadow-md transition-all duration-200 flex items-center gap-2"
          >
            <Filter :size="18" />
            <span class="hidden md:inline">Filters</span>
            
            <!-- Active indicator dot -->
            <span 
              v-if="hasActiveFilters"
              class="absolute -top-1 -right-1 w-3 h-3 bg-teal-500 rounded-full border-2 border-white"
            ></span>
          </button>

          <!-- Add Document -->
          <RouterLink
            to="/add-document"
            class="group px-4 py-2 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:scale-105 transition-all duration-200 flex items-center gap-2"
          >
            <FileText :size="18" />
            <span class="hidden lg:inline">Document</span>
          </RouterLink>

          <!-- Add Subscription -->
          <RouterLink
            to="/add-subscription"
            class="group px-4 py-2 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:scale-105 transition-all duration-200 flex items-center gap-2"
          >
            <Repeat :size="18" />
            <span class="hidden lg:inline">Subscription</span>
          </RouterLink>

        </div>
      </div>
    </template>

    <!-- INSIGHTS CARD -->
    <div class="mb-6 bg-gradient-to-br from-purple-50 via-pink-50 to-orange-50 rounded-2xl p-6 border-2 border-purple-200/50 shadow-lg">
      <div class="flex items-center gap-2 mb-4">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center shadow-md">
          <TrendingUp :size="20" class="text-white" />
        </div>
        <h3 class="text-lg font-bold text-gray-900">Insights</h3>
      </div>

      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
        
        <!-- Expiring This Month -->
        <div class="bg-white/70 backdrop-blur-sm rounded-xl p-4 border border-orange-200/50 hover:shadow-md transition-shadow">
          <div class="flex items-center gap-2 mb-2">
            <Clock :size="16" class="text-orange-500" />
            <p class="text-xs text-gray-600 font-medium">Expiring This Month</p>
          </div>
          <p class="text-3xl font-bold text-orange-600">
            {{ insights.expiringThisMonth }}
          </p>
          <button
            v-if="insights.expiringThisMonth > 0"
            @click="setFilter('soon')"
            class="mt-2 text-xs text-orange-600 hover:text-orange-700 font-medium hover:underline"
          >
            View items →
          </button>
        </div>

        <!-- Needs Attention -->
        <div class="bg-white/70 backdrop-blur-sm rounded-xl p-4 border border-red-200/50 hover:shadow-md transition-shadow">
          <div class="flex items-center gap-2 mb-2">
            <AlertTriangle :size="16" class="text-red-500" />
            <p class="text-xs text-gray-600 font-medium">Needs Attention</p>
          </div>
          <p class="text-3xl font-bold text-red-600">
            {{ insights.needsAttention }}
          </p>
          <button
            v-if="insights.needsAttention > 0"
            @click="setFilter('expired')"
            class="mt-2 text-xs text-red-600 hover:text-red-700 font-medium hover:underline"
          >
            View expired →
          </button>
        </div>

        <!-- Files Uploaded -->
        <div class="bg-white/70 backdrop-blur-sm rounded-xl p-4 border border-teal-200/50 hover:shadow-md transition-shadow">
          <div class="flex items-center gap-2 mb-2">
            <Upload :size="16" class="text-teal-500" />
            <p class="text-xs text-gray-600 font-medium">Files Uploaded</p>
          </div>
          <p class="text-3xl font-bold text-teal-600">
            {{ insights.filesUploaded }}
          </p>
          <p class="mt-2 text-xs text-gray-500">
            {{ itemsStore.items.length > 0 
              ? Math.round((insights.filesUploaded / itemsStore.items.length) * 100) 
              : 0 
            }}% of items
          </p>
        </div>

        <!-- Added This Week -->
        <div class="bg-white/70 backdrop-blur-sm rounded-xl p-4 border border-blue-200/50 hover:shadow-md transition-shadow">
          <div class="flex items-center gap-2 mb-2">
            <Calendar :size="16" class="text-blue-500" />
            <p class="text-xs text-gray-600 font-medium">Added This Week</p>
          </div>
          <p class="text-3xl font-bold text-blue-600">
            {{ insights.addedThisWeek }}
          </p>
          <p class="mt-2 text-xs text-gray-500">
            Last 7 days
          </p>
        </div>

      </div>
    </div>

    <!-- QUICK STATS (Simplified) -->
    <div class="mb-6 grid grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="bg-white rounded-xl p-4 border border-gray-200 hover:shadow-md transition-shadow">
        <p class="text-xs text-gray-500 mb-1">Total</p>
        <p class="text-2xl font-bold text-gray-900">{{ itemsStore.items.length }}</p>
      </div>
      
      <div class="bg-white rounded-xl p-4 border border-orange-200 hover:shadow-md transition-shadow">
        <p class="text-xs text-gray-500 mb-1">Expiring</p>
        <p class="text-2xl font-bold text-orange-600">
          {{ itemsStore.items.filter(i => getStatus(i.expiration_date) === 'soon').length }}
        </p>
      </div>

      <div class="bg-white rounded-xl p-4 border border-teal-200 hover:shadow-md transition-shadow">
        <p class="text-xs text-gray-500 mb-1">Documents</p>
        <p class="text-2xl font-bold text-teal-600">
          {{ itemsStore.items.filter(i => i.type === 'document').length }}
        </p>
      </div>

      <div class="bg-white rounded-xl p-4 border border-purple-200 hover:shadow-md transition-shadow">
        <p class="text-xs text-gray-500 mb-1">Subscriptions</p>
        <p class="text-2xl font-bold text-purple-600">
          {{ itemsStore.items.filter(i => i.type === 'subscription').length }}
        </p>
      </div>
    </div>

    <!-- ACTIVE FILTERS CHIPS -->
    <div 
      v-if="hasActiveFilters"
      class="mb-4 flex items-center gap-2 flex-wrap"
    >
      <span class="text-xs text-gray-500 font-medium">Active:</span>
      
      <button
        v-if="activeStatFilter !== 'all'"
        @click="setFilter('all')"
        class="px-3 py-1 bg-teal-100 text-teal-700 text-xs rounded-full font-medium hover:bg-teal-200 transition-colors flex items-center gap-1"
      >
        {{ activeStatFilter }}
        <span class="text-teal-600">×</span>
      </button>
      
      <button
        v-if="activeCategory !== 'All'"
        @click="setCategory('All')"
        class="px-3 py-1 bg-cyan-100 text-cyan-700 text-xs rounded-full font-medium hover:bg-cyan-200 transition-colors flex items-center gap-1"
      >
        {{ activeCategory }}
        <span class="text-cyan-600">×</span>
      </button>
      
      <button
        v-if="search"
        @click="search = ''"
        class="px-3 py-1 bg-blue-100 text-blue-700 text-xs rounded-full font-medium hover:bg-blue-200 transition-colors flex items-center gap-1"
      >
        "{{ search }}"
        <span class="text-blue-600">×</span>
      </button>

      <button
        @click="clearFilters"
        class="text-xs text-gray-500 hover:text-gray-700 font-medium underline"
      >
        Clear all
      </button>
    </div>

    <!-- COLLAPSIBLE FILTERS -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-4 max-h-0"
      enter-to-class="opacity-100 translate-y-0 max-h-[1000px]"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0 max-h-[1000px]"
      leave-to-class="opacity-0 -translate-y-4 max-h-0"
    >
      <div v-show="showFilters" class="mb-6 overflow-hidden">
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 space-y-6">
          
          <!-- Status Filters -->
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">Status</h3>
            <div class="flex flex-wrap gap-2">
              <button
                v-for="filter in ['all', 'expired', 'week', 'soon', 'missingDocs']"
                :key="filter"
                @click="setFilter(filter)"
                :class="[
                  'px-4 py-2 rounded-lg text-sm font-medium transition-all',
                  activeStatFilter === filter
                    ? 'bg-teal-500 text-white shadow-md'
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                ]"
              >
                {{ filter === 'all' ? 'All' : filter === 'week' ? 'This Week' : filter === 'missingDocs' ? 'Missing Docs' : filter.charAt(0).toUpperCase() + filter.slice(1) }}
              </button>
            </div>
          </div>

          <!-- Category Filters -->
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">Categories</h3>
            <FilterBar 
              :activeCategory="activeCategory" 
              :categories="categoryFilters"
              :show-clear-button="false"
              :show-summary="false"
              @change="setCategory" 
            />
          </div>

        </div>
      </div>
    </Transition>

    <!-- ITEMS GRID -->
    <div v-if="filteredItems.length > 0">
      <ItemGrid :items="filteredItems" @delete="openDeleteModal" />
    </div>

    <!-- EMPTY STATE -->
    <div v-else class="text-center py-20">
      <Package :size="64" class="text-gray-300 mx-auto mb-4" />
      <h3 class="text-xl font-bold text-gray-900 mb-2">No items found</h3>
      <p class="text-gray-600 mb-6">
        {{ hasActiveFilters
          ? 'Try adjusting your filters or search'
          : 'Get started by adding your first item'
        }}
      </p>
      <div class="flex items-center justify-center gap-3">
        <button
          v-if="hasActiveFilters"
          @click="clearFilters"
          class="px-6 py-3 bg-white text-gray-700 rounded-xl font-medium border-2 border-gray-200 hover:border-gray-300 transition-colors"
        >
          Clear Filters
        </button>
        <RouterLink
          to="/add-document"
          class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl transition-all"
        >
          Add Your First Item
        </RouterLink>
      </div>
    </div>

    <!-- DELETE MODAL -->
    <DeleteModal
      :show="deleteModalOpen"
      title="Delete Item?"
      message="Are you sure you want to delete this item? This action cannot be undone."
      :item-name="itemToDelete?.name"
      :item-description="itemToDelete?.category"
      :item-icon="itemToDelete?.type === 'document' ? FileText : Repeat"
      permanent
      @cancel="deleteModalOpen = false"
      @confirm="confirmDelete"
    />

  </DashboardLayout>
</template>