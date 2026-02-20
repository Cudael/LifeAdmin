<template>
  <DashboardLayout pageTitle="Billing & Plans">
    
    <!-- Ambient Background Mesh -->
    <div class="fixed inset-0 z-0 bg-[linear-gradient(to_right,#80808008_1px,transparent_1px),linear-gradient(to_bottom,#80808008_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none"></div>
    <div class="fixed top-0 right-1/4 w-[600px] h-[500px] bg-teal-500/10 blur-[150px] rounded-full pointer-events-none z-0 mix-blend-screen"></div>

    <div class="relative z-10 max-w-[1200px] mx-auto pb-12 animate-fade-in-up">
      
      <!-- ALERTS -->
      <Transition enter-active-class="transition-all duration-300 ease-out" enter-from-class="opacity-0 -translate-y-4" leave-active-class="transition-all duration-200" leave-to-class="opacity-0 -translate-y-4">
        <div v-if="showSuccess" class="mb-8 flex items-center gap-3 p-4 bg-emerald-500/10 border border-emerald-500/20 rounded-2xl shadow-inner">
          <div class="w-10 h-10 rounded-xl bg-emerald-500/20 flex items-center justify-center text-emerald-400 shrink-0"><CheckCircle2 :size="20" /></div>
          <div>
            <p class="font-bold text-emerald-300 text-sm">Payment Successful</p>
            <p class="text-xs font-medium text-emerald-400/70">Your vault has been upgraded to Pro.</p>
          </div>
        </div>
      </Transition>

      <Transition enter-active-class="transition-all duration-300 ease-out" enter-from-class="opacity-0 -translate-y-4" leave-active-class="transition-all duration-200" leave-to-class="opacity-0 -translate-y-4">
        <div v-if="showCanceled" class="mb-8 flex items-center gap-3 p-4 bg-amber-500/10 border border-amber-500/20 rounded-2xl shadow-inner">
          <div class="w-10 h-10 rounded-xl bg-amber-500/20 flex items-center justify-center text-amber-400 shrink-0"><AlertCircle :size="20" /></div>
          <div>
            <p class="font-bold text-amber-300 text-sm">Checkout Cancelled</p>
            <p class="text-xs font-medium text-amber-400/70">No charges were made. You can upgrade anytime.</p>
          </div>
        </div>
      </Transition>

      <!-- PAGE HEADER -->
      <div class="mb-10">
        <h1 class="text-3xl font-extrabold text-white mb-2 tracking-tight">Subscription & Billing</h1>
        <p class="text-slate-400 font-medium">Manage your vault capacity and premium features.</p>
      </div>

      <!-- BENTO BOX OVERVIEW -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-10">
        
        <!-- Current Plan Status -->
        <div class="lg:col-span-2 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 p-8 shadow-2xl relative overflow-hidden flex flex-col justify-between">
          <!-- Pro Glow -->
          <div v-if="isPremium" class="absolute top-0 right-0 w-64 h-64 bg-teal-500/10 blur-[80px] rounded-full pointer-events-none"></div>

          <div class="flex items-start justify-between mb-8 relative z-10">
            <div>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-2">Current Plan</p>
              <h2 class="text-3xl font-extrabold text-white tracking-tight flex items-center gap-3">
                LifeAdmin {{ isPremium ? 'Pro' : 'Basic' }}
                <Sparkles v-if="isPremium" :size="24" class="text-teal-400" />
              </h2>
            </div>
            
            <div class="flex items-center gap-2">
              <span 
                v-if="subscriptionStatus"
                class="px-3 py-1.5 rounded-lg text-[10px] font-bold uppercase tracking-widest border shadow-inner"
                :class="{
                  'bg-emerald-500/10 text-emerald-400 border-emerald-500/20': subscriptionStatus === 'active',
                  'bg-blue-500/10 text-blue-400 border-blue-500/20': subscriptionStatus === 'trialing',
                  'bg-rose-500/10 text-rose-400 border-rose-500/20': subscriptionStatus === 'past_due',
                  'bg-slate-800 text-slate-400 border-white/5': !['active', 'trialing', 'past_due'].includes(subscriptionStatus)
                }"
              >
                {{ subscriptionStatus }}
              </span>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row items-center gap-4 relative z-10 border-t border-white/5 pt-6">
            <button
              v-if="isPremium"
              @click="handleManageSubscription"
              :disabled="isLoading"
              class="w-full sm:w-auto px-6 py-3.5 bg-slate-800 hover:bg-slate-700 border border-white/5 text-white rounded-xl font-bold transition-all duration-300 disabled:opacity-50 flex items-center justify-center gap-2 shadow-inner"
            >
              <Loader2 v-if="isLoading" :size="18" class="animate-spin" />
              <CreditCard v-else :size="18" class="text-slate-400" />
              Manage Billing
            </button>
            <div v-if="isPremium && subscriptionCurrentPeriodEnd" class="text-sm font-medium text-slate-400 flex items-center gap-2 w-full sm:w-auto justify-center sm:justify-start">
              <Calendar :size="16" class="text-teal-400" /> Renews {{ formatDate(subscriptionCurrentPeriodEnd) }}
            </div>
            
            <button
              v-if="!isPremium"
              @click="handleUpgrade"
              :disabled="isLoading"
              class="w-full sm:w-auto group px-8 py-3.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.2)] hover:shadow-[0_0_30px_rgba(45,212,191,0.4)] transition-all duration-300 disabled:opacity-50 flex items-center justify-center gap-2"
            >
              <Loader2 v-if="isLoading" :size="18" class="animate-spin" />
              <Zap v-else :size="18" class="group-hover:scale-110 transition-transform" />
              Upgrade to Pro
            </button>
          </div>
          <p v-if="errorMessage" class="text-rose-400 text-xs font-bold mt-4">{{ errorMessage }}</p>
        </div>

        <!-- Vault Usage -->
        <div class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 p-8 shadow-2xl relative overflow-hidden flex flex-col justify-center">
          <div class="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 mb-6 shadow-inner">
            <Database :size="24" />
          </div>
          <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-2">Vault Capacity</p>
          <div class="flex items-baseline gap-2 mb-4">
            <span class="text-4xl font-extrabold text-white tracking-tight">{{ itemCount }}</span>
            <span class="text-lg font-medium text-slate-500" v-if="!isPremium">/ 20 items</span>
            <span class="text-lg font-medium text-teal-400" v-else>Unlimited</span>
          </div>

          <div v-if="!isPremium" class="space-y-2">
            <div class="h-2 w-full bg-slate-950 rounded-full overflow-hidden shadow-inner border border-white/5">
              <div 
                class="h-full transition-all duration-1000"
                :class="itemCount >= 20 ? 'bg-rose-500 shadow-[0_0_10px_rgba(225,29,72,0.8)]' : itemCount >= 15 ? 'bg-amber-400 shadow-[0_0_10px_rgba(251,191,36,0.8)]' : 'bg-indigo-500 shadow-[0_0_10px_rgba(99,102,241,0.8)]'"
                :style="`width: ${Math.min((itemCount / 20) * 100, 100)}%`"
              ></div>
            </div>
            <p v-if="itemCount >= 20" class="text-[10px] font-bold uppercase tracking-widest text-rose-400 flex items-center gap-1">
              <AlertTriangle :size="10" /> Capacity Reached
            </p>
            <p v-else class="text-[10px] font-bold uppercase tracking-widest text-slate-500">{{ 20 - itemCount }} slots remaining</p>
          </div>
        </div>

      </div>

      <!-- PRICING TIERS -->
      <h2 class="text-xl font-extrabold text-white mb-6 tracking-tight">Compare Plans</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <!-- Free Plan -->
        <div class="bg-slate-900/40 backdrop-blur-xl rounded-[2rem] border border-white/5 p-8 shadow-xl">
          <div class="mb-8">
            <h3 class="text-2xl font-extrabold text-white mb-2">Basic</h3>
            <p class="text-slate-400 text-sm font-medium h-10">Essential features to start organizing your life.</p>
            <div class="mt-6 flex items-baseline gap-1">
              <span class="text-4xl font-extrabold text-white">€0</span>
              <span class="text-slate-500 font-bold uppercase text-[10px] tracking-widest">/ forever</span>
            </div>
          </div>

          <div class="h-px bg-white/5 w-full mb-8"></div>

          <ul class="space-y-4">
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-slate-800 flex items-center justify-center shrink-0 text-slate-400"><Check :size="12" /></div>
              <span class="text-sm font-medium text-slate-300">Track up to 20 items</span>
            </li>
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-slate-800 flex items-center justify-center shrink-0 text-slate-400"><Check :size="12" /></div>
              <span class="text-sm font-medium text-slate-300">Smart notifications</span>
            </li>
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-slate-800 flex items-center justify-center shrink-0 text-slate-400"><Check :size="12" /></div>
              <span class="text-sm font-medium text-slate-300">Document uploads (100MB)</span>
            </li>
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-slate-800 flex items-center justify-center shrink-0 text-slate-400"><Check :size="12" /></div>
              <span class="text-sm font-medium text-slate-300">Secure cloud storage</span>
            </li>
          </ul>
        </div>

        <!-- Pro Plan -->
        <div class="bg-slate-900/80 backdrop-blur-xl rounded-[2rem] border border-teal-500/30 p-8 shadow-2xl relative overflow-hidden">
          <div class="absolute top-0 right-0 w-64 h-64 bg-teal-500/10 blur-[80px] rounded-full pointer-events-none"></div>
          <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-teal-400 to-cyan-400"></div>

          <div class="mb-8 relative z-10">
            <div class="flex justify-between items-start">
              <h3 class="text-2xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-cyan-400 mb-2">Pro</h3>
              <span class="px-3 py-1 bg-teal-500/10 border border-teal-500/20 text-teal-400 text-[10px] font-bold uppercase tracking-widest rounded-full">Recommended</span>
            </div>
            <p class="text-slate-300 text-sm font-medium h-10">Ultimate peace of mind with unlimited capacity.</p>
            <div class="mt-6 flex items-baseline gap-1">
              <span class="text-4xl font-extrabold text-white">€2.99</span>
              <span class="text-slate-400 font-bold uppercase text-[10px] tracking-widest">/ month</span>
            </div>
          </div>

          <button
            v-if="!isPremium"
            @click="handleUpgrade"
            :disabled="isLoading"
            class="w-full group px-6 py-4 mb-8 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.2)] hover:shadow-[0_0_30px_rgba(45,212,191,0.4)] transition-all duration-300 disabled:opacity-50 flex items-center justify-center gap-2 relative z-10"
          >
            <Loader2 v-if="isLoading" :size="18" class="animate-spin" />
            <span v-else>Upgrade to Pro</span>
          </button>
          
          <div v-else class="w-full px-6 py-4 mb-8 bg-teal-500/10 border border-teal-500/20 text-teal-400 rounded-xl font-bold flex items-center justify-center gap-2 relative z-10">
            <CheckCircle2 :size="18" /> Active Plan
          </div>

          <div class="h-px bg-white/5 w-full mb-8 relative z-10"></div>

          <ul class="space-y-4 relative z-10">
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-teal-500/20 flex items-center justify-center shrink-0 text-teal-400 shadow-[0_0_10px_rgba(45,212,191,0.3)]"><Check :size="12" stroke-width="3" /></div>
              <span class="text-sm font-bold text-white">Unlimited vault items</span>
            </li>
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-teal-500/20 flex items-center justify-center shrink-0 text-teal-400 shadow-[0_0_10px_rgba(45,212,191,0.3)]"><Check :size="12" stroke-width="3" /></div>
              <span class="text-sm font-bold text-white">Priority push & email reminders</span>
            </li>
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-teal-500/20 flex items-center justify-center shrink-0 text-teal-400 shadow-[0_0_10px_rgba(45,212,191,0.3)]"><Check :size="12" stroke-width="3" /></div>
              <span class="text-sm font-bold text-white">Unlimited document storage</span>
            </li>
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-teal-500/20 flex items-center justify-center shrink-0 text-teal-400 shadow-[0_0_10px_rgba(45,212,191,0.3)]"><Check :size="12" stroke-width="3" /></div>
              <span class="text-sm font-bold text-white">Advanced insights & analytics</span>
            </li>
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-teal-500/20 flex items-center justify-center shrink-0 text-teal-400 shadow-[0_0_10px_rgba(45,212,191,0.3)]"><Check :size="12" stroke-width="3" /></div>
              <span class="text-sm font-medium text-slate-300">Priority customer support</span>
            </li>
            <li class="flex items-start gap-3">
              <div class="mt-0.5 w-5 h-5 rounded-full bg-teal-500/20 flex items-center justify-center shrink-0 text-teal-400 shadow-[0_0_10px_rgba(45,212,191,0.3)]"><Check :size="12" stroke-width="3" /></div>
              <span class="text-sm font-medium text-slate-300">Early access to new features</span>
            </li>
          </ul>
        </div>

      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import { apiFetch } from '../utils/api'
