<template>
  <DashboardLayout pageTitle="Add Document">

    <!-- Breadcrumb -->
    <div class="mb-6">
      <div class="flex items-center gap-2 text-sm text-gray-600">
        <RouterLink to="/dashboard" class="hover:text-teal-600 transition-colors">Dashboard</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink to="/items" class="hover:text-teal-600 transition-colors">Items</RouterLink>
        <ChevronRight :size="16" />
        <span class="text-gray-900 font-medium">Add Document</span>
      </div>
    </div>

    <!-- Header Section -->
    <div class="relative mb-8 p-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-3xl shadow-xl text-white overflow-hidden">
      
      <!-- Decorative elements -->
      <div class="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
      <div class="absolute bottom-0 left-0 w-48 h-48 bg-white/10 rounded-full translate-y-1/2 -translate-x-1/2"></div>

      <div class="relative z-10 text-center">
        <div class="w-16 h-16 mx-auto mb-4 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center">
          <FileText :size="32" class="text-white" />
        </div>
        <h2 class="text-3xl font-bold mb-2">Add New Document</h2>
        <p class="text-white/90 text-lg">
          Upload and organize your important documents securely
        </p>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-3xl mx-auto">

      <!-- Back Button -->
      <button
        @click="$router.back()"
        class="group mb-6 inline-flex items-center gap-2 px-4 py-2 bg-white border-2 border-gray-200 rounded-xl shadow-sm hover:border-teal-300 hover:shadow-md transition-all duration-200"
      >
        <ArrowLeft :size="18" class="group-hover:-translate-x-1 transition-transform" />
        <span class="font-medium text-gray-700">Back</span>
      </button>

      <!-- ✅ VERIFICATION REQUIRED GUARD -->
      <div v-if="user && !isVerified" class="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl border-2 border-orange-200 p-8 md:p-10">
        <div class="text-center py-8">
          <div class="w-20 h-20 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <ShieldAlert :size="40" class="text-orange-600" />
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-3">Email Verification Required</h3>
          <p class="text-gray-600 mb-6 max-w-md mx-auto">
            Please verify your email address to add documents and upload files. Check your inbox for the verification link.
          </p>
          
          <!-- Resend Button -->
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

          <!-- Success Message -->
          <Transition
            enter-active-class="transition-all duration-200 ease-out"
            enter-from-class="opacity-0 translate-y-2"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition-all duration-150 ease-in"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 translate-y-2"
          >
            <div v-if="verificationEmailSent" class="mt-6 p-4 bg-green-50 border-2 border-green-200 rounded-xl flex items-center justify-center gap-2">
              <CheckCircle2 :size="18" class="text-green-600" />
              <p class="text-sm text-green-800 font-medium">✅ Verification email sent! Check your inbox.</p>
            </div>
          </Transition>
        </div>
      </div>

      <!-- ✅ FORM (Only show if verified) -->
      <div v-else-if="user" class="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl border-2 border-gray-100 p-8 md:p-10">

        <!-- SUCCESS MESSAGE -->
        <Transition
          enter-active-class="transition-all duration-300 ease-out"
          enter-from-class="opacity-0 -translate-y-2"
          enter-to-class="opacity-100 translate-y-0"
          leave-active-class="transition-all duration-200 ease-in"
          leave-from-class="opacity-100 translate-y-0"
          leave-to-class="opacity-0 -translate-y-2"
        >
          <div
            v-if="successMessage"
            class="mb-6 p-4 bg-green-50 border-2 border-green-200 rounded-xl flex items-start gap-3 animate-bounce-in"
          >
            <CheckCircle2 :size="20" class="text-green-500 flex-shrink-0 mt-0.5" />
            <div>
              <p class="text-sm font-semibold text-green-700">{{ successMessage }}</p>
              <p class="text-xs text-green-600 mt-1">Redirecting to items...</p>
            </div>
          </div>
        </Transition>

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

        <!-- FORM -->
        <form @submit.prevent="handleSubmit" class="space-y-6">

          <!-- CATEGORY -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <FolderOpen :size="16" class="text-teal-600" />
              Category
              <span class="text-red-500">*</span>
            </label>
            <select
              v-model="category"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 appearance-none cursor-pointer"
              required
              :disabled="loading"
            >
              <option value="" disabled>Select a category</option>
              <option v-for="cat in categoryOptions" :key="cat" :value="cat">
                {{ cat }}
              </option>
            </select>
          </div>

          <!-- DOCUMENT NAME -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <FileText :size="16" class="text-teal-600" />
              Document Name
              <span class="text-red-500">*</span>
            </label>
            <Autocomplete
              v-model="name"
              :suggestions="filteredDocumentNameSuggestions"
              placeholder="e.g., Passport, Visa, or type your own"
              :required="true"
              :disabled="loading"
              color="teal"
            />
          </div>

          <!-- FILE UPLOADER -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Upload :size="16" class="text-teal-600" />
              Upload Document File
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <FileUploader v-model="file" />
          </div>

          <!-- EXPIRATION DATE -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Calendar :size="16" class="text-teal-600" />
              Expiration Date
              <span class="text-red-500">*</span>
            </label>
            <input
              v-model="expirationDate"
              type="date"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50"
              required
              :disabled="loading"
              :min="today"
            />
            <p v-if="daysUntilExpiry !== null" class="text-xs text-gray-600 flex items-center gap-1">
              <Clock :size="12" />
              {{ daysUntilExpiry }} days from now
            </p>
          </div>

          <!-- REMINDER DAYS -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Bell :size="16" class="text-teal-600" />
              Reminder Schedule
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <div class="space-y-3">
              <div class="flex items-center gap-2 p-3 bg-blue-50 border border-blue-200 rounded-lg">
                <Info :size="16" class="text-blue-600 flex-shrink-0" />
                <p class="text-xs text-blue-700">
                  Set custom reminder days for this document, or leave blank to use your default setting ({{ userDefaultReminderDays }} days).
                </p>
              </div>
              
              <div class="flex gap-3">
                <button
                  type="button"
                  @click="reminderDaysBefore = null"
                  :class="[
                    'flex-1 px-4 py-3 rounded-xl font-medium transition-all duration-200 border-2',
                    reminderDaysBefore === null
                      ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white border-teal-500 shadow-md'
                      : 'bg-white text-gray-700 border-gray-200 hover:border-teal-300'
                  ]"
                  :disabled="loading"
                >
                  <div class="text-sm">Use Default</div>
                  <div class="text-xs opacity-75 mt-0.5">{{ userDefaultReminderDays }} days</div>
                </button>
                <button
                  type="button"
                  v-for="days in [7, 14, 30, 60]"
                  :key="days"
                  @click="reminderDaysBefore = days"
                  :class="[
                    'flex-1 px-4 py-3 rounded-xl font-medium transition-all duration-200 border-2',
                    reminderDaysBefore === days
                      ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white border-teal-500 shadow-md'
                      : 'bg-white text-gray-700 border-gray-200 hover:border-teal-300'
                  ]"
                  :disabled="loading"
                >
                  {{ days }} days
                </button>
              </div>
            </div>
          </div>

          <!-- DOCUMENT NUMBER -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Hash :size="16" class="text-teal-600" />
              Document Number
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <input
              v-model="documentNumber"
              type="text"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50"
              placeholder="e.g., Passport number, policy ID"
              :disabled="loading"
            />
          </div>

          <!-- ISSUING AUTHORITY -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Building :size="16" class="text-teal-600" />
              Issuing Authority
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <input
              v-model="issuingAuthority"
              type="text"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50"
              placeholder="e.g., Government office, insurance provider"
              :disabled="loading"
            />
          </div>

          <!-- NOTES -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <FileText :size="16" class="text-teal-600" />
              Notes
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <textarea
              v-model="notes"
              rows="4"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 resize-none"
              placeholder="Add any additional details or reminders..."
              :disabled="loading"
            ></textarea>
          </div>

          <!-- SUBMIT BUTTONS -->
          <div class="flex gap-4 pt-4">
            <button
              type="button"
              @click="$router.back()"
              class="flex-1 px-6 py-4 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
              :disabled="loading"
            >
              Cancel
            </button>
            <button
              type="submit"
              :disabled="loading"
              class="group flex-1 px-6 py-4 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <span v-if="!loading" class="flex items-center gap-2">
                <Plus :size="20" />
                Add Document
                <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
              </span>
              <span v-else class="flex items-center gap-3">
                <Loader2 :size="20" class="animate-spin" />
                Adding...
              </span>
            </button>
          </div>

        </form>

      </div>

      <!-- Loading State -->
      <div v-else class="bg-white/80 backdrop-blur-sm rounded-3xl shadow-xl border-2 border-gray-100 p-8 md:p-10">
        <div class="text-center py-12">
          <Loader2 :size="48" class="animate-spin text-teal-500 mx-auto mb-4" />
          <p class="text-gray-600">Loading...</p>
        </div>
      </div>

      <!-- Quick Tips -->
      <div class="mt-8 p-6 bg-gradient-to-br from-blue-50 to-cyan-50 rounded-2xl border-2 border-blue-200">
        <div class="flex items-start gap-3">
          <div class="w-10 h-10 rounded-xl bg-blue-500 flex items-center justify-center flex-shrink-0">
            <Lightbulb :size="20" class="text-white" />
          </div>
          <div>
            <h3 class="font-semibold text-gray-900 mb-2">Quick Tips</h3>
            <ul class="space-y-2 text-sm text-gray-700">
              <li class="flex items-start gap-2">
                <span class="text-teal-600 mt-0.5">•</span>
                <span>Upload clear scans or photos of your documents for easy reference</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-teal-600 mt-0.5">•</span>
                <span>Set expiration dates to receive timely reminders before renewal</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-teal-600 mt-0.5">•</span>
                <span>Add detailed notes to remember important context later</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

    </div>

  </DashboardLayout>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import FileUploader from "../components/FileUploader.vue"
