<script setup>
import { onMounted, ref, computed } from "vue"
import { useRoute, useRouter } from "vue-router"
import { apiFetch } from "../utils/api"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import DeleteModal from "../components/DeleteModal.vue"
import {
  Edit2,
  Trash2,
  FileText,
  Repeat,
  Calendar,
  Clock,
  FolderOpen,
  Tag,
  Download,
  ExternalLink,
  AlertTriangle,
  CheckCircle2,
  AlertCircle,
  ChevronRight,
  ArrowLeft,
  File,
  Bell
} from "lucide-vue-next"

const route = useRoute()
const router = useRouter()

const item = ref(null)
const user = ref(null)
const deleteModalOpen = ref(false)
const loading = ref(true)

function formatDate(date) {
  if (!date) return "—"
  return new Date(date).toLocaleDateString('en-US', { 
    month: 'short', 
    day: 'numeric', 
    year: 'numeric' 
  })
}

function daysLeft(date) {
  if (!date) return null
  const diff = (new Date(date) - new Date()) / (1000 * 60 * 60 * 24)
  return Math.ceil(diff)
}

const status = computed(() => {
  if (!item.value?.expiration_date) return { label: "Valid", icon: CheckCircle2 }

  const diff = daysLeft(item.value.expiration_date)

  if (diff < 0) return { label: "Expired", icon: AlertTriangle }
  if (diff < 7) return { label: "Expiring This Week", icon: AlertCircle }
  if (diff < 30) return { label: "Expiring Soon", icon: Clock }
  return { label: "Valid", icon: CheckCircle2 }
})

const statusColor = computed(() => {
  switch (status.value.label) {
    case "Expired": return "bg-red-500/10 text-red-700 border-red-200"
    case "Expiring This Week": return "bg-yellow-500/10 text-yellow-700 border-yellow-200"
    case "Expiring Soon": return "bg-orange-500/10 text-orange-700 border-orange-200"
    default: return "bg-green-500/10 text-green-700 border-green-200"
  }
})

const isDocument = computed(() => item.value?.type === "document")
const isSubscription = computed(() => item.value?.type === "subscription")

const reminderDaysDisplay = computed(() => {
  if (!item.value) return null
  if (item.value.reminder_days_before !== null && item.value.reminder_days_before !== undefined) {
    return item.value.reminder_days_before
  }
  return user.value?.notification_days_before || 7
})

const usingCustomReminder = computed(() => {
  return item.value?.reminder_days_before !== null && item.value?.reminder_days_before !== undefined
})

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

async function loadItem() {
  try {
    const res = await apiFetch(`/items/${route.params.id}`)
    if (!res.ok) {
      router.push("/items")
      return
    }
    item.value = await res.json()
    loading.value = false
  } catch (err) {
    console.error(err)
    router.push("/items")
  }
}

async function deleteItem() {
  await apiFetch(`/items/${item.value.id}`, { method: "DELETE" })
  router.push("/items")
}

onMounted(async () => {
  await loadUser()
  await loadItem()
})
</script>

