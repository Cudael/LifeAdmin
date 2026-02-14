import { ref, computed } from "vue"

export function usePagination(initialItemsPerPage = 10) {
  const currentPage = ref(1)
  const itemsPerPage = ref(initialItemsPerPage)
  const totalItems = ref(0)

  const totalPages = computed(() => {
    return Math.ceil(totalItems.value / itemsPerPage.value) || 1
  })

  const hasNextPage = computed(() => {
    return currentPage.value < totalPages.value
  })

  const hasPrevPage = computed(() => {
    return currentPage.value > 1
  })

  const startIndex = computed(() => {
    return (currentPage.value - 1) * itemsPerPage.value
  })

  const endIndex = computed(() => {
    return Math.min(startIndex.value + itemsPerPage.value, totalItems.value)
  })

  function nextPage() {
    if (hasNextPage.value) {
      currentPage.value++
    }
  }

  function prevPage() {
    if (hasPrevPage.value) {
      currentPage.value--
    }
  }

  function goToPage(page) {
    const pageNumber = Math.max(1, Math.min(page, totalPages.value))
    currentPage.value = pageNumber
  }

  function reset() {
    currentPage.value = 1
  }

  function setTotalItems(total) {
    totalItems.value = total
  }

  function setItemsPerPage(perPage) {
    itemsPerPage.value = perPage
    currentPage.value = 1
  }

  return {
    currentPage,
    itemsPerPage,
    totalItems,
    totalPages,
    hasNextPage,
    hasPrevPage,
    startIndex,
    endIndex,
    nextPage,
    prevPage,
    goToPage,
    reset,
    setTotalItems,
    setItemsPerPage
  }
}
