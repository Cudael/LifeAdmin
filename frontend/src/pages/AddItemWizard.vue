<template>
  <DashboardLayout pageTitle="Add Item">

    <!-- Breadcrumb -->
    <div class="mb-6">
      <div class="flex items-center gap-2 text-sm text-gray-600">
        <RouterLink to="/dashboard" class="hover:text-teal-600 transition-colors">Dashboard</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink to="/items" class="hover:text-teal-600 transition-colors">Items</RouterLink>
        <ChevronRight :size="16" />
        <span class="text-gray-900 font-medium">Add Item</span>
      </div>
    </div>

    <!-- Header Section -->
    <div class="relative mb-8 p-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-3xl shadow-xl text-white overflow-hidden">
      
      <!-- Decorative elements -->
      <div class="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
      <div class="absolute bottom-0 left-0 w-48 h-48 bg-white/10 rounded-full translate-y-1/2 -translate-x-1/2"></div>

      <div class="relative z-10 text-center">
        <div class="w-16 h-16 mx-auto mb-4 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center">
          <component :is="currentStepIcon" :size="32" class="text-white" />
        </div>
        <h2 class="text-3xl font-bold mb-2">{{ currentStepTitle }}</h2>
        <p class="text-white/90 text-lg">
          {{ currentStepDescription }}
        </p>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-4xl mx-auto">

      <!-- Back Button -->
      <button
        @click="handleBack"
        class="group mb-6 inline-flex items-center gap-2 px-4 py-2 bg-white border-2 border-gray-200 rounded-xl shadow-sm hover:border-teal-300 hover:shadow-md transition-all duration-200"
      >
        <ArrowLeft :size="18" class="group-hover:-translate-x-1 transition-transform" />
        <span class="font-medium text-gray-700">{{ currentStep === 1 ? 'Cancel' : 'Back' }}</span>
      </button>

      <!-- Progress Steps -->
      <div class="mb-8 px-4">
        <div class="flex items-center justify-between relative">
          <!-- Progress Line -->
          <div class="absolute top-4 left-0 right-0 h-1 bg-gray-200 -z-10">
            <div 
              class="h-full bg-gradient-to-r from-teal-500 to-cyan-500 transition-all duration-500"
              :style="{ width: `${((currentStep - 1) / 2) * 100}%` }"
            ></div>
          </div>

          <!-- Step 1 -->
          <div class="flex flex-col items-center">
            <div 
              :class="[
                'w-8 h-8 rounded-full flex items-center justify-center font-semibold text-sm transition-all duration-300',
                currentStep >= 1 
                  ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white shadow-lg' 
                  : 'bg-gray-200 text-gray-500'
              ]"
            >
              <CheckCircle2 v-if="currentStep > 1" :size="18" />
              <span v-else>1</span>
            </div>
            <span class="text-xs mt-2 font-medium text-gray-700">Details</span>
          </div>

          <!-- Step 2 -->
          <div class="flex flex-col items-center">
            <div 
              :class="[
                'w-8 h-8 rounded-full flex items-center justify-center font-semibold text-sm transition-all duration-300',
                currentStep >= 2 
                  ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white shadow-lg' 
                  : 'bg-gray-200 text-gray-500'
              ]"
            >
              <CheckCircle2 v-if="currentStep > 2" :size="18" />
              <span v-else>2</span>
            </div>
            <span class="text-xs mt-2 font-medium text-gray-700">Fields</span>
          </div>

          <!-- Step 3 -->
          <div class="flex flex-col items-center">
            <div 
              :class="[
                'w-8 h-8 rounded-full flex items-center justify-center font-semibold text-sm transition-all duration-300',
                currentStep >= 3 
                  ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white shadow-lg' 
                  : 'bg-gray-200 text-gray-500'
              ]"
            >
              3
            </div>
            <span class="text-xs mt-2 font-medium text-gray-700">Review</span>
          </div>
        </div>
      </div>

      <!-- ✅ VERIFICATION REQUIRED GUARD -->
      <div v-if="user && !isVerified" class="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl border-2 border-orange-200 p-8 md:p-10">
        <div class="text-center py-8">
          <div class="w-20 h-20 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <ShieldAlert :size="40" class="text-orange-600" />
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-3">Email Verification Required</h3>
          <p class="text-gray-600 mb-6 max-w-md mx-auto">
            Please verify your email address to add items. Check your inbox for the verification link.
          </p>
          
          <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
            <button
              @click="resendVerification"
              :disabled="resending"
              class="px-6 py-3 bg-gradient-to-r from-orange-500 to-amber-500 text-white rounded-xl font-semibold hover:shadow-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              <Loader2 v-if="resending" :size="20" class="animate-spin" />
              <Mail v-else :size="20" />
              {{ resending ? 'Sending...' : 'Resend Verification Email' }}
            </button>
            
            <RouterLink
              to="/items"
              class="px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-colors"
            >
              Back to Items
            </RouterLink>
          </div>
        </div>
      </div>

      <!-- ✅ WIZARD CONTENT (Only show if verified) -->
      <div v-else-if="user" class="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl border-2 border-gray-100 p-8 md:p-10">

        <!-- ERROR MESSAGE -->
        <Transition
          enter-active-class="transition-all duration-300 ease-out"
          enter-from-class="opacity-0 -translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition-all duration-200 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 -translate-y-2"
        >
          <div
            v-if="errorMessage"
            class="mb-6 p-4 bg-red-50 border-2 border-red-200 rounded-xl flex items-start gap-3 animate-shake"
          >
            <AlertCircle :size="20" class="text-red-500 flex-shrink-0 mt-0.5" />
            <p class="text-sm text-red-700">{{ errorMessage }}</p>
          </div>
        </Transition>

        <!-- STEP 1: General Information -->
        <div v-if="currentStep === 1" class="space-y-6">
          <Step1GeneralInfo
            v-model:category="formData.category"
            v-model:itemTypeName="formData.itemTypeName"
            v-model:name="formData.name"
            :categories="categories"
            :itemTypes="filteredItemTypes"
            :loading="loading"
          />

          <!-- Navigation -->
          <div class="flex gap-4 pt-4">
            <button
              type="button"
              @click="$router.back()"
              class="flex-1 px-6 py-4 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
            >
              Cancel
            </button>
            <button
              type="button"
              @click="goToStep(2)"
              :disabled="!canProceedFromStep1"
              class="group flex-1 px-6 py-4 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              Next Step
              <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
            </button>
          </div>
        </div>

        <!-- STEP 2: Dynamic Fields -->
        <div v-if="currentStep === 2" class="space-y-6">
          <Step2DynamicFields
            v-model:dynamicFields="formData.dynamicFields"
            v-model:file="formData.file"
            v-model:notes="formData.notes"
            v-model:reminderDaysBefore="formData.reminderDaysBefore"
            :selectedItemType="selectedItemType"
            :userDefaultReminderDays="userDefaultReminderDays"
            :loading="loading"
          />

          <!-- Navigation -->
          <div class="flex gap-4 pt-4">
            <button
              type="button"
              @click="goToStep(1)"
              class="flex-1 px-6 py-4 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
            >
              Back
            </button>
            <button
              type="button"
              @click="goToStep(3)"
              :disabled="!canProceedFromStep2"
              class="group flex-1 px-6 py-4 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              Review
              <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
            </button>
          </div>
        </div>

        <!-- STEP 3: Review and Submit -->
        <div v-if="currentStep === 3" class="space-y-6">
          <Step3Review
            :formData="formData"
            :selectedItemType="selectedItemType"
          />

          <!-- Navigation -->
          <div class="flex gap-4 pt-4">
            <button
              type="button"
              @click="goToStep(2)"
              :disabled="loading"
              class="flex-1 px-6 py-4 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200 disabled:opacity-50"
            >
              Back
            </button>
            <button
              type="button"
              @click="handleSubmit"
              :disabled="loading"
              class="group flex-1 px-6 py-4 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <span v-if="!loading" class="flex items-center gap-2">
                <CheckCircle2 :size="20" />
                Create Item
              </span>
              <span v-else class="flex items-center gap-3">
                <Loader2 :size="20" class="animate-spin" />
                Creating...
              </span>
            </button>
          </div>
        </div>

      </div>

      <!-- Loading State -->
      <div v-else class="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl border-2 border-gray-100 p-8 md:p-10">
        <div class="text-center py-12">
          <Loader2 :size="48" class="animate-spin text-teal-500 mx-auto mb-4" />
          <p class="text-gray-600">Loading...</p>
        </div>
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
import {
  FileText,
  List,
  CheckCircle2,
  ArrowRight,
  ArrowLeft,
  AlertCircle,
  Loader2,
  ChevronRight,
  ShieldAlert,
  Mail
} from "lucide-vue-next"

