import { defineStore } from "pinia"
import { ref, computed } from "vue"

export const useItemsStore = defineStore("items", () => {
  const items = ref([])

  function setItems(newItems) {
    items.value = Array.isArray(newItems) ? newItems : []
  }

  function addItem(item) {
    items.value.push(item)
  }

  // Expose items as a plain array, not a ref
  const itemsList = computed(() => items.value)

  return { items: itemsList, setItems, addItem }
})