<template>
  <div>
    <div class="space-y-8">

      <!-- PASSWORD CHANGE SECTION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-teal-100 flex items-center justify-center flex-shrink-0">
            <Lock :size="20" class="text-teal-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Change Password</h3>
            <p class="text-sm text-gray-600 mt-1">Update your password to keep your account secure</p>
          </div>
        </div>

        <form @submit.prevent="updatePassword" class="space-y-4">
          
          <!-- Current Password -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Current Password *
            </label>
            <div class="relative">
              <input
                v-model="passwordForm.current"
                :type="showCurrentPassword ? 'text' : 'password'"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                placeholder="Enter current password"
                required
              />
              <button
                type="button"
                @click="showCurrentPassword = !showCurrentPassword"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
              >
                <EyeOff v-if="showCurrentPassword" :size="20" />
                <Eye v-else :size="20" />
              </button>
            </div>
          </div>

          <!-- New Password -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              New Password *
            </label>
            <div class="relative">
              <input
                v-model="passwordForm.new"
                :type="showNewPassword ? 'text' : 'password'"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                placeholder="Enter new password"
                required
                @input="checkPasswordStrength"
              />
              <button
                type="button"
                @click="showNewPassword = !showNewPassword"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
              >
                <EyeOff v-if="showNewPassword" :size="20" />
                <Eye v-else :size="20" />
              </button>
            </div>

            <!-- Password Strength Indicator -->
            <div v-if="passwordForm.new" class="mt-3">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-medium text-gray-600">Password strength:</span>
                <span :class="[
                  'text-xs font-semibold',
                  passwordStrength === 'weak' ? 'text-red-600' :
                  passwordStrength === 'medium' ? 'text-orange-600' :
                  'text-green-600'
                ]">
                  {{ passwordStrength.toUpperCase() }}
                </span>
              </div>
              <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
                <div
                  :class="[
                    'h-full transition-all duration-300',
                    passwordStrength === 'weak' ? 'w-1/3 bg-red-500' :
                    passwordStrength === 'medium' ? 'w-2/3 bg-orange-500' :
                    'w-full bg-green-500'
                  ]"
                ></div>
              </div>
            </div>

            <!-- Password Requirements -->
            <div class="mt-3 space-y-1">
              <div class="flex items-center gap-2 text-xs">
                <CheckCircle2 v-if="passwordChecks.length" :size="14" class="text-green-500" />
                <XCircle v-else :size="14" class="text-gray-300" />
                <span :class="passwordChecks.length ? 'text-gray-700' : 'text-gray-400'">
                  At least 8 characters
                </span>
              </div>
              <div class="flex items-center gap-2 text-xs">
                <CheckCircle2 v-if="passwordChecks.uppercase" :size="14" class="text-green-500" />
                <XCircle v-else :size="14" class="text-gray-300" />
                <span :class="passwordChecks.uppercase ? 'text-gray-700' : 'text-gray-400'">
                  One uppercase letter
                </span>
              </div>
              <div class="flex items-center gap-2 text-xs">
                <CheckCircle2 v-if="passwordChecks.number" :size="14" class="text-green-500" />
                <XCircle v-else :size="14" class="text-gray-300" />
                <span :class="passwordChecks.number ? 'text-gray-700' : 'text-gray-400'">
                  One number
                </span>
              </div>
            </div>
          </div>

          <!-- Confirm New Password -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Confirm New Password *
            </label>
            <div class="relative">
              <input
                v-model="passwordForm.confirm"
                :type="showConfirmPassword ? 'text' : 'password'"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                placeholder="Confirm new password"
                required
              />
              <button
                type="button"
                @click="showConfirmPassword = !showConfirmPassword"
                class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600"
              >
                <EyeOff v-if="showConfirmPassword" :size="20" />
                <Eye v-else :size="20" />
              </button>
            </div>
            <p v-if="passwordForm.confirm && passwordForm.new !== passwordForm.confirm" class="text-xs text-red-600 mt-2 flex items-center gap-1">
              <AlertCircle :size="14" />
              Passwords do not match
            </p>
          </div>

          <!-- Submit Button -->
          <div class="flex items-center gap-3 pt-2">
            <button
              type="submit"
              :disabled="!isPasswordFormValid || updatingPassword"
              class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              <Check :size="18" v-if="!updatingPassword" />
              <Loader2 :size="18" class="animate-spin" v-else />
              {{ updatingPassword ? 'Updating...' : 'Update Password' }}
            </button>

            <button
              v-if="passwordForm.current || passwordForm.new || passwordForm.confirm"
              type="button"
              @click="resetPasswordForm"
              class="px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
            >
              Cancel
            </button>
          </div>

          <!-- Success Message -->
          <div v-if="passwordSuccess" class="flex items-center gap-2 p-4 bg-green-50 border border-green-200 rounded-xl text-green-800 text-sm">
            <CheckCircle2 :size="18" class="text-green-600" />
            <span>Password updated successfully!</span>
          </div>

        </form>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-200"></div>

      <!-- EMAIL CHANGE SECTION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-blue-100 flex items-center justify-center flex-shrink-0">
            <Mail :size="20" class="text-blue-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Email Address</h3>
            <p class="text-sm text-gray-600 mt-1">Manage your email address for account notifications</p>
          </div>
        </div>

        <div class="bg-gray-50 rounded-xl p-4 mb-4">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm text-gray-600">Current email</p>
              <p class="font-semibold text-gray-900">{{ currentEmail }}</p>
            </div>
            <button
              @click="showEmailForm = !showEmailForm"
              class="px-4 py-2 text-teal-600 font-medium hover:bg-teal-50 rounded-lg transition-colors"
            >
              {{ showEmailForm ? 'Cancel' : 'Change Email' }}
            </button>
          </div>
        </div>

        <!-- Change Email Form -->
        <Transition
          enter-active-class="transition-all duration-200 ease-out"
          enter-from-class="opacity-0 -translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition-all duration-150 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 -translate-y-2"
        >
          <form v-if="showEmailForm" @submit.prevent="updateEmail" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                New Email Address *
              </label>
              <input
                v-model="emailForm.new"
                type="email"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                placeholder="Enter new email address"
                required
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Confirm Password *
              </label>
              <input
                v-model="emailForm.password"
                type="password"
                class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                placeholder="Enter your password to confirm"
                required
              />
            </div>

            <button
              type="submit"
              :disabled="updatingEmail"
              class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              <Loader2 :size="18" class="animate-spin" v-if="updatingEmail" />
              <Check :size="18" v-else />
              {{ updatingEmail ? 'Updating...' : 'Update Email' }}
            </button>
          </form>
        </Transition>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-200"></div>

      <!-- DANGER ZONE -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-red-100 flex items-center justify-center flex-shrink-0">
            <AlertTriangle :size="20" class="text-red-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-red-600">Danger Zone</h3>
            <p class="text-sm text-gray-600 mt-1">Irreversible and destructive actions</p>
          </div>
        </div>

        <div class="bg-red-50 border-2 border-red-200 rounded-xl p-6">
          <div class="flex items-start justify-between gap-4">
            <div>
              <h4 class="font-bold text-gray-900 mb-1">Delete Account</h4>
              <p class="text-sm text-gray-600 mb-2">
                Once you delete your account, there is no going back. All your data will be permanently deleted.
              </p>
              <ul class="text-xs text-gray-600 space-y-1 mb-4">
                <li class="flex items-center gap-2">
                  <XCircle :size="14" class="text-red-500" />
                  All documents and subscriptions will be deleted
                </li>
                <li class="flex items-center gap-2">
                  <XCircle :size="14" class="text-red-500" />
                  Your account cannot be recovered
                </li>
                <li class="flex items-center gap-2">
                  <XCircle :size="14" class="text-red-500" />
                  This action is permanent
                </li>
              </ul>
            </div>
          </div>

          <button
            @click="showDeleteConfirm = true"
            class="px-5 py-2.5 bg-red-600 text-white rounded-xl font-semibold hover:bg-red-700 transition-all duration-200 shadow-md hover:shadow-lg flex items-center gap-2"
          >
            <Trash2 :size="18" />
            Delete My Account
          </button>
        </div>
      </div>

    </div>

    <!-- DELETE CONFIRMATION MODAL -->
    <Transition
      enter-active-class="transition-all duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-150 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="showDeleteConfirm"
        class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4"
        @click.self="showDeleteConfirm = false"
      >
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-6 space-y-4">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-full bg-red-100 flex items-center justify-center">
              <AlertTriangle :size="24" class="text-red-600" />
            </div>
            <div>
              <h3 class="text-xl font-bold text-gray-900">Delete Account?</h3>
              <p class="text-sm text-gray-600">This action cannot be undone</p>
            </div>
          </div>

          <div class="bg-red-50 border border-red-200 rounded-xl p-4">
            <p class="text-sm text-gray-700 mb-3">
              To confirm deletion, please type <span class="font-mono font-bold text-red-600">DELETE</span> in the box below:
            </p>
            <input
              v-model="deleteConfirmText"
              type="text"
              class="w-full px-4 py-2 border-2 border-red-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
              placeholder="Type DELETE"
            />
          </div>

          <div class="flex gap-3">
            <button
              @click="deleteAccount"
              :disabled="deleteConfirmText !== 'DELETE' || deletingAccount"
              class="flex-1 px-4 py-3 bg-red-600 text-white rounded-xl font-semibold hover:bg-red-700 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <Loader2 :size="18" class="animate-spin" v-if="deletingAccount" />
              <Trash2 :size="18" v-else />
              {{ deletingAccount ? 'Deleting...' : 'Yes, Delete My Account' }}
            </button>

            <button
              @click="showDeleteConfirm = false"
              :disabled="deletingAccount"
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
import { ref, computed } from "vue"
import {
  Lock,
  Eye,
  EyeOff,
  Check,
  CheckCircle2,
  XCircle,
  AlertCircle,
  AlertTriangle,
  Mail,
  Trash2,
  Loader2
} from "lucide-vue-next"

