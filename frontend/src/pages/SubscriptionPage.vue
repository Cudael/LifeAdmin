<template>
  <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white">
    <div class="max-w-4xl mx-auto px-6 py-12">
      <!-- Success/Canceled Messages -->
      <div v-if="showSuccess" class="mb-6 p-4 bg-green-50 border border-green-200 rounded-lg text-green-800">
        <div class="flex items-center gap-2">
          <CheckCircle2 :size="20" />
          <span class="font-semibold">Success! Your subscription is now active.</span>
        </div>
      </div>
      
      <div v-if="showCanceled" class="mb-6 p-4 bg-yellow-50 border border-yellow-200 rounded-lg text-yellow-800">
        <div class="flex items-center gap-2">
          <AlertCircle :size="20" />
          <span class="font-semibold">Checkout was canceled. You can try again anytime.</span>
        </div>
      </div>
      
      <!-- Page Header -->
      <div class="mb-8">
        <h1 class="text-4xl font-bold text-gray-900 mb-2">Subscription</h1>
        <p class="text-gray-600">Manage your Remindes subscription and billing</p>
      </div>
      
      <!-- Current Plan Card -->
      <div class="bg-white rounded-2xl shadow-lg p-8 mb-6">
        <div class="flex items-start justify-between mb-6">
          <div>
            <h2 class="text-2xl font-semibold text-gray-900 mb-2">Current Plan</h2>
            <div class="flex items-center gap-3">
              <span 
                :class="[
                  'px-4 py-2 rounded-full font-semibold text-lg',
                  isPremium 
                    ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white' 
                    : 'bg-gray-200 text-gray-700'
                ]"
              >
                {{ isPremium ? 'Premium' : 'Free' }}
              </span>
              <span 
                v-if="subscriptionStatus"
                :class="[
                  'px-3 py-1 rounded-full text-sm font-medium',
                  subscriptionStatus === 'active' ? 'bg-green-100 text-green-700' :
                  subscriptionStatus === 'trialing' ? 'bg-blue-100 text-blue-700' :
                  subscriptionStatus === 'past_due' ? 'bg-red-100 text-red-700' :
                  'bg-gray-100 text-gray-700'
                ]"
              >
                {{ subscriptionStatus }}
              </span>
            </div>
          </div>
          <Sparkles v-if="isPremium" :size="32" class="text-teal-500" />
          <Package v-else :size="32" class="text-gray-400" />
        </div>
        
        <!-- Plan Details -->
        <div class="grid md:grid-cols-2 gap-6 mb-6">
          <div class="p-4 bg-gray-50 rounded-lg">
            <div class="text-sm text-gray-600 mb-1">Item Limit</div>
            <div class="text-2xl font-bold text-gray-900">
              {{ isPremium ? 'Unlimited' : `${itemCount}/20` }}
            </div>
            <div v-if="!isPremium && itemCount >= 20" class="text-sm text-red-600 mt-1">
              Limit reached
            </div>
          </div>
          
          <div class="p-4 bg-gray-50 rounded-lg">
            <div class="text-sm text-gray-600 mb-1">Monthly Cost</div>
            <div class="text-2xl font-bold text-gray-900">
              {{ isPremium ? '€2.99' : '€0.00' }}
            </div>
          </div>
        </div>
        
        <!-- Next Billing Date -->
        <div v-if="isPremium && subscriptionCurrentPeriodEnd" class="p-4 bg-teal-50 border border-teal-200 rounded-lg mb-6">
          <div class="flex items-center gap-2 text-teal-800">
            <Calendar :size="20" />
            <span class="font-medium">
              Next billing date: {{ formatDate(subscriptionCurrentPeriodEnd) }}
            </span>
          </div>
        </div>
        
        <!-- Action Buttons -->
        <div class="flex gap-4">
          <button
            v-if="isPremium"
            @click="handleManageSubscription"
            :disabled="isLoading"
            class="flex items-center gap-2 px-6 py-3 bg-teal-500 text-white rounded-lg font-semibold hover:bg-teal-600 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <CreditCard :size="20" />
            {{ isLoading ? 'Loading...' : 'Manage Subscription' }}
          </button>
          
          <button
            v-else
            @click="handleUpgrade"
            :disabled="isLoading"
            class="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-lg font-semibold hover:from-teal-400 hover:to-cyan-400 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <ArrowUp :size="20" />
            {{ isLoading ? 'Loading...' : 'Upgrade to Premium' }}
          </button>
        </div>
        
        <p v-if="errorMessage" class="text-red-600 text-sm mt-4">{{ errorMessage }}</p>
      </div>
      
      <!-- Features Comparison -->
      <div class="bg-white rounded-2xl shadow-lg p-8">
        <h2 class="text-2xl font-semibold text-gray-900 mb-6">Plan Features</h2>
        
        <div class="grid md:grid-cols-2 gap-8">
          <!-- Free Plan Features -->
          <div>
            <h3 class="text-lg font-semibold text-gray-700 mb-4">Free Plan</h3>
            <ul class="space-y-3">
              <li class="flex items-start gap-2 text-gray-600">
                <CheckCircle2 :size="20" class="text-gray-400 flex-shrink-0 mt-0.5" />
                <span>Track up to 20 items</span>
              </li>
              <li class="flex items-start gap-2 text-gray-600">
                <CheckCircle2 :size="20" class="text-gray-400 flex-shrink-0 mt-0.5" />
                <span>Smart reminders</span>
              </li>
              <li class="flex items-start gap-2 text-gray-600">
                <CheckCircle2 :size="20" class="text-gray-400 flex-shrink-0 mt-0.5" />
                <span>Document uploads (100MB)</span>
              </li>
              <li class="flex items-start gap-2 text-gray-600">
                <CheckCircle2 :size="20" class="text-gray-400 flex-shrink-0 mt-0.5" />
                <span>Secure cloud storage</span>
              </li>
            </ul>
          </div>
          
          <!-- Premium Plan Features -->
          <div>
            <h3 class="text-lg font-semibold text-teal-600 mb-4">Premium Plan</h3>
            <ul class="space-y-3">
              <li class="flex items-start gap-2 text-gray-900">
                <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
                <span><strong>Unlimited items</strong></span>
              </li>
              <li class="flex items-start gap-2 text-gray-900">
                <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
                <span>Priority reminders</span>
              </li>
              <li class="flex items-start gap-2 text-gray-900">
                <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
                <span>Unlimited document uploads</span>
              </li>
              <li class="flex items-start gap-2 text-gray-900">
                <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
                <span>Advanced insights & analytics</span>
              </li>
              <li class="flex items-start gap-2 text-gray-900">
                <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
                <span>Priority support</span>
              </li>
              <li class="flex items-start gap-2 text-gray-900">
                <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
                <span>Early access to new features</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { 
  CheckCircle2, 
  AlertCircle, 
  Calendar, 
  CreditCard, 
  ArrowUp,
  Sparkles,
  Package
} from 'lucide-vue-next'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