import DashboardLayout from '../layouts/DashboardLayout.vue'
import { 
  CheckCircle2, AlertCircle, Calendar, CreditCard, Sparkles, Database, AlertTriangle, Check, Zap, Loader2
} from 'lucide-vue-next'

const route = useRoute()
const router = useRouter()
const authStore = useAuthStore()

const isLoading = ref(false)
const errorMessage = ref("")
const showSuccess = ref(false)
const showCanceled = ref(false)
const itemCount = ref(0)

const isPremium = computed(() => authStore.isPremium)
const subscriptionStatus = computed(() => authStore.subscriptionStatus)
const subscriptionCurrentPeriodEnd = computed(() => authStore.subscriptionCurrentPeriodEnd)

function formatDate(dateString) {
  if (!dateString) return ""
  return new Date(dateString).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
}

async function handleUpgrade() {
  try {
    isLoading.value = true
    errorMessage.value = ""
    
    const res = await apiFetch("/payments/create-checkout-session", { method: "POST" })
    if (!res.ok) throw new Error((await res.json()).detail || "Failed to create checkout session")
    
    const { url } = await res.json()
    window.location.href = url
  } catch (error) {
    errorMessage.value = error.message || "Failed to start checkout. Please try again."
    isLoading.value = false
  }
}

async function handleManageSubscription() {
  try {
    isLoading.value = true
    errorMessage.value = ""
    
    const res = await apiFetch("/payments/create-portal-session", { method: "POST" })
    if (!res.ok) throw new Error((await res.json()).detail || "Failed to open portal")
    
    const { url } = await res.json()
    window.location.href = url
  } catch (error) {
    errorMessage.value = error.message || "Failed to open subscription portal. Please try again."
    isLoading.value = false
  }
}

async function fetchItemCount() {
  try {
    const res = await apiFetch("/items")
    if (res.ok) {
      const data = await res.json()
      itemCount.value = data.length || data.items?.length || 0
    }
  } catch (error) {
    console.error("Failed to fetch item count:", error)
  }
}

onMounted(async () => {
  if (route.query.success === 'true') {
    showSuccess.value = true
    await authStore.fetchSubscriptionStatus()
    setTimeout(() => { showSuccess.value = false; router.replace({ query: {} }) }, 5000)
  }
  
  if (route.query.canceled === 'true') {
    showCanceled.value = true
    setTimeout(() => { showCanceled.value = false; router.replace({ query: {} }) }, 5000)
  }
  
  await authStore.fetchSubscriptionStatus()
  await fetchItemCount()
})
</script>

<style scoped>
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
  animation: fade-in-up 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>