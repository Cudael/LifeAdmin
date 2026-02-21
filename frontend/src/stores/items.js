import { defineStore } from "pinia"
import { ref, computed } from "vue"
import { apiFetch } from "../utils/api"

export const useItemsStore = defineStore("items", () => {
  const items = ref([])
  const loading = ref(false)
  const error = ref(null)

  const itemsList = computed(() => items.value)
  const totalItems = computed(() => items.value.length)
  const documents = computed(() => items.value.filter(i => i.type === "document"))
  const subscriptions = computed(() => items.value.filter(i => i.type === "subscription"))

  // Helper function to parse dynamic_fields and merge with item
  function parseItemDynamicFields(item) {
    if (item.dynamic_fields) {
      try {
        const dynamicData = JSON.parse(item.dynamic_fields)
        return { ...item, ...dynamicData }
      } catch (e) {
        console.warn('Failed to parse dynamic_fields for item:', item.id, e)
        return item
      }
    }
    return item
  }

  function setItems(newItems) {
    // Parse dynamic_fields and merge with each item
    const processedItems = Array.isArray(newItems) ? newItems.map(parseItemDynamicFields) : []
    items.value = processedItems
  }

  function addItem(item) {
    // Parse dynamic_fields for new item
    const processedItem = parseItemDynamicFields(item)
    items.value.push(processedItem)
  }

  async function fetchItems() {
    loading.value = true
    error.value = null
    try {
      const res = await apiFetch("/items")
      if (res && res.ok) {
        const data = await res.json()
        const rawItems = Array.isArray(data) ? data : (data.items || [])
        // Parse dynamic_fields for all items
        items.value = rawItems.map(parseItemDynamicFields)
      } else {
        error.value = "Failed to load items"
      }
    } catch (e) {
      error.value = "Network error loading items"
    } finally {
      loading.value = false
    }
  }

  async function deleteItem(id) {
    const res = await apiFetch(`/items/${id}`, { method: "DELETE" })
    if (res && res.ok) {
      items.value = items.value.filter(i => i.id !== id)
      return true
    }
    return false
  }

  async function updateItem(id, payload) {
    const res = await apiFetch(`/items/${id}`, {
      method: "PATCH",
      body: JSON.stringify(payload)
    })
    if (res && res.ok) {
      const updated = await res.json()
      // Parse dynamic_fields for updated item
      const processedItem = parseItemDynamicFields(updated)
      const idx = items.value.findIndex(i => i.id === id)
      if (idx !== -1) items.value[idx] = processedItem
      return processedItem
    }
    return null
  }

  return {
    items: itemsList,
    loading,
    error,
    totalItems,
    documents,
    subscriptions,
    setItems,
    addItem,
    fetchItems,
    deleteItem,
    updateItem,
  }
})