<template>
  <DashboardLayout pageTitle="Add Document">

    <!-- Breadcrumb -->
    <div class="mb-6">
      <div class="flex items-center gap-2 text-sm text-gray-600">
        <RouterLink to="/dashboard" class="hover:text-teal-600 transition-colors">Dashboard</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink to="/items" class="hover:text-teal-600 transition-colors">Items</RouterLink>
        <ChevronRight :size="16" />
        <span class="text-gray-900 font-medium">Add Document</span>
      </div>
    </div>

    <!-- Header Section -->
    <div class="relative mb-8 p-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-3xl shadow-xl text-white overflow-hidden">
      
      <!-- Decorative elements -->
      <div class="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
      <div class="absolute bottom-0 left-0 w-48 h-48 bg-white/10 rounded-full translate-y-1/2 -translate-x-1/2"></div>

      <div class="relative z-10 text-center">
        <div class="w-16 h-16 mx-auto mb-4 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center">
          <FileText :size="32" class="text-white" />
        </div>
        <h2 class="text-3xl font-bold mb-2">Add New Document</h2>
        <p class="text-white/90 text-lg">
          Upload and organize your important documents securely
        </p>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-3xl mx-auto">

      <!-- Back Button -->
      <button
        @click="$router.back()"
        class="group mb-6 inline-flex items-center gap-2 px-4 py-2 bg-white border-2 border-gray-200 rounded-xl shadow-sm hover:border-teal-300 hover:shadow-md transition-all duration-200"
      >
        <ArrowLeft :size="18" class="group-hover:-translate-x-1 transition-transform" />
        <span class="font-medium text-gray-700">Back</span>
      </button>

      <!-- Form Card -->
      <div class="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl border-2 border-gray-100 p-8 md:p-10">

        <!-- SUCCESS MESSAGE -->
        <Transition
          enter-active-class="transition-all duration-300 ease-out"
          enter-from-class="opacity-0 -translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition-all duration-200 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 -translate-y-2"
        >
          <div
            v-if="successMessage"
            class="mb-6 p-4 bg-green-50 border-2 border-green-200 rounded-xl flex items-start gap-3 animate-bounce-in"
          >
            <CheckCircle2 :size="20" class="text-green-500 flex-shrink-0 mt-0.5" />
            <div>
              <p class="text-sm font-semibold text-green-700">{{ successMessage }}</p>
              <p class="text-xs text-green-600 mt-1">Redirecting to items...</p>
            </div>
          </div>
        </Transition>

        <!-- ERROR MESSAGE -->
        <Transition
          enter-active-class="transition-all duration-300 ease-out"
          enter-from-class="opacity-0 -translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition-all duration-200 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 -translate-y-2"
        >
          <div
            v-if="errorMessage"
            class="mb-6 p-4 bg-red-50 border-2 border-red-200 rounded-xl flex items-start gap-3 animate-shake"
          >
            <AlertCircle :size="20" class="text-red-500 flex-shrink-0 mt-0.5" />
            <p class="text-sm text-red-700">{{ errorMessage }}</p>
          </div>
        </Transition>

        <!-- FORM -->
        <form @submit.prevent="handleSubmit" class="space-y-6">

          <!-- DOCUMENT NAME -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <FileText :size="16" class="text-teal-600" />
              Document Name
              <span class="text-red-500">*</span>
            </label>
            <input
              v-model="name"
              type="text"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50"
              placeholder="e.g., Passport, Driver's License, Insurance Policy"
              required
              :disabled="loading"
            />
          </div>

          <!-- CATEGORY -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <FolderOpen :size="16" class="text-teal-600" />
              Category
              <span class="text-red-500">*</span>
            </label>
            <div class="relative">
              <select
                v-model="category"
                class="w-full px-4 py-3 pr-10 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 appearance-none cursor-pointer"
                required
                :disabled="loading"
              >
                <option disabled value="">Select a category</option>
                <option value="Travel">🌍 Travel</option>
                <option value="Health">❤️ Health</option>
                <option value="Finance">💰 Finance</option>
                <option value="Work">💼 Work</option>
                <option value="Personal">👤 Personal</option>
              </select>
              <ChevronDown :size="20" class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 pointer-events-none" />
            </div>
          </div>

          <!-- FILE UPLOADER -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Upload :size="16" class="text-teal-600" />
              Upload Document File
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <FileUploader v-model="file" />
          </div>

          <!-- EXPIRATION DATE -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Calendar :size="16" class="text-teal-600" />
              Expiration Date
              <span class="text-red-500">*</span>
            </label>
            <input
              v-model="expirationDate"
              type="date"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50"
              required
              :disabled="loading"
              :min="today"
            />
            <p v-if="daysUntilExpiry !== null" class="text-xs text-gray-600 flex items-center gap-1">
              <Clock :size="12" />
              {{ daysUntilExpiry }} days from now
            </p>
          </div>

          <!-- DOCUMENT NUMBER -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Hash :size="16" class="text-teal-600" />
              Document Number
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <input
              v-model="documentNumber"
              type="text"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50"
              placeholder="e.g., Passport number, policy ID"
              :disabled="loading"
            />
          </div>

          <!-- ISSUING AUTHORITY -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Building :size="16" class="text-teal-600" />
              Issuing Authority
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <input
              v-model="issuingAuthority"
              type="text"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50"
              placeholder="e.g., Government office, insurance provider"
              :disabled="loading"
            />
          </div>

          <!-- NOTES -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <FileText :size="16" class="text-teal-600" />
              Notes
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <textarea
              v-model="notes"
              rows="4"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 resize-none"
              placeholder="Add any additional details or reminders..."
              :disabled="loading"
            ></textarea>
          </div>

          <!-- SUBMIT BUTTONS -->
          <div class="flex gap-4 pt-4">
            <button
              type="button"
              @click="$router.back()"
              class="flex-1 px-6 py-4 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
              :disabled="loading"
            >
              Cancel
            </button>
            <button
              type="submit"
              :disabled="loading"
              class="group flex-1 px-6 py-4 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <span v-if="!loading" class="flex items-center gap-2">
                <Plus :size="20" />
                Add Document
                <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
              </span>
              <span v-else class="flex items-center gap-3">
                <Loader2 :size="20" class="animate-spin" />
                Adding...
              </span>
            </button>
          </div>

        </form>

      </div>

      <!-- Quick Tips -->
      <div class="mt-8 p-6 bg-gradient-to-br from-blue-50 to-cyan-50 rounded-2xl border-2 border-blue-200">
        <div class="flex items-start gap-3">
          <div class="w-10 h-10 rounded-xl bg-blue-500 flex items-center justify-center flex-shrink-0">
            <Lightbulb :size="20" class="text-white" />
          </div>
          <div>
            <h3 class="font-semibold text-gray-900 mb-2">Quick Tips</h3>
            <ul class="space-y-2 text-sm text-gray-700">
              <li class="flex items-start gap-2">
                <span class="text-teal-600 mt-0.5">•</span>
                <span>Upload clear scans or photos of your documents for easy reference</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-teal-600 mt-0.5">•</span>
                <span>Set expiration dates to receive timely reminders before renewal</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-teal-600 mt-0.5">•</span>
                <span>Add detailed notes to remember important context later</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

    </div>

  </DashboardLayout>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import FileUploader from "../components/FileUploader.vue"