import Autocomplete from "../components/Autocomplete.vue"
import { apiFetch } from "../utils/api"
import {
  FileText,
  FolderOpen,
  Upload,
  Calendar,
  Hash,
  Building,
  Plus,
  ArrowRight,
  ArrowLeft,
  CheckCircle2,
  AlertCircle,
  Loader2,
  ChevronRight,
  Clock,
  Lightbulb,
  ShieldAlert,
  Mail,
  Bell,
  Info
} from "lucide-vue-next"

const router = useRouter()

// Document name suggestions organized by category
const documentNameSuggestions = [
  // Travel
  { value: 'Passport', label: 'Passport', icon: '🛂', description: 'Travel document', category: 'Travel' },
  { value: 'Visa', label: 'Visa', icon: '✈️', description: 'Travel authorization', category: 'Travel' },
  { value: 'Travel Insurance', label: 'Travel Insurance', icon: '🛡️', description: 'Travel coverage', category: 'Travel' },
  { value: 'Flight Ticket', label: 'Flight Ticket', icon: '🎫', description: 'Air travel ticket', category: 'Travel' },
  // Health
  { value: 'Health Insurance Card', label: 'Health Insurance Card', icon: '🏥', description: 'Health coverage card', category: 'Health' },
  { value: 'Medical Record', label: 'Medical Record', icon: '📋', description: 'Health documentation', category: 'Health' },
  { value: 'Vaccination Certificate', label: 'Vaccination Certificate', icon: '💉', description: 'Immunization record', category: 'Health' },
  { value: 'Prescription', label: 'Prescription', icon: '💊', description: 'Medical prescription', category: 'Health' },
  // Finance
  { value: 'Tax Return', label: 'Tax Return', icon: '💰', description: 'Annual tax filing', category: 'Finance' },
  { value: 'Bank Statement', label: 'Bank Statement', icon: '🏦', description: 'Banking document', category: 'Finance' },
  { value: 'Insurance Policy', label: 'Insurance Policy', icon: '🛡️', description: 'Insurance coverage', category: 'Finance' },
  { value: 'Investment Document', label: 'Investment Document', icon: '📈', description: 'Investment record', category: 'Finance' },
  // Work
  { value: 'Work Permit', label: 'Work Permit', icon: '💼', description: 'Employment authorization', category: 'Work' },
  { value: 'Employment Contract', label: 'Employment Contract', icon: '📝', description: 'Job agreement', category: 'Work' },
  { value: 'Professional License', label: 'Professional License', icon: '🎓', description: 'Professional certification', category: 'Work' },
  { value: 'Resume', label: 'Resume', icon: '📄', description: 'CV document', category: 'Work' },
  // Personal
  { value: 'Birth Certificate', label: 'Birth Certificate', icon: '👶', description: 'Official birth record', category: 'Personal' },
  { value: 'ID Card', label: 'ID Card', icon: '🪪', description: 'Identification card', category: 'Personal' },
  { value: 'Social Security Card', label: 'Social Security Card', icon: '🔐', description: 'SSN document', category: 'Personal' },
  { value: 'Marriage Certificate', label: 'Marriage Certificate', icon: '💍', description: 'Marriage record', category: 'Personal' },
  // Legal
  { value: 'Lease Agreement', label: 'Lease Agreement', icon: '🏠', description: 'Rental contract', category: 'Legal' },
  { value: 'Warranty', label: 'Warranty', icon: '🔧', description: 'Product guarantee', category: 'Legal' },
  { value: 'Power of Attorney', label: 'Power of Attorney', icon: '⚖️', description: 'Legal authorization', category: 'Legal' },
  { value: 'Will', label: 'Will', icon: '📜', description: 'Testament document', category: 'Legal' },
  // Education
  { value: 'Degree Certificate', label: 'Degree Certificate', icon: '🎓', description: 'Academic degree', category: 'Education' },
  { value: 'Transcript', label: 'Transcript', icon: '📊', description: 'Academic record', category: 'Education' },
  { value: 'Student ID', label: 'Student ID', icon: '🪪', description: 'Student identification', category: 'Education' },
  { value: 'Enrollment Document', label: 'Enrollment Document', icon: '📝', description: 'School enrollment', category: 'Education' },
  // Vehicle
  { value: "Driver's License", label: "Driver's License", icon: '🚗', description: 'Driving permit', category: 'Vehicle' },
  { value: 'Vehicle Registration', label: 'Vehicle Registration', icon: '🚙', description: 'Vehicle documents', category: 'Vehicle' },
  { value: 'Car Insurance', label: 'Car Insurance', icon: '🛡️', description: 'Auto coverage', category: 'Vehicle' },
  { value: 'Inspection Certificate', label: 'Inspection Certificate', icon: '✅', description: 'Vehicle inspection', category: 'Vehicle' }
]

