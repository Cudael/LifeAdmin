<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { 
  CheckCircle2, 
  ArrowRight,
  Star,
  Shield,
  Zap,
  TrendingUp,
  Award
} from "lucide-vue-next"

const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref("")

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000"

async function handleUpgradeClick() {
  try {
    isLoading.value = true
    errorMessage.value = ""
    
    // Check if user is logged in
    const token = localStorage.getItem("token")
    if (!token) {
      router.push("/login?redirect=/subscription")
      return
    }
    
    // Create checkout session
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
    
    // Redirect to Stripe checkout
    window.location.href = url
    
  } catch (error) {
    console.error("Upgrade error:", error)
    errorMessage.value = error.message || "Failed to start checkout. Please try again."
    isLoading.value = false
  }
}
</script>

<template>
  <section id="pricing" class="py-24 md:py-32 relative overflow-hidden z-10">
    
    <!-- Ambient glowing backgrounds -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-4xl h-[500px] bg-teal-600/10 rounded-full blur-[120px] pointer-events-none z-0"></div>

    <div class="max-w-screen-xl mx-auto px-6 text-center relative z-10">

      <!-- Section Label -->
      <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-500/10 border border-teal-500/20 text-teal-400 rounded-full mb-6 text-sm font-semibold tracking-wide">
        <Award :size="16" class="fill-current/20" />
        Simple Pricing
      </div>

      <!-- Title -->
      <h2 class="text-4xl md:text-5xl font-extrabold text-slate-50 tracking-tight mb-6">
        Choose the plan that <span class="bg-gradient-to-r from-teal-400 to-cyan-400 bg-clip-text text-transparent">fits you.</span>
      </h2>

      <p class="text-lg text-slate-400 max-w-2xl mx-auto mb-16">
        Start for free, upgrade when you need to. No hidden fees, cancel anytime.
      </p>

      <!-- Pricing Grid -->
      <div class="grid lg:grid-cols-3 gap-8 lg:gap-8 max-w-6xl mx-auto items-center">

        <!-- FREE PLAN (Left Card) -->
        <div class="group relative p-8 lg:p-10 bg-slate-900/40 backdrop-blur-md rounded-[2.5rem] border border-white/5 hover:border-white/10 transition-all duration-300 text-left flex flex-col h-full">
          <div class="mb-8">
            <div class="inline-block px-3 py-1 bg-slate-800 text-slate-300 rounded-full text-xs font-bold uppercase tracking-wider mb-6 border border-white/5">
              Free Forever
            </div>
            <h3 class="text-2xl font-bold text-slate-100 mb-2">Basic</h3>
            <!-- Removed fixed height, added min-h for responsive wrapping -->
            <p class="text-slate-400 text-sm min-h-[3rem]">Perfect for getting your life organized.</p>
          </div>

          <div class="mb-8">
            <p class="text-5xl font-extrabold text-slate-50 tracking-tight mb-2">€0</p>
            <p class="text-slate-500 text-sm font-medium">No credit card required</p>
          </div>

          <ul class="space-y-4 text-slate-300 mb-10 flex-1">
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500/70 flex-shrink-0 mt-0.5" />
              <span>Track up to 20 items</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500/70 flex-shrink-0 mt-0.5" />
              <span>Smart reminders</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500/70 flex-shrink-0 mt-0.5" />
              <span>Document uploads (100MB)</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500/70 flex-shrink-0 mt-0.5" />
              <span>Secure cloud storage</span>
            </li>
          </ul>

          <RouterLink
            to="/register"
            class="block text-center px-7 py-4 bg-white/5 hover:bg-white/10 border border-white/10 text-white rounded-2xl text-lg font-semibold transition-all duration-300 w-full mt-auto"
          >
            Start Free
          </RouterLink>
        </div>

        <!-- PREMIUM MONTHLY (Center Hero Card) -->
        <!-- Added pt-12 to ensure the badge doesn't overlap the inner content -->
        <div class="relative px-8 pt-12 pb-8 lg:px-10 lg:pt-14 lg:pb-10 bg-gradient-to-b from-slate-800/80 to-slate-900/80 backdrop-blur-xl rounded-[2.5rem] border border-teal-500/50 shadow-[0_0_40px_rgba(45,212,191,0.15)] transition-all duration-300 lg:-mt-8 lg:mb-8 text-left flex flex-col z-20">

          <!-- Glowing accent overlay -->
          <div class="absolute inset-0 bg-gradient-to-br from-teal-500/5 via-transparent to-cyan-500/5 rounded-[2.5rem] pointer-events-none"></div>

          <!-- Most Popular Badge -->
          <div class="absolute -top-5 left-1/2 -translate-x-1/2 bg-gradient-to-r from-teal-400 to-cyan-400 text-slate-950 text-xs font-extrabold uppercase tracking-widest px-5 py-2 rounded-full shadow-[0_0_20px_rgba(45,212,191,0.4)] flex items-center gap-1.5 whitespace-nowrap">
            <Star :size="14" class="fill-slate-950" />
            Most Popular
          </div>

          <div class="relative z-10 flex-1 flex flex-col">
            <div class="mb-8">
              <div class="inline-block px-3 py-1 bg-teal-500/10 text-teal-400 border border-teal-500/20 rounded-full text-xs font-bold uppercase tracking-wider mb-6">
                Best Value
              </div>
              <h3 class="text-2xl font-bold text-slate-50 mb-2">Premium</h3>
              <!-- Removed fixed height, added min-h for responsive wrapping -->
              <p class="text-slate-400 text-sm min-h-[3rem]">Full access. No limits. Total peace of mind.</p>
            </div>

            <div class="mb-8">
              <div class="flex items-baseline gap-1 mb-2">
                <p class="text-5xl font-extrabold text-white tracking-tight">€2.99</p>
                <span class="text-lg text-slate-400 font-medium">/mo</span>
              </div>
              <p class="text-teal-400 text-sm font-semibold">Billed monthly</p>
            </div>

            <ul class="space-y-4 text-slate-200 mb-10 flex-1">
              <li class="flex items-start gap-3">
                <CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0 mt-0.5 shadow-[0_0_10px_rgba(45,212,191,0.3)] rounded-full" />
                <span class="font-semibold text-white">Unlimited items</span>
              </li>
              <li class="flex items-start gap-3">
                <CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0 mt-0.5" />
                <span>Priority reminders</span>
              </li>
              <li class="flex items-start gap-3">
                <CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0 mt-0.5" />
                <span>Unlimited document uploads</span>
              </li>
              <li class="flex items-start gap-3">
                <CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0 mt-0.5" />
                <span>Advanced insights & analytics</span>
              </li>
              <li class="flex items-start gap-3">
                <CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0 mt-0.5" />
                <span>Priority support</span>
              </li>
              <li class="flex items-start gap-3">
                <CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0 mt-0.5" />
                <span>Early access to new features</span>
              </li>
            </ul>

            <div class="mt-auto">
              <button
                @click="handleUpgradeClick"
                :disabled="isLoading"
                class="group block text-center px-7 py-4 bg-gradient-to-r from-teal-400 to-cyan-400 text-slate-950 rounded-2xl text-lg font-bold shadow-[0_0_20px_rgba(45,212,191,0.3)] hover:shadow-[0_0_30px_rgba(45,212,191,0.5)] hover:from-teal-300 hover:to-cyan-300 transition-all items-center justify-center gap-2 disabled:opacity-70 disabled:cursor-not-allowed w-full"
              >
                <span v-if="isLoading" class="flex items-center justify-center gap-2">
                  <svg class="animate-spin h-5 w-5 text-slate-950" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                  Processing...
                </span>
                <span v-else class="flex items-center justify-center gap-2">
                  Upgrade Monthly
                  <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
                </span>
              </button>
              <p v-if="errorMessage" class="text-rose-400 text-sm mt-3 text-center font-medium">{{ errorMessage }}</p>
            </div>
          </div>
        </div>

        <!-- PREMIUM YEARLY (Right Card) -->
        <div class="group relative p-8 lg:p-10 bg-slate-900/40 backdrop-blur-md rounded-[2.5rem] border border-white/5 hover:border-teal-500/30 transition-all duration-300 text-left flex flex-col h-full">
          <div class="mb-8">
            <div class="inline-block px-3 py-1 bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 rounded-full text-xs font-bold uppercase tracking-wider mb-6">
              Save 33%
            </div>
            <h3 class="text-2xl font-bold text-slate-100 mb-2">Yearly</h3>
            <!-- Removed fixed height, added min-h for responsive wrapping -->
            <p class="text-slate-400 text-sm min-h-[3rem]">Save money with a one-time yearly payment.</p>
          </div>

          <div class="mb-8">
            <div class="flex items-baseline gap-1 mb-2">
              <p class="text-5xl font-extrabold text-slate-50 tracking-tight">€24</p>
              <span class="text-lg text-slate-500 font-medium">/yr</span>
            </div>
            <p class="text-cyan-400 text-sm font-semibold">€2/mo · Save €12/year</p>
          </div>

          <ul class="space-y-4 text-slate-300 mb-10 flex-1">
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500/70 flex-shrink-0 mt-0.5" />
              <span>Everything in Monthly</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5 shadow-[0_0_10px_rgba(45,212,191,0.2)] rounded-full" />
              <span class="font-semibold text-white">33% annual discount</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500/70 flex-shrink-0 mt-0.5" />
              <span>Priority support</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500/70 flex-shrink-0 mt-0.5" />
              <span>Exclusive yearly-only perks</span>
            </li>
          </ul>

          <RouterLink
            to="/register"
            class="block text-center px-7 py-4 bg-teal-500/10 hover:bg-teal-500/20 border border-teal-500/20 text-teal-400 rounded-2xl text-lg font-semibold transition-all duration-300 w-full group-hover:border-teal-500/40 mt-auto"
          >
            Upgrade Yearly
          </RouterLink>
        </div>

      </div>

      <!-- Trust Badge / Money Back Guarantee -->
      <div class="mt-20 p-1 bg-gradient-to-r from-teal-500/20 via-cyan-500/20 to-teal-500/20 rounded-3xl inline-block max-w-xl w-full">
        <div class="flex items-center gap-4 sm:gap-6 p-6 sm:p-8 bg-slate-950 rounded-[1.4rem]">
          <div class="w-14 h-14 shrink-0 rounded-2xl bg-teal-500/10 border border-teal-500/20 flex items-center justify-center shadow-[0_0_15px_rgba(45,212,191,0.15)]">
            <Shield :size="28" class="text-teal-400" />
          </div>
          <div class="text-left">
            <p class="text-lg font-bold text-slate-100 mb-1">30-day money-back guarantee</p>
            <p class="text-sm text-slate-400 leading-relaxed">No questions asked. Try it completely risk-free. Full refund if you're not entirely satisfied.</p>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>