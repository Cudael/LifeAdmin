<template>
  <DashboardLayout pageTitle="Add Subscription">

    <!-- Breadcrumb -->
    <div class="mb-6">
      <div class="flex items-center gap-2 text-sm text-gray-600">
        <RouterLink to="/dashboard" class="hover:text-teal-600 transition-colors">Dashboard</RouterLink>
        <ChevronRight :size="16" />
        <RouterLink to="/items" class="hover:text-teal-600 transition-colors">Items</RouterLink>
        <ChevronRight :size="16" />
        <span class="text-gray-900 font-medium">Add Subscription</span>
      </div>
    </div>

    <!-- Header Section -->
    <div class="relative mb-8 p-8 bg-gradient-to-br from-purple-500 to-pink-500 rounded-3xl shadow-xl text-white overflow-hidden">
      
      <!-- Decorative elements -->
      <div class="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
      <div class="absolute bottom-0 left-0 w-48 h-48 bg-white/10 rounded-full translate-y-1/2 -translate-x-1/2"></div>

      <div class="relative z-10 text-center">
        <div class="w-16 h-16 mx-auto mb-4 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center">
          <Repeat :size="32" class="text-white" />
        </div>
        <h2 class="text-3xl font-bold mb-2">Add New Subscription</h2>
        <p class="text-white/90 text-lg">
          Track and manage your recurring subscriptions easily
        </p>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-3xl mx-auto">

      <!-- Back Button -->
      <button
        @click="$router.back()"
        class="group mb-6 inline-flex items-center gap-2 px-4 py-2 bg-white border-2 border-gray-200 rounded-xl shadow-sm hover:border-purple-300 hover:shadow-md transition-all duration-200"
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
            Please verify your email address to add subscriptions and upload files. Check your inbox for the verification link.
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

          <!-- SUBSCRIPTION NAME -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Repeat :size="16" class="text-purple-600" />
              Subscription Name
              <span class="text-red-500">*</span>
            </label>
            <input
              v-model="name"
              type="text"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200 bg-white/50"
              placeholder="e.g., Netflix, Spotify, Gym Membership"
              required
              :disabled="loading"
            />
          </div>

          <!-- PROVIDER -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Building :size="16" class="text-purple-600" />
              Provider
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <input
              v-model="provider"
              type="text"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200 bg-white/50"
              placeholder="e.g., Netflix Inc., Spotify AB"
              :disabled="loading"
            />
          </div>

          <!-- SUBSCRIPTION URL -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Link :size="16" class="text-purple-600" />
              Subscription URL
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <input
              v-model="subscriptionUrl"
              type="url"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200 bg-white/50"
              placeholder="https://account.netflix.com"
              :disabled="loading"
            />
          </div>

          <!-- PRICE & BILLING CYCLE (Side by Side) -->
          <div class="grid md:grid-cols-2 gap-6">
            
            <!-- PRICE -->
            <div class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
                <DollarSign :size="16" class="text-purple-600" />
                Price
                <span class="text-gray-500 text-xs font-normal">(optional)</span>
              </label>
              <div class="relative">
                <span class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400">€</span>
                <input
                  v-model="price"
                  type="number"
                  step="0.01"
                  min="0"
                  class="w-full pl-8 pr-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200 bg-white/50"
                  placeholder="9.99"
                  :disabled="loading"
                />
              </div>
            </div>

            <!-- BILLING CYCLE -->
            <div class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
                <CalendarClock :size="16" class="text-purple-600" />
                Billing Cycle
                <span class="text-red-500">*</span>
              </label>
              <div class="relative">
                <select
                  v-model="billingCycle"
                  class="w-full px-4 py-3 pr-10 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200 bg-white/50 appearance-none cursor-pointer"
                  required
                  :disabled="loading"
                >
                  <option disabled value="">Select cycle</option>
                  <option value="Weekly">📅 Weekly</option>
                  <option value="Monthly">🗓️ Monthly</option>
                  <option value="Quarterly">📆 Quarterly</option>
                  <option value="Yearly">🎯 Yearly</option>
                </select>
                <ChevronDown :size="20" class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 pointer-events-none" />
              </div>
            </div>

          </div>

          <!-- NEXT RENEWAL DATE -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Calendar :size="16" class="text-purple-600" />
              Next Renewal Date
              <span class="text-red-500">*</span>
            </label>
            <input
              v-model="renewalDate"
              type="date"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200 bg-white/50"
              required
              :disabled="loading"
              :min="today"
            />
            <p v-if="daysUntilRenewal !== null" class="text-xs text-gray-600 flex items-center gap-1">
              <Clock :size="12" />
              {{ daysUntilRenewal }} days until renewal
            </p>
          </div>

          <!-- EXPIRATION TOGGLE -->
          <div class="p-4 bg-gradient-to-r from-purple-50 to-pink-50 border-2 border-purple-200 rounded-xl">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-purple-500 flex items-center justify-center">
                  <AlertTriangle :size="20" class="text-white" />
                </div>
                <div>
                  <p class="text-sm font-semibold text-gray-900">Has an expiration date?</p>
                  <p class="text-xs text-gray-600">Some subscriptions have a fixed end date</p>
                </div>
              </div>

              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" v-model="hasExpiration" class="sr-only peer" />
                <div class="w-14 h-7 bg-gray-300 rounded-full peer peer-checked:bg-purple-500 transition-all"></div>
                <div class="absolute left-1 top-1 w-5 h-5 bg-white rounded-full shadow peer-checked:translate-x-7 transition-all"></div>
              </label>
            </div>
          </div>

          <!-- EXPIRATION DATE (Conditional) -->
          <Transition
            enter-active-class="transition-all duration-300 ease-out"
            enter-from-class="opacity-0 -translate-y-2"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition-all duration-200 ease-in"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 -translate-y-2"
          >
            <div v-if="hasExpiration" class="space-y-2">
              <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
                <CalendarX :size="16" class="text-red-600" />
                Expiration Date
                <span class="text-red-500">*</span>
              </label>
              <input
                v-model="expirationDate"
                type="date"
                class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200 bg-white/50"
                :required="hasExpiration"
                :disabled="loading"
                :min="today"
              />
            </div>
          </Transition>

          <!-- FILE UPLOADER -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <Upload :size="16" class="text-purple-600" />
              Upload File
              <span class="text-gray-500 text-xs font-normal">(optional - contract, receipt, etc.)</span>
            </label>
            <FileUploader v-model="file" />
          </div>

          <!-- NOTES -->
          <div class="space-y-2">
            <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
              <FileText :size="16" class="text-purple-600" />
              Notes
              <span class="text-gray-500 text-xs font-normal">(optional)</span>
            </label>
            <textarea
              v-model="notes"
              rows="4"
              class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200 bg-white/50 resize-none"
              placeholder="Add payment method, cancellation info, or other details..."
              :disabled="loading"
            ></textarea>
          </div>

          <!-- COST SUMMARY (if price is entered) -->
          <Transition
            enter-active-class="transition-all duration-300 ease-out"
            enter-from-class="opacity-0 scale-95"
            enter-to-class="opacity-100 scale-100"
          >
            <div v-if="price && billingCycle" class="p-4 bg-gradient-to-br from-blue-50 to-cyan-50 border-2 border-blue-200 rounded-xl">
              <div class="flex items-start gap-3">
                <div class="w-10 h-10 rounded-xl bg-blue-500 flex items-center justify-center flex-shrink-0">
                  <Calculator :size="20" class="text-white" />
                </div>
                <div class="flex-1">
                  <h4 class="font-semibold text-gray-900 mb-2">Cost Breakdown</h4>
                  <div class="grid grid-cols-2 gap-3 text-sm">
                    <div>
                      <p class="text-gray-600">Per {{ billingCycle.toLowerCase() }}</p>
                      <p class="text-lg font-bold text-gray-900">€{{ parseFloat(price).toFixed(2) }}</p>
                    </div>
                    <div>
                      <p class="text-gray-600">Per year (est.)</p>
                      <p class="text-lg font-bold text-gray-900">€{{ yearlyEstimate }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </Transition>

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
              class="group flex-1 px-6 py-4 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-purple-600 hover:to-pink-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
            >
              <span v-if="!loading" class="flex items-center gap-2">
                <Plus :size="20" />
                Add Subscription
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
          <Loader2 :size="48" class="animate-spin text-purple-500 mx-auto mb-4" />
          <p class="text-gray-600">Loading...</p>
        </div>
      </div>

      <!-- Quick Tips -->
      <div class="mt-8 p-6 bg-gradient-to-br from-purple-50 to-pink-50 rounded-2xl border-2 border-purple-200">
        <div class="flex items-start gap-3">
          <div class="w-10 h-10 rounded-xl bg-purple-500 flex items-center justify-center flex-shrink-0">
            <Lightbulb :size="20" class="text-white" />
          </div>
          <div>
            <h3 class="font-semibold text-gray-900 mb-2">Subscription Tips</h3>
            <ul class="space-y-2 text-sm text-gray-700">
              <li class="flex items-start gap-2">
                <span class="text-purple-600 mt-0.5">•</span>
                <span>Set renewal dates to track when your next payment is due</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-purple-600 mt-0.5">•</span>
                <span>Add subscription URLs for quick access to manage your account</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-purple-600 mt-0.5">•</span>
                <span>Track costs to see your total monthly/yearly subscription spending</span>
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
import { apiFetch } from "../utils/api"
import {
  Repeat,
  Building,
  Link,
  DollarSign,
  CalendarClock,
  Calendar,
  CalendarX,
  Clock,
  Upload,
  FileText,
  Plus,
  ArrowRight,
  ArrowLeft,
  CheckCircle2,
  AlertCircle,
  AlertTriangle,
  Loader2,
  ChevronRight,
  ChevronDown,
  Lightbulb,
  Calculator,
  ShieldAlert,
  Mail
} from "lucide-vue-next"

const router = useRouter()

// ✅ User state
const user = ref(null)
const isVerified = computed(() => user.value?.email_verified || false)
const resending = ref(false)
const verificationEmailSent = ref(false)

// Form fields
const name = ref("")
const provider = ref("")
const subscriptionUrl = ref("")
const price = ref("")
const billingCycle = ref("")
const renewalDate = ref("")
const notes = ref("")
const file = ref(null)

// Expiration toggle
const hasExpiration = ref(false)
const expirationDate = ref(null)

// State
const loading = ref(false)
const successMessage = ref("")
const errorMessage = ref("")

// Computed
const today = computed(() => {
  const date = new Date()
  return date.toISOString().split('T')[0]
})

const daysUntilRenewal = computed(() => {
  if (!renewalDate.value) return null
  
  const today = new Date()
  const renewal = new Date(renewalDate.value)
  const diffTime = renewal - today
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
  
  return diffDays
})

const yearlyEstimate = computed(() => {
  if (!price.value || !billingCycle.value) return "0.00"
  
  const priceNum = parseFloat(price.value)
  let multiplier = 1
  
  switch(billingCycle.value) {
    case "Weekly": multiplier = 52; break
    case "Monthly": multiplier = 12; break
    case "Quarterly": multiplier = 4; break
    case "Yearly": multiplier = 1; break
  }
  
  return (priceNum * multiplier).toFixed(2)
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

  // Validation
  if (!billingCycle.value) {
    errorMessage.value = "Please select a billing cycle"
    return
  }

  if (!renewalDate.value) {
    errorMessage.value = "Please select a renewal date"
    return
  }

  if (hasExpiration.value && !expirationDate.value) {
    errorMessage.value = "Please select an expiration date"
    return
  }

  if (!name.value.trim()) {
    errorMessage.value = "Please enter a subscription name"
    return
  }

  loading.value = true

  try {
    const formData = new FormData()
    formData.append("name", name.value.trim())
    formData.append("provider", provider.value.trim())
    formData.append("subscription_url", subscriptionUrl.value.trim())
    formData.append("price", price.value)
    formData.append("billing_cycle", billingCycle.value)
    formData.append("renewal_date", renewalDate.value)
    formData.append("notes", notes.value.trim())
    formData.append("category", "Subscriptions")
    formData.append("type", "subscription")

    if (hasExpiration.value && expirationDate.value) {
      formData.append("expiration_date", expirationDate.value)
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
        errorMessage.value = "⚠️ Email verification required. Please verify your email to add subscriptions."
        loading.value = false
        return
      }
      
      errorMessage.value = data.detail || "Failed to add subscription"
      loading.value = false
      return
    }

    successMessage.value = "Subscription added successfully! 🎉"

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