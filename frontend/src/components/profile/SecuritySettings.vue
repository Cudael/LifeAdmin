<template>
  <div class="space-y-8">

    <!-- PASSWORD CHANGE SECTION -->
    <div>
      <div class="flex items-start gap-3 mb-6">
        <div class="w-10 h-10 rounded-lg bg-teal-900/40 flex items-center justify-center flex-shrink-0">
          <Lock :size="20" class="text-teal-400" />
        </div>
        <div>
          <h3 class="text-lg font-bold text-white">Change Password</h3>
          <p class="text-sm text-gray-300 mt-1">Update your password to keep your account secure</p>
        </div>
      </div>

      <form @submit.prevent="updatePassword" class="space-y-4">
        
        <!-- Current Password -->
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">
            Current Password *
          </label>
          <div class="relative">
            <input
              v-model="passwordForm.current"
              :type="showCurrentPassword ? 'text' : 'password'"
              class="w-full px-4 py-3 bg-gray-800 border border-gray-700 text-white placeholder:text-gray-500 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
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
          <label class="block text-sm font-medium text-gray-300 mb-2">
            New Password *
          </label>
          <div class="relative">
            <input
              v-model="passwordForm.new"
              :type="showNewPassword ? 'text' : 'password'"
              class="w-full px-4 py-3 bg-gray-800 border border-gray-700 text-white placeholder:text-gray-500 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
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
              <span class="text-xs font-medium text-gray-300">Password strength:</span>
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
              <CheckCircle2 v-if="passwordChecks.length" :size="14" class="text-green-400" />
              <XCircle v-else :size="14" class="text-gray-600" />
              <span :class="passwordChecks.length ? 'text-gray-300' : 'text-gray-500'">
                At least 8 characters
              </span>
            </div>
            <div class="flex items-center gap-2 text-xs">
              <CheckCircle2 v-if="passwordChecks.uppercase" :size="14" class="text-green-400" />
              <XCircle v-else :size="14" class="text-gray-600" />
              <span :class="passwordChecks.uppercase ? 'text-gray-300' : 'text-gray-500'">
                One uppercase letter
              </span>
            </div>
            <div class="flex items-center gap-2 text-xs">
              <CheckCircle2 v-if="passwordChecks.number" :size="14" class="text-green-400" />
              <XCircle v-else :size="14" class="text-gray-600" />
              <span :class="passwordChecks.number ? 'text-gray-300' : 'text-gray-500'">
                One number
              </span>
            </div>
          </div>
        </div>

        <!-- Confirm New Password -->
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">
            Confirm New Password *
          </label>
          <div class="relative">
            <input
              v-model="passwordForm.confirm"
              :type="showConfirmPassword ? 'text' : 'password'"
              class="w-full px-4 py-3 bg-gray-800 border border-gray-700 text-white placeholder:text-gray-500 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
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
            <Loader2 :size="18" class="animate-spin" v-if="updatingPassword" />
            <Check :size="18" v-else />
            {{ updatingPassword ? 'Updating...' : 'Update Password' }}
          </button>

          <button
            v-if="passwordForm.current || passwordForm.new || passwordForm.confirm"
            type="button"
            @click="resetPasswordForm"
            class="px-6 py-3 bg-gray-800 text-gray-300 rounded-xl font-semibold hover:bg-gray-700 transition-all duration-200"
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
          <div v-if="passwordSuccess" class="flex items-center gap-2 p-4 bg-green-50 border border-green-200 rounded-xl text-green-800 text-sm">
            <CheckCircle2 :size="18" class="text-green-600" />
            <span>Password updated successfully!</span>
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

    <!-- DELETE ACCOUNT SECTION (DANGER ZONE) -->
    <div>
      <div class="flex items-start gap-3 mb-6">
        <div class="w-10 h-10 rounded-lg bg-red-900/40 flex items-center justify-center flex-shrink-0">
          <AlertTriangle :size="20" class="text-red-400" />
        </div>
        <div>
          <h3 class="text-lg font-bold text-white">Danger Zone</h3>
          <p class="text-sm text-gray-300 mt-1">Irreversible and destructive actions</p>
        </div>
      </div>

      <div class="border-2 border-red-800 rounded-xl p-6 bg-red-900/20">
        <div class="flex items-start justify-between gap-4">
          <div class="flex-1">
            <h4 class="text-base font-bold text-red-300 mb-2 flex items-center gap-2">
              <Trash2 :size="18" />
              Delete Account
            </h4>
            <p class="text-sm text-red-400 mb-3">
              Permanently delete your account and all associated data. This action cannot be undone.
            </p>
            <ul class="text-xs text-red-400 space-y-1 mb-4">
              <li class="flex items-center gap-2">
                <div class="w-1 h-1 rounded-full bg-red-600"></div>
                All your items and documents will be deleted
              </li>
              <li class="flex items-center gap-2">
                <div class="w-1 h-1 rounded-full bg-red-600"></div>
                All uploaded files will be permanently removed
              </li>
              <li class="flex items-center gap-2">
                <div class="w-1 h-1 rounded-full bg-red-600"></div>
                Your profile and settings will be lost forever
              </li>
              <li class="flex items-center gap-2">
                <div class="w-1 h-1 rounded-full bg-red-600"></div>
                This action is irreversible
              </li>
            </ul>
          </div>
        </div>

        <button
          @click="showDeleteModal = true"
          class="px-6 py-3 bg-red-600 text-white rounded-xl font-semibold hover:bg-red-700 transition-all duration-200 flex items-center gap-2 shadow-lg hover:shadow-xl"
        >
          <Trash2 :size="18" />
          Delete My Account
        </button>
      </div>
    </div>

    <!-- DELETE ACCOUNT MODAL -->
    <DeleteAccountModal
      :show="showDeleteModal"
      :loading="deleteLoading"
      :error="deleteError"
      @cancel="showDeleteModal = false; deleteError = ''"
      @confirm="handleDeleteAccount"
    />

  </div>
