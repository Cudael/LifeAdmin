<script setup>
import { ref, computed, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useItemsStore } from "../stores/items"
import { useAuthStore } from "../stores/auth"
import { apiFetch } from "../utils/api"

import DashboardLayout from "../layouts/DashboardLayout.vue"
import SearchBar from "../components/SearchBar.vue"
import ItemGrid from "../components/ItemGrid.vue"
import DeleteModal from "../components/DeleteModal.vue"
import ItemsHeader from "../components/items/ItemsHeader.vue"
import ItemsInsights from "../components/items/ItemsInsights.vue"
import ItemsFilters from "../components/items/ItemsFilters.vue"
import ItemsEmptyState from "../components/items/ItemsEmptyState.vue"

import { FileText, Repeat, Layers, Heart, Wallet, Briefcase, User, Plane, Home, AlertTriangle } from "lucide-vue-next"

const itemsStore = useItemsStore()
const authStore = useAuthStore()
const route = useRoute()
const router = useRouter()

// UI State
const activeCategory = ref("All")
const activeStatFilter = ref("all")
const search = ref("")
const deleteModalOpen = ref(false)
const showFilters = ref(false)
const itemToDelete = ref(null)

// Helper functions
const getStatus = (date) => {
  if (!date) return "valid"
  const diff = (new Date(date) - new Date()) / (1000 * 60 * 60 * 24)
  if (diff < 0) return "expired"
  if (diff < 7) return "week"
  if (diff < 30) return "soon"
  return "valid"
}

const daysLeft = (date) => {
  if (!date) return null
  return Math.ceil((new Date(date) - new Date()) / (1000 * 60 * 60 * 24))
}

// Computed properties
const insights = computed(() => {
  const items = itemsStore.items
  return {
    expiringThisMonth: items.filter(i => {
      const days = daysLeft(i.expiration_date)
      return days !== null && days >= 0 && days <= 30
    }).length,
    needsAttention: items.filter(i => getStatus(i.expiration_date) === 'expired').length,
    filesUploaded: items.filter(i => i.file_path).length,
    addedThisWeek: items.filter(i => {
      if (!i.created_at) return false
      const weekAgo = new Date()
      weekAgo.setDate(weekAgo.getDate() - 7)
      return new Date(i.created_at) >= weekAgo
    }).length
  }
})

const totalItems = computed(() => itemsStore.items.length)
const documentsCount = computed(() => itemsStore.items.filter(i => i.type === 'document').length)
const subscriptionsCount = computed(() => itemsStore.items.filter(i => i.type === 'subscription').length)

const categoryFilters = computed(() => {
  const items = itemsStore.items
  const categoryCounts = items.reduce((acc, item) => {
    const cat = item.category || 'Uncategorized'
    acc[cat] = (acc[cat] || 0) + 1
    return acc
  }, {})

  const uniqueCategories = [...new Set(items.map(item => item.category || 'Uncategorized'))]
  const categoryIcons = {
    'Travel': Plane, 'Health': Heart, 'Finance': Wallet, 'Work': Briefcase,
    'Personal': User, 'Subscriptions': Repeat, 'Home': Home, 'Uncategorized': Layers
  }

  const dynamicCategories = uniqueCategories.map(cat => ({
    label: cat, value: cat, icon: categoryIcons[cat] || Layers, count: categoryCounts[cat] || 0
  })).sort((a, b) => a.label.localeCompare(b.label))

  return [{ label: 'All', value: 'All', icon: Layers, count: items.length }, ...dynamicCategories]
})

const filteredItems = computed(() => {
  let list = [...itemsStore.items]

  // Status filter
  if (activeStatFilter.value !== 'all') {
    if (['soon', 'week', 'expired'].includes(activeStatFilter.value)) {
      list = list.filter(i => getStatus(i.expiration_date) === activeStatFilter.value)
    } else if (activeStatFilter.value === 'documents') {
      list = list.filter(i => i.type === 'document')
    } else if (activeStatFilter.value === 'subscriptions') {
      list = list.filter(i => i.type === 'subscription')
    } else if (activeStatFilter.value === 'missingDocs') {
      list = list.filter(i => !i.file_path)
    }
  }

  // Category filter
  if (activeCategory.value !== "All") {
    list = list.filter(i => i.category === activeCategory.value)
  }

  // Search filter
  if (search.value.trim()) {
    const q = search.value.toLowerCase()
    list = list.filter(i => i.name.toLowerCase().includes(q) || i.notes?.toLowerCase().includes(q))
  }

  return list
})

