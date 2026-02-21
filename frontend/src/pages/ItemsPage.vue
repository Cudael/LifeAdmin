<template>
  <DashboardLayout pageTitle="Vault Items">

    <!-- Ambient Background Mesh -->
    <div class="fixed inset-0 z-0 bg-[linear-gradient(to_right,#80808008_1px,transparent_1px),linear-gradient(to_bottom,#80808008_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none"></div>
    <div class="fixed top-0 left-1/4 w-[600px] h-[400px] bg-teal-500/5 blur-[120px] rounded-full pointer-events-none z-0 mix-blend-screen"></div>

    <div class="relative z-10 w-full max-w-[1600px] mx-auto pb-12 space-y-6">

      <!-- PAGE HEADER ACTIONS -->
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4 w-full bg-slate-900/60 backdrop-blur-xl p-4 rounded-[2rem] border border-white/5 shadow-lg">
        
        <!-- Search Bar Container -->
        <div class="flex-1 w-full max-w-xl">
          <div class="relative group/input">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <Search :size="18" class="text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
            </div>
            <input 
              v-model="search" 
              type="text" 
              placeholder="Search vault items..."
              class="w-full bg-slate-950/50 border border-white/5 text-white placeholder:text-slate-500 rounded-xl pl-11 pr-4 py-3 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300"
            />
          </div>
        </div>

        <div class="flex flex-col sm:flex-row items-center gap-3 w-full sm:w-auto">
          
          <!-- Filter Toggle Button -->
          <button
            @click="showFilters = !showFilters"
            :class="[
              'group relative inline-flex items-center justify-center gap-2 px-6 py-3 rounded-xl font-bold transition-all duration-300 w-full sm:w-auto border',
              showFilters || hasActiveFilters 
                ? 'bg-teal-500/10 border-teal-500/30 text-teal-400 shadow-[0_0_15px_rgba(20,184,166,0.15)]' 
                : 'bg-slate-950/50 border-white/5 text-slate-300 hover:bg-slate-800'
            ]"
          >
            <Filter :size="18" class="transition-transform duration-300" :class="{ 'scale-110': showFilters }" />
            <span>{{ hasActiveFilters ? 'Filters Active' : 'Filters' }}</span>
            
            <!-- Active Indicator Ping -->
            <span 
              v-if="hasActiveFilters" 
              class="absolute -top-1 -right-1 flex h-3.5 w-3.5"
            >
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-teal-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-3.5 w-3.5 bg-teal-500 border-2 border-slate-900"></span>
            </span>
          </button>

          <!-- Add Item Button -->
          <RouterLink
            to="/add-item"
            class="group relative inline-flex items-center justify-center gap-2 px-6 py-3 bg-slate-50 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(255,255,255,0.1)] hover:bg-white hover:shadow-[0_0_25px_rgba(255,255,255,0.2)] transition-all duration-300 w-full sm:w-auto"
          >
            <Plus :size="18" class="text-teal-600 group-hover:rotate-90 transition-transform" />
            <span>New Item</span>
          </RouterLink>
        </div>
      </div>

      <!-- FILTER PANEL CONTENT -->
      <Transition
        enter-active-class="transition-all duration-300 ease-out overflow-hidden"
        enter-from-class="opacity-0 max-h-0 -translate-y-4"
        enter-to-class="opacity-100 max-h-[800px] translate-y-0"
        leave-active-class="transition-all duration-200 ease-in overflow-hidden"
        leave-from-class="opacity-100 max-h-[800px] translate-y-0"
        leave-to-class="opacity-0 max-h-0 -translate-y-4"
      >
        <div v-show="showFilters" class="w-full">
          <FilterPanel
            :activeCategory="activeCategory"
            :activeStatFilter="activeStatFilter"
            :categoryFilters="categoryFilters"
            :hasActiveFilters="hasActiveFilters"
            @update:activeCategory="activeCategory = $event"
            @update:activeStatFilter="activeStatFilter = $event"
            @clearFilters="clearFilters"
          />
        </div>
      </Transition>

      <!-- INSIGHTS CARD -->
      <ItemsInsights 
        v-model:showInsights="showInsights"
        :insights="insights"
        :totalItems="totalItems"
        :documentsCount="documentsCount"
        :subscriptionsCount="subscriptionsCount"
        :isPremium="authStore.isPremium"
        @filter="setFilter"
      />

      <!-- ITEM LIMIT WARNING -->
      <Transition
        enter-active-class="transition-all duration-500 ease-out"
        enter-from-class="opacity-0 -translate-y-4 scale-95"
        enter-to-class="opacity-100 translate-y-0 scale-100"
        leave-active-class="transition-all duration-300 ease-in"
        leave-from-class="opacity-100 translate-y-0 scale-100"
        leave-to-class="opacity-0 -translate-y-4 scale-95"
      >
        <div v-if="showLimitWarning" class="w-full">
          <div 
            class="relative overflow-hidden rounded-[2rem] border p-6 sm:p-8 backdrop-blur-xl flex flex-col sm:flex-row items-center gap-6"
            :class="isAtLimit ? 'bg-rose-500/5 border-rose-500/20' : 'bg-amber-500/5 border-amber-500/20'"
          >
            <!-- Ambient Warning Glow -->
            <div 
              class="absolute -top-20 -right-20 w-64 h-64 rounded-full blur-[80px] opacity-40 pointer-events-none"
              :class="isAtLimit ? 'bg-rose-500' : 'bg-amber-500'"
            ></div>

            <div class="flex items-center gap-5 flex-1 relative z-10">
              <div 
                class="w-14 h-14 rounded-2xl flex items-center justify-center shrink-0 shadow-inner"
                :class="isAtLimit ? 'bg-rose-500/10 border border-rose-500/20 text-rose-400' : 'bg-amber-500/10 border border-amber-500/20 text-amber-400'"
              >
                <AlertTriangle :size="28" :class="isAtLimit ? 'animate-pulse' : ''" />
              </div>
              <div>
                <h4 class="font-extrabold text-xl mb-1 text-white tracking-tight">
                  {{ isAtLimit ? 'Vault Capacity Reached' : 'Approaching Vault Limit' }}
                </h4>
                <p class="text-slate-400 text-sm leading-relaxed">
                  {{ isAtLimit 
                    ? 'You have reached the free plan limit of 20 items. Upgrade to Pro to add unlimited items.' 
                    : `You are using ${totalItems}/20 items on the free plan. Upgrade to Pro for unlimited items.` 
                  }}
                </p>
              </div>
            </div>

            <button
              @click="router.push('/subscription')"
              class="relative z-10 shrink-0 inline-flex items-center gap-2 px-6 py-3.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.3)] hover:shadow-[0_0_30px_rgba(45,212,191,0.5)] transition-all duration-300 hover:-translate-y-0.5 w-full sm:w-auto justify-center"
            >
              <Sparkles :size="18" />
              Upgrade to Pro
            </button>
          </div>
        </div>
      </Transition>

      <!-- ITEMS GRID -->
      <div v-if="filteredItems.length > 0" class="animate-fade-in-up">
        <ItemGrid :items="filteredItems" @delete="openDeleteModal" />
      </div>

      <!-- EMPTY STATE -->
      <div v-else class="animate-fade-in-up">
        <ItemsEmptyState 
          :hasActiveFilters="hasActiveFilters"
          @clearFilters="clearFilters"
        />
      </div>

      <!-- DELETE MODAL -->
      <DeleteModal
        :show="deleteModalOpen"
        title="Delete Item from Vault?"
        message="Are you sure you want to permanently delete this item? This action cannot be undone and the data will be lost."
        :item-name="itemToDelete?.name"
        :item-description="itemToDelete?.category"
        :item-icon="itemToDelete?.type === 'document' ? FileText : Repeat"
        permanent
        @cancel="deleteModalOpen = false"
        @confirm="confirmDelete"
      />

    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useItemsStore } from "../stores/items"