</template>

<script setup>
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import { apiFetch } from "../../utils/api"
import DeleteAccountModal from "../../components/DeleteAccountModal.vue"
import {
  Lock,
  Eye,
  EyeOff,
  Check,
  CheckCircle2,
  XCircle,
  AlertCircle,
  AlertTriangle,
  Trash2,
  Loader2
} from "lucide-vue-next"

const router = useRouter()

// Password form state
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
const error = ref('')

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

// Delete account state
const showDeleteModal = ref(false)
const deleteLoading = ref(false)
const deleteError = ref('')

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
  error.value = ''
}

async function updatePassword() {
  updatingPassword.value = true
  error.value = ''
  passwordSuccess.value = false
  
  try {
    const res = await apiFetch('/auth/change-password', {
      method: 'POST',
      body: JSON.stringify({
        current_password: passwordForm.value.current,
        new_password: passwordForm.value.new
      })
    })
    
    if (!res.ok) {
      const data = await res.json()
      throw new Error(data.detail || 'Failed to update password')
    }
    
    passwordSuccess.value = true
    setTimeout(() => {
      resetPasswordForm()
    }, 3000)
    
  } catch (err) {
    console.error('Failed to update password:', err)
    error.value = err.message || 'Failed to update password. Please try again.'
    setTimeout(() => {
      error.value = ''
    }, 5000)
  } finally {
    updatingPassword.value = false
  }
}

async function handleDeleteAccount(password) {
  deleteError.value = ""
  deleteLoading.value = true

  try {
    const res = await apiFetch("/auth/me", {
      method: "DELETE",
      body: JSON.stringify({ password })
    })

    if (!res.ok) {
      const data = await res.json()
      deleteError.value = data.detail || "Failed to delete account"
      deleteLoading.value = false
      return
    }

    // Account deleted successfully
    // Clear tokens
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    
    // Close modal
    showDeleteModal.value = false
    
    // Redirect to landing page
    router.push('/')
    
  } catch (err) {
    console.error("Delete account error:", err)
    deleteError.value = "Something went wrong. Please try again."
    deleteLoading.value = false
  }
}
</script>