const hasActiveFilters = computed(() => {
  return activeStatFilter.value !== 'all' || activeCategory.value !== 'All' || search.value
})

const showLimitWarning = computed(() => {
  return !authStore.isPremium && totalItems.value >= 15
})

const isAtLimit = computed(() => {
  return !authStore.isPremium && totalItems.value >= 20
})

// Methods
const setCategory = (cat) => activeCategory.value = cat
const setFilter = (filter) => activeStatFilter.value = filter
const clearFilters = () => {
  activeCategory.value = "All"
  activeStatFilter.value = "all"
  search.value = ""
}

const openDeleteModal = (item) => {
  itemToDelete.value = item
  deleteModalOpen.value = true
}

const confirmDelete = async () => {
  if (!itemToDelete.value) return
  try {
    await apiFetch(`/items/${itemToDelete.value.id}`, { method: "DELETE" })
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
  
  // Fetch subscription status
  await authStore.fetchSubscriptionStatus()
  
  // Apply filter from query parameter
  const filterParam = route.query.filter
  const validFilters = ['all', 'soon', 'week', 'expired', 'documents', 'subscriptions', 'missingDocs']
  if (filterParam && validFilters.includes(filterParam)) {
    activeStatFilter.value = filterParam
    showFilters.value = true
  }
})
</script>

<template>
  <DashboardLayout pageTitle="Items">

    <!-- PAGE HEADER ACTIONS -->
    <template #actions>
      <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full">
        
        <!-- Action Buttons (Left Side) -->
        <div class="flex items-center gap-3">
          <ItemsHeader />
        </div>

        <!-- Search Bar and Filters (Right Side) -->
        <div class="flex items-center gap-2 flex-1 justify-end">
          
          <!-- Filters Button -->
          <ItemsFilters 
            :activeCategory="activeCategory"
            :activeStatFilter="activeStatFilter"
            :categoryFilters="categoryFilters"
            :showFilters="showFilters"
            :hasActiveFilters="hasActiveFilters"
            :search="search"
            @update:showFilters="showFilters = $event"
            @update:activeCategory="activeCategory = $event"
            @update:activeStatFilter="activeStatFilter = $event"
            @update:search="search = $event"
            @clearFilters="clearFilters"
          />

          <!-- Search Bar -->
          <div class="max-w-md w-full">
            <SearchBar v-model="search" placeholder="Search items..." />
          </div>

        </div>
      </div>
    </template>

    <!-- INSIGHTS CARD -->
    <ItemsInsights 
      :insights="insights"
      :totalItems="totalItems"
      :documentsCount="documentsCount"
      :subscriptionsCount="subscriptionsCount"
      :isPremium="authStore.isPremium"
      @filter="setFilter"
    />

    <!-- ITEM LIMIT WARNING -->
    <div v-if="showLimitWarning" class="mb-6">
      <div 
        :class="[
          'p-4 rounded-xl border-2 flex items-start gap-3',
          isAtLimit 
            ? 'bg-red-50 border-red-200' 
            : 'bg-yellow-50 border-yellow-200'
        ]"
      >
        <AlertTriangle 
          :size="24" 
          :class="isAtLimit ? 'text-red-600' : 'text-yellow-600'" 
          class="flex-shrink-0 mt-0.5"
        />
        <div class="flex-1">
          <h4 
            :class="[
              'font-semibold mb-1',
              isAtLimit ? 'text-red-900' : 'text-yellow-900'
            ]"
          >
            {{ isAtLimit ? 'Item Limit Reached' : 'Approaching Item Limit' }}
          </h4>
          <p 
            :class="[
              'text-sm mb-3',
              isAtLimit ? 'text-red-700' : 'text-yellow-700'
            ]"
          >
            {{ isAtLimit 
              ? 'You have reached the free plan limit of 20 items. Upgrade to Premium for unlimited items.' 
              : `You are using ${totalItems}/20 items on the free plan. Upgrade to Premium for unlimited items.` 
            }}
          </p>
          <button
            @click="router.push('/subscription')"
            class="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-lg font-semibold shadow-md hover:shadow-lg hover:from-teal-400 hover:to-cyan-400 transition-all text-sm"
          >
            Upgrade to Premium
          </button>
        </div>
      </div>
    </div>

    <!-- ITEMS GRID -->
    <div v-if="filteredItems.length > 0">
      <ItemGrid :items="filteredItems" @delete="openDeleteModal" />
    </div>

    <!-- EMPTY STATE -->
    <ItemsEmptyState 
      v-else
      :hasActiveFilters="hasActiveFilters"
      @clearFilters="clearFilters"
    />

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