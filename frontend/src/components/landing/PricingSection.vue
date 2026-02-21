<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { CheckCircle2, ArrowRight, Star, Shield, Award } from "lucide-vue-next"

const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref("")
const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000"

async function handleUpgradeClick() {
  try {
    isLoading.value = true; errorMessage.value = ""
    const token = localStorage.getItem("token")
    if (!token) { router.push("/login?redirect=/subscription"); return }
    const response = await fetch(`${API_URL}/payments/create-checkout-session`, {
      method: "POST", headers: { "Content-Type": "application/json", "Authorization": `Bearer ${token}` }
    })
    if (!response.ok) { const error = await response.json(); throw new Error(error.detail || "Failed to create checkout session") }
    const { url } = await response.json()
    window.location.href = url
  } catch (error) {
    errorMessage.value = error.message || "Failed to start checkout. Please try again."
    isLoading.value = false
  }
}
</script>

<template>
  <section id="pricing" class="py-24 md:py-32 relative z-10">
    <div class="max-w-screen-xl mx-auto px-6 text-center relative z-10">

      <div class="inline-flex items-center gap-2 px-4 py-2 bg-slate-900 ring-1 ring-white/10 text-slate-300 rounded-full mb-6 text-sm font-bold tracking-wide shadow-lg">
        <Award :size="16" class="text-teal-400" />
        Simple Pricing
      </div>

      <h2 class="text-4xl md:text-5xl font-extrabold text-white tracking-tight mb-6 text-balance">
        Choose the plan that <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-cyan-400">fits you.</span>
      </h2>

      <p class="text-lg text-slate-400 max-w-2xl mx-auto mb-16 text-balance">
        Start for free, upgrade when you need to. No hidden fees, cancel anytime.
      </p>

      <div class="grid lg:grid-cols-3 gap-8 max-w-6xl mx-auto items-stretch">

        <!-- FREE PLAN -->
        <div class="relative p-8 lg:p-10 bg-slate-900/50 backdrop-blur-xl rounded-[2.5rem] ring-1 ring-white/5 hover:ring-white/10 transition-all duration-300 text-left flex flex-col h-full shadow-2xl">
          <div class="mb-8">
            <div class="inline-block px-4 py-1.5 bg-slate-800 text-slate-300 rounded-full text-xs font-bold uppercase tracking-wider mb-6 ring-1 ring-white/5">
              Free Forever
            </div>
            <h3 class="text-2xl font-bold text-white mb-2">Basic</h3>
            <p class="text-slate-400 text-sm h-10">Perfect for getting your life organized.</p>
          </div>
          <div class="mb-8">
            <p class="text-5xl font-extrabold text-white tracking-tight mb-2">€0</p>
            <p class="text-slate-500 text-sm font-medium">No credit card required</p>
          </div>
          <ul class="space-y-4 text-slate-300 mb-10 flex-1">
            <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-slate-500 flex-shrink-0" /><span>Track up to 20 items</span></li>
            <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-slate-500 flex-shrink-0" /><span>Smart reminders</span></li>
            <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-slate-500 flex-shrink-0" /><span>Document uploads (100MB)</span></li>
          </ul>
          <RouterLink to="/register" class="block text-center px-7 py-4 bg-white/5 hover:bg-white/10 ring-1 ring-white/10 text-white rounded-2xl text-lg font-bold transition-all w-full mt-auto">
            Start Free
          </RouterLink>
        </div>

        <!-- PREMIUM MONTHLY (Animated Gradient Border) -->
        <div class="relative group flex flex-col h-full lg:-mt-6 lg:mb-6 z-20">
          <!-- Animated Glow Background -->
          <div class="absolute -inset-[2px] bg-gradient-to-b from-teal-400 via-cyan-500 to-emerald-500 rounded-[2.6rem] blur-md opacity-60 group-hover:opacity-100 transition-opacity duration-500"></div>
          <!-- Real Border -->
          <div class="absolute -inset-[1px] bg-gradient-to-b from-teal-400 via-cyan-500 to-emerald-500 rounded-[2.6rem]"></div>
          
          <div class="relative bg-slate-900 rounded-[2.5rem] h-full p-8 lg:p-10 flex flex-col z-10 shadow-2xl">
            <div class="absolute -top-5 left-1/2 -translate-x-1/2 bg-gradient-to-r from-teal-400 to-cyan-400 text-slate-950 text-xs font-extrabold uppercase tracking-widest px-5 py-2 rounded-full shadow-[0_0_20px_rgba(45,212,191,0.5)] flex items-center gap-1.5 whitespace-nowrap">
              <Star :size="14" class="fill-slate-950" /> Most Popular
            </div>

            <div class="mb-8 mt-4">
              <h3 class="text-2xl font-bold text-white mb-2">Premium</h3>
              <p class="text-slate-400 text-sm h-10">Full access. No limits. Total peace of mind.</p>
            </div>
            <div class="mb-8">
              <div class="flex items-baseline gap-1 mb-2">
                <p class="text-5xl font-extrabold text-white tracking-tight">€2.99</p>
                <span class="text-lg text-slate-400 font-medium">/mo</span>
              </div>
              <p class="text-teal-400 text-sm font-bold">Billed monthly</p>
            </div>
            <ul class="space-y-4 text-slate-200 mb-10 flex-1">
              <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0" /><span class="font-bold text-white">Unlimited items</span></li>
              <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0" /><span>Priority reminders</span></li>
              <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0" /><span>Unlimited document uploads</span></li>
              <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-teal-400 flex-shrink-0" /><span>Advanced analytics</span></li>
            </ul>
            <button @click="handleUpgradeClick" :disabled="isLoading" class="group/btn block text-center px-7 py-4 bg-gradient-to-r from-teal-400 to-cyan-400 text-slate-950 rounded-2xl text-lg font-bold shadow-[0_0_20px_rgba(45,212,191,0.4)] hover:shadow-[0_0_30px_rgba(45,212,191,0.6)] hover:scale-[1.02] transition-all disabled:opacity-70 w-full mt-auto flex items-center justify-center gap-2">
              <span v-if="isLoading">Processing...</span>
              <template v-else>Upgrade Monthly <ArrowRight :size="18" class="group-hover/btn:translate-x-1 transition-transform" /></template>
            </button>
            <p v-if="errorMessage" class="text-rose-400 text-sm mt-3 text-center font-bold">{{ errorMessage }}</p>
          </div>
        </div>

        <!-- PREMIUM YEARLY -->
        <div class="relative p-8 lg:p-10 bg-slate-900/50 backdrop-blur-xl rounded-[2.5rem] ring-1 ring-white/5 hover:ring-white/10 transition-all duration-300 text-left flex flex-col h-full shadow-2xl">
          <div class="mb-8">
            <div class="inline-block px-4 py-1.5 bg-cyan-500/10 text-cyan-400 rounded-full text-xs font-bold uppercase tracking-wider mb-6 ring-1 ring-cyan-500/20">
              Save 33%
            </div>
            <h3 class="text-2xl font-bold text-white mb-2">Yearly</h3>
            <p class="text-slate-400 text-sm h-10">Save money with a one-time yearly payment.</p>
          </div>
          <div class="mb-8">
            <div class="flex items-baseline gap-1 mb-2">
              <p class="text-5xl font-extrabold text-white tracking-tight">€24</p>
              <span class="text-lg text-slate-500 font-medium">/yr</span>
            </div>
            <p class="text-cyan-400 text-sm font-bold">€2/mo · Save €12/year</p>
          </div>
          <ul class="space-y-4 text-slate-300 mb-10 flex-1">
            <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-slate-500 flex-shrink-0" /><span>Everything in Monthly</span></li>
            <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-cyan-400 flex-shrink-0" /><span class="font-bold text-white">33% annual discount</span></li>
            <li class="flex items-start gap-3"><CheckCircle2 :size="20" class="text-slate-500 flex-shrink-0" /><span>Exclusive yearly perks</span></li>
          </ul>
          <RouterLink to="/register" class="block text-center px-7 py-4 bg-white/5 hover:bg-white/10 ring-1 ring-white/10 text-white rounded-2xl text-lg font-bold transition-all w-full mt-auto">
            Upgrade Yearly
          </RouterLink>
        </div>

      </div>

      <!-- Trust Badge -->
      <div class="mt-20 p-[1px] bg-gradient-to-r from-teal-500/30 via-cyan-500/30 to-teal-500/30 rounded-3xl inline-block max-w-xl w-full shadow-2xl">
        <div class="flex flex-col sm:flex-row items-center gap-4 sm:gap-6 p-6 sm:p-8 bg-slate-900 rounded-[calc(1.5rem-1px)]">
          <div class="w-16 h-16 shrink-0 rounded-2xl bg-teal-500/10 ring-1 ring-teal-500/30 flex items-center justify-center shadow-[0_0_20px_rgba(45,212,191,0.2)]">
            <Shield :size="32" class="text-teal-400" />
          </div>
          <div class="text-center sm:text-left">
            <p class="text-lg font-bold text-white mb-1">30-day money-back guarantee</p>
            <p class="text-sm text-slate-400 leading-relaxed text-balance">No questions asked. Try it completely risk-free. Full refund if you're not entirely satisfied.</p>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>