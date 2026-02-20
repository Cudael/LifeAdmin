<template>
  <div class="space-y-10">

    <!-- Loading State -->
    <div v-if="loading" class="flex flex-col items-center justify-center py-20">
      <div class="w-16 h-16 bg-teal-500/10 rounded-2xl flex items-center justify-center mb-4 border border-teal-500/20 shadow-inner">
        <Loader2 :size="32" class="animate-spin text-teal-400" />
      </div>
      <p class="text-slate-400 font-medium tracking-wide">Loading identity data...</p>
    </div>

    <div v-else class="space-y-10">

      <!-- PERSONAL INFORMATION FORM -->
      <form @submit.prevent="save" class="space-y-6">
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Full Name -->
          <div class="space-y-2">
            <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
              Full Name <span class="text-rose-400">*</span>
            </label>
            <div class="relative group/input">
              <input
                v-model="form.full_name"
                type="text"
                class="w-full pl-11 pr-4 py-3.5 bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all hover:border-white/20 font-medium shadow-inner"
                placeholder="John Doe"
                required
              />
              <User :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-500 group-focus-within/input:text-teal-400 transition-colors" />
            </div>
          </div>

          <!-- Email (Read-only) -->
          <div class="space-y-2">
            <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
              Account Email
            </label>
            <div class="relative">
              <input
                :value="form.email"
                type="email"
                class="w-full pl-11 pr-4 py-3.5 bg-slate-900/50 border border-transparent text-slate-500 rounded-xl cursor-not-allowed font-medium"
                readonly
              />
              <Mail :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-slate-600" />
              
              <!-- Google Connected Badge -->
              <div class="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-1.5 px-2 py-1 bg-emerald-500/10 border border-emerald-500/20 rounded-md">
                <CheckCircle2 :size="12" class="text-emerald-400" />
                <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-400">Verified</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex items-center gap-4 pt-2">
          <button
            type="submit"
            :disabled="saving || !hasChanges"
            class="group px-6 py-3.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.2)] hover:shadow-[0_0_30px_rgba(45,212,191,0.4)] transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
          >
            <Loader2 :size="18" class="animate-spin" v-if="saving" />
            <Save :size="18" class="group-hover:scale-110 transition-transform" v-else />
            {{ saving ? 'Encrypting...' : 'Save Changes' }}
          </button>

          <button
            v-if="hasChanges"
            type="button"
            @click="resetForm"
            :disabled="saving"
            class="px-6 py-3.5 bg-white/5 hover:bg-white/10 border border-white/5 text-white rounded-xl font-bold transition-all duration-200 disabled:opacity-50"
          >
            Discard
          </button>
        </div>

        <!-- Success Message -->
        <Transition
          enter-active-class="transition-all duration-300 ease-out"
          enter-from-class="opacity-0 translate-y-2 scale-95"
          enter-to-class="opacity-100 translate-y-0 scale-100"
          leave-active-class="transition-all duration-200 ease-in"
          leave-from-class="opacity-100 translate-y-0 scale-100"
          leave-to-class="opacity-0 translate-y-2 scale-95"
        >
          <div v-if="saveSuccess" class="flex items-center gap-3 p-4 bg-emerald-500/10 border border-emerald-500/20 rounded-xl shadow-inner">
            <div class="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400 shrink-0">
              <CheckCircle2 :size="16" />
            </div>
            <span class="text-sm font-bold text-emerald-300">Identity parameters updated successfully.</span>
          </div>
        </Transition>

        <!-- Error Message -->
        <Transition
          enter-active-class="transition-all duration-300 ease-out"
          enter-from-class="opacity-0 translate-y-2 scale-95"
          enter-to-class="opacity-100 translate-y-0 scale-100"
          leave-active-class="transition-all duration-200 ease-in"
          leave-from-class="opacity-100 translate-y-0 scale-100"
          leave-to-class="opacity-0 translate-y-2 scale-95"
        >
          <div v-if="error" class="flex items-center gap-3 p-4 bg-rose-500/10 border border-rose-500/20 rounded-xl shadow-inner">
            <div class="w-8 h-8 rounded-full bg-rose-500/20 flex items-center justify-center text-rose-400 shrink-0">
              <AlertCircle :size="16" />
            </div>
            <span class="text-sm font-bold text-rose-300">{{ error }}</span>
          </div>
        </Transition>
      </form>

      <div class="h-px bg-white/5 w-full"></div>

      <!-- ACCOUNT METRICS (Bento Box) -->
      <div>
        <h3 class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-4 ml-1">Account Telemetry</h3>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          
          <!-- Member Since -->
          <div class="p-6 bg-slate-950/50 rounded-2xl border border-white/5 flex items-center gap-4 hover:border-teal-500/30 transition-colors group">
            <div class="w-12 h-12 rounded-xl bg-teal-500/10 border border-teal-500/20 flex items-center justify-center text-teal-400 shrink-0 group-hover:scale-110 transition-transform shadow-inner">
              <Calendar :size="20" />
            </div>
            <div>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-0.5">Member Since</p>
              <p class="text-lg font-extrabold text-white">{{ formatDate(form.created_at) }}</p>
            </div>
          </div>

          <!-- Last Updated -->
          <div class="p-6 bg-slate-950/50 rounded-2xl border border-white/5 flex items-center gap-4 hover:border-blue-500/30 transition-colors group">
            <div class="w-12 h-12 rounded-xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400 shrink-0 group-hover:scale-110 transition-transform shadow-inner">
              <RefreshCw :size="20" />
            </div>
            <div>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-0.5">Last Sync</p>
              <p class="text-lg font-extrabold text-white">{{ formatDate(form.updated_at) }}</p>
            </div>
          </div>

          <!-- Total Items -->
          <div class="p-6 bg-slate-950/50 rounded-2xl border border-white/5 flex items-center gap-4 hover:border-purple-500/30 transition-colors group">
            <div class="w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400 shrink-0 group-hover:scale-110 transition-transform shadow-inner">
              <Package :size="20" />
            </div>
            <div>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-0.5">Vault Items</p>
              <p class="text-2xl font-extrabold text-white">{{ stats.total_items }}</p>
            </div>
          </div>

          <!-- Subscriptions -->
          <div class="p-6 bg-slate-950/50 rounded-2xl border border-white/5 flex items-center gap-4 hover:border-orange-500/30 transition-colors group">
            <div class="w-12 h-12 rounded-xl bg-orange-500/10 border border-orange-500/20 flex items-center justify-center text-orange-400 shrink-0 group-hover:scale-110 transition-transform shadow-inner">
              <Repeat :size="20" />
            </div>
            <div>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-0.5">Active Subs</p>
              <p class="text-2xl font-extrabold text-white">{{ stats.active_subscriptions }}</p>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { apiFetch } from "../../utils/api"
