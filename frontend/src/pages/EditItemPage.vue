<script setup>
import { ref, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { apiFetch } from "../utils/api"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import FileUploader from "../components/FileUploader.vue"

const route = useRoute()
const router = useRouter()

const loading = ref(true)
const saving = ref(false)
const deleting = ref(false)

const item = ref({
  name: "",
  type: "document",
  category: "",
  expiration_date: "",
  notes: "",
  file_path: null
})

const file = ref(null)

function formatDateInput(date) {
  if (!date) return ""
  return new Date(date).toISOString().split("T")[0]
}

async function loadItem() {
  const res = await apiFetch(`/items/${route.params.id}`)
  const data = await res.json()

  item.value = {
    ...data,
    expiration_date: formatDateInput(data.expiration_date)
  }

  loading.value = false
}

async function saveItem() {
  saving.value = true

  const formData = new FormData()
  formData.append("name", item.value.name)
  formData.append("type", item.value.type)
  formData.append("category", item.value.category)
  formData.append("expiration_date", item.value.expiration_date)
  formData.append("notes", item.value.notes)

  if (file.value) {
    formData.append("file", file.value)
  }

  await apiFetch(`/items/${item.value.id}`, {
    method: "PUT",
    body: formData
  })

  saving.value = false
  router.push(`/items/${item.value.id}`)
}

async function deleteItem() {
  deleting.value = true

  await apiFetch(`/items/${item.value.id}`, {
    method: "DELETE"
  })

  deleting.value = false
  router.push("/items")
}

onMounted(loadItem)
</script>

<template>
  <DashboardLayout :pageTitle="loading ? 'Loading…' : `Edit: ${item.name}`">

    <template #actions>
      <button
        @click="deleteItem"
        class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 transition"
        :disabled="deleting"
      >
        {{ deleting ? "Deleting…" : "Delete" }}
      </button>
    </template>

    <div v-if="loading" class="text-gray-500">Loading item…</div>

    <div v-else class="space-y-10">

      <!-- FORM CARD -->
      <div class="bg-white rounded-3xl shadow p-8 border border-teal-100">

        <h2 class="text-2xl font-bold text-gray-900 mb-6">Edit Item</h2>

        <div class="grid md:grid-cols-2 gap-8">

          <!-- NAME -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
            <input
              v-model="item.name"
              type="text"
              class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-teal-400 focus:border-teal-400"
            />
          </div>

          <!-- TYPE -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Type</label>
            <select
              v-model="item.type"
              class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-teal-400 focus:border-teal-400"
            >
              <option value="document">Document</option>
              <option value="subscription">Subscription</option>
            </select>
          </div>

          <!-- CATEGORY -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Category</label>
            <input
              v-model="item.category"
              type="text"
              class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-teal-400 focus:border-teal-400"
            />
          </div>

          <!-- EXPIRATION DATE -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Expiration Date</label>
            <input
              v-model="item.expiration_date"
              type="date"
              class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-teal-400 focus:border-teal-400"
            />
          </div>

        </div>

        <!-- NOTES -->
        <div class="mt-8">
          <label class="block text-sm font-medium text-gray-700 mb-1">Notes</label>
          <textarea
            v-model="item.notes"
            rows="4"
            class="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-teal-400 focus:border-teal-400"
          ></textarea>
        </div>

        <!-- FILE UPLOAD -->
        <div class="mt-8">
          <label class="block text-sm font-medium text-gray-700 mb-2">File</label>

          <FileUploader
            v-model="file"
            :existingFile="item.file_path ? item.file_path.split('/').pop() : null"
          />
        </div>

        <!-- ACTION BUTTONS -->
        <div class="mt-10 flex gap-4">
          <button
            @click="saveItem"
            class="px-6 py-3 bg-teal-500 text-white rounded-lg font-semibold hover:bg-teal-600 transition"
            :disabled="saving"
          >
            {{ saving ? "Saving…" : "Save Changes" }}
          </button>

          <RouterLink
            :to="`/items/${item.id}`"
            class="px-6 py-3 bg-gray-100 text-gray-700 rounded-lg font-semibold hover:bg-gray-200 transition"
          >
            Cancel
          </RouterLink>
        </div>

      </div>

    </div>

  </DashboardLayout>
</template>