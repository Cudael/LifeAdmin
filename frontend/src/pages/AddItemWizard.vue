<template>
  <DashboardLayout pageTitle="New Vault Item">

    <!-- Ambient Background Mesh -->
    <div class="fixed inset-0 z-0 bg-[linear-gradient(to_right,#80808008_1px,transparent_1px),linear-gradient(to_bottom,#80808008_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none"></div>
    <div class="fixed top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-teal-500/10 blur-[150px] rounded-full pointer-events-none z-0 mix-blend-screen"></div>

    <div class="relative z-10 max-w-3xl mx-auto pb-12 w-full animate-fade-in-up">

      <!-- Breadcrumb -->
      <div class="mb-8 flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-slate-500">
        <RouterLink to="/dashboard" class="hover:text-teal-400 transition-colors">Dashboard</RouterLink>
        <ChevronRight :size="14" />
        <RouterLink to="/items" class="hover:text-teal-400 transition-colors">Vault</RouterLink>
        <ChevronRight :size="14" />
        <span class="text-teal-400">Add Item</span>
      </div>

      <!-- ✅ VERIFICATION REQUIRED GUARD -->
      <div v-if="user && !isVerified" class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-orange-500/20 p-10 text-center shadow-2xl relative overflow-hidden">
        <div class="absolute top-0 right-0 w-64 h-64 bg-orange-500/10 blur-[80px] rounded-full"></div>
        <div class="w-20 h-20 bg-orange-500/10 border border-orange-500/20 rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-inner relative z-10">
          <ShieldAlert :size="32" class="text-orange-400" />
        </div>
        <h3 class="text-2xl font-extrabold text-white mb-3 tracking-tight relative z-10">Email Verification Required</h3>
        <p class="text-slate-400 mb-8 max-w-md mx-auto relative z-10">
          Please verify your email address to add items to your secure vault. Check your inbox for the verification link.
        </p>
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4 relative z-10">
          <button
            @click="resendVerification"
            :disabled="resending"
            class="px-6 py-3.5 bg-gradient-to-r from-orange-500 to-amber-500 text-slate-950 rounded-xl font-bold hover:shadow-[0_0_20px_rgba(249,115,22,0.4)] transition-all disabled:opacity-50 flex items-center gap-2"
          >
            <Loader2 v-if="resending" :size="18" class="animate-spin" />
            <Mail v-else :size="18" />
            {{ resending ? 'Sending...' : 'Resend Email' }}
          </button>
          <RouterLink to="/items" class="px-6 py-3.5 bg-white/5 border border-white/10 text-white rounded-xl font-bold hover:bg-white/10 transition-colors">
            Back to Vault
          </RouterLink>
        </div>
      </div>

      <!-- ✅ WIZARD CONTENT -->
      <div v-else-if="user" class="relative">
        
        <!-- Header & Sleek Progress Bar -->
        <div class="mb-8">
          <div class="flex items-end justify-between mb-6">
            <div>
              <h1 class="text-3xl font-extrabold text-white tracking-tight mb-2">{{ currentStepTitle }}</h1>
              <p class="text-slate-400 font-medium">{{ currentStepDescription }}</p>
            </div>
            <div class="hidden sm:flex items-center gap-2 bg-slate-900/80 border border-white/5 px-4 py-2 rounded-xl backdrop-blur-md shadow-inner">
              <span class="text-xs font-bold uppercase tracking-widest text-slate-500">Step</span>
              <span class="text-lg font-extrabold text-teal-400">{{ currentStep }}</span>
              <span class="text-sm font-bold text-slate-600">/ 3</span>
            </div>
          </div>

          <!-- Segmented Progress Bar -->
          <div class="flex gap-2 h-1.5">
            <div class="flex-1 rounded-full overflow-hidden bg-slate-800">
              <div class="h-full bg-teal-400 transition-all duration-500" :class="currentStep >= 1 ? 'w-full shadow-[0_0_10px_rgba(45,212,191,0.8)]' : 'w-0'"></div>
            </div>
            <div class="flex-1 rounded-full overflow-hidden bg-slate-800">
              <div class="h-full bg-teal-400 transition-all duration-500" :class="currentStep >= 2 ? 'w-full shadow-[0_0_10px_rgba(45,212,191,0.8)]' : 'w-0'"></div>
            </div>
            <div class="flex-1 rounded-full overflow-hidden bg-slate-800">
              <div class="h-full bg-teal-400 transition-all duration-500" :class="currentStep >= 3 ? 'w-full shadow-[0_0_10px_rgba(45,212,191,0.8)]' : 'w-0'"></div>
            </div>
          </div>
        </div>

        <!-- Main Form Canvas -->
        <div class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 p-6 sm:p-10 shadow-2xl relative overflow-hidden">
          
          <!-- Top Glow Edge -->
          <div class="absolute top-0 left-0 right-0 h-px flex justify-center opacity-50">
            <div class="h-full w-3/4 bg-gradient-to-r from-transparent via-teal-400 to-transparent"></div>
          </div>

          <!-- ERROR MESSAGE -->
          <Transition
            enter-active-class="transition-all duration-300 ease-out"
            enter-from-class="opacity-0 -translate-y-2"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition-all duration-200 ease-in"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 -translate-y-2"
          >
            <div v-if="errorMessage" class="mb-8 p-4 bg-rose-500/10 border border-rose-500/20 rounded-2xl flex items-center gap-3">
              <div class="w-8 h-8 rounded-full bg-rose-500/20 flex items-center justify-center shrink-0 text-rose-400">
                <AlertCircle :size="16" />
              </div>
              <p class="text-sm font-bold text-rose-300">{{ errorMessage }}</p>
            </div>
          </Transition>

          <!-- Step Transitions -->
          <div class="relative min-h-[400px]">
            <Transition
              name="fade-slide"
              mode="out-in"
            >
              <!-- STEP 1 -->
              <div v-if="currentStep === 1" :key="'step1'">
                <Step1GeneralInfo
                  v-model:category="formData.category"
                  v-model:itemTypeName="formData.itemTypeName"
                  v-model:name="formData.name"
                  :categories="categories"
                  :itemTypes="filteredItemTypes"
                  :loading="loading"
                />
              </div>

              <!-- STEP 2 -->
              <div v-else-if="currentStep === 2" :key="'step2'">
                <Step2DynamicFields
                  v-model:dynamicFields="formData.dynamicFields"
                  v-model:file="formData.file"
                  v-model:notes="formData.notes"
                  v-model:reminderDaysBefore="formData.reminderDaysBefore"
                  :selectedItemType="selectedItemType"
                  :userDefaultReminderDays="userDefaultReminderDays"
                  :loading="loading"
                />
              </div>

              <!-- STEP 3 -->
              <div v-else-if="currentStep === 3" :key="'step3'">
                <Step3Review
                  :formData="formData"
                  :selectedItemType="selectedItemType"
                />
              </div>
            </Transition>
          </div>

          <!-- Bottom Navigation Bar -->
          <div class="mt-10 pt-6 border-t border-white/5 flex items-center justify-between gap-4">
            <button
              type="button"
              @click="handleBack"
              class="px-6 py-3.5 bg-white/5 hover:bg-white/10 border border-white/5 text-white rounded-xl font-bold transition-all duration-200 flex items-center gap-2"
            >
              <ArrowLeft :size="16" v-if="currentStep > 1" />
              {{ currentStep === 1 ? 'Cancel' : 'Back' }}
            </button>
            
            <button
              v-if="currentStep < 3"
              type="button"
              @click="goToStep(currentStep + 1)"
              :disabled="(currentStep === 1 && !canProceedFromStep1) || (currentStep === 2 && !canProceedFromStep2)"
              class="group px-8 py-3.5 bg-slate-50 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(255,255,255,0.1)] hover:bg-white hover:shadow-[0_0_25px_rgba(255,255,255,0.2)] transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              Continue
              <ArrowRight :size="16" class="text-teal-600 group-hover:translate-x-1 transition-transform" />
            </button>

            <button
              v-else
              type="button"
              @click="handleSubmit"
              :disabled="loading"
              class="group px-8 py-3.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.3)] hover:shadow-[0_0_30px_rgba(45,212,191,0.5)] transition-all duration-300 disabled:opacity-50 flex items-center gap-2"
            >
              <Loader2 v-if="loading" :size="18" class="animate-spin" />
              <CheckCircle2 v-else :size="18" />
              {{ loading ? 'Securing Item...' : 'Confirm & Save' }}
            </button>
          </div>

        </div>
      </div>

      <!-- Loading State -->
      <div v-else class="flex flex-col items-center justify-center py-32">
        <div class="w-16 h-16 bg-teal-500/10 rounded-2xl flex items-center justify-center mb-4 border border-teal-500/20 shadow-inner">
          <Loader2 :size="32" class="animate-spin text-teal-400" />
        </div>
        <p class="text-slate-400 font-medium tracking-wide">Initializing secure canvas...</p>
      </div>

    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import Step1GeneralInfo from "../components/wizard/Step1GeneralInfo.vue"