const router = useRouter()

// User state
const user = ref(null)
const isVerified = computed(() => user.value?.email_verified || false)
const resending = ref(false)
const userDefaultReminderDays = computed(() => user.value?.notification_days_before || 7)

// Wizard state
const currentStep = ref(1)
const loading = ref(false)
const errorMessage = ref("")

// Categories and item types
const categories = ref([])
const itemTypes = ref([])

// Form data
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

// Computed
const currentStepIcon = computed(() => {
  if (currentStep.value === 1) return List
  if (currentStep.value === 2) return FileText
  return CheckCircle2
})

const currentStepTitle = computed(() => {
  if (currentStep.value === 1) return "General Information"
  if (currentStep.value === 2) return "Item Details"
  return "Review & Confirm"
})

const currentStepDescription = computed(() => {
  if (currentStep.value === 1) return "Choose a category and type for your item"
  if (currentStep.value === 2) return "Fill in the specific fields for this item"
  return "Review your information before saving"
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
  // Check if all required fields are filled
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

// Methods
onMounted(async () => {
  await Promise.all([
    loadUser(),
    loadItemTypes(),
    loadCategories()
  ])
})

async function loadUser() {
  try {
    const res = await apiFetch("/auth/me")
    if (res.ok) {
      user.value = await res.json()
    }
  } catch (err) {
    console.error("Failed to load user:", err)
  }
}

async function loadItemTypes() {
  try {
    const res = await apiFetch("/item-types")
    if (res.ok) {
      const data = await res.json()
      itemTypes.value = data.item_types || []
    }
  } catch (err) {
    console.error("Failed to load item types:", err)
  }
}

async function loadCategories() {
  try {
    const res = await apiFetch("/item-types/categories")
    if (res.ok) {
      const data = await res.json()
      categories.value = Object.keys(data.categories || {})
    }
  } catch (err) {
    console.error("Failed to load categories:", err)
  }
}

async function resendVerification() {
  resending.value = true
  
  try {
    const res = await apiFetch("/auth/resend-verification", {
      method: "POST"
    })

    if (res.ok) {
      alert("Verification email sent! Check your inbox.")
    } else {
      const data = await res.json()
      alert(data.detail || "Failed to send verification email")
    }
  } catch (err) {
    console.error("Resend verification error:", err)
    alert("Something went wrong. Please try again.")
  } finally {
    resending.value = false
  }
}

function goToStep(step) {
  if (step === 2 && !canProceedFromStep1.value) {
    errorMessage.value = "Please fill in all required fields"
    return
  }
  
  if (step === 3 && !canProceedFromStep2.value) {
    errorMessage.value = "Please fill in all required fields"
    return
  }
  
  errorMessage.value = ""
  currentStep.value = step
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function handleBack() {
  if (currentStep.value === 1) {
    router.back()
  } else {
    goToStep(currentStep.value - 1)
  }
}

async function handleSubmit() {
  errorMessage.value = ""
  loading.value = true

  try {
    const formPayload = new FormData()
    
    // Basic fields
    formPayload.append("name", formData.value.name.trim())
    formPayload.append("category", formData.value.category)
    formPayload.append("type", selectedItemType.value.item_class)
    
    // Item type info
    if (selectedItemType.value) {
      formPayload.append("item_type_id", selectedItemType.value.id)
      formPayload.append("item_type_name", selectedItemType.value.name)
    }
    
    // Dynamic fields as JSON
    formPayload.append("dynamic_fields", JSON.stringify(formData.value.dynamicFields))
    
    // Notes
    if (formData.value.notes) {
      formPayload.append("notes", formData.value.notes.trim())
    }
    
    // Reminder days
    if (formData.value.reminderDaysBefore !== null) {
      formPayload.append("reminder_days_before", formData.value.reminderDaysBefore.toString())
    }
    
    // File
    if (formData.value.file) {
      formPayload.append("file", formData.value.file)
    }

    const res = await apiFetch("/items/upload", {
      method: "POST",
      body: formPayload
    })

    if (!res.ok) {
      const data = await res.json()
      errorMessage.value = data.detail || "Failed to create item"
      loading.value = false
      return
    }

    // Success - redirect to items page
    router.push("/items")

  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong. Please try again."
    loading.value = false
  }
}
</script>

<style scoped>
@keyframes shake {
  0%, 100% {
    transform: translateX(0);
  }
  10%, 30%, 50%, 70%, 90% {
    transform: translateX(-5px);
  }
  20%, 40%, 60%, 80% {
    transform: translateX(5px);
  }
}

.animate-shake {
  animation: shake 0.5s ease-in-out;
}
</style>