import { User, Mail, Calendar, RefreshCw, Package, Repeat, Save, CheckCircle2, AlertCircle, Info, Loader2 } from "lucide-vue-next"

const form = ref({ full_name: "", email: "", created_at: "", updated_at: "" })
const stats = ref({ total_items: 0, active_subscriptions: 0 })
const originalForm = ref({})
const saving = ref(false)
const saveSuccess = ref(false)
const error = ref("")
const loading = ref(true)

const hasChanges = computed(() => JSON.stringify(form.value) !== JSON.stringify(originalForm.value))

onMounted(async () => {
  await loadProfile()
  await loadStats()
})

async function loadProfile() {
  try {
    const res = await apiFetch("/auth/me")
    if (!res.ok) throw new Error("Failed to fetch profile")
    const data = await res.json()
    form.value = {
      full_name: data.full_name || data.name || "",
      email: data.email || "",
      created_at: data.created_at || new Date().toISOString(),
      updated_at: data.updated_at || new Date().toISOString()
    }
    originalForm.value = JSON.parse(JSON.stringify(form.value))
  } catch (err) {
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
      stats.value = { total_items: data.total_items || 0, active_subscriptions: data.active_subscriptions || 0 }
    }
  } catch (err) {}
}

async function save() {
  saving.value = true; error.value = ""; saveSuccess.value = false
  try {
    const res = await apiFetch("/auth/me", { method: "PUT", body: JSON.stringify({ full_name: form.value.full_name }) })
    if (!res.ok) throw new Error("Failed to update profile")
    const data = await res.json()
    form.value.updated_at = data.updated_at || new Date().toISOString()
    originalForm.value = JSON.parse(JSON.stringify(form.value))
    saveSuccess.value = true
    setTimeout(() => { saveSuccess.value = false }, 3000)
  } catch (err) {
    error.value = "Failed to update profile. Please try again."
    setTimeout(() => { error.value = "" }, 5000)
  } finally {
    saving.value = false
  }
}

function resetForm() { form.value = JSON.parse(JSON.stringify(originalForm.value)) }

function formatDate(dateString) {
  if (!dateString) return "N/A"
  return new Date(dateString).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
}
</script>