import Step2DynamicFields from "../components/wizard/Step2DynamicFields.vue"
import Step3Review from "../components/wizard/Step3Review.vue"
import { apiFetch } from "../utils/api"
import { CheckCircle2, ArrowRight, ArrowLeft, AlertCircle, Loader2, ChevronRight, ShieldAlert, Mail } from "lucide-vue-next"

const router = useRouter()

const user = ref(null)
const isVerified = computed(() => user.value?.email_verified || false)
const resending = ref(false)
const userDefaultReminderDays = computed(() => user.value?.notification_days_before || 7)

const currentStep = ref(1)
const loading = ref(false)
const errorMessage = ref("")

const categories = ref([])
const itemTypes = ref([])

const formData = ref({
  category: "",
  itemTypeName: "",
  itemTypeId: null,
  name: "",
  dynamicFields: {},
  file: null,
  notes: "",
  reminderDaysBefore: null
})

const currentStepTitle = computed(() => {
  if (currentStep.value === 1) return "Classification"
  if (currentStep.value === 2) return "Item Details"
  return "Review & Confirm"
})

const currentStepDescription = computed(() => {
  if (currentStep.value === 1) return "Define the category and type of asset."
  if (currentStep.value === 2) return "Provide the secure metadata for your record."
  return "Verify the data before encrypting it into your vault."
})

