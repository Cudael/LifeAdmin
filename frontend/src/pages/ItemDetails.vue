<script setup>
import { onMounted, ref, computed } from "vue"
import { useRoute, useRouter } from "vue-router"
import { apiFetch, BASE_URL } from "../utils/api"
import { useAuthStore } from "../stores/auth"
import { useItemsStore } from "../stores/items"
import { useItemStatus } from "../composables/useItemStatus"
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
const authStore = useAuthStore()
const itemsStore = useItemsStore()
const { daysLeft, getStatus, getStatusColor } = useItemStatus()

const item = ref(null)
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

const status = computed(() => {
  if (!item.value?.expiration_date) return { label: "Valid", icon: CheckCircle2 }

  const s = getStatus(item.value.expiration_date)
  
  const iconMap = {
    expired: AlertTriangle,
    week: AlertCircle,
    soon: Clock,
    valid: CheckCircle2
  }

  return { label: s.label, icon: iconMap[s.key] }
})

const statusColor = computed(() => {
  if (!item.value?.expiration_date) return "bg-green-500/10 text-green-400 border-green-500/30"
  
  const s = getStatus(item.value.expiration_date)
  const colorMap = {
    expired: "bg-red-500/10 text-red-400 border-red-500/30",
    week: "bg-orange-500/10 text-orange-400 border-orange-500/30",
    soon: "bg-amber-500/10 text-amber-400 border-amber-500/30",
    valid: "bg-green-500/10 text-green-400 border-green-500/30"
  }
  
  return colorMap[s.key] || colorMap.valid
})

const isDocument = computed(() => item.value?.type === "document")
const isSubscription = computed(() => item.value?.type === "subscription")

const reminderDaysDisplay = computed(() => {
  if (!item.value) return null
  if (item.value.reminder_days_before !== null && item.value.reminder_days_before !== undefined) {
    return item.value.reminder_days_before
  }
  return authStore.user?.notification_days_before || 7
})

const usingCustomReminder = computed(() => {
  return item.value?.reminder_days_before !== null && item.value?.reminder_days_before !== undefined
})

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
  await itemsStore.deleteItem(item.value.id)
  router.push("/items")
}

onMounted(async () => {
  await authStore.fetchUser()
  await loadItem()
})
</script>

