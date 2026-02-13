<script setup>
import { ref, computed, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { apiFetch } from "../utils/api"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import FileUploader from "../components/FileUploader.vue"
import DeleteModal from "../components/DeleteModal.vue"
import {
  Save,
  X,
  Trash2,
  AlertTriangle,
  CheckCircle2,
  FileText,
  Repeat,
  FolderOpen,
  Calendar,
  Upload,
  ArrowLeft,
  Loader2,
  ChevronRight,
  Bell,
  Info
} from "lucide-vue-next"

const route = useRoute()
const router = useRouter()

// User state
const user = ref(null)
const userDefaultReminderDays = computed(() => user.value?.notification_days_before || 7)

const loading = ref(true)
const saving = ref(false)
const showDeleteModal = ref(false)
const deleting = ref(false)
const successMessage = ref("")
const errorMessage = ref("")

const item = ref({
  name: "",
  type: "document",
  category: "",
  expiration_date: "",
  notes: "",
  file_path: null
})

const file = ref(null)

const isDocument = computed(() => item.value.type === "document")
const isSubscription = computed(() => item.value.type === "subscription")

function formatDateInput(date) {
  if (!date) return ""
  return new Date(date).toISOString().split("T")[0]
}

async function loadItem() {
  try {
    const res = await apiFetch(`/items/${route.params.id}`)
    if (!res.ok) {
      errorMessage.value = "Failed to load item"
      return
    }
    const data = await res.json()

    item.value = {
      ...data,
      expiration_date: formatDateInput(data.expiration_date),
      renewal_date: formatDateInput(data.renewal_date),
      reminder_days_before: data.reminder_days_before
    }

    loading.value = false
  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong"
    loading.value = false
  }
}

async function loadUser() {
  try {
    const res = await apiFetch("/auth/me")
    if (res.ok) {
      user.value = await res.json()
    }
  } catch (err) {
    console.error("Failed to load user:", err)
  }
}

async function saveItem() {
  errorMessage.value = ""
  successMessage.value = ""
  saving.value = true

  try {
    const formData = new FormData()
    formData.append("name", item.value.name)
    formData.append("type", item.value.type)
    formData.append("category", item.value.category)
    formData.append("expiration_date", item.value.expiration_date || "")
    formData.append("renewal_date", item.value.renewal_date || "")
    formData.append("notes", item.value.notes || "")
    
    // Add reminder days if set (null means use default)
    if (item.value.reminder_days_before !== null && item.value.reminder_days_before !== undefined) {
      formData.append("reminder_days_before", item.value.reminder_days_before.toString())
    }

    if (file.value) {
      formData.append("file", file.value)
    }

    const res = await apiFetch(`/items/${item.value.id}`, {
      method: "PUT",
      body: formData
    })

    if (!res.ok) {
      errorMessage.value = "Failed to save changes"
      saving.value = false
      return
    }

    successMessage.value = "Changes saved successfully! 🎉"
    
    setTimeout(() => {
      router.push(`/items/${item.value.id}`)
    }, 1500)

  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong"
    saving.value = false
  }
}

async function deleteItem() {
  deleting.value = true

  try {
    const res = await apiFetch(`/items/${item.value.id}`, {
      method: "DELETE"
    })

    if (!res.ok) {
      errorMessage.value = "Failed to delete item"
      deleting.value = false
      showDeleteModal.value = false
      return
    }

    router.push("/items")
  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong"
    deleting.value = false
    showDeleteModal.value = false
  }
}

onMounted(async () => {
  await loadUser()
  await loadItem()
})
</script>

<template>
  <DashboardLayout :pageTitle="loading ? 'Loading…' : `Edit: ${item.name}`">

    <!-- Breadcrumb -->
    <div class="mb-6">
      <div class="flex items-center gap-2 text-sm text-gray-600">
        <RouterLink to="/dashboard" class="hover:text-teal-600 transition-colors">Dashboard</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink to="/items" class="hover:text-teal-600 transition-colors">Items</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink :to="`/items/${route.params.id}`" class="hover:text-teal-600 transition-colors">
          {{ item.name || 'Item' }}
        </RouterLink>
        <ChevronRight :size="16" />
        <span class="text-gray-900 font-medium">Edit</span>
      </div>
    </div>

    <!-- Header Actions -->
    <div class="flex justify-between items-center mb-8">
      <button
        @click="$router.back()"
        class="group inline-flex items-center gap-2 px-4 py-2 bg-white border-2 border-gray-200 rounded-xl shadow-sm hover:border-teal-300 hover:shadow-md transition-all duration-200"
      >
        <ArrowLeft :size="18" class="group-hover:-translate-x-1 transition-transform" />
        <span class="font-medium text-gray-700">Back</span>
      </button>

      <button
        @click="showDeleteModal = true"
        :disabled="saving || deleting"
        class="group inline-flex items-center gap-2 px-4 py-2 bg-red-50 border-2 border-red-200 text-red-600 rounded-xl font-medium hover:bg-red-100 hover:border-red-300 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <Trash2 :size="18" />
        Delete Item
      </button>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-20">
      <div class="text-center">
        <Loader2 :size="48" class="text-teal-500 animate-spin mx-auto mb-4" />
        <p class="text-gray-600">Loading item...</p>
      </div>
    </div>

    <!-- Main Content -->
    <div v-else class="max-w-4xl mx-auto">

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
            <p class="text-xs text-green-600 mt-1">Redirecting...</p>
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
          <AlertTriangle :size="20" class="text-red-500 flex-shrink-0 mt-0.5" />
          <p class="text-sm text-red-700">{{ errorMessage }}</p>
        </div>
      </Transition>

      <!-- FORM CARD -->
      <div class="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl border-2 border-gray-100 p-8 md:p-10">

        <!-- Header -->
        <div class="flex items-center gap-3 mb-8 pb-6 border-b border-gray-200">
          <div :class="[
            'w-12 h-12 rounded-xl flex items-center justify-center',
            isDocument ? 'bg-gradient-to-br from-teal-500 to-cyan-500' : 'bg-gradient-to-br from-purple-500 to-pink-500'
          ]">
            <component :is="isDocument ? FileText : Repeat" :size="24" class="text-white" />
          </div>
          <div>
            <h2 class="text-2xl font-bold text-gray-900">Edit Item</h2>
            <p class="text-sm text-gray-600">Update your {{ item.type }} details</p>
          </div>
        </div>

        <!-- Form -->
        <form @submit.prevent="saveItem" class="space-y-6">

          <!-- NAME & TYPE (Side by Side) -->
          <div class="grid md:grid-cols-2 gap-6">

            <!-- NAME -->
            <div class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
                <FileText :size="16" class="text-teal-600" />
                Name
                <span class="text-red-500">*</span>
              </label>
              <input
                v-model="item.name"
                type="text"
                class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200"
                required
                :disabled="saving"
              />
            </div>

            <!-- TYPE -->
            <div class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
                <Repeat :size="16" class="text-teal-600" />
                Type
                <span class="text-red-500">*</span>
              </label>
              <select
                v-model="item.type"
                class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 appearance-none cursor-pointer"
                required
                :disabled="saving"
              >
                <option value="document">📄 Document</option>
                <option value="subscription">🔄 Subscription</option>
              </select>
            </div>

          </div>

          <!-- CATEGORY -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <FolderOpen :size="16" class="text-teal-600" />
              Category
              <span class="text-red-500">*</span>
            </label>
            <input
              v-model="item.category"
              type="text"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200"
              placeholder="Travel, Health, Finance, etc."
              required
              :disabled="saving"
            />
          </div>

          <!-- DATES (Different based on type) -->
          <div class="grid md:grid-cols-2 gap-6">

            <!-- EXPIRATION DATE (for documents) -->
            <div v-if="isDocument" class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
                <Calendar :size="16" class="text-teal-600" />
                Expiration Date
              </label>
              <input
                v-model="item.expiration_date"
                type="date"
                class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200"
                :disabled="saving"
              />
            </div>

            <!-- RENEWAL DATE (for subscriptions) -->
            <div v-if="isSubscription" class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
                <Calendar :size="16" class="text-purple-600" />
                Renewal Date
              </label>
              <input
                v-model="item.renewal_date"
                type="date"
                class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200"
                :disabled="saving"
              />
            </div>

            <!-- EXPIRATION DATE (for subscriptions - optional) -->
            <div v-if="isSubscription" class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
                <Calendar :size="16" class="text-purple-600" />
                Expiration Date
                <span class="text-gray-500 text-xs font-normal">(optional)</span>
              </label>
              <input
                v-model="item.expiration_date"
                type="date"
                class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200"
                :disabled="saving"
              />
            </div>

            <!-- REMINDER SCHEDULE -->
            <div class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
                <Bell :size="16" :class="isDocument ? 'text-teal-600' : 'text-purple-600'" />
                Reminder Schedule
                <span class="text-gray-500 text-xs font-normal">(optional)</span>
              </label>
              <div class="space-y-3">
                <div class="flex items-center gap-2 p-3 bg-blue-50 border border-blue-200 rounded-lg">
                  <Info :size="16" class="text-blue-600 flex-shrink-0" />
                  <p class="text-xs text-blue-700">
                    Custom reminder for this item, or leave as default to use your account setting ({{ userDefaultReminderDays }} days).
                  </p>
                </div>
                
                <div class="flex gap-2">
                  <button
                    type="button"
                    @click="item.reminder_days_before = null"
                    :class="[
                      'flex-1 px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 border-2',
                      item.reminder_days_before === null
                        ? `bg-gradient-to-r ${isDocument ? 'from-teal-500 to-cyan-500 border-teal-500' : 'from-purple-500 to-pink-500 border-purple-500'} text-white shadow-md`
                        : 'bg-white text-gray-700 border-gray-200 hover:border-teal-300'
                    ]"
                    :disabled="saving"
                  >
                    Default ({{ userDefaultReminderDays }}d)
                  </button>
                  <button
                    type="button"
                    v-for="days in [7, 14, 30, 60]"
                    :key="days"
                    @click="item.reminder_days_before = days"
                    :class="[
                      'flex-1 px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 border-2',
                      item.reminder_days_before === days
                        ? `bg-gradient-to-r ${isDocument ? 'from-teal-500 to-cyan-500 border-teal-500' : 'from-purple-500 to-pink-500 border-purple-500'} text-white shadow-md`
                        : 'bg-white text-gray-700 border-gray-200 hover:border-teal-300'
                    ]"
                    :disabled="saving"
                  >
                    {{ days }}d
                  </button>
                </div>
              </div>
            </div>

          </div>

          <!-- NOTES -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <FileText :size="16" class="text-teal-600" />
              Notes
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <textarea
              v-model="item.notes"
              rows="4"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 resize-none"
              placeholder="Add any additional details..."
              :disabled="saving"
            ></textarea>
          </div>

          <!-- FILE UPLOAD -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Upload :size="16" class="text-teal-600" />
              File
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <FileUploader
              v-model="file"
              :existingFile="item.file_path ? item.file_path.split('/').pop() : null"
            />
          </div>

          <!-- ACTION BUTTONS -->
          <div class="flex gap-4 pt-6 border-t border-gray-200">
            <button
              type="button"
              @click="$router.push(`/items/${item.id}`)"
              class="flex-1 px-6 py-4 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200 flex items-center justify-center gap-2"
              :disabled="saving"
            >
              <X :size="20" />
              Cancel
            </button>

            <button
              type="submit"
              :disabled="saving"
              class="group flex-1 px-6 py-4 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <span v-if="!saving" class="flex items-center gap-2">
                <Save :size="20" />
                Save Changes
              </span>
              <span v-else class="flex items-center gap-3">
                <Loader2 :size="20" class="animate-spin" />
                Saving...
              </span>
            </button>
          </div>

        </form>

      </div>

    </div>

    <!-- DELETE MODAL -->
    <DeleteModal
      :show="showDeleteModal"
      :loading="deleting"
      title="Delete Item?"
      message="This will permanently delete this item and all its associated data. This action cannot be undone."
      :item-name="item.name"
      :item-description="`${item.category} • ${item.type === 'document' ? 'Document' : 'Subscription'}`"
      :item-icon="item.type === 'document' ? FileText : Repeat"
      :warning-message="item.file_path ? 'This item has an attached file that will also be deleted.' : ''"
      permanent
      @cancel="showDeleteModal = false"
      @confirm="deleteItem"
    />

  </DashboardLayout>
</template>

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

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>