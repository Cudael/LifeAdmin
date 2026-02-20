<template>
  <div class="space-y-10">

    <!-- LOCALIZATION (DATE & TIME) -->
    <div>
      <h3 class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-6 ml-1">Localization</h3>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- Date Format -->
        <div class="space-y-3">
          <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
            Date Format
          </label>
          <div class="relative group/select">
            <select
              v-model="preferences.date_format"
              class="w-full bg-slate-950/50 border border-white/10 text-white rounded-xl pl-4 pr-10 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300 appearance-none cursor-pointer hover:border-white/20 font-medium"
            >
              <option value="MM/DD/YYYY" class="bg-slate-900">MM/DD/YYYY (US Standard)</option>
              <option value="DD/MM/YYYY" class="bg-slate-900">DD/MM/YYYY (Global Format)</option>
              <option value="YYYY-MM-DD" class="bg-slate-900">YYYY-MM-DD (ISO 8601)</option>
            </select>
            <div class="absolute inset-y-0 right-4 flex items-center pointer-events-none text-slate-500 group-hover/select:text-white transition-colors">
              <ChevronDown :size="16" />
            </div>
          </div>
        </div>

        <!-- Time Format -->
        <div class="space-y-3">
          <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
            Time Format
          </label>
          <div class="flex gap-2 p-1.5 bg-slate-900 rounded-xl border border-white/5 shadow-inner h-[54px]">
            <button
              @click="preferences.time_format = '12h'"
              class="flex-1 rounded-lg font-bold transition-all duration-300 text-sm flex items-center justify-center gap-2"
              :class="preferences.time_format === '12h'
                ? 'bg-teal-500 text-slate-950 shadow-[0_0_15px_rgba(45,212,191,0.3)] border border-teal-400'
                : 'text-slate-400 hover:text-white hover:bg-white/5 border border-transparent'"
            >
              <Clock :size="16" />
              12-Hour
            </button>
            <button
              @click="preferences.time_format = '24h'"
              class="flex-1 rounded-lg font-bold transition-all duration-300 text-sm flex items-center justify-center gap-2"
              :class="preferences.time_format === '24h'
                ? 'bg-teal-500 text-slate-950 shadow-[0_0_15px_rgba(45,212,191,0.3)] border border-teal-400'
                : 'text-slate-400 hover:text-white hover:bg-white/5 border border-transparent'"
            >
              <Clock :size="16" />
              24-Hour
            </button>
          </div>
        </div>

      </div>

      <!-- Preview Box -->
      <div class="mt-6 p-6 bg-slate-950/30 rounded-2xl border border-white/5 flex items-center justify-between">
        <div>
          <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-1">Live Preview</p>
          <div class="flex items-center gap-6">
            <div class="flex items-center gap-2">
              <Calendar :size="16" class="text-teal-400" />
              <span class="text-white font-bold tracking-wide">{{ previewDate }}</span>
            </div>
            <div class="flex items-center gap-2">
              <Clock :size="16" class="text-cyan-400" />
              <span class="text-white font-bold tracking-wide">{{ previewTime }}</span>
            </div>
          </div>
        </div>
      </div>

    </div>

    <div class="h-px bg-white/5 w-full"></div>

    <!-- DISPLAY SETTINGS -->
    <div>
      <h3 class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-6 ml-1">Vault Display</h3>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- Items per page -->
        <div class="space-y-3">
          <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
            Pagination Limit
          </label>
          <div class="relative group/select">
            <select
              v-model="preferences.items_per_page"
              class="w-full bg-slate-950/50 border border-white/10 text-white rounded-xl pl-4 pr-10 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300 appearance-none cursor-pointer hover:border-white/20 font-medium"
            >
              <option :value="10" class="bg-slate-900">10 Items per page</option>
              <option :value="25" class="bg-slate-900">25 Items per page</option>
              <option :value="50" class="bg-slate-900">50 Items per page</option>
              <option :value="100" class="bg-slate-900">100 Items per page</option>
            </select>
            <div class="absolute inset-y-0 right-4 flex items-center pointer-events-none text-slate-500 group-hover/select:text-white transition-colors">
              <ChevronDown :size="16" />
            </div>
          </div>
        </div>

        <!-- Default Sort -->
        <div class="space-y-3">
          <label class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
            Default Matrix Sort
          </label>
          <div class="relative group/select">
            <select
              v-model="preferences.default_sort"
              class="w-full bg-slate-950/50 border border-white/10 text-white rounded-xl pl-4 pr-10 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300 appearance-none cursor-pointer hover:border-white/20 font-medium"
            >
              <option value="expiration_asc" class="bg-slate-900">Expiring Soonest First (Recommended)</option>
              <option value="expiration_desc" class="bg-slate-900">Expiring Latest First</option>
              <option value="name_asc" class="bg-slate-900">Alphabetical (A-Z)</option>
              <option value="name_desc" class="bg-slate-900">Alphabetical (Z-A)</option>
              <option value="created_desc" class="bg-slate-900">Recently Added First</option>
              <option value="created_asc" class="bg-slate-900">Oldest Added First</option>
            </select>
            <div class="absolute inset-y-0 right-4 flex items-center pointer-events-none text-slate-500 group-hover/select:text-white transition-colors">
              <ChevronDown :size="16" />
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- SAVE BUTTONS -->
    <div class="flex items-center gap-4 pt-4 border-t border-white/5">
      <button
        @click="savePreferences"
        :disabled="saving || !hasChanges"
        class="group px-6 py-3.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.2)] hover:shadow-[0_0_30px_rgba(45,212,191,0.4)] transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
      >
        <Loader2 :size="18" class="animate-spin" v-if="saving" />
        <Save :size="18" class="group-hover:scale-110 transition-transform" v-else />
        {{ saving ? 'Saving...' : 'Save Configuration' }}
      </button>

      <button
        v-if="hasChanges"
        @click="resetPreferences"
        :disabled="saving"
        class="px-6 py-3.5 bg-white/5 hover:bg-white/10 border border-white/5 text-white rounded-xl font-bold transition-all duration-200 disabled:opacity-50"
      >
        Discard Changes
      </button>
    </div>

    <!-- Success Message -->
    <Transition enter-active-class="transition-all duration-300" enter-from-class="opacity-0 translate-y-2 scale-95" leave-active-class="transition-all duration-200" leave-to-class="opacity-0 translate-y-2 scale-95">
      <div v-if="saveSuccess" class="flex items-center gap-3 p-4 bg-emerald-500/10 border border-emerald-500/20 rounded-xl shadow-inner">
        <div class="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400 shrink-0"><CheckCircle2 :size="16" /></div>
        <span class="text-sm font-bold text-emerald-300">Display configuration saved successfully.</span>
      </div>
    </Transition>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { apiFetch } from "../../utils/api"