<template>
  <DashboardLayout :pageTitle="item ? item.name : 'Loading…'">

    <!-- Breadcrumb -->
    <div class="mb-6">
      <div class="flex items-center gap-2 text-sm text-gray-400">
        <RouterLink to="/dashboard" class="hover:text-teal-400 transition-colors">Dashboard</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink to="/items" class="hover:text-teal-400 transition-colors">Items</RouterLink>
        <ChevronRight :size="16" />
        <span class="text-white font-medium">{{ item?.name || 'Loading...' }}</span>
      </div>
    </div>

    <!-- Back Button & Actions -->
    <div class="flex justify-between items-center mb-6">
      <button
        @click="$router.back()"
        class="group inline-flex items-center gap-2 px-4 py-2.5 bg-gradient-to-br from-gray-900 to-gray-800/80 border border-gray-700/40 text-gray-300 rounded-lg hover:border-gray-600 transition-all duration-200"
      >
        <ArrowLeft :size="18" class="group-hover:-translate-x-1 transition-transform" />
        <span class="font-medium">Back</span>
      </button>

      <div class="flex gap-3">
        <RouterLink
          :to="`/items/${item?.id}/edit`"
          class="group inline-flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-lg font-semibold shadow-lg hover:shadow-xl hover:from-teal-400 hover:to-cyan-400 transition-all duration-300"
        >
          <Edit2 :size="18" />
          Edit
        </RouterLink>

        <button
          @click="deleteModalOpen = true"
          class="group inline-flex items-center gap-2 px-5 py-2.5 bg-gradient-to-br from-red-950/40 to-red-900/20 border border-red-800/50 text-red-400 rounded-lg font-semibold hover:bg-red-950/60 transition-all duration-200"
        >
          <Trash2 :size="18" />
          Delete
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-20">
      <div class="text-center">
        <div class="w-16 h-16 border-4 border-teal-500/20 border-t-teal-500 rounded-full animate-spin mx-auto mb-4"></div>
        <p class="text-gray-400">Loading item details...</p>
      </div>
    </div>

    <!-- Content -->
    <div v-else-if="item" class="space-y-6">

      <!-- HERO CARD -->
      <div class="relative overflow-hidden bg-gradient-to-br from-gray-900 to-gray-800/80 rounded-xl border border-gray-700/40 p-8 md:p-10">
        
        <!-- Decorative element -->
        <div class="absolute top-0 right-0 w-64 h-64 bg-gradient-to-br from-teal-500/10 to-cyan-500/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>

        <div class="relative z-10">
          <!-- Type Badge & Status -->
          <div class="flex flex-wrap items-center gap-3 mb-6">
            <div :class="[
              'inline-flex items-center gap-2 px-4 py-2 rounded-lg font-semibold text-sm shadow-lg',
              isDocument ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white' : 'bg-gradient-to-r from-purple-500 to-pink-500 text-white'
            ]">
              <component :is="isDocument ? FileText : Repeat" :size="18" />
              {{ item.type === 'document' ? 'Document' : 'Subscription' }}
            </div>

            <div :class="['inline-flex items-center gap-2 px-4 py-2 rounded-lg font-semibold text-sm border', statusColor]">
              <component :is="status.icon" :size="18" />
              {{ status.label }}
            </div>
          </div>

          <!-- Title -->
          <h2 class="text-4xl font-bold text-white mb-4">{{ item.name }}</h2>

          <!-- Meta Info -->
          <div class="flex flex-wrap gap-6 text-sm text-gray-400">
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
        <div class="bg-gradient-to-br from-gray-900 to-gray-800/80 backdrop-blur-xl rounded-xl border border-gray-700/40 p-6 hover:border-gray-600 transition-all duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-12 h-12 rounded-xl bg-blue-500/20 flex items-center justify-center ring-1 ring-blue-500/30">
              <FolderOpen :size="24" class="text-blue-400" />
            </div>
            <div>
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Category</p>
              <p class="text-xl font-bold text-white">{{ item.category || "—" }}</p>
            </div>
          </div>
        </div>

        <!-- Type -->
        <div class="bg-gradient-to-br from-gray-900 to-gray-800/80 backdrop-blur-xl rounded-xl border border-gray-700/40 p-6 hover:border-gray-600 transition-all duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div :class="[
              'w-12 h-12 rounded-xl flex items-center justify-center ring-1',
              isDocument ? 'bg-teal-500/20 ring-teal-500/30' : 'bg-purple-500/20 ring-purple-500/30'
            ]">
              <component :is="isDocument ? FileText : Repeat" :size="24" :class="isDocument ? 'text-teal-400' : 'text-purple-400'" />
            </div>
            <div>
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Type</p>
              <p class="text-xl font-bold text-white capitalize">{{ item.type }}</p>
            </div>
          </div>
        </div>

        <!-- Expiration Date -->
        <div class="bg-gradient-to-br from-gray-900 to-gray-800/80 backdrop-blur-xl rounded-xl border border-gray-700/40 p-6 hover:border-gray-600 transition-all duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-12 h-12 rounded-xl bg-orange-500/20 flex items-center justify-center ring-1 ring-orange-500/30">
              <Calendar :size="24" class="text-orange-400" />
            </div>
            <div>
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">
                {{ isSubscription ? 'Renewal Date' : 'Expiration Date' }}
              </p>
              <p class="text-xl font-bold text-white">
                {{ item.expiration_date ? formatDate(item.expiration_date) : "—" }}
              </p>
            </div>
          </div>
        </div>

        <!-- Days Left -->
        <div class="bg-gradient-to-br from-gray-900 to-gray-800/80 backdrop-blur-xl rounded-xl border border-gray-700/40 p-6 hover:border-gray-600 transition-all duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-12 h-12 rounded-xl bg-green-500/20 flex items-center justify-center ring-1 ring-green-500/30">
              <Clock :size="24" class="text-green-400" />
            </div>
            <div>
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Days Left</p>
              <p class="text-xl font-bold text-white">
                {{ item.expiration_date ? (daysLeft(item.expiration_date) < 0 ? 'Overdue' : daysLeft(item.expiration_date)) : "—" }}
              </p>
            </div>
          </div>
        </div>

        <!-- Reminder Schedule -->
        <div class="bg-gradient-to-br from-gray-900 to-gray-800/80 backdrop-blur-xl rounded-xl border border-gray-700/40 p-6 hover:border-gray-600 transition-all duration-300">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-12 h-12 rounded-xl bg-indigo-500/20 flex items-center justify-center ring-1 ring-indigo-500/30">
              <Bell :size="24" class="text-indigo-400" />
            </div>
            <div class="flex-1">
              <p class="text-xs text-gray-500 uppercase tracking-wide font-semibold">Reminder Schedule</p>
              <p class="text-xl font-bold text-white">
                {{ reminderDaysDisplay }} days before
              </p>
              <p v-if="usingCustomReminder" class="text-xs text-blue-400 font-medium mt-1">
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
      <div class="bg-gradient-to-br from-gray-900 to-gray-800/80 backdrop-blur-xl rounded-xl border border-gray-700/40 p-8">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 rounded-xl bg-amber-500/20 flex items-center justify-center ring-1 ring-amber-500/30">
            <FileText :size="24" class="text-amber-400" />
          </div>
          <h3 class="text-2xl font-bold text-white">Notes</h3>
        </div>
        
        <div class="bg-white/5 border border-gray-700/50 rounded-lg p-6">
          <p class="text-gray-300 whitespace-pre-line leading-relaxed">
            {{ item.notes || "No notes added." }}
          </p>
        </div>
      </div>

      <!-- ATTACHED FILE -->
      <div class="bg-gradient-to-br from-gray-900 to-gray-800/80 backdrop-blur-xl rounded-xl border border-gray-700/40 p-8">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 rounded-xl bg-violet-500/20 flex items-center justify-center ring-1 ring-violet-500/30">
            <File :size="24" class="text-violet-400" />
          </div>
          <h3 class="text-2xl font-bold text-white">Attached File</h3>
        </div>

        <div v-if="item.file_path" class="bg-gradient-to-br from-teal-500/10 to-cyan-500/10 border border-teal-500/20 rounded-lg p-6">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-4">
              <div class="w-14 h-14 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-500 flex items-center justify-center shadow-lg">
                <File :size="28" class="text-white" />
              </div>
              <div>
                <p class="font-semibold text-white">Document attached</p>
                <p class="text-sm text-gray-400">Click to view or download</p>
              </div>
            </div>
            <a
              :href="`${BASE_URL}${item.file_path}`"
              target="_blank"
              class="group inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-lg font-semibold hover:from-teal-400 hover:to-cyan-400 transition-all duration-300 shadow-lg hover:shadow-xl"
            >
              <ExternalLink :size="18" />
              View File
            </a>
          </div>
        </div>

        <div v-else class="bg-white/5 border-2 border-dashed border-gray-700/50 rounded-lg p-8 text-center">
          <File :size="48" class="text-gray-600 mx-auto mb-3" />
          <p class="text-gray-400 font-medium">No file uploaded</p>
          <RouterLink 
            :to="`/items/${item.id}/edit`"
            class="inline-block mt-3 text-teal-400 hover:text-teal-300 font-semibold text-sm hover:underline"
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