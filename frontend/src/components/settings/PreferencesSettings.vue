<template>
  <div>
    <div class="space-y-8">

      <!-- APPEARANCE SECTION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-purple-100 flex items-center justify-center flex-shrink-0">
            <Palette :size="20" class="text-purple-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Appearance</h3>
            <p class="text-sm text-gray-600 mt-1">Customize how LifeAdmin looks on your device</p>
          </div>
        </div>

        <!-- Theme Selection -->
        <div class="space-y-3">
          <label class="block text-sm font-medium text-gray-700 mb-3">Theme</label>
          
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <!-- Light Theme -->
            <button
              @click="preferences.theme = 'light'"
              :class="[
                'relative p-4 border-2 rounded-xl transition-all duration-200 text-left group',
                preferences.theme === 'light'
                  ? 'border-teal-500 bg-teal-50'
                  : 'border-gray-200 hover:border-gray-300 bg-white'
              ]"
            >
              <div class="flex items-center justify-between mb-3">
                <Sun :size="24" :class="preferences.theme === 'light' ? 'text-teal-600' : 'text-gray-400'" />
                <div v-if="preferences.theme === 'light'" class="w-5 h-5 rounded-full bg-teal-500 flex items-center justify-center">
                  <Check :size="14" class="text-white" />
                </div>
              </div>
              <p class="font-semibold text-gray-900 mb-1">Light</p>
              <p class="text-xs text-gray-600">Bright and clean interface</p>
            </button>

            <!-- Dark Theme -->
            <button
              @click="preferences.theme = 'dark'"
              :class="[
                'relative p-4 border-2 rounded-xl transition-all duration-200 text-left group',
                preferences.theme === 'dark'
                  ? 'border-teal-500 bg-teal-50'
                  : 'border-gray-200 hover:border-gray-300 bg-white'
              ]"
            >
              <div class="flex items-center justify-between mb-3">
                <Moon :size="24" :class="preferences.theme === 'dark' ? 'text-teal-600' : 'text-gray-400'" />
                <div v-if="preferences.theme === 'dark'" class="w-5 h-5 rounded-full bg-teal-500 flex items-center justify-center">
                  <Check :size="14" class="text-white" />
                </div>
              </div>
              <p class="font-semibold text-gray-900 mb-1">Dark</p>
              <p class="text-xs text-gray-600">Easy on the eyes at night</p>
            </button>

            <!-- System Theme -->
            <button
              @click="preferences.theme = 'system'"
              :class="[
                'relative p-4 border-2 rounded-xl transition-all duration-200 text-left group',
                preferences.theme === 'system'
                  ? 'border-teal-500 bg-teal-50'
                  : 'border-gray-200 hover:border-gray-300 bg-white'
              ]"
            >
              <div class="flex items-center justify-between mb-3">
                <Monitor :size="24" :class="preferences.theme === 'system' ? 'text-teal-600' : 'text-gray-400'" />
                <div v-if="preferences.theme === 'system'" class="w-5 h-5 rounded-full bg-teal-500 flex items-center justify-center">
                  <Check :size="14" class="text-white" />
                </div>
              </div>
              <p class="font-semibold text-gray-900 mb-1">System</p>
              <p class="text-xs text-gray-600">Use device settings</p>
            </button>
          </div>
        </div>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-200"></div>

      <!-- NOTIFICATIONS SECTION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-blue-100 flex items-center justify-center flex-shrink-0">
            <Bell :size="20" class="text-blue-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Notifications</h3>
            <p class="text-sm text-gray-600 mt-1">Manage how you receive notifications and alerts</p>
          </div>
        </div>

        <div class="space-y-4">
          
          <!-- Email Notifications -->
          <div class="flex items-start justify-between p-4 bg-gray-50 rounded-xl">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-1">
                <Mail :size="18" class="text-gray-600" />
                <p class="font-semibold text-gray-900">Email Notifications</p>
              </div>
              <p class="text-sm text-gray-600">Receive email alerts for important updates</p>
            </div>
            <button
              @click="preferences.notifications.email = !preferences.notifications.email"
              :class="[
                'relative w-12 h-6 rounded-full transition-colors duration-200 flex-shrink-0 ml-4',
                preferences.notifications.email ? 'bg-teal-500' : 'bg-gray-300'
              ]"
            >
              <span
                :class="[
                  'absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow-md transition-transform duration-200',
                  preferences.notifications.email ? 'translate-x-6' : 'translate-x-0'
                ]"
              ></span>
            </button>
          </div>

          <!-- Push Notifications -->
          <div class="flex items-start justify-between p-4 bg-gray-50 rounded-xl">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-1">
                <Smartphone :size="18" class="text-gray-600" />
                <p class="font-semibold text-gray-900">Push Notifications</p>
              </div>
              <p class="text-sm text-gray-600">Get instant alerts on your device</p>
            </div>
            <button
              @click="preferences.notifications.push = !preferences.notifications.push"
              :class="[
                'relative w-12 h-6 rounded-full transition-colors duration-200 flex-shrink-0 ml-4',
                preferences.notifications.push ? 'bg-teal-500' : 'bg-gray-300'
              ]"
            >
              <span
                :class="[
                  'absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow-md transition-transform duration-200',
                  preferences.notifications.push ? 'translate-x-6' : 'translate-x-0'
                ]"
              ></span>
            </button>
          </div>

          <!-- Expiration Reminders -->
          <div class="flex items-start justify-between p-4 bg-gray-50 rounded-xl">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-1">
                <Clock :size="18" class="text-gray-600" />
                <p class="font-semibold text-gray-900">Expiration Reminders</p>
              </div>
              <p class="text-sm text-gray-600">Alert me when documents are expiring soon</p>
            </div>
            <button
              @click="preferences.notifications.expiration = !preferences.notifications.expiration"
              :class="[
                'relative w-12 h-6 rounded-full transition-colors duration-200 flex-shrink-0 ml-4',
                preferences.notifications.expiration ? 'bg-teal-500' : 'bg-gray-300'
              ]"
            >
              <span
                :class="[
                  'absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow-md transition-transform duration-200',
                  preferences.notifications.expiration ? 'translate-x-6' : 'translate-x-0'
                ]"
              ></span>
            </button>
          </div>

          <!-- Subscription Reminders -->
          <div class="flex items-start justify-between p-4 bg-gray-50 rounded-xl">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-1">
                <Repeat :size="18" class="text-gray-600" />
                <p class="font-semibold text-gray-900">Subscription Reminders</p>
              </div>
              <p class="text-sm text-gray-600">Remind me before subscription renewals</p>
            </div>
            <button
              @click="preferences.notifications.subscription = !preferences.notifications.subscription"
              :class="[
                'relative w-12 h-6 rounded-full transition-colors duration-200 flex-shrink-0 ml-4',
                preferences.notifications.subscription ? 'bg-teal-500' : 'bg-gray-300'
              ]"
            >
              <span
                :class="[
                  'absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow-md transition-transform duration-200',
                  preferences.notifications.subscription ? 'translate-x-6' : 'translate-x-0'
                ]"
              ></span>
            </button>
          </div>

          <!-- Notification Timing -->
          <div class="p-4 bg-gray-50 rounded-xl">
            <label class="block text-sm font-semibold text-gray-900 mb-3">
              Remind me before expiration
            </label>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
              <button
                v-for="day in [7, 14, 30, 60]"
                :key="day"
                @click="preferences.reminderDays = day"
                :class="[
                  'px-4 py-2 rounded-lg font-medium text-sm transition-all duration-200',
                  preferences.reminderDays === day
                    ? 'bg-teal-500 text-white shadow-md'
                    : 'bg-white text-gray-700 border border-gray-200 hover:border-teal-300'
                ]"
              >
                {{ day }} days
              </button>
            </div>
          </div>

        </div>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-200"></div>

      <!-- LANGUAGE & REGION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-green-100 flex items-center justify-center flex-shrink-0">
            <Globe :size="20" class="text-green-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Language & Region</h3>
            <p class="text-sm text-gray-600 mt-1">Set your language and regional preferences</p>
          </div>
        </div>

        <div class="space-y-4">
          <!-- Language -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Language</label>
            <select
              v-model="preferences.language"
              class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-white"
            >
              <option value="en">English</option>
              <option value="es">Español</option>
              <option value="fr">Français</option>
              <option value="de">Deutsch</option>
              <option value="it">Italiano</option>
              <option value="pt">Português</option>
            </select>
          </div>

          <!-- Date Format -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Date Format</label>
            <select
              v-model="preferences.dateFormat"
              class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-white"
            >
              <option value="MM/DD/YYYY">MM/DD/YYYY (US)</option>
              <option value="DD/MM/YYYY">DD/MM/YYYY (EU)</option>
              <option value="YYYY-MM-DD">YYYY-MM-DD (ISO)</option>
            </select>
            <p class="text-xs text-gray-500 mt-2">
              Example: {{ formatDateExample(preferences.dateFormat) }}
            </p>
          </div>

          <!-- Time Format -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Time Format</label>
            <div class="flex gap-3">
              <button
                @click="preferences.timeFormat = '12h'"
                :class="[
                  'flex-1 px-4 py-3 rounded-xl font-medium transition-all duration-200',
                  preferences.timeFormat === '12h'
                    ? 'bg-teal-500 text-white shadow-md'
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                ]"
              >
                12-hour (2:30 PM)
              </button>
              <button
                @click="preferences.timeFormat = '24h'"
                :class="[
                  'flex-1 px-4 py-3 rounded-xl font-medium transition-all duration-200',
                  preferences.timeFormat === '24h'
                    ? 'bg-teal-500 text-white shadow-md'
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                ]"
              >
                24-hour (14:30)
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-200"></div>

      <!-- DATA & PRIVACY -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-indigo-100 flex items-center justify-center flex-shrink-0">
            <Shield :size="20" class="text-indigo-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Data & Privacy</h3>
            <p class="text-sm text-gray-600 mt-1">Control your data and privacy settings</p>
          </div>
        </div>

        <div class="space-y-4">
          
          <!-- Analytics -->
          <div class="flex items-start justify-between p-4 bg-gray-50 rounded-xl">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-1">
                <BarChart3 :size="18" class="text-gray-600" />
                <p class="font-semibold text-gray-900">Analytics</p>
              </div>
              <p class="text-sm text-gray-600">Help improve LifeAdmin by sharing usage data</p>
            </div>
            <button
              @click="preferences.analytics = !preferences.analytics"
              :class="[
                'relative w-12 h-6 rounded-full transition-colors duration-200 flex-shrink-0 ml-4',
                preferences.analytics ? 'bg-teal-500' : 'bg-gray-300'
              ]"
            >
              <span
                :class="[
                  'absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow-md transition-transform duration-200',
                  preferences.analytics ? 'translate-x-6' : 'translate-x-0'
                ]"
              ></span>
            </button>
          </div>

          <!-- Auto-save -->
          <div class="flex items-start justify-between p-4 bg-gray-50 rounded-xl">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-1">
                <Save :size="18" class="text-gray-600" />
                <p class="font-semibold text-gray-900">Auto-save</p>
              </div>
              <p class="text-sm text-gray-600">Automatically save changes as you type</p>
            </div>
            <button
              @click="preferences.autoSave = !preferences.autoSave"
              :class="[
                'relative w-12 h-6 rounded-full transition-colors duration-200 flex-shrink-0 ml-4',
                preferences.autoSave ? 'bg-teal-500' : 'bg-gray-300'
              ]"
            >
              <span
                :class="[
                  'absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow-md transition-transform duration-200',
                  preferences.autoSave ? 'translate-x-6' : 'translate-x-0'
                ]"
              ></span>
            </button>
          </div>

        </div>
      </div>

      <!-- SAVE BUTTON -->
      <div class="flex items-center gap-3 pt-4">
        <button
          @click="savePreferences"
          :disabled="saving"
          class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
        >
          <Loader2 :size="18" class="animate-spin" v-if="saving" />
          <Check :size="18" v-else />
          {{ saving ? 'Saving...' : 'Save Preferences' }}
        </button>

        <button
          @click="resetPreferences"
          class="px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
        >
          Reset to Defaults
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
  </div>
