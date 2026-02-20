<template>
  <div class="space-y-12">

    <!-- PASSWORD UPDATE SECTION -->
    <div>
      <h3 class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-6 ml-1">Authentication Credentials</h3>

      <form @submit.prevent="updatePassword" class="space-y-6">
        
        <!-- Current Password -->
        <div class="space-y-2">
          <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
            Current Password <span class="text-rose-400">*</span>
          </label>
          <div class="relative group/input">
            <input
              v-model="passwordForm.current"
              :type="showCurrentPassword ? 'text' : 'password'"
              class="w-full px-4 py-3.5 bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all hover:border-white/20 font-medium shadow-inner"
              placeholder="Enter current password"
              required
            />
            <button
              type="button"
              @click="showCurrentPassword = !showCurrentPassword"
              class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-500 hover:text-white transition-colors"
            >
              <EyeOff v-if="showCurrentPassword" :size="18" />
              <Eye v-else :size="18" />
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- New Password -->
          <div class="space-y-2">
            <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
              New Password <span class="text-rose-400">*</span>
            </label>
            <div class="relative group/input">
              <input
                v-model="passwordForm.new"
                :type="showNewPassword ? 'text' : 'password'"
                class="w-full px-4 py-3.5 bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all hover:border-white/20 font-medium shadow-inner"
                placeholder="Enter new password"
                required
                @input="checkPasswordStrength"
              />
              <button
                type="button"
                @click="showNewPassword = !showNewPassword"
                class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-500 hover:text-white transition-colors"
              >
                <EyeOff v-if="showNewPassword" :size="18" />
                <Eye v-else :size="18" />
              </button>
            </div>

            <!-- Password Strength Neon Indicator -->
            <div v-if="passwordForm.new" class="pt-2">
              <div class="flex items-center gap-1 h-1.5 rounded-full overflow-hidden bg-slate-900">
                <div class="h-full transition-all duration-300 flex-1" :class="passwordStrength === 'weak' || passwordStrength === 'medium' || passwordStrength === 'strong' ? 'bg-rose-500 shadow-[0_0_10px_rgba(225,29,72,0.8)]' : ''"></div>
                <div class="h-full transition-all duration-300 flex-1" :class="passwordStrength === 'medium' || passwordStrength === 'strong' ? 'bg-amber-400 shadow-[0_0_10px_rgba(251,191,36,0.8)]' : ''"></div>
                <div class="h-full transition-all duration-300 flex-1" :class="passwordStrength === 'strong' ? 'bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.8)]' : ''"></div>
              </div>
              <div class="flex justify-between items-center mt-2">
                <span class="text-[10px] font-bold uppercase tracking-widest text-slate-500">Strength</span>
                <span class="text-[10px] font-bold uppercase tracking-widest" :class="{
                  'text-rose-400': passwordStrength === 'weak',
                  'text-amber-400': passwordStrength === 'medium',
                  'text-emerald-400': passwordStrength === 'strong'
                }">{{ passwordStrength }}</span>
              </div>
            </div>

            <!-- Checklist -->
            <div v-if="passwordForm.new" class="mt-3 space-y-1.5 bg-slate-950/30 p-3 rounded-xl border border-white/5">
              <div class="flex items-center gap-2 text-[11px] font-bold uppercase tracking-wider" :class="passwordChecks.length ? 'text-emerald-400' : 'text-slate-600'">
                <CheckCircle2 v-if="passwordChecks.length" :size="14" />
                <div v-else class="w-3.5 h-3.5 rounded-full border-2 border-slate-700"></div>
                8+ Characters
              </div>
              <div class="flex items-center gap-2 text-[11px] font-bold uppercase tracking-wider" :class="passwordChecks.uppercase ? 'text-emerald-400' : 'text-slate-600'">
                <CheckCircle2 v-if="passwordChecks.uppercase" :size="14" />
                <div v-else class="w-3.5 h-3.5 rounded-full border-2 border-slate-700"></div>
                1+ Uppercase
              </div>
              <div class="flex items-center gap-2 text-[11px] font-bold uppercase tracking-wider" :class="passwordChecks.number ? 'text-emerald-400' : 'text-slate-600'">
                <CheckCircle2 v-if="passwordChecks.number" :size="14" />
                <div v-else class="w-3.5 h-3.5 rounded-full border-2 border-slate-700"></div>
                1+ Number
              </div>
            </div>
          </div>

          <!-- Confirm New Password -->
          <div class="space-y-2">
            <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
              Verify Password <span class="text-rose-400">*</span>
            </label>
            <div class="relative group/input">
              <input
                v-model="passwordForm.confirm"
                :type="showConfirmPassword ? 'text' : 'password'"
                class="w-full px-4 py-3.5 bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all hover:border-white/20 font-medium shadow-inner"
                placeholder="Confirm new password"
                required
              />
              <button
                type="button"
                @click="showConfirmPassword = !showConfirmPassword"
                class="absolute right-4 top-1/2 -translate-y-1/2 text-slate-500 hover:text-white transition-colors"
              >
                <EyeOff v-if="showConfirmPassword" :size="18" />
                <Eye v-else :size="18" />
              </button>
            </div>
            
            <Transition enter-active-class="transition-all duration-200" enter-from-class="opacity-0 -translate-y-2" leave-to-class="opacity-0 -translate-y-2">
              <p v-if="passwordForm.confirm && passwordForm.new !== passwordForm.confirm" class="text-xs font-bold text-rose-400 mt-2 flex items-center gap-1.5 ml-1">
                <AlertCircle :size="14" />
                Passwords do not match
              </p>
            </Transition>
          </div>
        </div>

        <!-- Submit Button -->
        <div class="flex items-center gap-4 pt-2">
          <button
            type="submit"
            :disabled="!isPasswordFormValid || updatingPassword"
            class="group px-6 py-3.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.2)] hover:shadow-[0_0_30px_rgba(45,212,191,0.4)] transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
          >
            <Loader2 :size="18" class="animate-spin" v-if="updatingPassword" />
            <ShieldCheck :size="18" class="group-hover:scale-110 transition-transform" v-else />
            {{ updatingPassword ? 'Encrypting...' : 'Update Password' }}
          </button>

          <button
            v-if="passwordForm.current || passwordForm.new || passwordForm.confirm"
            type="button"
            @click="resetPasswordForm"
            class="px-6 py-3.5 bg-white/5 hover:bg-white/10 border border-white/5 text-white rounded-xl font-bold transition-all duration-200"
          >
            Clear
          </button>
        </div>

        <!-- Messages -->
        <Transition enter-active-class="transition-all duration-300 ease-out" enter-from-class="opacity-0 translate-y-2 scale-95" enter-to-class="opacity-100 translate-y-0 scale-100" leave-active-class="transition-all duration-200 ease-in" leave-from-class="opacity-100 translate-y-0 scale-100" leave-to-class="opacity-0 translate-y-2 scale-95">
          <div v-if="passwordSuccess" class="flex items-center gap-3 p-4 bg-emerald-500/10 border border-emerald-500/20 rounded-xl shadow-inner">
            <div class="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400 shrink-0"><CheckCircle2 :size="16" /></div>
            <span class="text-sm font-bold text-emerald-300">Authentication credentials successfully updated.</span>
          </div>
        </Transition>

        <Transition enter-active-class="transition-all duration-300 ease-out" enter-from-class="opacity-0 translate-y-2 scale-95" enter-to-class="opacity-100 translate-y-0 scale-100" leave-active-class="transition-all duration-200 ease-in" leave-from-class="opacity-100 translate-y-0 scale-100" leave-to-class="opacity-0 translate-y-2 scale-95">
          <div v-if="error" class="flex items-center gap-3 p-4 bg-rose-500/10 border border-rose-500/20 rounded-xl shadow-inner">
            <div class="w-8 h-8 rounded-full bg-rose-500/20 flex items-center justify-center text-rose-400 shrink-0"><AlertCircle :size="16" /></div>
            <span class="text-sm font-bold text-rose-300">{{ error }}</span>
          </div>
        </Transition>
      </form>
    </div>

    <div class="h-px bg-white/5 w-full"></div>

    <!-- DANGER ZONE -->
    <div class="relative">
      <h3 class="text-[10px] font-bold uppercase tracking-widest text-rose-500 mb-4 ml-1 flex items-center gap-2">
        <AlertTriangle :size="12" /> Critical Operations
      </h3>

      <div class="relative border border-rose-500/30 rounded-[2rem] p-8 bg-rose-500/5 overflow-hidden group hover:bg-rose-500/10 transition-colors">
        <!-- Warning Glow -->
        <div class="absolute -top-24 -right-24 w-64 h-64 bg-rose-500/20 blur-[80px] rounded-full pointer-events-none transition-opacity opacity-50 group-hover:opacity-100"></div>

        <div class="relative z-10 flex flex-col md:flex-row items-start justify-between gap-8">
          <div class="flex-1">
            <h4 class="text-xl font-extrabold text-white mb-2 tracking-tight">Delete Secure Vault</h4>
            <p class="text-sm font-medium text-rose-200/70 mb-4 leading-relaxed">
              Initiating this protocol will permanently destroy your account and purge all encrypted data from our servers. This action is irreversible.
            </p>
            <ul class="text-xs font-bold uppercase tracking-widest text-rose-400 space-y-2">
              <li class="flex items-center gap-2.5"><div class="w-1.5 h-1.5 rounded-full bg-rose-500 shadow-[0_0_8px_rgba(225,29,72,0.8)]"></div> Identities & Subscriptions Purged</li>
              <li class="flex items-center gap-2.5"><div class="w-1.5 h-1.5 rounded-full bg-rose-500 shadow-[0_0_8px_rgba(225,29,72,0.8)]"></div> Secure Documents Deleted</li>
              <li class="flex items-center gap-2.5"><div class="w-1.5 h-1.5 rounded-full bg-rose-500 shadow-[0_0_8px_rgba(225,29,72,0.8)]"></div> Access Credentials Terminated</li>
            </ul>
          </div>

          <button
            @click="showDeleteModal = true"
            class="shrink-0 px-6 py-3.5 bg-rose-500/10 hover:bg-rose-500 border border-rose-500/50 hover:border-transparent text-rose-400 hover:text-white rounded-xl font-bold transition-all duration-300 flex items-center gap-2 shadow-[0_0_20px_rgba(225,29,72,0.1)] hover:shadow-[0_0_30px_rgba(225,29,72,0.5)]"
          >
            <Trash2 :size="18" />
            Delete Account
          </button>
        </div>
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
import { Lock, Eye, EyeOff, Check, CheckCircle2, ShieldCheck, AlertCircle, AlertTriangle, Trash2, Loader2 } from "lucide-vue-next"