<template>
  <DashboardLayout :pageTitle="item ? item.name : 'Loading…'">

    <!-- Breadcrumb -->
    <div class="mb-6">
      <div class="flex items-center gap-2 text-sm text-gray-600">
        <RouterLink to="/dashboard" class="hover:text-teal-600 transition-colors">Dashboard</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink to="/items" class="hover:text-teal-600 transition-colors">Items</RouterLink>
        <ChevronRight :size="16" />
        <span class="text-gray-900 font-medium">{{ item?.name || 'Loading...' }}</span>
      </div>
    </div>

    <!-- Back Button & Actions -->
    <div class="flex justify-between items-center mb-6">
      <button
        @click="$router.back()"
        class="group inline-flex items-center gap-2 px-4 py-2 bg-white border-2 border-gray-200 rounded-xl shadow-sm hover:border-teal-300 hover:shadow-md transition-all duration-200"
      >
        <ArrowLeft :size="18" class="group-hover:-translate-x-1 transition-transform" />
        <span class="font-medium text-gray-700">Back</span>
      </button>

      <div class="flex gap-3">
        <RouterLink
          :to="`/items/${item?.id}/edit`"
          class="group inline-flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300"
        >
          <Edit2 :size="18" />
          Edit
        </RouterLink>

        <button
          @click="deleteModalOpen = true"
          class="group inline-flex items-center gap-2 px-5 py-2.5 bg-red-50 border-2 border-red-200 text-red-600 rounded-xl font-semibold hover:bg-red-100 hover:border-red-300 transition-all duration-200"
        >
          <Trash2 :size="18" />
          Delete
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-20">
      <div class="text-center">
        <div class="w-16 h-16 border-4 border-teal-200 border-t-teal-500 rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-gray-600">Loading item details...</p>
      </div>
    </div>

    <!-- Content -->
    <div v-else-if="item" class="space-y-6">

      <!-- HERO CARD -->
      <div class="relative overflow-hidden bg-gradient-to-br from-white to-gray-50 rounded-3xl shadow-xl border-2 border-gray-100 p-8 md:p-10">
        
        <!-- Decorative element -->
        <div class="absolute top-0 right-0 w-64 h-64 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-full opacity-20 -translate-y-1/2 translate-x-1/2"></div>

        <div class="relative z-10">
          <!-- Type Badge & Status -->
          <div class="flex flex-wrap items-center gap-3 mb-6">
            <div :class="[
              'inline-flex items-center gap-2 px-4 py-2 rounded-xl font-semibold text-sm shadow-md',
              isDocument ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white' : 'bg-gradient-to-r from-purple-500 to-pink-500 text-white'
            ]">
              <component :is="isDocument ? FileText : Repeat" :size="18" />
              {{ item.type === 'document' ? 'Document' : 'Subscription' }}
            </div>

            <div :class="['inline-flex items-center gap-2 px-4 py-2 rounded-xl font-semibold text-sm border-2', statusColor]">
              <component :is="status.icon" :size="18" />
              {{ status.label }}
            </div>
          </div>

          <!-- Title -->
          <h2 class="text-4xl font-bold text-gray-900 mb-4">{{ item.name }}</h2>

          <!-- Meta Info -->
          <div class="flex flex-wrap gap-6 text-sm text-gray-600">
            <div class="flex items-center gap-2">
              <Calendar :size="16" />
              <span>Created {{ formatDate(item.created_at) }}</span>
            </div>
            <div class="flex items-center gap-2">
              <Clock :size="16" />
              <span>Updated {{ formatDate(item.updated_at) }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- DETAILS GRID -->
      <div class="grid md:grid-cols-2 gap-6">

        <!-- Category -->
        <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border-2 border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-500 flex items-center justify-center">
              <FolderOpen :size="24" class="text-white" />
            </div>
            <div>
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Category</p>
              <p class="text-xl font-bold text-gray-900">{{ item.category || "—" }}</p>
            </div>
          </div>
        </div>

        <!-- Type -->
        <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border-2 border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div :class="[
              'w-12 h-12 rounded-xl flex items-center justify-center',
              isDocument ? 'bg-gradient-to-br from-teal-500 to-cyan-500' : 'bg-gradient-to-br from-purple-500 to-pink-500'
            ]">
              <component :is="isDocument ? FileText : Repeat" :size="24" class="text-white" />
            </div>
            <div>
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Type</p>
              <p class="text-xl font-bold text-gray-900 capitalize">{{ item.type }}</p>
            </div>
          </div>
        </div>

        <!-- Expiration Date -->
        <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border-2 border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-orange-500 to-red-500 flex items-center justify-center">
              <Calendar :size="24" class="text-white" />
            </div>
            <div>
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">
                {{ isSubscription ? 'Renewal Date' : 'Expiration Date' }}
              </p>
              <p class="text-xl font-bold text-gray-900">
                {{ item.expiration_date ? formatDate(item.expiration_date) : "—" }}
              </p>
            </div>
          </div>
        </div>

        <!-- Days Left -->
        <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border-2 border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-green-500 to-emerald-500 flex items-center justify-center">
              <Clock :size="24" class="text-white" />
            </div>
            <div>
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Days Left</p>
              <p class="text-xl font-bold text-gray-900">
                {{ item.expiration_date ? (daysLeft(item.expiration_date) < 0 ? 'Overdue' : daysLeft(item.expiration_date)) : "—" }}
              </p>
            </div>
          </div>
        </div>

        <!-- Reminder Schedule -->
        <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border-2 border-gray-100 p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-500 flex items-center justify-center">
              <Bell :size="24" class="text-white" />
            </div>
            <div class="flex-1">
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Reminder Schedule</p>
              <p class="text-xl font-bold text-gray-900">
                {{ reminderDaysDisplay }} days before
              </p>
              <p v-if="usingCustomReminder" class="text-xs text-blue-600 font-medium mt-1">
                ✨ Custom reminder
              </p>
              <p v-else class="text-xs text-gray-500 mt-1">
                Using account default
              </p>
            </div>
          </div>
        </div>

      </div>

      <!-- NOTES -->
      <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border-2 border-gray-100 p-8">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-amber-500 to-orange-500 flex items-center justify-center">
            <FileText :size="24" class="text-white" />
          </div>
          <h3 class="text-2xl font-bold text-gray-900">Notes</h3>
        </div>
        
        <div class="bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl p-6 border border-gray-200">
          <p class="text-gray-700 whitespace-pre-line leading-relaxed">
            {{ item.notes || "No notes added." }}
          </p>
        </div>
      </div>

      <!-- ATTACHED FILE -->
      <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-lg border-2 border-gray-100 p-8">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-violet-500 to-purple-500 flex items-center justify-center">
            <File :size="24" class="text-white" />
          </div>
          <h3 class="text-2xl font-bold text-gray-900">Attached File</h3>
        </div>

        <div v-if="item.file_path" class="bg-gradient-to-br from-teal-50 to-cyan-50 rounded-xl p-6 border-2 border-teal-200">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-4">
              <div class="w-14 h-14 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-500 flex items-center justify-center">
                <File :size="28" class="text-white" />
              </div>
              <div>
                <p class="font-semibold text-gray-900">Document attached</p>
                <p class="text-sm text-gray-600">Click to view or download</p>
              </div>
            </div>
            <a
              :href="`http://localhost:8000${item.file_path}`"
              target="_blank"
              class="group inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 shadow-lg hover:shadow-xl"
            >
              <ExternalLink :size="18" />
              View File
            </a>
          </div>
        </div>

        <div v-else class="bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl p-8 border-2 border-dashed border-gray-300 text-center">
          <File :size="48" class="text-gray-300 mx-auto mb-3" />
          <p class="text-gray-500 font-medium">No file uploaded</p>
          <RouterLink 
            :to="`/items/${item.id}/edit`"
            class="inline-block mt-3 text-teal-600 hover:text-teal-700 font-semibold text-sm hover:underline"
          >
            Add a file →
          </RouterLink>
        </div>
      </div>

    </div>

    <!-- DELETE MODAL -->
    <DeleteModal
      :show="deleteModalOpen"
      title="Delete Item?"
      message="This will permanently delete this item and all its associated data. This action cannot be undone."
      :item-name="item?.name"
      :item-description="`${item?.category} • ${item?.type === 'document' ? 'Document' : 'Subscription'}`"
      :item-icon="item?.type === 'document' ? FileText : Repeat"
      permanent
      @cancel="deleteModalOpen = false"
      @confirm="deleteItem"
    />

  </DashboardLayout>
</template>