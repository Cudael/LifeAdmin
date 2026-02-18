<template>
  <div class="space-y-8">

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-12">
      <Loader2 :size="32" class="animate-spin text-teal-400" />
    </div>

    <div v-else>

      <!-- PERSONAL INFORMATION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-teal-900/40 flex items-center justify-center flex-shrink-0">
            <User :size="20" class="text-teal-400" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-white">Personal Information</h3>
            <p class="text-sm text-gray-300 mt-1">Your account details</p>
          </div>
        </div>

        <form @submit.prevent="save" class="space-y-6">
          
          <!-- Full Name -->
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-2">
              Full Name *
            </label>
            <div class="relative">
              <input
                v-model="form.full_name"
                type="text"
                class="w-full pl-11 pr-4 py-3 bg-gray-800 border border-gray-700 text-white placeholder:text-gray-500 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                placeholder="John Doe"
                required
              />
              <User :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
            </div>
            <p class="text-xs text-gray-400 mt-2">
              This name will be displayed throughout the app
            </p>
          </div>

          <!-- Email (Read-only) -->
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-2">
              Email Address
            </label>
            <div class="relative">
              <input
                :value="form.email"
                type="email"
                class="w-full pl-11 pr-4 py-3 border border-gray-700 bg-gray-800/50 rounded-xl text-gray-400 cursor-not-allowed"
                readonly
              />
              <Mail :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
            </div>
            <div class="flex items-center gap-2 mt-2">
              <div class="flex items-center gap-1.5 px-2.5 py-1 bg-green-50 border border-green-200 rounded-lg">
                <CheckCircle2 :size="14" class="text-green-600" />
                <span class="text-xs font-medium text-green-700">Connected via Google</span>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex items-center gap-3 pt-2">
            <button
              type="submit"
              :disabled="saving || !hasChanges"
              class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              <Loader2 :size="18" class="animate-spin" v-if="saving" />
              <Save :size="18" v-else />
              {{ saving ? 'Saving...' : 'Save Changes' }}
            </button>

            <button
              v-if="hasChanges"
              type="button"
              @click="resetForm"
              :disabled="saving"
              class="px-6 py-3 bg-gray-800 text-gray-300 rounded-xl font-semibold hover:bg-gray-700 transition-all duration-200 disabled:opacity-50"
            >
              Cancel
            </button>
          </div>

          <!-- Success Message -->
          <Transition
            enter-active-class="transition-all duration-200 ease-out"
            enter-from-class="opacity-0 translate-y-2"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition-all duration-150 ease-in"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 translate-y-2"
          >
            <div v-if="saveSuccess" class="flex items-center gap-2 p-4 bg-green-50 border border-green-200 rounded-xl text-green-800 text-sm">
              <CheckCircle2 :size="18" class="text-green-600" />
              <span>Profile updated successfully!</span>
            </div>
          </Transition>

          <!-- Error Message -->
          <Transition
            enter-active-class="transition-all duration-200 ease-out"
            enter-from-class="opacity-0 translate-y-2"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition-all duration-150 ease-in"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 translate-y-2"
          >
            <div v-if="error" class="flex items-center gap-2 p-4 bg-red-900/20 border border-red-800 rounded-xl text-red-400 text-sm">
              <AlertCircle :size="18" class="text-red-400" />
              <span>{{ error }}</span>
            </div>
          </Transition>

        </form>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-800"></div>

      <!-- ACCOUNT INFORMATION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-blue-900/40 flex items-center justify-center flex-shrink-0">
            <Info :size="20" class="text-blue-400" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-white">Account Information</h3>
            <p class="text-sm text-gray-300 mt-1">Overview of your account</p>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          <!-- Member Since -->
          <div class="p-5 bg-teal-900/20 rounded-xl border border-teal-800">
            <div class="flex items-center gap-2 mb-2">
              <Calendar :size="18" class="text-teal-400" />
              <p class="text-sm font-medium text-gray-300">Member Since</p>
            </div>
            <p class="text-xl font-bold text-white">
              {{ formatDate(form.created_at) }}
            </p>
          </div>

          <!-- Last Updated -->
          <div class="p-5 bg-blue-900/20 rounded-xl border border-blue-800">
            <div class="flex items-center gap-2 mb-2">
              <RefreshCw :size="18" class="text-blue-400" />
              <p class="text-sm font-medium text-gray-300">Last Updated</p>
            </div>
            <p class="text-xl font-bold text-white">
              {{ formatDate(form.updated_at) }}
            </p>
          </div>

          <!-- Total Items -->
          <div class="p-5 bg-purple-900/20 rounded-xl border border-purple-800">
            <div class="flex items-center gap-2 mb-2">
              <Package :size="18" class="text-purple-400" />
              <p class="text-sm font-medium text-gray-300">Total Items</p>
            </div>
            <p class="text-xl font-bold text-white">
              {{ stats.total_items }}
            </p>
            <p class="text-xs text-gray-400 mt-1">Documents & subscriptions</p>
          </div>

          <!-- Active Subscriptions -->
          <div class="p-5 bg-orange-900/20 rounded-xl border border-orange-800">
            <div class="flex items-center gap-2 mb-2">
              <Repeat :size="18" class="text-orange-400" />
              <p class="text-sm font-medium text-gray-300">Subscriptions</p>
            </div>
            <p class="text-xl font-bold text-white">
              {{ stats.active_subscriptions }}
            </p>
            <p class="text-xs text-gray-400 mt-1">Active recurring items</p>
          </div>

        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { apiFetch } from "../../utils/api"
