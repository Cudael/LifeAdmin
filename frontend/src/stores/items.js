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

  function setItems(newItems) {
    items.value = Array.isArray(newItems) ? newItems : []
  }

  function addItem(item) {
    items.value.push(item)
  }

  async function fetchItems() {
    loading.value = true
    error.value = null
    try {
      const res = await apiFetch("/items")
      if (res && res.ok) {
        const data = await res.json()
        items.value = Array.isArray(data) ? data : (data.items || [])
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
      const idx = items.value.findIndex(i => i.id === id)
      if (idx !== -1) items.value[idx] = updated
      return updated
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