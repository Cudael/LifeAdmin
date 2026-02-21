<script setup>
import { ref, onMounted } from "vue"
import { ArrowRight, Sparkles, Plane, ShieldAlert, CreditCard, CheckCircle2, Clock } from "lucide-vue-next"

const stats = ref({ users: 0, documents: 0, reminders: 0 })

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
    stats.value = { users: Math.floor(current.users), documents: Math.floor(current.documents), reminders: Math.floor(current.reminders) }
    if (current.users >= targets.users) { clearInterval(interval); stats.value = targets }
  }, increment)
}

onMounted(() => { animateStats() })
</script>

<template>
  <section class="relative min-h-[90vh] flex flex-col items-center justify-start overflow-hidden pt-32 md:pt-40 z-10">
    
    <!-- High-end Grid Background -->
    <div class="absolute inset-0 z-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:32px_32px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)]"></div>

    <div class="relative z-10 max-w-5xl mx-auto px-6 text-center flex-1 flex flex-col items-center">
      
      <!-- New Badge -->
      <div class="inline-flex items-center gap-3 p-1 pr-4 bg-slate-900/80 backdrop-blur-xl ring-1 ring-white/10 rounded-full mb-10 animate-fade-in-down cursor-pointer hover:ring-teal-500/40 transition-all duration-300 shadow-xl">
        <span class="px-3 py-1.5 bg-white text-slate-950 text-xs font-bold rounded-full uppercase tracking-wider">v2.0</span>
        <span class="text-sm font-medium text-slate-300 flex items-center gap-1.5">
          <Sparkles :size="14" class="text-teal-400" />
          Meet the new AI Auto-Scanner
        </span>
        <ArrowRight :size="14" class="text-slate-500 ml-1" />
      </div>

      <!-- Hero Typography -->
      <h1 class="text-6xl md:text-7xl lg:text-[5.5rem] font-extrabold tracking-tighter leading-[1.05] mb-8 animate-fade-in-up text-balance text-white">
        Master your life's admin. <br />
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal-300 via-cyan-300 to-emerald-300 pb-2">
          Effortlessly.
        </span>
      </h1>

      <p class="text-lg md:text-xl text-slate-400 max-w-2xl mx-auto mb-12 animate-fade-in-up animation-delay-200 text-balance leading-relaxed">
        The intelligent vault that monitors your documents, tracks your subscriptions, and eliminates missed deadlines so you can focus on living.
      </p>

      <!-- CTA -->
      <div class="flex flex-col sm:flex-row justify-center items-center gap-4 mb-24 animate-fade-in-up animation-delay-400 w-full sm:w-auto">
        <RouterLink
          to="/register"
          class="group relative px-8 py-4 bg-white text-slate-950 rounded-full text-lg font-bold shadow-[0_0_40px_rgba(255,255,255,0.2)] hover:shadow-[0_0_60px_rgba(255,255,255,0.3)] hover:scale-[1.02] transition-all duration-300 flex items-center justify-center gap-2 w-full sm:w-auto ring-1 ring-white/50"
        >
          Start for free
          <ArrowRight :size="18" class="group-hover:translate-x-1 transition-transform" />
        </RouterLink>

        <RouterLink
          to="/demo"
          class="px-8 py-4 bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/10 text-white rounded-full text-lg font-medium hover:bg-slate-800 transition-all duration-300 w-full sm:w-auto flex justify-center items-center gap-2 shadow-lg"
        >
          See how it works
        </RouterLink>
      </div>
    </div>

    <!-- UI Dashboard Preview -->
    <div class="relative z-10 w-full max-w-6xl mx-auto px-4 mt-auto animate-fade-in-up animation-delay-600 hidden md:block">
      <!-- Glow behind dashboard -->
      <div class="absolute inset-0 bg-gradient-to-t from-teal-500/20 to-transparent blur-[100px] -z-10"></div>
      
      <div class="relative w-full h-[450px] bg-slate-900/60 backdrop-blur-3xl ring-1 ring-white/10 rounded-t-[2.5rem] shadow-[0_-20px_80px_rgba(0,0,0,0.6)] [mask-image:linear-gradient(to_bottom,black_50%,transparent_100%)] overflow-hidden flex flex-col">
        
        <!-- Window Controls -->
        <div class="h-14 border-b border-white/5 flex items-center px-6 gap-2 bg-white/[0.01]">
          <div class="w-3 h-3 rounded-full bg-slate-700 hover:bg-rose-500 transition-colors"></div>
          <div class="w-3 h-3 rounded-full bg-slate-700 hover:bg-amber-500 transition-colors"></div>
          <div class="w-3 h-3 rounded-full bg-slate-700 hover:bg-emerald-500 transition-colors"></div>
          
          <div class="ml-auto flex gap-6 text-xs font-bold text-slate-500 tracking-wider uppercase">
            <span class="flex items-center gap-2"><div class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shadow-[0_0_10px_rgba(52,211,153,0.8)]"></div> {{ stats.users }}+ Online</span>
          </div>
        </div>

        <div class="flex-1 p-8 relative">
          <!-- Sidebar -->
          <div class="absolute left-8 top-8 bottom-8 w-56 border-r border-white/5 space-y-5 pr-6">
            <div class="h-8 w-full bg-white/5 rounded-lg border border-white/5"></div>
            <div class="h-4 w-2/3 bg-white/5 rounded-md"></div>
            <div class="h-4 w-3/4 bg-white/5 rounded-md"></div>
            <div class="h-4 w-1/2 bg-white/5 rounded-md mt-10"></div>
            <div class="h-4 w-full bg-white/5 rounded-md"></div>
          </div>

          <!-- Floating Cards -->
          <div class="ml-64 relative h-full flex justify-center items-start pt-8 gap-8 perspective-[1000px]">

            <div class="w-72 bg-slate-800/90 backdrop-blur-2xl rounded-2xl p-5 ring-1 ring-rose-500/30 shadow-[0_20px_50px_rgba(0,0,0,0.5),0_0_30px_rgba(225,29,72,0.1)] animate-float transform -rotate-3 z-20">
              <div class="flex justify-between items-start mb-5">
                <div class="w-12 h-12 rounded-xl bg-rose-500/20 flex items-center justify-center text-rose-400 ring-1 ring-rose-500/30">
                  <Plane :size="22" />
                </div>
                <span class="px-3 py-1 bg-rose-500/20 text-rose-300 text-xs font-bold rounded-full ring-1 ring-rose-500/40">Urgent</span>
              </div>
              <h4 class="text-white font-bold text-lg mb-1">Passport Expiring</h4>
              <p class="text-slate-400 text-sm mb-4">Action required in 14 days.</p>
              <div class="w-full bg-slate-900 rounded-full h-2 mb-1 ring-1 ring-white/5 overflow-hidden">
                <div class="bg-gradient-to-r from-rose-600 to-rose-400 h-full w-[85%] rounded-full shadow-[0_0_10px_rgba(225,29,72,0.5)]"></div>
              </div>
            </div>

            <div class="w-72 bg-slate-800/90 backdrop-blur-2xl rounded-2xl p-5 ring-1 ring-amber-500/30 shadow-[0_20px_50px_rgba(0,0,0,0.5),0_0_30px_rgba(245,158,11,0.1)] animate-float-delayed transform translate-y-10 z-10">
              <div class="flex justify-between items-start mb-5">
                <div class="w-12 h-12 rounded-xl bg-amber-500/20 flex items-center justify-center text-amber-400 ring-1 ring-amber-500/30">
                  <CreditCard :size="22" />
                </div>
                <span class="flex items-center gap-1.5 text-slate-400 text-xs font-bold bg-slate-900/50 px-3 py-1 rounded-full ring-1 ring-white/5">
                  <Clock :size="12" class="text-amber-400" /> in 3 days
                </span>
              </div>
              <h4 class="text-white font-bold text-lg mb-1">Car Insurance</h4>
              <p class="text-slate-400 text-sm mb-5">Auto-renews for €850.00.</p>
              <button class="w-full py-2.5 bg-white/5 hover:bg-white/10 text-white text-sm font-bold rounded-xl transition-colors ring-1 ring-white/10">
                Review Policy
              </button>
            </div>

            <div class="w-72 bg-slate-800/90 backdrop-blur-2xl rounded-2xl p-5 ring-1 ring-emerald-500/30 shadow-[0_20px_50px_rgba(0,0,0,0.5),0_0_30px_rgba(16,185,129,0.1)] animate-float transform rotate-3 z-20">
              <div class="flex justify-between items-start mb-5">
                <div class="w-12 h-12 rounded-xl bg-emerald-500/20 flex items-center justify-center text-emerald-400 ring-1 ring-emerald-500/30">
                  <ShieldAlert :size="22" />
                </div>
                <CheckCircle2 :size="22" class="text-emerald-400 drop-shadow-[0_0_8px_rgba(52,211,153,0.5)]" />
              </div>
              <h4 class="text-white font-bold text-lg mb-1">Tax Returns 2025</h4>
              <p class="text-slate-400 text-sm mb-5">Encrypted and securely backed up.</p>
              <div class="flex items-center gap-2.5 bg-slate-900/50 p-2 rounded-xl ring-1 ring-white/5">
                <div class="flex -space-x-2">
                  <div class="w-6 h-6 rounded-full bg-gradient-to-br from-teal-400 to-cyan-500 ring-2 ring-slate-800"></div>
                  <div class="w-6 h-6 rounded-full bg-gradient-to-br from-indigo-400 to-purple-500 ring-2 ring-slate-800"></div>
                </div>
                <span class="text-xs text-slate-300 font-semibold">Shared with Accountant</span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@keyframes fade-in-down { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fade-in-up { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
@keyframes float { 0%, 100% { transform: translateY(0px) rotate(-3deg); } 50% { transform: translateY(-12px) rotate(-1deg); } }
@keyframes float-delayed { 0%, 100% { transform: translateY(40px); } 50% { transform: translateY(28px); } }

.animate-fade-in-down { animation: fade-in-down 0.8s cubic-bezier(0.16, 1, 0.3, 1); }
.animate-fade-in-up { animation: fade-in-up 1s cubic-bezier(0.16, 1, 0.3, 1); animation-fill-mode: both; }
.animation-delay-200 { animation-delay: 0.1s; }
.animation-delay-400 { animation-delay: 0.2s; }
.animation-delay-600 { animation-delay: 0.4s; }
.animate-float { animation: float 7s ease-in-out infinite; }
.animate-float-delayed { animation: float-delayed 8s ease-in-out infinite 1s; }
</style>