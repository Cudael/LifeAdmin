<script setup>
import { onMounted, ref, computed } from "vue"
import { useRoute, useRouter } from "vue-router"
import { apiFetch } from "../utils/api"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import DeleteModal from "../components/DeleteModal.vue"

const route = useRoute()
const router = useRouter()

const item = ref(null)
const deleteModalOpen = ref(false)

function formatDate(date) {
  return new Date(date).toLocaleDateString()
}

function daysLeft(date) {
  const diff = (new Date(date) - new Date()) / (1000 * 60 * 60 * 24)
  return Math.ceil(diff)
}

const status = computed(() => {
  if (!item.value?.expiration_date) return "Valid"

  const diff = daysLeft(item.value.expiration_date)

  if (diff < 0) return "Expired"
  if (diff < 7) return "Expiring This Week"
  if (diff < 30) return "Expiring Soon"
  return "Valid"
})

const statusColor = computed(() => {
  switch (status.value) {
    case "Expired": return "bg-red-100 text-red-700"
    case "Expiring This Week": return "bg-yellow-100 text-yellow-700"
    case "Expiring Soon": return "bg-orange-100 text-orange-700"
    default: return "bg-green-100 text-green-700"
  }
})

async function loadItem() {
  const res = await apiFetch(`/items/${route.params.id}`)
  item.value = await res.json()
}

async function deleteItem() {
  await apiFetch(`/items/${item.value.id}`, { method: "DELETE" })
  router.push("/items")
}

onMounted(loadItem)
</script>

<template>
  <DashboardLayout :pageTitle="item ? item.name : 'Loading…'">

    <template #actions>
      <div class="flex gap-3">
        <RouterLink
          :to="`/items/${item?.id}/edit`"
          class="px-4 py-2 bg-teal-500 text-white rounded-lg hover:bg-teal-600 transition"
        >
          Edit
        </RouterLink>

        <button
          @click="deleteModalOpen = true"
          class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 transition"
        >
          Delete
        </button>
      </div>
    </template>

    <div v-if="item" class="space-y-10">

      <!-- TOP CARD -->
      <div class="bg-white rounded-3xl shadow p-8 border border-teal-100">
        <div class="flex justify-between items-start">

          <div>
            <h2 class="text-3xl font-bold text-gray-900 mb-2">{{ item.name }}</h2>

            <span :class="`px-3 py-1 rounded-full text-sm font-medium ${statusColor}`">
              {{ status }}
            </span>
          </div>

          <div class="text-right text-gray-500 text-sm">
            <p>Created: {{ formatDate(item.created_at) }}</p>
            <p>Updated: {{ formatDate(item.updated_at) }}</p>
          </div>

        </div>

        <div class="grid md:grid-cols-2 gap-8 mt-8">

          <div>
            <p class="text-gray-500 text-sm mb-1">Type</p>
            <p class="text-lg font-medium text-gray-900 capitalize">{{ item.type }}</p>
          </div>

          <div>
            <p class="text-gray-500 text-sm mb-1">Category</p>
            <p class="text-lg font-medium text-gray-900">{{ item.category || "—" }}</p>
          </div>

          <div>
            <p class="text-gray-500 text-sm mb-1">Expiration Date</p>
            <p class="text-lg font-medium text-gray-900">
              {{ item.expiration_date ? formatDate(item.expiration_date) : "—" }}
            </p>
          </div>

          <div>
            <p class="text-gray-500 text-sm mb-1">Days Left</p>
            <p class="text-lg font-medium text-gray-900">
              {{ item.expiration_date ? daysLeft(item.expiration_date) : "—" }}
            </p>
          </div>

        </div>
      </div>

      <!-- NOTES -->
      <div class="bg-white rounded-3xl shadow p-6 border border-teal-100">
        <h3 class="text-xl font-semibold mb-3 text-gray-900">Notes</h3>
        <p class="text-gray-700 whitespace-pre-line">
          {{ item.notes || "No notes added." }}
        </p>
      </div>

      <!-- FILE -->
      <div class="bg-white rounded-3xl shadow p-6 border border-teal-100">
        <h3 class="text-xl font-semibold mb-3 text-gray-900">Attached File</h3>

        <div v-if="item.file_path">
          <a
            :href="item.file_path"
            target="_blank"
            class="text-teal-600 font-medium hover:underline"
          >
            View / Download File
          </a>
        </div>

        <p v-else class="text-gray-500 text-sm">No file uploaded.</p>
      </div>

    </div>

    <!-- DELETE MODAL -->
    <DeleteModal
      v-if="deleteModalOpen"
      @cancel="deleteModalOpen = false"
      @confirm="deleteItem"
    />

  </DashboardLayout>
</template>