import { useAuthStore } from "../stores/auth"
import { useItemStatus } from "../composables/useItemStatus"
import { apiFetch } from "../utils/api"

import DashboardLayout from "../layouts/DashboardLayout.vue"
import ItemGrid from "../components/items/ItemGrid.vue"
import DeleteModal from "../components/common/DeleteModal.vue"
import ItemsInsights from "../components/items/ItemsInsights.vue"
import FilterPanel from "../components/items/FilterPanel.vue"
import ItemsEmptyState from "../components/items/ItemsEmptyState.vue"

import { Search, Plus, FileText, Repeat, Layers, Heart, Wallet, Briefcase, User, Plane, Home, AlertTriangle, Sparkles, Filter } from "lucide-vue-next"

const itemsStore = useItemsStore()
const authStore = useAuthStore()
const route = useRoute()
const router = useRouter()
const { getStatus, daysLeft } = useItemStatus()

// UI State
const activeCategory = ref("All")
const activeStatFilter = ref("all")
const search = ref("")
const deleteModalOpen = ref(false)
const itemToDelete = ref(null)
const showInsights = ref(false)
const showFilters = ref(false)

// Computed properties
const insights = computed(() => {
  const items = itemsStore.items
  return {
    expiringThisMonth: items.filter(i => {
      const days = daysLeft(i.expiration_date)
      return days !== null && days >= 0 && days <= 30
    }).length,
    needsAttention: items.filter(i => getStatus(i.expiration_date).key === 'expired').length,
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

  const categories = [...new Set(items.map(item => item.category || 'Uncategorized'))]
  const categoryIcons = {
    'Travel': Plane, 'Health': Heart, 'Finance': Wallet, 'Work': Briefcase,
    'Personal': User, 'Subscriptions': Repeat, 'Home': Home, 'Uncategorized': Layers
  }

  const dynamicCategories = categories.map(cat => ({
    label: cat, value: cat, icon: categoryIcons[cat] || Layers, count: categoryCounts[cat] || 0
  })).sort((a, b) => a.label.localeCompare(b.label))

  return [{ label: 'All Categories', value: 'All', icon: Layers, count: items.length }, ...dynamicCategories]
})

const filteredItems = computed(() => {
  let list = [...itemsStore.items]

  if (activeStatFilter.value !== 'all') {
    if (['soon', 'week', 'expired'].includes(activeStatFilter.value)) {
      list = list.filter(i => getStatus(i.expiration_date).key === activeStatFilter.value)
    } else if (activeStatFilter.value === 'documents') {
      list = list.filter(i => i.type === 'document')
    } else if (activeStatFilter.value === 'subscriptions') {
      list = list.filter(i => i.type === 'subscription')
    } else if (activeStatFilter.value === 'missingDocs') {
      list = list.filter(i => !i.file_path)
    }
  }

  if (activeCategory.value !== "All") {
    list = list.filter(i => i.category === activeCategory.value)
  }

  if (search.value.trim()) {
    const q = search.value.toLowerCase()
    list = list.filter(i => i.name.toLowerCase().includes(q) || i.notes?.toLowerCase().includes(q))
  }

  return list
})

const hasActiveFilters = computed(() => {
  return activeStatFilter.value !== 'all' || activeCategory.value !== 'All' || search.value !== ''
})

const showLimitWarning = computed(() => !authStore.isPremium && totalItems.value >= 15)
const isAtLimit = computed(() => !authStore.isPremium && totalItems.value >= 20)

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
    await itemsStore.deleteItem(itemToDelete.value.id)
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
  
  await authStore.fetchSubscriptionStatus()
  
  const filterParam = route.query.filter
  const validFilters = ['all', 'soon', 'week', 'expired', 'documents', 'subscriptions', 'missingDocs']
  if (filterParam && validFilters.includes(filterParam)) {
    activeStatFilter.value = filterParam
    showFilters.value = true
  }
})
</script>

<style scoped>
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
  animation: fade-in-up 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>