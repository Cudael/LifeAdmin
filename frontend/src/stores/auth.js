import { defineStore } from "pinia"
import { ref, computed } from "vue"
import { apiFetch } from "../utils/api"

export const useAuthStore = defineStore("auth", () => {
  const user = ref(null)
  const isAuthenticated = ref(false)
  const loading = ref(false)

  const subscriptionPlan = computed(() => user.value?.subscription_plan || "free")
  const subscriptionStatus = computed(() => user.value?.subscription_status || null)
  const subscriptionCurrentPeriodEnd = computed(() => user.value?.subscription_current_period_end || null)
  const stripeCustomerId = computed(() => user.value?.stripe_customer_id || null)

  const isPremium = computed(() => {
    return subscriptionPlan.value === "premium" &&
           (subscriptionStatus.value === "active" || subscriptionStatus.value === "trialing")
  })

  function setUser(userData) {
    if (userData) {
      user.value = userData
      isAuthenticated.value = true
    } else {
      clearUser()
    }
  }

  function clearUser() {
    user.value = null
    isAuthenticated.value = false
  }

  async function fetchUser() {
    if (user.value) return  // Already loaded – skip redundant request
    loading.value = true
    try {
      const res = await apiFetch("/auth/me")
      if (res && res.ok) {
        const data = await res.json()
        setUser(data)
      }
    } catch (e) {
      // silently fail – user stays null
    } finally {
      loading.value = false
    }
  }

  async function fetchSubscriptionStatus() {
    await fetchUser()
  }

  return {
    user,
    isAuthenticated,
    loading,
    isPremium,
    subscriptionPlan,
    subscriptionStatus,
    subscriptionCurrentPeriodEnd,
    stripeCustomerId,
    setUser,
    clearUser,
    fetchUser,
    fetchSubscriptionStatus,
  }
})