import { Calendar, Clock, Save, CheckCircle2, Loader2, ChevronDown } from "lucide-vue-next"

const preferences = ref({
  date_format: 'MM/DD/YYYY',
  time_format: '12h',
  items_per_page: 25,
  default_sort: 'expiration_asc'
})

const originalPreferences = ref({})
const saving = ref(false)
const saveSuccess = ref(false)

const hasChanges = computed(() => JSON.stringify(preferences.value) !== JSON.stringify(originalPreferences.value))

const previewDate = computed(() => {
  switch(preferences.value.date_format) {
    case 'MM/DD/YYYY': return '02/14/2026'
    case 'DD/MM/YYYY': return '14/02/2026'
    case 'YYYY-MM-DD': return '2026-02-14'
    default: return '02/14/2026'
  }
})

const previewTime = computed(() => preferences.value.time_format === '12h' ? '2:30 PM' : '14:30')

onMounted(async () => { await loadPreferences() })

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
  } catch (err) {}
}

async function savePreferences() {
  saving.value = true; saveSuccess.value = false
  try {
    const res = await apiFetch('/auth/preferences', { method: 'PUT', body: JSON.stringify(preferences.value) })
    if (!res.ok) throw new Error('Failed to save preferences')
    originalPreferences.value = JSON.parse(JSON.stringify(preferences.value))
    saveSuccess.value = true
    setTimeout(() => { saveSuccess.value = false }, 3000)
  } catch (err) {} finally { saving.value = false }
}

function resetPreferences() { preferences.value = JSON.parse(JSON.stringify(originalPreferences.value)) }
</script>