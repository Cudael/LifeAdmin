<script setup>
import { ref, onMounted } from "vue"
import { 
  ArrowRight, 
  Sparkles,
  Plane,
  ShieldAlert,
  CreditCard,
  CheckCircle2,
  Clock
} from "lucide-vue-next"

const stats = ref({
  users: 0,
  documents: 0,
  reminders: 0
})

const animateStats = () => {
  const targets = { users: 500, documents: 5000, reminders: 2500 }
  const duration = 2000
  const steps = 60
  const increment = duration / steps

  let current = { users: 0, documents: 0, reminders: 0 }

  const interval = setInterval(() => {
    current.users += targets.users / steps
    current.documents += targets.documents / steps
    current.reminders += targets.reminders / steps

    stats.value = {
      users: Math.floor(current.users),
      documents: Math.floor(current.documents),
      reminders: Math.floor(current.reminders)
    }

    if (current.users >= targets.users) {
      clearInterval(interval)
      stats.value = targets
    }
  }, increment)
}

onMounted(() => {
  animateStats()
})
</script>

<template>
  <section class="relative min-h-screen flex flex-col items-center justify-start overflow-hidden text-slate-50 pt-28 md:pt-36 z-10">

    <!-- Deep Space Grid Background -->
    <div class="absolute inset-0 z-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px] [mask-image:radial-gradient(ellipse_80%_50%_at_50%_0%,#000_70%,transparent_100%)]"></div>
    
    <!-- Massive ambient background glows -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-3xl h-[600px] bg-teal-500/10 blur-[120px] rounded-full pointer-events-none z-0 mix-blend-screen"></div>
    <div class="absolute top-40 right-0 w-96 h-96 bg-cyan-500/10 blur-[120px] rounded-full pointer-events-none z-0 mix-blend-screen"></div>

    <!-- MAIN HERO CONTENT -->
    <div class="relative z-10 max-w-5xl mx-auto px-6 text-center flex-1 flex flex-col items-center">

      <!-- Glowing Pill Badge -->
      <div class="inline-flex items-center gap-3 p-1.5 pr-4 bg-slate-900/50 backdrop-blur-md border border-white/10 rounded-full mb-8 animate-fade-in-down cursor-pointer hover:border-teal-500/30 hover:bg-slate-800/80 transition-all duration-300 shadow-[0_0_20px_rgba(0,0,0,0.2)]">
        <span class="px-3 py-1 bg-gradient-to-r from-teal-400 to-cyan-400 text-slate-950 text-xs font-bold rounded-full uppercase tracking-widest shadow-sm">v2.0</span>
        <span class="text-sm font-medium text-slate-300 flex items-center gap-2">
          <Sparkles :size="14" class="text-teal-400" />
          Meet the new AI Auto-Scanner
        </span>
        <ArrowRight :size="14" class="text-slate-500 ml-1" />
      </div>

      <!-- Ultra-tight, massive typography -->
      <h1 class="text-6xl md:text-7xl lg:text-8xl font-extrabold tracking-tighter leading-[1.05] mb-8 animate-fade-in-up">
        Master your life's admin. <br />
        <span class="bg-gradient-to-r from-teal-400 via-cyan-400 to-blue-400 bg-clip-text text-transparent drop-shadow-sm pb-2 inline-block">
          Effortlessly.
        </span>
      </h1>

      <p class="text-lg md:text-2xl text-slate-400 max-w-2xl mx-auto mb-10 animate-fade-in-up animation-delay-200 leading-relaxed font-light">
        The intelligent vault that monitors your documents, tracks your subscriptions, and eliminates missed deadlines.
      </p>

      <!-- CTA Buttons with glowing aura -->
      <div class="flex flex-col sm:flex-row justify-center items-center gap-5 mb-20 animate-fade-in-up animation-delay-400 w-full sm:w-auto">
        <div class="relative group/btn w-full sm:w-auto">
          <div class="absolute -inset-1 bg-gradient-to-r from-teal-500 to-cyan-500 rounded-full blur opacity-60 group-hover/btn:opacity-100 transition duration-300 group-hover/btn:duration-200"></div>
          <RouterLink
            to="/register"
            class="relative px-8 py-4 bg-slate-950 text-white rounded-full text-lg font-bold border border-white/10 hover:bg-slate-900 transition-all duration-300 flex items-center justify-center gap-2 w-full"
          >
            Start for free
            <ArrowRight :size="18" class="group-hover/btn:translate-x-1 transition-transform text-teal-400" />
          </RouterLink>
        </div>

        <RouterLink
          to="/demo"
          class="px-8 py-4 bg-white/5 backdrop-blur-md border border-white/10 text-white rounded-full text-lg font-medium hover:bg-white/10 transition-all duration-300 w-full sm:w-auto flex justify-center items-center gap-2"
        >
          See how it works
        </RouterLink>
      </div>

    </div>

    <!-- ABSTRACT UI DASHBOARD PREVIEW (CSS Only) -->
    <div class="relative z-10 w-full max-w-6xl mx-auto px-4 sm:px-6 mt-auto animate-fade-in-up animation-delay-600 hidden md:block">
      
      <!-- Fades out the bottom of the dashboard smoothly into the next section -->
      <div class="relative w-full h-[400px] bg-slate-900/40 backdrop-blur-2xl border-t border-l border-r border-white/10 rounded-t-[2.5rem] shadow-[0_-20px_50px_rgba(0,0,0,0.5)] [mask-image:linear-gradient(to_bottom,black_40%,transparent_100%)] overflow-hidden flex flex-col">
        
        <!-- Mac-style App Window Header -->
        <div class="h-14 border-b border-white/5 flex items-center px-6 gap-3 bg-white/[0.02]">
          <div class="w-3.5 h-3.5 rounded-full bg-rose-500/50 border border-rose-500/20"></div>
          <div class="w-3.5 h-3.5 rounded-full bg-amber-500/50 border border-amber-500/20"></div>
          <div class="w-3.5 h-3.5 rounded-full bg-emerald-500/50 border border-emerald-500/20"></div>
          
          <!-- Live Stats incorporated into the UI -->
          <div class="ml-auto flex gap-6 text-xs font-semibold text-slate-500 tracking-wider uppercase">
            <span class="flex items-center gap-1.5"><div class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></div> {{ stats.users }}+ Online</span>
            <span>{{ stats.documents.toLocaleString() }} Vaults secured</span>
          </div>
        </div>

        <!-- Dashboard Content Area -->
        <div class="flex-1 p-8 relative">
          
          <!-- Abstract Sidebar -->
          <div class="absolute left-8 top-8 bottom-8 w-48 border-r border-white/5 space-y-4">
            <div class="h-8 w-3/4 bg-white/5 rounded-lg"></div>
            <div class="h-4 w-1/2 bg-white/5 rounded-lg"></div>
            <div class="h-4 w-2/3 bg-white/5 rounded-lg"></div>
            <div class="h-4 w-1/2 bg-white/5 rounded-lg mt-8"></div>
            <div class="h-4 w-3/4 bg-white/5 rounded-lg"></div>
          </div>

          <!-- Floating Notification Cards (The core value prop visualization) -->
          <div class="ml-56 relative h-full flex justify-center items-start pt-10 gap-6">

            <!-- Danger Card (Passport Expiring) -->
            <div class="w-72 bg-slate-800/80 backdrop-blur-md rounded-2xl p-5 border border-rose-500/30 shadow-[0_10px_40px_rgba(225,29,72,0.15)] animate-float transform -rotate-2 z-20">
              <div class="flex justify-between items-start mb-4">
                <div class="w-10 h-10 rounded-xl bg-rose-500/20 flex items-center justify-center text-rose-400">
                  <Plane :size="20" />
                </div>
                <span class="px-2.5 py-1 bg-rose-500/10 text-rose-400 text-xs font-bold rounded-full">Urgent</span>
              </div>
              <h4 class="text-slate-100 font-bold mb-1">Passport Expiring</h4>
              <p class="text-slate-400 text-sm mb-3">Action required in 14 days.</p>
              <div class="w-full bg-slate-900 rounded-full h-1.5 mb-2">
                <div class="bg-rose-500 h-1.5 rounded-full w-[85%]"></div>
              </div>
            </div>

            <!-- Warning Card (Subscription Renewal) -->
            <div class="w-72 bg-slate-800/80 backdrop-blur-md rounded-2xl p-5 border border-amber-500/30 shadow-[0_10px_40px_rgba(245,158,11,0.1)] animate-float-delayed transform translate-y-12 z-10">
              <div class="flex justify-between items-start mb-4">
                <div class="w-10 h-10 rounded-xl bg-amber-500/20 flex items-center justify-center text-amber-400">
                  <CreditCard :size="20" />
                </div>
                <span class="flex items-center gap-1 text-slate-500 text-xs font-semibold">
                  <Clock :size="12" /> in 3 days
                </span>
              </div>
              <h4 class="text-slate-100 font-bold mb-1">Annual Car Insurance</h4>
              <p class="text-slate-400 text-sm mb-4">Auto-renews for €850.00.</p>
              <button class="w-full py-2 bg-white/5 hover:bg-white/10 text-slate-300 text-sm font-semibold rounded-lg transition-colors border border-white/10">
                Review Policy
              </button>
            </div>

            <!-- Success Card (Protected Document) -->
            <div class="w-72 bg-slate-800/80 backdrop-blur-md rounded-2xl p-5 border border-emerald-500/30 shadow-[0_10px_40px_rgba(16,185,129,0.1)] animate-float transform rotate-2 z-20">
              <div class="flex justify-between items-start mb-4">
                <div class="w-10 h-10 rounded-xl bg-emerald-500/20 flex items-center justify-center text-emerald-400">
                  <ShieldAlert :size="20" />
                </div>
                <CheckCircle2 :size="18" class="text-emerald-400" />
              </div>
              <h4 class="text-slate-100 font-bold mb-1">Tax Returns 2025</h4>
              <p class="text-slate-400 text-sm mb-4">Encrypted and securely backed up.</p>
              <div class="flex items-center gap-2">
                <div class="flex -space-x-2">
                  <div class="w-6 h-6 rounded-full bg-teal-500/20 border border-teal-500/50"></div>
                  <div class="w-6 h-6 rounded-full bg-cyan-500/20 border border-cyan-500/50"></div>
                </div>
                <span class="text-xs text-slate-500 font-medium">Shared with Accountant</span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@keyframes fade-in-down {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px) rotate(-2deg);
  }
  50% {
    transform: translateY(-10px) rotate(-1deg);
  }
}

@keyframes float-delayed {
  0%, 100% {
    transform: translateY(48px); /* 48px = translate-y-12 */
  }
  50% {
    transform: translateY(38px);
  }
}

.animate-fade-in-down {
  animation: fade-in-down 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.animate-fade-in-up {
  animation: fade-in-up 1s cubic-bezier(0.16, 1, 0.3, 1);
  animation-fill-mode: both;
}

.animation-delay-200 {
  animation-delay: 0.1s;
}

.animation-delay-400 {
  animation-delay: 0.2s;
}

.animation-delay-600 {
  animation-delay: 0.4s;
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-float-delayed {
  animation: float-delayed 8s ease-in-out infinite 1s;
}
</style>