<script setup>
import { ref, computed, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { apiFetch } from "../utils/api"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import FileUploader from "../components/FileUploader.vue"
import DeleteModal from "../components/common/DeleteModal.vue"
import Autocomplete from "../components/common/Autocomplete.vue"
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

// Document name suggestions organized by category
const documentNameSuggestions = [
  // Travel
  { value: 'Passport', label: 'Passport', icon: '🛂', description: 'Travel document', category: 'Travel' },
  { value: 'Visa', label: 'Visa', icon: '✈️', description: 'Travel authorization', category: 'Travel' },
  { value: 'Travel Insurance', label: 'Travel Insurance', icon: '🛡️', description: 'Travel coverage', category: 'Travel' },
  { value: 'Flight Ticket', label: 'Flight Ticket', icon: '🎫', description: 'Air travel ticket', category: 'Travel' },
  // Health
  { value: 'Health Insurance Card', label: 'Health Insurance Card', icon: '🏥', description: 'Health coverage card', category: 'Health' },
  { value: 'Medical Record', label: 'Medical Record', icon: '📋', description: 'Health documentation', category: 'Health' },
  { value: 'Vaccination Certificate', label: 'Vaccination Certificate', icon: '💉', description: 'Immunization record', category: 'Health' },
  { value: 'Prescription', label: 'Prescription', icon: '💊', description: 'Medical prescription', category: 'Health' },
  // Finance
  { value: 'Tax Return', label: 'Tax Return', icon: '💰', description: 'Annual tax filing', category: 'Finance' },
  { value: 'Bank Statement', label: 'Bank Statement', icon: '🏦', description: 'Banking document', category: 'Finance' },
  { value: 'Insurance Policy', label: 'Insurance Policy', icon: '🛡️', description: 'Insurance coverage', category: 'Finance' },
  { value: 'Investment Document', label: 'Investment Document', icon: '📈', description: 'Investment record', category: 'Finance' },
  // Work
  { value: 'Work Permit', label: 'Work Permit', icon: '💼', description: 'Employment authorization', category: 'Work' },
  { value: 'Employment Contract', label: 'Employment Contract', icon: '📝', description: 'Job agreement', category: 'Work' },
  { value: 'Professional License', label: 'Professional License', icon: '🎓', description: 'Professional certification', category: 'Work' },
  { value: 'Resume', label: 'Resume', icon: '📄', description: 'CV document', category: 'Work' },
  // Personal
  { value: 'Birth Certificate', label: 'Birth Certificate', icon: '👶', description: 'Official birth record', category: 'Personal' },
  { value: 'ID Card', label: 'ID Card', icon: '🪪', description: 'Identification card', category: 'Personal' },
  { value: 'Social Security Card', label: 'Social Security Card', icon: '🔐', description: 'SSN document', category: 'Personal' },
  { value: 'Marriage Certificate', label: 'Marriage Certificate', icon: '💍', description: 'Marriage record', category: 'Personal' },
  // Legal
  { value: 'Lease Agreement', label: 'Lease Agreement', icon: '🏠', description: 'Rental contract', category: 'Legal' },
  { value: 'Warranty', label: 'Warranty', icon: '🔧', description: 'Product guarantee', category: 'Legal' },
  { value: 'Power of Attorney', label: 'Power of Attorney', icon: '⚖️', description: 'Legal authorization', category: 'Legal' },
  { value: 'Will', label: 'Will', icon: '📜', description: 'Testament document', category: 'Legal' },
  // Education
  { value: 'Degree Certificate', label: 'Degree Certificate', icon: '🎓', description: 'Academic degree', category: 'Education' },
  { value: 'Transcript', label: 'Transcript', icon: '📊', description: 'Academic record', category: 'Education' },
  { value: 'Student ID', label: 'Student ID', icon: '🪪', description: 'Student identification', category: 'Education' },
  { value: 'Enrollment Document', label: 'Enrollment Document', icon: '📝', description: 'School enrollment', category: 'Education' },
  // Vehicle
  { value: "Driver's License", label: "Driver's License", icon: '🚗', description: 'Driving permit', category: 'Vehicle' },
  { value: 'Vehicle Registration', label: 'Vehicle Registration', icon: '🚙', description: 'Vehicle documents', category: 'Vehicle' },
  { value: 'Car Insurance', label: 'Car Insurance', icon: '🛡️', description: 'Auto coverage', category: 'Vehicle' },
  { value: 'Inspection Certificate', label: 'Inspection Certificate', icon: '✅', description: 'Vehicle inspection', category: 'Vehicle' }
]

// Subscription name suggestions
const subscriptionNameSuggestions = [
  // Streaming / Video
  { value: 'Netflix Subscription', label: 'Netflix', icon: '🎬', description: 'Video streaming', category: 'Subscriptions' },
  { value: 'YouTube Premium', label: 'YouTube Premium', icon: '🎥', description: 'Ad-free YouTube', category: 'Subscriptions' },
  { value: 'Disney+', label: 'Disney+', icon: '🏰', description: 'Disney streaming', category: 'Subscriptions' },
  { value: 'HBO Max', label: 'HBO Max', icon: '🎬', description: 'HBO streaming', category: 'Subscriptions' },
  { value: 'Amazon Prime', label: 'Amazon Prime', icon: '📦', description: 'Amazon streaming & shopping', category: 'Subscriptions' },
  { value: 'Apple TV+', label: 'Apple TV+', icon: '🍎', description: 'Apple streaming', category: 'Subscriptions' },
  { value: 'Hulu', label: 'Hulu', icon: '📺', description: 'Hulu streaming', category: 'Subscriptions' },
  { value: 'Paramount+', label: 'Paramount+', icon: '⭐', description: 'Paramount streaming', category: 'Subscriptions' },
  { value: 'Crunchyroll', label: 'Crunchyroll', icon: '🍥', description: 'Anime streaming', category: 'Subscriptions' },
  { value: 'Twitch', label: 'Twitch', icon: '🎮', description: 'Live streaming', category: 'Subscriptions' },
  // Music
  { value: 'Spotify Subscription', label: 'Spotify', icon: '🎵', description: 'Music streaming', category: 'Subscriptions' },
  { value: 'Apple Music', label: 'Apple Music', icon: '🎵', description: 'Apple music streaming', category: 'Subscriptions' },
  { value: 'Tidal', label: 'Tidal', icon: '🌊', description: 'HiFi music streaming', category: 'Subscriptions' },
  { value: 'YouTube Music', label: 'YouTube Music', icon: '🎶', description: 'YouTube music streaming', category: 'Subscriptions' },
  // Cloud / Productivity
  { value: 'Dropbox Subscription', label: 'Dropbox', icon: '☁️', description: 'Cloud storage', category: 'Subscriptions' },
  { value: 'Google One', label: 'Google One', icon: '☁️', description: 'Google cloud storage', category: 'Subscriptions' },
  { value: 'iCloud+', label: 'iCloud+', icon: '🍏', description: 'Apple cloud storage', category: 'Subscriptions' },
  { value: 'Microsoft 365', label: 'Microsoft 365', icon: '🖥️', description: 'Microsoft productivity suite', category: 'Subscriptions' },
  { value: 'Adobe Creative Cloud', label: 'Adobe Creative Cloud', icon: '🎨', description: 'Adobe creative apps', category: 'Subscriptions' },
  { value: 'Notion', label: 'Notion', icon: '📝', description: 'Notes & productivity', category: 'Subscriptions' },
  { value: 'Slack', label: 'Slack', icon: '💬', description: 'Team communication', category: 'Subscriptions' },
  { value: 'Zoom', label: 'Zoom', icon: '📹', description: 'Video conferencing', category: 'Subscriptions' },
  { value: 'GitHub Subscription', label: 'GitHub', icon: '💻', description: 'Code hosting', category: 'Subscriptions' },
  // Gaming
  { value: 'PlayStation Plus', label: 'PlayStation Plus', icon: '🎮', description: 'PlayStation online gaming', category: 'Subscriptions' },
  { value: 'Xbox Game Pass', label: 'Xbox Game Pass', icon: '🎯', description: 'Xbox games subscription', category: 'Subscriptions' },
  { value: 'Nintendo Switch Online', label: 'Nintendo Switch Online', icon: '🕹️', description: 'Nintendo online gaming', category: 'Subscriptions' },
  { value: 'Steam', label: 'Steam', icon: '🎲', description: 'PC gaming platform', category: 'Subscriptions' },
  { value: 'Gym Membership', label: 'Gym Membership', icon: '💪', description: 'Fitness membership', category: 'Subscriptions' },
  // Other Popular
  { value: 'ChatGPT Plus', label: 'ChatGPT Plus', icon: '🤖', description: 'AI assistant subscription', category: 'Subscriptions' },
  { value: 'NordVPN', label: 'NordVPN', icon: '🔒', description: 'VPN service', category: 'Subscriptions' },
  { value: 'ExpressVPN', label: 'ExpressVPN', icon: '🛡️', description: 'VPN service', category: 'Subscriptions' },
  { value: 'Duolingo', label: 'Duolingo', icon: '🦉', description: 'Language learning', category: 'Subscriptions' },
  { value: 'Audible', label: 'Audible', icon: '🎧', description: 'Audiobook subscription', category: 'Subscriptions' },
  { value: 'Kindle Unlimited', label: 'Kindle Unlimited', icon: '📚', description: 'Ebook subscription', category: 'Subscriptions' },
  // Insurance / Memberships
  { value: 'Auto Insurance', label: 'Auto Insurance', icon: '🚗', description: 'Vehicle insurance', category: 'Subscriptions' },
  { value: 'Professional Membership', label: 'Professional Membership', icon: '👔', description: 'Professional org membership', category: 'Subscriptions' },
]

// Category options
const categoryOptions = [
  'Travel',
  'Health',
  'Finance',
  'Work',
  'Personal',
  'Subscriptions',
  'Legal',
  'Education',
  'Vehicle'
]

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

// Filter document name suggestions based on selected category
const filteredDocumentNameSuggestions = computed(() => {
  if (!item.value.category) {
    return documentNameSuggestions // Show all if no category selected
  }
  return documentNameSuggestions.filter(suggestion => suggestion.category === item.value.category)
})

// Filter subscription name suggestions based on selected category
const filteredSubscriptionNameSuggestions = computed(() => {
  if (!item.value.category) {
    return subscriptionNameSuggestions // Show all if no category selected
  }
  return subscriptionNameSuggestions.filter(suggestion => suggestion.category === item.value.category)
})

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
      <div class="flex items-center gap-2 text-sm text-gray-400">
        <RouterLink to="/dashboard" class="hover:text-teal-400 transition-colors">Dashboard</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink to="/items" class="hover:text-teal-400 transition-colors">Items</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink :to="`/items/${route.params.id}`" class="hover:text-teal-400 transition-colors">
          {{ item.name || 'Item' }}
        </RouterLink>
        <ChevronRight :size="16" />
        <span class="text-white font-medium">Edit</span>
      </div>
    </div>

    <!-- Header Actions -->
    <div class="flex justify-between items-center mb-8">
      <button
        @click="$router.back()"
        class="group inline-flex items-center gap-2 px-4 py-2.5 bg-gradient-to-br from-gray-900 to-gray-800/80 border border-gray-700/40 text-gray-300 rounded-lg hover:border-gray-600 transition-all duration-200"
      >
        <ArrowLeft :size="18" class="group-hover:-translate-x-1 transition-transform" />
        <span class="font-medium">Back</span>
      </button>

      <button
        @click="showDeleteModal = true"
        :disabled="saving || deleting"
        class="group inline-flex items-center gap-2 px-4 py-2.5 bg-gradient-to-br from-red-950/40 to-red-900/20 border border-red-800/50 text-red-400 rounded-lg font-medium hover:bg-red-950/60 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <Trash2 :size="18" />
        Delete Item
      </button>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-20">
      <div class="text-center">
        <Loader2 :size="48" class="text-teal-500 animate-spin mx-auto mb-4" />
        <p class="text-gray-400">Loading item...</p>
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
          class="mb-6 p-4 bg-gradient-to-br from-green-950/40 to-green-900/20 border border-green-800/50 rounded-xl flex items-start gap-3 animate-bounce-in"
        >
          <CheckCircle2 :size="20" class="text-green-400 flex-shrink-0 mt-0.5" />
          <div>
            <p class="text-sm font-semibold text-green-300">{{ successMessage }}</p>
            <p class="text-xs text-green-400 mt-1">Redirecting...</p>
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
          class="mb-6 p-4 bg-gradient-to-br from-red-950/40 to-red-900/20 border border-red-800/50 rounded-xl flex items-start gap-3 animate-shake"
        >
          <AlertTriangle :size="20" class="text-red-400 flex-shrink-0 mt-0.5" />
          <p class="text-sm text-red-300">{{ errorMessage }}</p>
        </div>
      </Transition>

      <!-- FORM CARD -->
      <div class="bg-gradient-to-br from-gray-900 to-gray-800/80 backdrop-blur-xl rounded-xl border border-gray-700/40 p-8 md:p-10">

        <!-- Header -->
        <div class="flex items-center gap-3 mb-8 pb-6 border-b border-gray-700/50">
          <div :class="[
            'w-12 h-12 rounded-xl flex items-center justify-center ring-1',
            isDocument ? 'bg-teal-500/20 ring-teal-500/30' : 'bg-purple-500/20 ring-purple-500/30'
          ]">
            <component :is="isDocument ? FileText : Repeat" :size="24" :class="isDocument ? 'text-teal-400' : 'text-purple-400'" />
          </div>
          <div>
            <h2 class="text-2xl font-bold text-white">Edit Item</h2>
            <p class="text-sm text-gray-400">Update your {{ item.type }} details</p>
          </div>
        </div>

        <!-- Form -->
        <form @submit.prevent="saveItem" class="space-y-6">

          <!-- NAME & TYPE (Side by Side) -->
          <div class="grid md:grid-cols-2 gap-6">

            <!-- NAME -->
            <div class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-300">
                <FileText :size="16" class="text-teal-400" />
                Name
                <span class="text-red-400">*</span>
              </label>
              <Autocomplete
                v-if="isDocument"
                v-model="item.name"
                :suggestions="filteredDocumentNameSuggestions"
                placeholder="e.g., Passport, Visa, or type your own"
                :required="true"
                :disabled="saving"
                color="teal"
              />
              <Autocomplete
                v-else-if="isSubscription"
                v-model="item.name"
                :suggestions="filteredSubscriptionNameSuggestions"
                placeholder="e.g., Netflix, Spotify, or type your own"
                :required="true"
                :disabled="saving"
                color="teal"
              />
              <input
                v-else
                v-model="item.name"
                type="text"
                class="w-full px-4 py-3 bg-white/5 border border-gray-700/50 rounded-lg text-white placeholder-gray-500 focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200"
                required
                :disabled="saving"
              />
            </div>

            <!-- TYPE -->
            <div class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-300">
                <Repeat :size="16" class="text-teal-400" />
                Type
                <span class="text-red-400">*</span>
              </label>
              <select
                v-model="item.type"
                class="w-full px-4 py-3 bg-white/5 border border-gray-700/50 rounded-lg text-white focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 appearance-none cursor-pointer"
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
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-300">
              <FolderOpen :size="16" class="text-teal-400" />
              Category
              <span class="text-red-400">*</span>
            </label>
            <select
              v-model="item.category"
              class="w-full px-4 py-3 bg-white/5 border border-gray-700/50 rounded-lg text-white focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 appearance-none cursor-pointer"
              required
              :disabled="saving"
            >
              <option value="" disabled>Select a category</option>
              <option v-for="cat in categoryOptions" :key="cat" :value="cat">
                {{ cat }}
              </option>
            </select>
          </div>

          <!-- DATES (Different based on type) -->
          <div class="grid md:grid-cols-2 gap-6">

            <!-- EXPIRATION DATE (for documents) -->
            <div v-if="isDocument" class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-300">
                <Calendar :size="16" class="text-teal-400" />
                Expiration Date
              </label>
              <input
                v-model="item.expiration_date"
                type="date"
                class="w-full px-4 py-3 bg-white/5 border border-gray-700/50 rounded-lg text-white focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200"
                :disabled="saving"
              />
            </div>

            <!-- RENEWAL DATE (for subscriptions) -->
            <div v-if="isSubscription" class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-300">
                <Calendar :size="16" class="text-purple-400" />
                Renewal Date
              </label>
              <input
                v-model="item.renewal_date"
                type="date"
                class="w-full px-4 py-3 bg-white/5 border border-gray-700/50 rounded-lg text-white focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200"
                :disabled="saving"
              />
            </div>

            <!-- EXPIRATION DATE (for subscriptions - optional) -->
            <div v-if="isSubscription" class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-300">
                <Calendar :size="16" class="text-purple-400" />
                Expiration Date
                <span class="text-gray-500 text-xs font-normal">(optional)</span>
              </label>
              <input
                v-model="item.expiration_date"
                type="date"
                class="w-full px-4 py-3 bg-white/5 border border-gray-700/50 rounded-lg text-white focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200"
                :disabled="saving"
              />
            </div>

            <!-- REMINDER SCHEDULE -->
            <div class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-300">
                <Bell :size="16" :class="isDocument ? 'text-teal-400' : 'text-purple-400'" />
                Reminder Schedule
                <span class="text-gray-500 text-xs font-normal">(optional)</span>
              </label>
              <div class="space-y-3">
                <div class="flex items-center gap-2 p-3 bg-blue-500/10 border border-blue-500/20 rounded-lg">
                  <Info :size="16" class="text-blue-400 flex-shrink-0" />
                  <p class="text-xs text-blue-300">
                    Custom reminder for this item, or leave as default to use your account setting ({{ userDefaultReminderDays }} days).
                  </p>
                </div>
                
                <div class="flex gap-2">
                  <button
                    type="button"
                    @click="item.reminder_days_before = null"
                    :class="[
                      'flex-1 px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 border',
                      item.reminder_days_before === null
                        ? `bg-gradient-to-r ${isDocument ? 'from-teal-500 to-cyan-500' : 'from-purple-500 to-pink-500'} border-transparent text-white shadow-lg`
                        : 'bg-white/5 text-gray-300 border-gray-700/50 hover:border-gray-600'
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
                      'flex-1 px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200 border',
                      item.reminder_days_before === days
                        ? `bg-gradient-to-r ${isDocument ? 'from-teal-500 to-cyan-500' : 'from-purple-500 to-pink-500'} border-transparent text-white shadow-lg`
                        : 'bg-white/5 text-gray-300 border-gray-700/50 hover:border-gray-600'
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
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-300">
              <FileText :size="16" class="text-teal-400" />
              Notes
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <textarea
              v-model="item.notes"
              rows="4"
              class="w-full px-4 py-3 bg-white/5 border border-gray-700/50 rounded-lg text-white placeholder-gray-500 focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 resize-none"
              placeholder="Add any additional details..."
              :disabled="saving"
            ></textarea>
          </div>

          <!-- FILE UPLOAD -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-300">
              <Upload :size="16" class="text-teal-400" />
              File
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <FileUploader
              v-model="file"
              :existingFile="item.file_path ? item.file_path.split('/').pop() : null"
            />
          </div>

          <!-- ACTION BUTTONS -->
          <div class="flex gap-4 pt-6 border-t border-gray-700/50">
            <button
              type="button"
              @click="$router.push(`/items/${item.id}`)"
              class="flex-1 px-6 py-4 bg-white/5 text-gray-300 border border-gray-700/50 rounded-lg font-semibold hover:bg-white/10 hover:border-gray-600 transition-all duration-200 flex items-center justify-center gap-2"
              :disabled="saving"
            >
              <X :size="20" />
              Cancel
            </button>

            <button
              type="submit"
              :disabled="saving"
              class="group flex-1 px-6 py-4 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-lg font-semibold shadow-lg hover:shadow-xl hover:from-teal-400 hover:to-cyan-400 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
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

/* Dark theme for select dropdowns */
select option {
  background-color: #1f2937;
  color: white;
}
</style>