// Category options
const categoryOptions = [
  'Travel',
  'Health',
  'Finance',
  'Work',
  'Personal',
  'Subscriptions',
  'Legal',
  'Education',
  'Vehicle'
]

// ✅ User state
const user = ref(null)
const isVerified = computed(() => user.value?.email_verified || false)
const resending = ref(false)
const verificationEmailSent = ref(false)
const userDefaultReminderDays = computed(() => user.value?.notification_days_before || 7)

// Form fields
const name = ref("")
const category = ref("")
const expirationDate = ref("")
const documentNumber = ref("")
const issuingAuthority = ref("")
const notes = ref("")
const file = ref(null)
const reminderDaysBefore = ref(null) // null = use user default

// State
const loading = ref(false)
const successMessage = ref("")
const errorMessage = ref("")

// Computed
const today = computed(() => {
  const date = new Date()
  return date.toISOString().split('T')[0]
})

const daysUntilExpiry = computed(() => {
  if (!expirationDate.value) return null
  
  const today = new Date()
  const expiry = new Date(expirationDate.value)
  const diffTime = expiry - today
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
  
  return diffDays
})

// Filter document name suggestions based on selected category
const filteredDocumentNameSuggestions = computed(() => {
  if (!category.value) {
    return documentNameSuggestions // Show all if no category selected
  }
  return documentNameSuggestions.filter(suggestion => suggestion.category === category.value)
})