const filteredItemTypes = computed(() => {
  if (!formData.value.category) return []
  return itemTypes.value.filter(type => type.category === formData.value.category)
})

const selectedItemType = computed(() => {
  if (!formData.value.itemTypeName) return null
  return itemTypes.value.find(type => type.name === formData.value.itemTypeName)
})

const canProceedFromStep1 = computed(() => {
  return formData.value.category && formData.value.itemTypeName && formData.value.name.trim().length >= 2
})

const canProceedFromStep2 = computed(() => {
  if (!selectedItemType.value) return false
  for (const field of selectedItemType.value.fields) {
    if (field.required) {
      const value = formData.value.dynamicFields[field.name]
      if (!value || (typeof value === 'string' && value.trim() === '')) {
        return false
      }
    }
  }
  return true
})

onMounted(async () => {
  await Promise.all([ loadUser(), loadItemTypes(), loadCategories() ])
})

async function loadUser() {
  try {
    const res = await apiFetch("/auth/me")
    if (!res) return
    const contentType = res.headers.get("content-type") || ""
    if (res.ok && contentType.includes("application/json")) {
      user.value = await res.json()
    }
  } catch (err) {}
}

async function loadItemTypes() {
  try {
    const res = await apiFetch("/item-types")
    if (!res) return
    const data = await res.json()
    itemTypes.value = data.item_types || []
  } catch (err) {}
}

async function loadCategories() {
  try {
    const res = await apiFetch("/item-types/categories")
    if (!res) return
    const data = await res.json()
    categories.value = Object.keys(data.categories || {})
  } catch (err) {}
}

async function resendVerification() {
  resending.value = true
  try {
    const res = await apiFetch("/auth/resend-verification", { method: "POST" })
    if (res.ok) alert("Verification email sent! Check your inbox.")
    else alert((await res.json()).detail || "Failed to send verification email")
  } catch (err) {
    alert("Something went wrong. Please try again.")
  } finally {
    resending.value = false
  }
}

function goToStep(step) {
  if (step === 2 && !canProceedFromStep1.value) return (errorMessage.value = "Please fill in all required fields")
  if (step === 3 && !canProceedFromStep2.value) return (errorMessage.value = "Please fill in all required fields")
  
  errorMessage.value = ""
  currentStep.value = step
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function handleBack() {
  if (currentStep.value === 1) router.back()
  else goToStep(currentStep.value - 1)
}

async function handleSubmit() {
  errorMessage.value = ""
  loading.value = true
  try {
    const formPayload = new FormData()
    formPayload.append("name", formData.value.name.trim())
    formPayload.append("category", formData.value.category)
    formPayload.append("type", selectedItemType.value.item_class)
    if (selectedItemType.value) {
      formPayload.append("item_type_id", selectedItemType.value.id)
      formPayload.append("item_type_name", selectedItemType.value.name)
    }
    formPayload.append("dynamic_fields", JSON.stringify(formData.value.dynamicFields))
    if (formData.value.notes) formPayload.append("notes", formData.value.notes.trim())
    if (formData.value.reminderDaysBefore !== null) formPayload.append("reminder_days_before", formData.value.reminderDaysBefore.toString())
    if (formData.value.file) formPayload.append("file", formData.value.file)

    const res = await apiFetch("/items/upload", { method: "POST", body: formPayload })
    if (!res.ok) {
      errorMessage.value = (await res.json()).detail || "Failed to create item"
      loading.value = false
      return
    }
    router.push("/items")
  } catch (err) {
    errorMessage.value = "Something went wrong. Please try again."
    loading.value = false
  }
}
</script>

<style scoped>
/* Smooth sliding transitions for wizard steps */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateX(15px);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateX(-15px);
}

@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
  animation: fade-in-up 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>