<template>
  <div class="space-y-8">

    <!-- Loading State -->
    <div v-if="loading" class="flex items-center justify-center py-12">
      <Loader2 :size="32" class="animate-spin text-teal-500" />
    </div>

    <div v-else>

      <!-- EMAIL NOTIFICATIONS -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-teal-100 flex items-center justify-center flex-shrink-0">
            <Bell :size="20" class="text-teal-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Email Notifications</h3>
            <p class="text-sm text-gray-600 mt-1">Manage how you receive notifications</p>
          </div>
        </div>

        <div class="space-y-4">
          
          <!-- Master Toggle -->
          <div class="flex items-center justify-between p-4 bg-gradient-to-r from-teal-50 to-cyan-50 rounded-xl border border-teal-200">
            <div>
              <p class="font-semibold text-gray-900">Email Notifications</p>
              <p class="text-sm text-gray-600 mt-0.5">Receive alerts about expiring items</p>
            </div>
            <button
              @click="toggleEmailNotifications"
              :class="[
                'relative w-12 h-6 rounded-full transition-colors duration-200 flex-shrink-0',
                settings.email_notifications_enabled ? 'bg-teal-500' : 'bg-gray-300'
              ]"
            >
              <span
                :class="[
                  'absolute top-0.5 left-0.5 w-5 h-5 bg-white rounded-full shadow-md transition-transform duration-200',
                  settings.email_notifications_enabled ? 'translate-x-6' : 'translate-x-0'
                ]"
              ></span>
            </button>
          </div>

          <!-- Notification Timing -->
          <Transition
            enter-active-class="transition-all duration-200 ease-out"
            enter-from-class="opacity-0 -translate-y-2"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition-all duration-150 ease-in"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 -translate-y-2"
          >
            <div v-if="settings.email_notifications_enabled" class="space-y-3">
              <p class="text-sm font-medium text-gray-700">Notify me when items expire in:</p>
              
              <div class="grid grid-cols-3 gap-3">
                <button
                  v-for="days in [7, 14, 30]"
                  :key="days"
                  @click="settings.notification_days = days"
                  :class="[
                    'px-4 py-3 rounded-xl font-medium transition-all duration-200 border-2',
                    settings.notification_days === days
                      ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white border-teal-500 shadow-lg'
                      : 'bg-white text-gray-700 border-gray-200 hover:border-teal-300'
                  ]"
                >
                  {{ days }} days
                </button>
              </div>

              <!-- Test Email Button -->
              <button
                @click="sendTestEmail"
                :disabled="sendingTest"
                class="w-full px-4 py-3 bg-white border-2 border-gray-200 text-gray-700 rounded-xl font-medium hover:border-teal-300 hover:bg-teal-50 transition-all duration-200 flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <Loader2 :size="18" class="animate-spin" v-if="sendingTest" />
                <Mail :size="18" v-else />
                {{ sendingTest ? 'Sending...' : 'Send Test Email' }}
              </button>
            </div>
          </Transition>

        </div>
      </div>

      <!-- SAVE BUTTON -->
      <div class="flex items-center gap-3 pt-4">
        <button
          @click="saveSettings"
          :disabled="saving || !hasChanges"
          class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
        >
          <Loader2 :size="18" class="animate-spin" v-if="saving" />
          <Save :size="18" v-else />
          {{ saving ? 'Saving...' : 'Save Changes' }}
        </button>

        <button
          v-if="hasChanges"
          @click="resetSettings"
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
          <span>Settings saved successfully!</span>
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
        <div v-if="error" class="flex items-center gap-2 p-4 bg-red-50 border border-red-200 rounded-xl text-red-800 text-sm">
          <AlertCircle :size="18" class="text-red-600" />
          <span>{{ error }}</span>
        </div>
      </Transition>

      <!-- Test Email Success -->
      <Transition
        enter-active-class="transition-all duration-200 ease-out"
        enter-from-class="opacity-0 translate-y-2"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition-all duration-150 ease-in"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 translate-y-2"
      >
        <div v-if="testEmailSent" class="flex items-center gap-2 p-4 bg-blue-50 border border-blue-200 rounded-xl text-blue-800 text-sm">
          <Mail :size="18" class="text-blue-600" />
          <span>Test email sent! Check your inbox.</span>
        </div>
      </Transition>

    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { apiFetch } from "../../utils/api"
import {
  Bell,
  Mail,
  Save,
  CheckCircle2,
  AlertCircle,
  Loader2
} from "lucide-vue-next"

const settings = ref({
  email_notifications_enabled: true,
  notification_days: 7
})

const originalSettings = ref({})
const loading = ref(true)
const saving = ref(false)
const saveSuccess = ref(false)
const error = ref('')
const sendingTest = ref(false)
const testEmailSent = ref(false)

const hasChanges = computed(() => {
  return JSON.stringify(settings.value) !== JSON.stringify(originalSettings.value)
})

onMounted(async () => {
  await loadSettings()
})

async function loadSettings() {
  loading.value = true
  error.value = ''
  
  try {
    const res = await apiFetch('/auth/settings')
    
    if (!res.ok) {
      throw new Error('Failed to load settings')
    }
    
    const data = await res.json()
    settings.value = {
      email_notifications_enabled: data.email_notifications_enabled ?? true,
      notification_days: data.notification_days ?? 7
    }
    originalSettings.value = JSON.parse(JSON.stringify(settings.value))
    
  } catch (err) {
    console.error('Failed to load settings:', err)
    error.value = 'Failed to load settings. Using defaults.'
    setTimeout(() => {
      error.value = ''
    }, 5000)
  } finally {
    loading.value = false
  }
}

async function saveSettings() {
  saving.value = true
  saveSuccess.value = false
  error.value = ''
  
  try {
    const res = await apiFetch('/auth/settings', {
      method: 'PUT',
      body: JSON.stringify(settings.value)
    })
    
    if (!res.ok) {
      throw new Error('Failed to save settings')
    }
    
    originalSettings.value = JSON.parse(JSON.stringify(settings.value))
    saveSuccess.value = true
    setTimeout(() => {
      saveSuccess.value = false
    }, 3000)
    
  } catch (err) {
    console.error('Failed to save settings:', err)
    error.value = 'Failed to save settings. Please try again.'
    setTimeout(() => {
      error.value = ''
    }, 5000)
  } finally {
    saving.value = false
  }
}

function resetSettings() {
  settings.value = JSON.parse(JSON.stringify(originalSettings.value))
}

function toggleEmailNotifications() {
  settings.value.email_notifications_enabled = !settings.value.email_notifications_enabled
}

async function sendTestEmail() {
  sendingTest.value = true
  testEmailSent.value = false
  error.value = ''
  
  try {
    const res = await apiFetch('/notifications/test-email', {
      method: 'POST'
    })
    
    if (!res.ok) {
      throw new Error('Failed to send test email')
    }
    
    testEmailSent.value = true
    setTimeout(() => {
      testEmailSent.value = false
    }, 5000)
    
  } catch (err) {
    console.error('Failed to send test email:', err)
    error.value = 'Test email feature not yet implemented.'
    setTimeout(() => {
      error.value = ''
    }, 5000)
  } finally {
    sendingTest.value = false
  }
}
</script>