import {
  User,
  Mail,
  Calendar,
  RefreshCw,
  Package,
  Repeat,
  Save,
  CheckCircle2,
  AlertCircle,
  Info,
  Loader2
} from "lucide-vue-next"

const form = ref({
  full_name: "",
  email: "",
  created_at: "",
  updated_at: ""
})

const stats = ref({
  total_items: 0,
  active_subscriptions: 0
})

const originalForm = ref({})
const saving = ref(false)
const saveSuccess = ref(false)
const error = ref("")
const loading = ref(true)

const hasChanges = computed(() => {
  return JSON.stringify(form.value) !== JSON.stringify(originalForm.value)
})

onMounted(async () => {
  await loadProfile()
  await loadStats()
})

async function loadProfile() {
  try {
    const res = await apiFetch("/auth/me")
    
    if (!res.ok) {
      throw new Error("Failed to fetch profile")
    }
    
    const data = await res.json()
    
    form.value = {
      full_name: data.full_name || data.name || "",
      email: data.email || "",
      created_at: data.created_at || new Date().toISOString(),
      updated_at: data.updated_at || new Date().toISOString()
    }
    
    // Store original form state
    originalForm.value = JSON.parse(JSON.stringify(form.value))
    
  } catch (err) {
    console.error("Error fetching profile:", err)
    error.value = "Failed to load profile data"
  } finally {
    loading.value = false
  }
}

async function loadStats() {
  try {
    const res = await apiFetch("/items/stats")
    
    if (res.ok) {
      const data = await res.json()
      stats.value = {
        total_items: data.total_items || 0,
        active_subscriptions: data.active_subscriptions || 0
      }
    }
  } catch (err) {
    console.error("Error fetching stats:", err)
    // Don't show error, just use default values
  }
}

async function save() {
  saving.value = true
  error.value = ""
  saveSuccess.value = false
  
  try {
    const res = await apiFetch("/auth/me", {
      method: "PUT",
      body: JSON.stringify({
        full_name: form.value.full_name
      })
    })
    
    if (!res.ok) {
      throw new Error("Failed to update profile")
    }
    
    const data = await res.json()
    
    // Update timestamp
    form.value.updated_at = data.updated_at || new Date().toISOString()
    
    // Update original form state
    originalForm.value = JSON.parse(JSON.stringify(form.value))
    
    saveSuccess.value = true
    setTimeout(() => {
      saveSuccess.value = false
    }, 3000)
    
  } catch (err) {
    console.error("Error saving profile:", err)
    error.value = "Failed to update profile. Please try again."
    setTimeout(() => {
      error.value = ""
    }, 5000)
  } finally {
    saving.value = false
  }
}

function resetForm() {
  form.value = JSON.parse(JSON.stringify(originalForm.value))
}

function formatDate(dateString) {
  if (!dateString) return "N/A"
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>