const isLoading = ref(false)
const errorMessage = ref("")
const showSuccess = ref(false)
const showCanceled = ref(false)
const itemCount = ref(0)

const API_URL = import.meta.env.VITE_API_URL || "/api"

// Computed properties from auth store
const isPremium = computed(() => authStore.isPremium)
const subscriptionStatus = computed(() => authStore.subscriptionStatus)
const subscriptionCurrentPeriodEnd = computed(() => authStore.subscriptionCurrentPeriodEnd)

// Format date
function formatDate(dateString) {
  if (!dateString) return ""
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  })
}

// Handle upgrade
async function handleUpgrade() {
  try {
    isLoading.value = true
    errorMessage.value = ""
    
    const token = localStorage.getItem("token")
    if (!token) {
      router.push("/login?redirect=/subscription")
      return
    }
    
    const response = await fetch(`${API_URL}/payments/create-checkout-session`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      }
    })
    
    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.detail || "Failed to create checkout session")
    }
    
    const { url } = await response.json()
    window.location.href = url
    
  } catch (error) {
    console.error("Upgrade error:", error)
    errorMessage.value = error.message || "Failed to start checkout. Please try again."
    isLoading.value = false
  }
}

// Handle manage subscription
async function handleManageSubscription() {
  try {
    isLoading.value = true
    errorMessage.value = ""
    
    const token = localStorage.getItem("token")
    const response = await fetch(`${API_URL}/payments/create-portal-session`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      }
    })
    
    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.detail || "Failed to open portal")
    }
    
    const { url } = await response.json()
    window.location.href = url
    
  } catch (error) {
    console.error("Portal error:", error)
    errorMessage.value = error.message || "Failed to open subscription portal. Please try again."
    isLoading.value = false
  }
}

// Fetch item count
async function fetchItemCount() {
  try {
    const token = localStorage.getItem("token")
    const response = await fetch(`${API_URL}/items`, {
      headers: {
        "Authorization": `Bearer ${token}`
      }
    })
    
    if (response.ok) {
      const data = await response.json()
      itemCount.value = data.length || 0
    }
  } catch (error) {
    console.error("Failed to fetch item count:", error)
  }
}

onMounted(async () => {
  // Check for success/canceled query params
  if (route.query.success === 'true') {
    showSuccess.value = true
    // Refresh subscription status
    await authStore.fetchSubscriptionStatus()
    // Clear query param after showing message
    setTimeout(() => {
      showSuccess.value = false
      router.replace({ query: {} })
    }, 5000)
  }
  
  if (route.query.canceled === 'true') {
    showCanceled.value = true
    setTimeout(() => {
      showCanceled.value = false
      router.replace({ query: {} })
    }, 5000)
  }
  
  // Fetch subscription status and item count
  await authStore.fetchSubscriptionStatus()
  await fetchItemCount()
})
</script>