import { apiFetch } from "../utils/api"
import {
  FileText,
  FolderOpen,
  Upload,
  Calendar,
  Hash,
  Building,
  Plus,
  ArrowRight,
  ArrowLeft,
  CheckCircle2,
  AlertCircle,
  Loader2,
  ChevronRight,
  ChevronDown,
  Clock,
  Lightbulb
} from "lucide-vue-next"

const router = useRouter()

// Form fields
const name = ref("")
const category = ref("")
const expirationDate = ref("")
const documentNumber = ref("")
const issuingAuthority = ref("")
const notes = ref("")
const file = ref(null)

// State
const loading = ref(false)
const successMessage = ref("")
const errorMessage = ref("")

// Computed
const today = computed(() => {
  const date = new Date()
  return date.toISOString().split('T')[0]
})

const daysUntilExpiry = computed(() => {
  if (!expirationDate.value) return null
  
  const today = new Date()
  const expiry = new Date(expirationDate.value)
  const diffTime = expiry - today
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
  
  return diffDays
})

async function handleSubmit() {
  errorMessage.value = ""
  successMessage.value = ""

  // Validation
  if (!category.value) {
    errorMessage.value = "Please select a category"
    return
  }

  if (!expirationDate.value) {
    errorMessage.value = "Please select an expiration date"
    return
  }

  if (!name.value.trim()) {
    errorMessage.value = "Please enter a document name"
    return
  }

  loading.value = true

  try {
    const formData = new FormData()
    formData.append("name", name.value.trim())
    formData.append("category", category.value)
    formData.append("expiration_date", expirationDate.value)
    formData.append("document_number", documentNumber.value.trim())
    formData.append("issuing_authority", issuingAuthority.value.trim())
    formData.append("notes", notes.value.trim())
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
      loading.value = false
      return
    }

    successMessage.value = "Document added successfully! 🎉"

    // Redirect after 1.5 seconds
    setTimeout(() => {
      router.push("/items")
    }, 1500)

  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong. Please try again."
    loading.value = false
  }
}
</script>

<style scoped>
@keyframes shake {
  0%, 100% {
    transform: translateX(0);
  }
  10%, 30%, 50%, 70%, 90% {
    transform: translateX(-5px);
  }
  20%, 40%, 60%, 80% {
    transform: translateX(5px);
  }
}

@keyframes bounce-in {
  0% {
    opacity: 0;
    transform: scale(0.9);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-shake {
  animation: shake 0.5s ease-in-out;
}

.animate-bounce-in {
  animation: bounce-in 0.5s ease-out;
}
</style>