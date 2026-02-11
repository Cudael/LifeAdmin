<template>
  <div>
    <div class="space-y-8">

      <!-- TWO-FACTOR AUTHENTICATION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-green-100 flex items-center justify-center flex-shrink-0">
            <Shield :size="20" class="text-green-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Two-Factor Authentication</h3>
            <p class="text-sm text-gray-600 mt-1">Add an extra layer of security to your account</p>
          </div>
        </div>

        <div class="bg-gradient-to-br from-green-50 to-emerald-50 border-2 border-green-200 rounded-xl p-6">
          <div class="flex items-start justify-between gap-4 mb-4">
            <div class="flex-1">
              <div class="flex items-center gap-2 mb-2">
                <h4 class="font-bold text-gray-900">
                  {{ twoFactorEnabled ? 'Two-Factor Authentication Enabled' : 'Enable Two-Factor Authentication' }}
                </h4>
                <span v-if="twoFactorEnabled" class="px-2 py-1 bg-green-500 text-white text-xs font-semibold rounded-full flex items-center gap-1">
                  <CheckCircle2 :size="12" />
                  Active
                </span>
              </div>
              <p class="text-sm text-gray-600 mb-3">
                {{ twoFactorEnabled 
                  ? 'Your account is protected with two-factor authentication.' 
                  : 'Protect your account with an additional security layer. You\'ll need to enter a code from your phone when signing in.'
                }}
              </p>
              
              <ul v-if="!twoFactorEnabled" class="text-xs text-gray-600 space-y-1">
                <li class="flex items-center gap-2">
                  <CheckCircle2 :size="14" class="text-green-600" />
                  Prevents unauthorized access
                </li>
                <li class="flex items-center gap-2">
                  <CheckCircle2 :size="14" class="text-green-600" />
                  Works with authenticator apps
                </li>
                <li class="flex items-center gap-2">
                  <CheckCircle2 :size="14" class="text-green-600" />
                  Backup codes provided
                </li>
              </ul>
            </div>
          </div>

          <div class="flex gap-3">
            <button
              v-if="!twoFactorEnabled"
              @click="showSetup2FA = true"
              class="px-5 py-2.5 bg-green-600 text-white rounded-xl font-semibold hover:bg-green-700 transition-all duration-200 shadow-md hover:shadow-lg flex items-center gap-2"
            >
              <ShieldCheck :size="18" />
              Enable 2FA
            </button>

            <button
              v-else
              @click="showDisable2FA = true"
              class="px-5 py-2.5 bg-red-600 text-white rounded-xl font-semibold hover:bg-red-700 transition-all duration-200 shadow-md hover:shadow-lg flex items-center gap-2"
            >
              <ShieldOff :size="18" />
              Disable 2FA
            </button>

            <button
              v-if="twoFactorEnabled"
              @click="showBackupCodes = true"
              class="px-5 py-2.5 bg-white border-2 border-green-600 text-green-600 rounded-xl font-semibold hover:bg-green-50 transition-all duration-200"
            >
              View Backup Codes
            </button>
          </div>
        </div>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-200"></div>

      <!-- ACTIVE SESSIONS -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-blue-100 flex items-center justify-center flex-shrink-0">
            <Laptop :size="20" class="text-blue-600" />
          </div>
          <div class="flex-1">
            <div class="flex items-center justify-between">
              <div>
                <h3 class="text-lg font-bold text-gray-900">Active Sessions</h3>
                <p class="text-sm text-gray-600 mt-1">Manage devices where you're currently logged in</p>
              </div>
              <button
                @click="loadSessions"
                :disabled="loadingSessions"
                class="text-teal-600 hover:text-teal-700 font-medium text-sm flex items-center gap-1"
              >
                <RefreshCw :size="16" :class="{ 'animate-spin': loadingSessions }" />
                Refresh
              </button>
            </div>
          </div>
        </div>

        <div class="space-y-3">
          <div
            v-for="session in sessions"
            :key="session.id"
            class="p-4 bg-gray-50 border border-gray-200 rounded-xl hover:border-gray-300 transition-colors"
          >
            <div class="flex items-start justify-between gap-4">
              <div class="flex items-start gap-3 flex-1">
                <!-- Device Icon -->
                <div class="w-10 h-10 rounded-lg bg-white border border-gray-200 flex items-center justify-center flex-shrink-0">
                  <Smartphone v-if="session.device_type === 'mobile'" :size="20" class="text-gray-600" />
                  <Tablet v-else-if="session.device_type === 'tablet'" :size="20" class="text-gray-600" />
                  <Laptop v-else :size="20" class="text-gray-600" />
                </div>

                <div class="flex-1">
                  <div class="flex items-center gap-2 mb-1">
                    <p class="font-semibold text-gray-900">{{ session.browser }} on {{ session.os }}</p>
                    <span v-if="session.is_current" class="px-2 py-0.5 bg-teal-100 text-teal-700 text-xs font-semibold rounded-full">
                      Current
                    </span>
                  </div>
                  
                  <div class="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-gray-600">
                    <span class="flex items-center gap-1">
                      <MapPin :size="12" />
                      {{ session.location }}
                    </span>
                    <span class="flex items-center gap-1">
                      <Globe :size="12" />
                      {{ session.ip_address }}
                    </span>
                    <span class="flex items-center gap-1">
                      <Clock :size="12" />
                      Last active {{ formatRelativeTime(session.last_active) }}
                    </span>
                  </div>
                </div>
              </div>

              <button
                v-if="!session.is_current"
                @click="revokeSession(session.id)"
                class="px-3 py-1.5 text-red-600 hover:bg-red-50 border border-red-200 rounded-lg text-sm font-medium transition-colors flex-shrink-0"
              >
                Revoke
              </button>
            </div>
          </div>

          <!-- No Sessions -->
          <div v-if="sessions.length === 0" class="text-center py-12">
            <Laptop :size="48" class="text-gray-300 mx-auto mb-3" />
            <p class="text-gray-500 text-sm">No active sessions found</p>
          </div>
        </div>

        <!-- Revoke All Button -->
        <div v-if="sessions.length > 1" class="mt-4">
          <button
            @click="showRevokeAll = true"
            class="w-full px-4 py-3 bg-red-50 text-red-600 border border-red-200 rounded-xl font-semibold hover:bg-red-100 transition-all duration-200"
          >
            Revoke All Other Sessions
          </button>
        </div>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-200"></div>

      <!-- LOGIN HISTORY -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-purple-100 flex items-center justify-center flex-shrink-0">
            <History :size="20" class="text-purple-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Login History</h3>
            <p class="text-sm text-gray-600 mt-1">Recent login attempts to your account</p>
          </div>
        </div>

        <div class="space-y-2">
          <div
            v-for="login in loginHistory"
            :key="login.id"
            class="p-4 bg-gray-50 border border-gray-200 rounded-xl"
          >
            <div class="flex items-start justify-between gap-4">
              <div class="flex items-start gap-3 flex-1">
                <div :class="[
                  'w-2 h-2 rounded-full mt-2',
                  login.success ? 'bg-green-500' : 'bg-red-500'
                ]"></div>
                
                <div class="flex-1">
                  <div class="flex items-center gap-2 mb-1">
                    <p class="font-semibold text-gray-900">
                      {{ login.success ? 'Successful login' : 'Failed login attempt' }}
                    </p>
                    <span v-if="!login.success" class="px-2 py-0.5 bg-red-100 text-red-700 text-xs font-semibold rounded-full">
                      Failed
                    </span>
                  </div>
                  
                  <div class="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-gray-600">
                    <span>{{ formatDateTime(login.timestamp) }}</span>
                    <span class="flex items-center gap-1">
                      <MapPin :size="12" />
                      {{ login.location }}
                    </span>
                    <span class="flex items-center gap-1">
                      <Globe :size="12" />
                      {{ login.ip_address }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- No History -->
          <div v-if="loginHistory.length === 0" class="text-center py-12">
            <History :size="48" class="text-gray-300 mx-auto mb-3" />
            <p class="text-gray-500 text-sm">No login history available</p>
          </div>
        </div>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-200"></div>

      <!-- SECURITY RECOMMENDATIONS -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-orange-100 flex items-center justify-center flex-shrink-0">
            <AlertTriangle :size="20" class="text-orange-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Security Recommendations</h3>
            <p class="text-sm text-gray-600 mt-1">Improve your account security</p>
          </div>
        </div>

        <div class="space-y-3">
          
          <div v-if="!twoFactorEnabled" class="p-4 bg-orange-50 border-2 border-orange-200 rounded-xl">
            <div class="flex items-start gap-3">
              <AlertTriangle :size="20" class="text-orange-600 flex-shrink-0 mt-0.5" />
              <div class="flex-1">
                <p class="font-semibold text-gray-900 mb-1">Enable Two-Factor Authentication</p>
                <p class="text-sm text-gray-600 mb-3">
                  Protect your account with an additional layer of security
                </p>
                <button
                  @click="showSetup2FA = true"
                  class="text-orange-600 hover:text-orange-700 font-medium text-sm flex items-center gap-1"
                >
                  Set up now →
                </button>
              </div>
            </div>
          </div>

          <div v-if="securityScore < 80" class="p-4 bg-yellow-50 border-2 border-yellow-200 rounded-xl">
            <div class="flex items-start gap-3">
              <ShieldAlert :size="20" class="text-yellow-600 flex-shrink-0 mt-0.5" />
              <div class="flex-1">
                <p class="font-semibold text-gray-900 mb-1">Update Your Password</p>
                <p class="text-sm text-gray-600 mb-3">
                  Your password was last changed {{ passwordLastChanged }}. Consider updating it regularly.
                </p>
                <RouterLink
                  to="/settings?tab=account"
                  class="text-yellow-600 hover:text-yellow-700 font-medium text-sm flex items-center gap-1"
                >
                  Change password →
                </RouterLink>
              </div>
            </div>
          </div>

          <div v-if="securityScore >= 80" class="p-4 bg-green-50 border-2 border-green-200 rounded-xl">
            <div class="flex items-start gap-3">
              <ShieldCheck :size="20" class="text-green-600 flex-shrink-0 mt-0.5" />
              <div class="flex-1">
                <p class="font-semibold text-gray-900 mb-1">Great! Your account is secure</p>
                <p class="text-sm text-gray-600">
                  You're following security best practices. Keep it up!
                </p>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>

    <!-- 2FA SETUP MODAL -->
    <Transition
      enter-active-class="transition-all duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-150 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="showSetup2FA"
        class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
        @click.self="showSetup2FA = false"
      >
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-6 space-y-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center">
                <ShieldCheck :size="24" class="text-green-600" />
              </div>
              <div>
                <h3 class="text-xl font-bold text-gray-900">Enable 2FA</h3>
                <p class="text-sm text-gray-600">Secure your account</p>
              </div>
            </div>
            <button @click="showSetup2FA = false" class="text-gray-400 hover:text-gray-600">
              <X :size="24" />
            </button>
          </div>

          <div class="space-y-4">
            <div v-if="setup2FAStep === 1">
              <p class="text-sm text-gray-700 mb-4">
                Scan this QR code with your authenticator app (Google Authenticator, Authy, etc.)
              </p>
              
              <!-- QR Code Placeholder -->
              <div class="bg-gray-100 rounded-xl p-8 flex items-center justify-center">
                <div class="w-48 h-48 bg-white rounded-lg flex items-center justify-center border-4 border-gray-200">
                  <QrCode :size="160" class="text-gray-400" />
                </div>
              </div>

              <div class="mt-4 p-3 bg-gray-50 rounded-lg">
                <p class="text-xs text-gray-600 mb-2">Or enter this code manually:</p>
                <code class="block text-center font-mono text-sm font-bold text-gray-900 select-all">
                  JBSWY3DPEHPK3PXP
                </code>
              </div>
            </div>

            <div v-if="setup2FAStep === 2">
              <p class="text-sm text-gray-700 mb-4">
                Enter the 6-digit code from your authenticator app:
              </p>
              
              <input
                v-model="verify2FACode"
                type="text"
                maxlength="6"
                class="w-full px-4 py-3 border-2 border-gray-300 rounded-xl text-center text-2xl font-mono tracking-widest focus:ring-2 focus:ring-green-500 focus:border-transparent"
                placeholder="000000"
              />

              <div class="mt-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
                <p class="text-xs text-blue-800 flex items-start gap-2">
                  <Info :size="14" class="flex-shrink-0 mt-0.5" />
                  Save your backup codes after enabling 2FA. You'll need them if you lose access to your authenticator app.
                </p>
              </div>
            </div>
          </div>

          <div class="flex gap-3">
            <button
              v-if="setup2FAStep === 1"
              @click="setup2FAStep = 2"
              class="flex-1 px-4 py-3 bg-green-600 text-white rounded-xl font-semibold hover:bg-green-700 transition-all duration-200"
            >
              Continue
            </button>

            <button
              v-if="setup2FAStep === 2"
              @click="enable2FA"
              :disabled="verify2FACode.length !== 6 || enabling2FA"
              class="flex-1 px-4 py-3 bg-green-600 text-white rounded-xl font-semibold hover:bg-green-700 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <Loader2 :size="18" class="animate-spin" v-if="enabling2FA" />
              Enable 2FA
            </button>

            <button
              @click="showSetup2FA = false; setup2FAStep = 1; verify2FACode = ''"
              class="px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- DISABLE 2FA MODAL -->
    <Transition
      enter-active-class="transition-all duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-150 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="showDisable2FA"
        class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
        @click.self="showDisable2FA = false"
      >
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-6 space-y-4">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-full bg-red-100 flex items-center justify-center">
              <ShieldOff :size="24" class="text-red-600" />
            </div>
            <div>
              <h3 class="text-xl font-bold text-gray-900">Disable 2FA?</h3>
              <p class="text-sm text-gray-600">This will reduce your account security</p>
            </div>
          </div>

          <div class="bg-red-50 border border-red-200 rounded-xl p-4">
            <p class="text-sm text-gray-700 mb-3">
              Enter the 6-digit code from your authenticator app to confirm:
            </p>
            <input
              v-model="disable2FACode"
              type="text"
              maxlength="6"
              class="w-full px-4 py-3 border-2 border-red-300 rounded-xl text-center text-2xl font-mono tracking-widest focus:ring-2 focus:ring-red-500 focus:border-transparent"
              placeholder="000000"
            />
          </div>

          <div class="flex gap-3">
            <button
              @click="disable2FA"
              :disabled="disable2FACode.length !== 6 || disabling2FA"
              class="flex-1 px-4 py-3 bg-red-600 text-white rounded-xl font-semibold hover:bg-red-700 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <Loader2 :size="18" class="animate-spin" v-if="disabling2FA" />
              Yes, Disable 2FA
            </button>

            <button
              @click="showDisable2FA = false; disable2FACode = ''"
              class="px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- BACKUP CODES MODAL -->
    <Transition
      enter-active-class="transition-all duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-150 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="showBackupCodes"
        class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
        @click.self="showBackupCodes = false"
      >
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-6 space-y-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center">
                <Key :size="24" class="text-blue-600" />
              </div>
              <div>
                <h3 class="text-xl font-bold text-gray-900">Backup Codes</h3>
                <p class="text-sm text-gray-600">Save these in a safe place</p>
              </div>
            </div>
            <button @click="showBackupCodes = false" class="text-gray-400 hover:text-gray-600">
              <X :size="24" />
            </button>
          </div>

          <div class="bg-yellow-50 border border-yellow-200 rounded-xl p-4">
            <p class="text-xs text-yellow-800 flex items-start gap-2">
              <AlertTriangle :size="14" class="flex-shrink-0 mt-0.5" />
              Each code can only be used once. Store them securely.
            </p>
          </div>

          <div class="bg-gray-50 rounded-xl p-4">
            <div class="grid grid-cols-2 gap-2">
              <code v-for="code in backupCodes" :key="code" class="block p-2 bg-white rounded border border-gray-200 text-center font-mono text-sm font-semibold text-gray-900">
                {{ code }}
              </code>
            </div>
          </div>

          <div class="flex gap-3">
            <button
              @click="downloadBackupCodes"
              class="flex-1 px-4 py-3 bg-teal-500 text-white rounded-xl font-semibold hover:bg-teal-600 transition-all duration-200 flex items-center justify-center gap-2"
            >
              <Download :size="18" />
              Download Codes
            </button>

            <button
              @click="copyBackupCodes"
              class="px-4 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200 flex items-center gap-2"
            >
              <Copy :size="18" />
              Copy
            </button>
          </div>
        </div>
      </div>
    </Transition>

    <!-- REVOKE ALL SESSIONS MODAL -->
    <Transition
      enter-active-class="transition-all duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-150 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="showRevokeAll"
        class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
        @click.self="showRevokeAll = false"
      >
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-6 space-y-4">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-full bg-red-100 flex items-center justify-center">
              <AlertTriangle :size="24" class="text-red-600" />
            </div>
            <div>
              <h3 class="text-xl font-bold text-gray-900">Revoke All Sessions?</h3>
              <p class="text-sm text-gray-600">This will log you out everywhere except this device</p>
            </div>
          </div>

          <p class="text-sm text-gray-700">
            All other devices will be signed out immediately. You'll need to log in again on those devices.
          </p>

          <div class="flex gap-3">
            <button
              @click="revokeAllSessions"
              :disabled="revokingAll"
              class="flex-1 px-4 py-3 bg-red-600 text-white rounded-xl font-semibold hover:bg-red-700 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <Loader2 :size="18" class="animate-spin" v-if="revokingAll" />
              Yes, Revoke All
            </button>

            <button
              @click="showRevokeAll = false"
              class="px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { apiFetch } from "../../utils/api"
import {
  Shield,
  ShieldCheck,
  ShieldOff,
  ShieldAlert,
  Laptop,
  Smartphone,
  Tablet,
  RefreshCw,
  MapPin,
  Globe,
  Clock,
  History,
  AlertTriangle,
  CheckCircle2,
  Loader2,
  QrCode,
  X,
  Info,
  Key,
  Download,
  Copy
} from "lucide-vue-next"

// 2FA State
const twoFactorEnabled = ref(false)
const showSetup2FA = ref(false)
const showDisable2FA = ref(false)
const showBackupCodes = ref(false)
const setup2FAStep = ref(1)
const verify2FACode = ref("")
const disable2FACode = ref("")
const enabling2FA = ref(false)
const disabling2FA = ref(false)

const backupCodes = ref([
  "A1B2-C3D4",
  "E5F6-G7H8",
  "I9J0-K1L2",
  "M3N4-O5P6",
  "Q7R8-S9T0",
  "U1V2-W3X4",
  "Y5Z6-A7B8",
  "C9D0-E1F2"
])

// Sessions State
const sessions = ref([])
const loadingSessions = ref(false)
const showRevokeAll = ref(false)
const revokingAll = ref(false)

// Login History
const loginHistory = ref([])

// Security Score
const securityScore = computed(() => {
  let score = 50
  if (twoFactorEnabled.value) score += 30
  if (sessions.value.length <= 2) score += 20
  return score
})

const passwordLastChanged = ref("6 months ago")

onMounted(() => {
  loadSecurityData()
})

async function loadSecurityData() {
  try {
    // TODO: Replace with actual API calls
    
    // Load 2FA status
    // const res = await apiFetch("/auth/2fa/status")
    // twoFactorEnabled.value = res.enabled
    
    loadSessions()
    loadLoginHistory()
    
  } catch (error) {
    console.error("Failed to load security data:", error)
  }
}

async function loadSessions() {
  loadingSessions.value = true
  
  try {
    // TODO: Replace with actual API call
    await new Promise(resolve => setTimeout(resolve, 500))
    
    sessions.value = [
      {
        id: 1,
        device_type: "desktop",
        browser: "Chrome",
        os: "Windows 11",
        location: "San Francisco, US",
        ip_address: "192.168.1.1",
        last_active: new Date(),
        is_current: true
      },
      {
        id: 2,
        device_type: "mobile",
        browser: "Safari",
        os: "iOS 17",
        location: "New York, US",
        ip_address: "192.168.1.2",
        last_active: new Date(Date.now() - 2 * 60 * 60 * 1000),
        is_current: false
      }
    ]
  } catch (error) {
    console.error("Failed to load sessions:", error)
  } finally {
    loadingSessions.value = false
  }
}

async function loadLoginHistory() {
  try {
    // TODO: Replace with actual API call
    loginHistory.value = [
      {
        id: 1,
        success: true,
        timestamp: new Date(),
        location: "San Francisco, US",
        ip_address: "192.168.1.1"
      },
      {
        id: 2,
        success: false,
        timestamp: new Date(Date.now() - 24 * 60 * 60 * 1000),
        location: "Unknown",
        ip_address: "123.456.789.0"
      },
      {
        id: 3,
        success: true,
        timestamp: new Date(Date.now() - 48 * 60 * 60 * 1000),
        location: "San Francisco, US",
        ip_address: "192.168.1.1"
      }
    ]
  } catch (error) {
    console.error("Failed to load login history:", error)
  }
}

async function enable2FA() {
  enabling2FA.value = true
  
  try {
    // TODO: Add your API call here
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    twoFactorEnabled.value = true
    showSetup2FA.value = false
    setup2FAStep.value = 1
    verify2FACode.value = ""
    showBackupCodes.value = true
  } catch (error) {
    console.error("Failed to enable 2FA:", error)
  } finally {
    enabling2FA.value = false
  }
}

async function disable2FA() {
  disabling2FA.value = true
  
  try {
    // TODO: Add your API call here
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    twoFactorEnabled.value = false
    showDisable2FA.value = false
    disable2FACode.value = ""
  } catch (error) {
    console.error("Failed to disable 2FA:", error)
  } finally {
    disabling2FA.value = false
  }
}

async function revokeSession(sessionId) {
  try {
    // TODO: Add your API call here
    await new Promise(resolve => setTimeout(resolve, 500))
    
    sessions.value = sessions.value.filter(s => s.id !== sessionId)
  } catch (error) {
    console.error("Failed to revoke session:", error)
  }
}

async function revokeAllSessions() {
  revokingAll.value = true
  
  try {
    // TODO: Add your API call here
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    sessions.value = sessions.value.filter(s => s.is_current)
    showRevokeAll.value = false
  } catch (error) {
    console.error("Failed to revoke all sessions:", error)
  } finally {
    revokingAll.value = false
  }
}

function downloadBackupCodes() {
  const text = backupCodes.value.join("\n")
  const blob = new Blob([text], { type: "text/plain" })
  const url = URL.createObjectURL(blob)
  const a = document.createElement("a")
  a.href = url
  a.download = "lifeadmin-backup-codes.txt"
  a.click()
  URL.revokeObjectURL(url)
}

function copyBackupCodes() {
  const text = backupCodes.value.join("\n")
  navigator.clipboard.writeText(text)
  // TODO: Show toast notification
}

function formatRelativeTime(date) {
  const now = new Date()
  const diff = now - new Date(date)
  const minutes = Math.floor(diff / 60000)
  const hours = Math.floor(diff / 3600000)
  const days = Math.floor(diff / 86400000)
  
  if (minutes < 1) return "just now"
  if (minutes < 60) return `${minutes}m ago`
  if (hours < 24) return `${hours}h ago`
  return `${days}d ago`
}

function formatDateTime(date) {
  return new Date(date).toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    hour: 'numeric',
    minute: '2-digit'
  })
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