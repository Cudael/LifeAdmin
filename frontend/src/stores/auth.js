import { defineStore } from "pinia"
import { ref, computed } from "vue"
import axios from "axios"

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000"

export const useAuthStore = defineStore("auth", () => {
  // User state
  const user = ref(null)
  const isAuthenticated = ref(false)
  
  // Subscription state
  const subscriptionPlan = ref("free")
  const subscriptionStatus = ref(null)
  const subscriptionCurrentPeriodEnd = ref(null)
  const stripeCustomerId = ref(null)
  
  // Computed properties
  const isPremium = computed(() => {
    return subscriptionPlan.value === "premium" && 
           (subscriptionStatus.value === "active" || subscriptionStatus.value === "trialing")
  })
  
  // Set user data
  function setUser(userData) {
    if (userData) {
      user.value = userData
      isAuthenticated.value = true
      
      // Set subscription data
      subscriptionPlan.value = userData.subscription_plan || "free"
      subscriptionStatus.value = userData.subscription_status || null
      subscriptionCurrentPeriodEnd.value = userData.subscription_current_period_end || null
      stripeCustomerId.value = userData.stripe_customer_id || null
    } else {
      clearUser()
    }
  }
  
  // Clear user data
  function clearUser() {
    user.value = null
    isAuthenticated.value = false
    subscriptionPlan.value = "free"
    subscriptionStatus.value = null
    subscriptionCurrentPeriodEnd.value = null
    stripeCustomerId.value = null
  }
  
  // Fetch subscription status
  async function fetchSubscriptionStatus() {
    try {
      const token = localStorage.getItem("token")
      if (!token) return
      
      const response = await axios.get(`${API_URL}/auth/me`, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      
      if (response.data) {
        setUser(response.data)
      }
    } catch (error) {
      console.error("Failed to fetch subscription status:", error)
    }
  }
  
  return {
    user,
    isAuthenticated,
    subscriptionPlan,
    subscriptionStatus,
    subscriptionCurrentPeriodEnd,
    stripeCustomerId,
    isPremium,
    setUser,
    clearUser,
    fetchSubscriptionStatus
  }
})