// ✅ Load user on mount
onMounted(async () => {
  await loadUser()
})

// ✅ Load user function
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

// ✅ Resend verification email
async function resendVerification() {
  resending.value = true
  verificationEmailSent.value = false
  
  try {
    const res = await apiFetch("/auth/resend-verification", {
      method: "POST"
    })

    if (res.ok) {
      verificationEmailSent.value = true
      setTimeout(() => {
        verificationEmailSent.value = false
      }, 5000)
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

async function handleSubmit() {
  errorMessage.value = ""
  successMessage.value = ""

  // Validation (in field order: Category → Document Name → Expiration Date)
  if (!category.value) {
    errorMessage.value = "Please select a category"
    return
  }

  if (!name.value.trim()) {
    errorMessage.value = "Please enter a document name"
    return
  }

  if (!expirationDate.value) {
    errorMessage.value = "Please select an expiration date"
    return
  }

  loading.value = true

  try {
    const formData = new FormData()
    formData.append("name", name.value.trim())
    formData.append("category", category.value)
    formData.append("expiration_date", expirationDate.value)
    formData.append("document_number", documentNumber.value.trim())
    formData.append("issuing_authority", issuingAuthority.value.trim())
    formData.append("notes", notes.value.trim())
    formData.append("type", "document")
    
    // Add reminder days if custom value is set (null means use default)
    if (reminderDaysBefore.value !== null) {
      formData.append("reminder_days_before", reminderDaysBefore.value.toString())
    }

    if (file.value) {
      formData.append("file", file.value)
    }

    const res = await apiFetch("/items/upload", {
      method: "POST",
      body: formData
    })

    if (!res.ok) {
      const data = await res.json()
      
      // ✅ Check if it's a verification error
      if (res.status === 403 && data.detail?.includes('verification')) {
        errorMessage.value = "⚠️ Email verification required. Please verify your email to add documents."
        loading.value = false
        return
      }
      
      errorMessage.value = data.detail || "Failed to add document"
      loading.value = false
      return
    }

    successMessage.value = "Document added successfully! 🎉"

    // Redirect after 1.5 seconds
    setTimeout(() => {
      router.push("/items")
    }, 1500)

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

@keyframes bounce-in {
  0% {
    opacity: 0;
    transform: scale(0.9);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-shake {
  animation: shake 0.5s ease-in-out;
}

.animate-bounce-in {
  animation: bounce-in 0.5s ease-out;
}
</style>