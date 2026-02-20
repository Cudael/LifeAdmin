<template>
  <div class="space-y-10">

    <!-- Loading State -->
    <div v-if="loading" class="flex flex-col items-center justify-center py-20">
      <div class="w-16 h-16 bg-cyan-500/10 rounded-2xl flex items-center justify-center mb-4 border border-cyan-500/20 shadow-inner">
        <Loader2 :size="32" class="animate-spin text-cyan-400" />
      </div>
      <p class="text-slate-400 font-medium tracking-wide">Loading configuration...</p>
    </div>

    <div v-else class="space-y-10">

      <!-- EMAIL NOTIFICATIONS -->
      <div>
        <h3 class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-6 ml-1">Communication Channels</h3>

        <div class="space-y-6">
          
          <!-- Master Toggle -->
          <div class="flex items-center justify-between p-5 bg-slate-950/50 rounded-2xl border border-white/5 shadow-inner">
            <div class="flex items-center gap-4">
              <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400 shrink-0">
                <Mail :size="20" />
              </div>
              <div>
                <p class="font-bold text-white text-lg tracking-tight">Email Alerts</p>
                <p class="text-xs font-medium text-slate-500 mt-0.5">Receive warnings about expiring documents & subscriptions.</p>
              </div>
            </div>
            
            <!-- Sleek iOS Style Toggle -->
            <button
              @click="toggleEmailNotifications"
              class="relative w-14 h-8 rounded-full transition-colors duration-300 flex-shrink-0 focus:outline-none focus:ring-2 focus:ring-cyan-500/50"
              :class="settings.email_notifications_enabled ? 'bg-cyan-500 shadow-[0_0_15px_rgba(34,211,238,0.5)]' : 'bg-slate-700'"
            >
              <span
                class="absolute top-1 left-1 w-6 h-6 bg-white rounded-full shadow-md transition-transform duration-300"
                :class="settings.email_notifications_enabled ? 'translate-x-6' : 'translate-x-0'"
              ></span>
            </button>
          </div>

          <!-- Notification Timing -->
          <Transition
            enter-active-class="transition-all duration-300 ease-out"
            enter-from-class="opacity-0 -translate-y-4 scale-[0.98]"
            enter-to-class="opacity-100 translate-y-0 scale-100"
            leave-active-class="transition-all duration-200 ease-in"
            leave-from-class="opacity-100 translate-y-0 scale-100"
            leave-to-class="opacity-0 -translate-y-4 scale-[0.98]"
          >
            <div v-if="settings.email_notifications_enabled" class="p-6 bg-slate-950/30 rounded-2xl border border-white/5 space-y-6">
              
              <div>
                <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-3">
                  Default Notification Lead Time
                </label>
                
                <!-- Segmented Control -->
                <div class="flex flex-wrap sm:flex-nowrap gap-2 p-1.5 bg-slate-900 rounded-xl border border-white/5 shadow-inner">
                  <button
                    v-for="days in [7, 14, 30]"
                    :key="days"
                    @click="settings.notification_days = days"
                    class="flex-1 py-2.5 rounded-lg text-sm font-bold transition-all duration-300"
                    :class="settings.notification_days === days
                      ? 'bg-cyan-500 text-slate-950 shadow-[0_0_15px_rgba(34,211,238,0.3)]'
                      : 'text-slate-400 hover:text-white hover:bg-white/5'"
                  >
                    {{ days }} Days Prior
                  </button>
                </div>
              </div>

              <div class="h-px w-full bg-white/5"></div>

              <!-- Test Email Button -->
              <div class="flex items-center justify-between">
                <div>
                  <p class="text-sm font-bold text-slate-300">Verify Connection</p>
                  <p class="text-xs font-medium text-slate-500 mt-0.5">Send a test ping to your registered email.</p>
                </div>
                <button
                  @click="sendTestEmail"
                  :disabled="sendingTest"
                  class="px-5 py-2.5 bg-slate-800 hover:bg-slate-700 border border-white/5 text-white rounded-xl font-bold transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                >
                  <Loader2 :size="16" class="animate-spin" v-if="sendingTest" />
                  <Send :size="16" v-else class="text-cyan-400" />
                  {{ sendingTest ? 'Sending...' : 'Send Test' }}
                </button>
              </div>
            </div>
          </Transition>

        </div>
      </div>

      <!-- SAVE BUTTONS -->
      <div class="flex items-center gap-4 pt-4 border-t border-white/5">
        <button
          @click="saveSettings"
          :disabled="saving || !hasChanges"
          class="group px-6 py-3.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(34,211,238,0.2)] hover:shadow-[0_0_30px_rgba(34,211,238,0.4)] transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
        >
          <Loader2 :size="18" class="animate-spin" v-if="saving" />
          <Save :size="18" class="group-hover:scale-110 transition-transform" v-else />
          {{ saving ? 'Saving...' : 'Save Configuration' }}
        </button>

        <button
          v-if="hasChanges"
          @click="resetSettings"
          :disabled="saving"
          class="px-6 py-3.5 bg-white/5 hover:bg-white/10 border border-white/5 text-white rounded-xl font-bold transition-all duration-200 disabled:opacity-50"
        >
          Discard Changes
        </button>
      </div>

      <!-- ALERTS -->
      <div class="space-y-3">
        <Transition enter-active-class="transition-all duration-300" enter-from-class="opacity-0 translate-y-2 scale-95" leave-active-class="transition-all duration-200" leave-to-class="opacity-0 translate-y-2 scale-95">
          <div v-if="saveSuccess" class="flex items-center gap-3 p-4 bg-emerald-500/10 border border-emerald-500/20 rounded-xl shadow-inner">
            <div class="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400 shrink-0"><CheckCircle2 :size="16" /></div>
            <span class="text-sm font-bold text-emerald-300">Notification preferences saved successfully.</span>
          </div>
        </Transition>

        <Transition enter-active-class="transition-all duration-300" enter-from-class="opacity-0 translate-y-2 scale-95" leave-active-class="transition-all duration-200" leave-to-class="opacity-0 translate-y-2 scale-95">
          <div v-if="testEmailSent" class="flex items-center gap-3 p-4 bg-blue-500/10 border border-blue-500/20 rounded-xl shadow-inner">
            <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center text-blue-400 shrink-0"><Mail :size="16" /></div>
            <span class="text-sm font-bold text-blue-300">Test ping deployed. Please check your inbox.</span>
          </div>
        </Transition>

        <Transition enter-active-class="transition-all duration-300" enter-from-class="opacity-0 translate-y-2 scale-95" leave-active-class="transition-all duration-200" leave-to-class="opacity-0 translate-y-2 scale-95">
          <div v-if="error" class="flex items-center gap-3 p-4 bg-rose-500/10 border border-rose-500/20 rounded-xl shadow-inner">
            <div class="w-8 h-8 rounded-full bg-rose-500/20 flex items-center justify-center text-rose-400 shrink-0"><AlertCircle :size="16" /></div>
            <span class="text-sm font-bold text-rose-300">{{ error }}</span>
          </div>
        </Transition>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { apiFetch } from "../../utils/api"
