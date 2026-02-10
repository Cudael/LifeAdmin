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

const itemsStore = useItemsStore()
const route = useRoute()
const router = useRouter()

// UI State
const activeCategory = ref("All")
const activeStatFilter = ref("all")
const search = ref("")
const deleteModalOpen = ref(false)
let itemToDelete = null

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

// Apply filter from URL
function applyQueryFilter() {
  const filter = route.query.filter

  if (!filter) return

  const validFilters = [
    "expired",
    "soon",
    "week",
    "documents",
    "subscriptions",
    "missingDocs",
    "all"
  ]

  if (validFilters.includes(filter)) {
    activeStatFilter.value = filter
  }
}

// Update URL when filter changes
function setFilter(filter) {
  activeStatFilter.value = filter

  router.replace({
    query: {
      ...route.query,
      filter
    }
  })
}

// Filtering logic
const filteredItems = computed(() => {
  let list = [...itemsStore.items]

  // Stat filter
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

function setCategory(cat) {
  activeCategory.value = cat
}

function openDeleteModal(item) {
  itemToDelete = item
  deleteModalOpen.value = true
}

async function confirmDelete() {
  await apiFetch(`/items/${itemToDelete.id}`, {
    method: "DELETE"
  })

  itemsStore.setItems(itemsStore.items.filter(i => i.id !== itemToDelete.id))
  deleteModalOpen.value = false
}

onMounted(async () => {
  const res = await apiFetch("/items")
  const data = await res.json()
  itemsStore.setItems(data)

  applyQueryFilter()
})
</script>

<template>
  <DashboardLayout pageTitle="Items">

    <!-- PAGE HEADER ACTIONS -->
    <template #actions>
      <RouterLink
        to="/add-item"
        class="px-4 py-2 bg-gradient-to-r from-teal-400 to-cyan-400 text-black rounded-lg font-semibold shadow hover:from-teal-300 hover:to-cyan-300 transition"
      >
        + Add Item
      </RouterLink>
    </template>

    <!-- SEARCH -->
    <div class="mb-6">
      <SearchBar v-model="search" />
    </div>

    <!-- FILTERS -->
    <div class="mb-6">
      <FilterBar :activeCategory="activeCategory" @change="setCategory" />
    </div>

    <!-- ITEMS GRID -->
    <ItemGrid :items="filteredItems" @delete="openDeleteModal" />

    <!-- DELETE MODAL -->
    <DeleteModal
      v-if="deleteModalOpen"
      @cancel="deleteModalOpen = false"
      @confirm="confirmDelete"
    />

  </DashboardLayout>
</template>