// Password Form
const passwordForm = ref({
  current: '',
  new: '',
  confirm: ''
})

const showCurrentPassword = ref(false)
const showNewPassword = ref(false)
const showConfirmPassword = ref(false)
const updatingPassword = ref(false)
const passwordSuccess = ref(false)

// Email Form
const currentEmail = ref("user@example.com") // Replace with actual user email
const showEmailForm = ref(false)
const emailForm = ref({
  new: '',
  password: ''
})
const updatingEmail = ref(false)

// Delete Account
const showDeleteConfirm = ref(false)
const deleteConfirmText = ref('')
const deletingAccount = ref(false)

// Password Strength
const passwordStrength = ref('weak')
const passwordChecks = computed(() => ({
  length: passwordForm.value.new.length >= 8,
  uppercase: /[A-Z]/.test(passwordForm.value.new),
  number: /[0-9]/.test(passwordForm.value.new)
}))

const isPasswordFormValid = computed(() => {
  return (
    passwordForm.value.current &&
    passwordForm.value.new &&
    passwordForm.value.confirm &&
    passwordForm.value.new === passwordForm.value.confirm &&
    passwordChecks.value.length &&
    passwordChecks.value.uppercase &&
    passwordChecks.value.number
  )
})

function checkPasswordStrength() {
  const { length, uppercase, number } = passwordChecks.value
  
  if (length && uppercase && number) {
    passwordStrength.value = 'strong'
  } else if (length && (uppercase || number)) {
    passwordStrength.value = 'medium'
  } else {
    passwordStrength.value = 'weak'
  }
}