import { Mail, Send, Save, CheckCircle2, AlertCircle, Loader2 } from "lucide-vue-next"

const settings = ref({ email_notifications_enabled: true, notification_days: 7 })
const originalSettings = ref({})
const loading = ref(true)
const saving = ref(false)
const saveSuccess = ref(false)
const error = ref('')
const sendingTest = ref(false)
const testEmailSent = ref(false)

const hasChanges = computed(() => JSON.stringify(settings.value) !== JSON.stringify(originalSettings.value))

onMounted(async () => { await loadSettings() })

async function loadSettings() {
  loading.value = true; error.value = ''
  try {
    const res = await apiFetch('/auth/settings')
    if (!res.ok) throw new Error('Failed to load settings')
    const data = await res.json()
    settings.value = {
      email_notifications_enabled: data.email_notifications_enabled ?? true,
      notification_days: data.notification_days ?? 7
    }
    originalSettings.value = JSON.parse(JSON.stringify(settings.value))
  } catch (err) {
    error.value = 'Failed to load settings. Using defaults.'
    setTimeout(() => { error.value = '' }, 5000)
  } finally {
    loading.value = false
  }
}

async function saveSettings() {
  saving.value = true; saveSuccess.value = false; error.value = ''
  try {
    const res = await apiFetch('/auth/settings', { method: 'PUT', body: JSON.stringify(settings.value) })
    if (!res.ok) throw new Error('Failed to save settings')
    originalSettings.value = JSON.parse(JSON.stringify(settings.value))
    saveSuccess.value = true
    setTimeout(() => { saveSuccess.value = false }, 3000)
  } catch (err) {
    error.value = 'Failed to save settings. Please try again.'
    setTimeout(() => { error.value = '' }, 5000)
  } finally {
    saving.value = false
  }
}

function resetSettings() { settings.value = JSON.parse(JSON.stringify(originalSettings.value)) }
function toggleEmailNotifications() { settings.value.email_notifications_enabled = !settings.value.email_notifications_enabled }

async function sendTestEmail() {
  sendingTest.value = true; testEmailSent.value = false; error.value = ''
  try {
    const res = await apiFetch('/notifications/test-email', { method: 'POST' })
    if (!res.ok) throw new Error('Failed to send test email')
    testEmailSent.value = true
    setTimeout(() => { testEmailSent.value = false }, 5000)
  } catch (err) {
    error.value = 'Test email feature not yet implemented.'
    setTimeout(() => { error.value = '' }, 5000)
  } finally {
    sendingTest.value = false
  }
}
</script>