const router = useRouter()

const passwordForm = ref({ current: '', new: '', confirm: '' })
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
  return passwordForm.value.current && passwordForm.value.new && passwordForm.value.confirm &&
    passwordForm.value.new === passwordForm.value.confirm &&
    passwordChecks.value.length && passwordChecks.value.uppercase && passwordChecks.value.number
})

const showDeleteModal = ref(false)
const deleteLoading = ref(false)
const deleteError = ref('')

function checkPasswordStrength() {
  const { length, uppercase, number } = passwordChecks.value
  if (length && uppercase && number) passwordStrength.value = 'strong'
  else if (length && (uppercase || number)) passwordStrength.value = 'medium'
  else passwordStrength.value = 'weak'
}

function resetPasswordForm() {
  passwordForm.value = { current: '', new: '', confirm: '' }
  passwordSuccess.value = false; error.value = ''
}

async function updatePassword() {
  updatingPassword.value = true; error.value = ''; passwordSuccess.value = false
  try {
    const res = await apiFetch('/auth/change-password', {
      method: 'POST',
      body: JSON.stringify({ current_password: passwordForm.value.current, new_password: passwordForm.value.new })
    })
    if (!res.ok) throw new Error((await res.json()).detail || 'Failed to update password')
    passwordSuccess.value = true
    setTimeout(resetPasswordForm, 3000)
  } catch (err) {
    error.value = err.message || 'Failed to update password. Please try again.'
    setTimeout(() => { error.value = '' }, 5000)
  } finally {
    updatingPassword.value = false
  }
}

async function handleDeleteAccount(password) {
  deleteError.value = ""; deleteLoading.value = true
  try {
    const res = await apiFetch("/auth/me", { method: "DELETE", body: JSON.stringify({ password }) })
    if (!res.ok) {
      deleteError.value = (await res.json()).detail || "Failed to delete account"
      deleteLoading.value = false; return
    }
    localStorage.removeItem('access_token'); localStorage.removeItem('refresh_token')
    showDeleteModal.value = false; router.push('/')
  } catch (err) {
    deleteError.value = "Something went wrong. Please try again."
    deleteLoading.value = false
  }
}
</script>