</template>

<script setup>
import { ref } from "vue"
import {
  Palette,
  Sun,
  Moon,
  Monitor,
  Bell,
  Mail,
  Smartphone,
  Clock,
  Repeat,
  Globe,
  Shield,
  BarChart3,
  Save,
  Check,
  CheckCircle2,
  Loader2
} from "lucide-vue-next"

const defaultPreferences = {
  theme: 'light',
  notifications: {
    email: true,
    push: true,
    expiration: true,
    subscription: true
  },
  reminderDays: 7,
  language: 'en',
  dateFormat: 'MM/DD/YYYY',
  timeFormat: '12h',
  analytics: true,
  autoSave: true
}

const preferences = ref({ ...defaultPreferences })
const saving = ref(false)
const saveSuccess = ref(false)

function formatDateExample(format) {
  const date = new Date(2026, 1, 14) // Feb 14, 2026
  
  switch(format) {
    case 'MM/DD/YYYY':
      return '02/14/2026'
    case 'DD/MM/YYYY':
      return '14/02/2026'
    case 'YYYY-MM-DD':
      return '2026-02-14'
    default:
      return '02/14/2026'
  }
}

async function savePreferences() {
  saving.value = true
  
  try {
    // TODO: Add your API call here
    await new Promise(resolve => setTimeout(resolve, 1000)) // Simulated API call
    
    saveSuccess.value = true
    setTimeout(() => {
      saveSuccess.value = false
    }, 3000)
  } catch (error) {
    console.error('Failed to save preferences:', error)
  } finally {
    saving.value = false
  }
}

function resetPreferences() {
  if (confirm('Are you sure you want to reset all preferences to defaults?')) {
    preferences.value = { ...defaultPreferences }
  }
}
</script>

<style scoped>
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>