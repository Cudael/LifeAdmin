<template>
  <DashboardLayout pageTitle="Add Document">

    <!-- Header Section -->
    <div class="text-center mt-4">
      <h2 class="text-2xl font-bold text-gray-800">Add New Document</h2>
      <p class="text-gray-500 text-sm mt-1">
        Upload and organize your important documents
      </p>
    </div>

    <!-- Back Button -->
    <div class="flex justify-center mt-6">
      <button
        @click="$router.back()"
        class="inline-flex items-center gap-2 px-4 py-2 
               bg-white border border-gray-300 rounded-lg shadow-sm
               hover:bg-gray-50 hover:shadow transition-all"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4"
             fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 19l-7-7 7-7" />
        </svg>
        Back
      </button>
    </div>

    <!-- Centered container -->
    <div class="flex justify-center mt-6 px-4">
      <div class="w-full max-w-2xl bg-white p-8 rounded-2xl shadow border border-teal-100">

        <!-- SUCCESS MESSAGE -->
        <div
          v-if="successMessage"
          class="mb-4 p-3 rounded bg-green-100 text-green-700"
        >
          {{ successMessage }}
        </div>

        <!-- ERROR MESSAGE -->
        <div
          v-if="errorMessage"
          class="mb-4 p-3 rounded bg-red-100 text-red-700"
        >
          {{ errorMessage }}
        </div>

        <!-- FORM -->
        <form @submit.prevent="handleSubmit" class="space-y-8">

          <!-- DOCUMENT NAME -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Document Name</label>
            <input
              v-model="name"
              type="text"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              placeholder="Passport, Driver’s License, Insurance Policy..."
              required
            />
          </div>

          <!-- CATEGORY -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Category</label>
            <select
              v-model="category"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              required
            >
              <option disabled value="">Select category</option>
              <option>Travel</option>
              <option>Health</option>
              <option>Finance</option>
              <option>Work</option>
              <option>Personal</option>
            </select>
          </div>

          <!-- FILE UPLOADER -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Upload Document File</label>

            <FileUploader v-model="file" />
          </div>

          <!-- EXPIRATION DATE -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Expiration Date</label>
            <input
              v-model="expirationDate"
              type="date"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              required
            />
          </div>

          <!-- DOCUMENT NUMBER -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Document Number (optional)</label>
            <input
              v-model="documentNumber"
              type="text"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              placeholder="Passport number, policy ID, etc."
            />
          </div>

          <!-- ISSUING AUTHORITY (NEW FIELD) -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Issuing Authority (optional)</label>
            <input
              v-model="issuingAuthority"
              type="text"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              placeholder="Government office, insurance provider, employer..."
            />
          </div>

          <!-- NOTES -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Notes (optional)</label>
            <textarea
              v-model="notes"
              rows="3"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              placeholder="Any extra details..."
            ></textarea>
          </div>

          <!-- SUBMIT -->
          <button
            type="submit"
            class="w-full bg-teal-500 text-white py-3 rounded-lg font-semibold hover:bg-teal-600 transition"
          >
            Add Document
          </button>

        </form>
      </div>
    </div>

  </DashboardLayout>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import FileUploader from "../components/FileUploader.vue"
import { apiFetch } from "../utils/api"

const router = useRouter()

// Form fields
const name = ref("")
const category = ref("")
const expirationDate = ref("")
const documentNumber = ref("")
const issuingAuthority = ref("") // NEW FIELD
const notes = ref("")
const file = ref(null)

// Messages
const successMessage = ref("")
const errorMessage = ref("")

async function handleSubmit() {
  if (!category.value) {
    errorMessage.value = "Please select a category"
    return
  }

  if (!expirationDate.value) {
    errorMessage.value = "Please select an expiration date"
    return
  }

  try {
    const formData = new FormData()
    formData.append("name", name.value)
    formData.append("category", category.value)
    formData.append("expiration_date", expirationDate.value)
    formData.append("document_number", documentNumber.value)
    formData.append("issuing_authority", issuingAuthority.value)
    formData.append("notes", notes.value)
    formData.append("type", "document")

    if (file.value) {
      formData.append("file", file.value)
    }

    const res = await apiFetch("/items/upload", {
      method: "POST",
      body: formData
    })

    if (!res.ok) {
      const data = await res.json()
      errorMessage.value = data.detail || "Failed to add document"
      return
    }

    successMessage.value = "Document added successfully!"

    setTimeout(() => {
      router.push("/items")
    }, 1000)

  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong"
  }
}
</script>