<template>
  <div class="space-y-8">

    <!-- DATE & TIME FORMATS -->
    <div>
      <div class="flex items-start gap-3 mb-6">
        <div class="w-10 h-10 rounded-lg bg-blue-100 flex items-center justify-center flex-shrink-0">
          <Calendar :size="20" class="text-blue-600" />
        </div>
        <div>
          <h3 class="text-lg font-bold text-gray-900">Date & Time Formats</h3>
          <p class="text-sm text-gray-600 mt-1">Choose how dates and times are displayed throughout the app</p>
        </div>
      </div>

      <div class="space-y-4">
        
        <!-- Date Format -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            Date Format
          </label>
          <select
            v-model="preferences.date_format"
            class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-white"
          >
            <option value="MM/DD/YYYY">MM/DD/YYYY - 02/14/2026 (United States)</option>
            <option value="DD/MM/YYYY">DD/MM/YYYY - 14/02/2026 (Europe, Latin America)</option>
            <option value="YYYY-MM-DD">YYYY-MM-DD - 2026-02-14 (ISO Standard)</option>
          </select>
          <p class="text-xs text-gray-500 mt-2">
            This affects how expiration dates are shown in items and notifications
          </p>
        </div>

        <!-- Time Format -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            Time Format
          </label>
          <div class="grid grid-cols-2 gap-3">
            <button
              @click="preferences.time_format = '12h'"
              :class="[
                'px-4 py-3 rounded-xl font-medium transition-all duration-200 border-2',
                preferences.time_format === '12h'
                  ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white border-teal-500 shadow-md'
                  : 'bg-white text-gray-700 border-gray-200 hover:border-teal-300'
              ]"
            >
              <div class="flex items-center justify-center gap-2">
                <Clock :size="18" />
                <span>2:30 PM</span>
              </div>
              <p class="text-xs mt-1 opacity-75">12-hour</p>
            </button>
            
            <button
              @click="preferences.time_format = '24h'"
              :class="[
                'px-4 py-3 rounded-xl font-medium transition-all duration-200 border-2',
                preferences.time_format === '24h'
                  ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white border-teal-500 shadow-md'
                  : 'bg-white text-gray-700 border-gray-200 hover:border-teal-300'
              ]"
            >
              <div class="flex items-center justify-center gap-2">
                <Clock :size="18" />
                <span>14:30</span>
              </div>
              <p class="text-xs mt-1 opacity-75">24-hour</p>
            </button>
          </div>
        </div>

        <!-- Preview -->
        <div class="p-4 bg-gradient-to-br from-teal-50 to-cyan-50 rounded-xl border border-teal-200">
          <p class="text-sm font-medium text-gray-700 mb-2">Preview</p>
          <div class="flex items-center gap-2">
            <Calendar :size="16" class="text-teal-600" />
            <span class="text-gray-900 font-semibold">{{ previewDate }}</span>
          </div>
          <div class="flex items-center gap-2 mt-1">
            <Clock :size="16" class="text-teal-600" />
            <span class="text-gray-900 font-semibold">{{ previewTime }}</span>
          </div>
        </div>

      </div>
    </div>

    <!-- DIVIDER -->
    <div class="border-t border-gray-200"></div>

    <!-- ITEM DISPLAY -->
    <div>
      <div class="flex items-start gap-3 mb-6">
        <div class="w-10 h-10 rounded-lg bg-purple-100 flex items-center justify-center flex-shrink-0">
          <LayoutGrid :size="20" class="text-purple-600" />
        </div>
        <div>
          <h3 class="text-lg font-bold text-gray-900">Item Display</h3>
          <p class="text-sm text-gray-600 mt-1">Control how items are shown in lists</p>
        </div>
      </div>

      <div class="space-y-4">
        
        <!-- Items per page -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            Items per page
          </label>
          <select
            v-model="preferences.items_per_page"
            class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-white"
          >
            <option :value="10">10 items</option>
            <option :value="25">25 items</option>
            <option :value="50">50 items</option>
            <option :value="100">100 items</option>
          </select>
        </div>

        <!-- Sort by default -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">
            Default sort order
          </label>
          <select
            v-model="preferences.default_sort"
            class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-white"
          >
            <option value="expiration_asc">Expiring soonest first</option>
            <option value="expiration_desc">Expiring latest first</option>
            <option value="name_asc">Name (A-Z)</option>
            <option value="name_desc">Name (Z-A)</option>
            <option value="created_desc">Newest first</option>
            <option value="created_asc">Oldest first</option>
          </select>
        </div>

      </div>
    </div>

    <!-- SAVE BUTTON -->
    <div class="flex items-center gap-3 pt-4">
      <button
        @click="savePreferences"
        :disabled="saving || !hasChanges"
        class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
      >
        <Loader2 :size="18" class="animate-spin" v-if="saving" />
        <Save :size="18" v-else />
        {{ saving ? 'Saving...' : 'Save Preferences' }}
      </button>

      <button
        v-if="hasChanges"
        @click="resetPreferences"
        :disabled="saving"
        class="px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
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
        <span>Preferences saved successfully!</span>
      </div>
    </Transition>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { apiFetch } from "../../utils/api"
import {
  Calendar,
  Clock,
  LayoutGrid,
  Save,
  CheckCircle2,
  Loader2
} from "lucide-vue-next"

const preferences = ref({
  date_format: 'MM/DD/YYYY',
  time_format: '12h',
  items_per_page: 25,
  default_sort: 'expiration_asc'
})

const originalPreferences = ref({})
const saving = ref(false)
const saveSuccess = ref(false)

const hasChanges = computed(() => {
  return JSON.stringify(preferences.value) !== JSON.stringify(originalPreferences.value)
})

const previewDate = computed(() => {
  const date = new Date(2026, 1, 14) // Feb 14, 2026
  
  switch(preferences.value.date_format) {
    case 'MM/DD/YYYY':
      return '02/14/2026'
    case 'DD/MM/YYYY':
      return '14/02/2026'
    case 'YYYY-MM-DD':
      return '2026-02-14'
    default:
      return '02/14/2026'
  }
})

const previewTime = computed(() => {
  return preferences.value.time_format === '12h' ? '2:30 PM' : '14:30'
})

onMounted(async () => {
  await loadPreferences()
})

async function loadPreferences() {
  try {
    const res = await apiFetch('/auth/preferences')
    if (res.ok) {
      const data = await res.json()
      preferences.value = {
        date_format: data.date_format ?? 'MM/DD/YYYY',
        time_format: data.time_format ?? '12h',
        items_per_page: data.items_per_page ?? 25,
        default_sort: data.default_sort ?? 'expiration_asc'
      }
      originalPreferences.value = JSON.parse(JSON.stringify(preferences.value))
    }
  } catch (err) {
    console.error('Failed to load preferences:', err)
  }
}

async function savePreferences() {
  saving.value = true
  saveSuccess.value = false
  
  try {
    const res = await apiFetch('/auth/preferences', {
      method: 'PUT',
      body: JSON.stringify(preferences.value)
    })
    
    if (!res.ok) {
      throw new Error('Failed to save preferences')
    }
    
    originalPreferences.value = JSON.parse(JSON.stringify(preferences.value))
    saveSuccess.value = true
    setTimeout(() => {
      saveSuccess.value = false
    }, 3000)
    
  } catch (err) {
    console.error('Failed to save preferences:', err)
  } finally {
    saving.value = false
  }
}

function resetPreferences() {
  preferences.value = JSON.parse(JSON.stringify(originalPreferences.value))
}
</script>