function resetPasswordForm() {
  passwordForm.value = { current: '', new: '', confirm: '' }
  passwordSuccess.value = false
}

async function updatePassword() {
  updatingPassword.value = true
  
  try {
    // TODO: Add your API call here
    await new Promise(resolve => setTimeout(resolve, 1000)) // Simulated API call
    
    passwordSuccess.value = true
    setTimeout(() => {
      resetPasswordForm()
      passwordSuccess.value = false
    }, 3000)
  } catch (error) {
    console.error('Failed to update password:', error)
  } finally {
    updatingPassword.value = false
  }
}

async function updateEmail() {
  updatingEmail.value = true
  
  try {
    // TODO: Add your API call here
    await new Promise(resolve => setTimeout(resolve, 1000)) // Simulated API call
    
    currentEmail.value = emailForm.value.new
    showEmailForm.value = false
    emailForm.value = { new: '', password: '' }
  } catch (error) {
    console.error('Failed to update email:', error)
  } finally {
    updatingEmail.value = false
  }
}

async function deleteAccount() {
  deletingAccount.value = true
  
  try {
    // TODO: Add your API call here
    await new Promise(resolve => setTimeout(resolve, 1500)) // Simulated API call
    
    // Clear tokens and redirect to login
    // clearTokens()
    // router.push('/login')
  } catch (error) {
    console.error('Failed to delete account:', error)
  } finally {
    deletingAccount.value = false
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