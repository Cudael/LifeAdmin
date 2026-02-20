<script setup>
import { TrendingUp, AlertCircle, DollarSign, SearchX, ShieldCheck, Flame } from "lucide-vue-next"
</script>

<template>
  <section class="py-32 relative overflow-hidden z-10">
    
    <!-- Dramatic ambient background for the "Problem" section -->
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,rgba(239,68,68,0.03),transparent_70%)] pointer-events-none z-0"></div>
    <div class="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-white/10 to-transparent"></div>

    <div class="max-w-screen-xl mx-auto px-6 relative z-10">

      <!-- Header Section -->
      <div class="text-center max-w-3xl mx-auto mb-20">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-rose-500/10 border border-rose-500/20 text-rose-400 rounded-full mb-6 text-sm font-semibold tracking-wide">
          <Flame :size="16" class="fill-current/20" />
          The Chaos
        </div>

        <h2 class="text-4xl md:text-5xl font-extrabold text-slate-50 tracking-tight mb-8 leading-tight">
          Life admin sneaks up on everyone. <br class="hidden md:block" />
          <span class="text-slate-500">Don't let it cost you.</span>
        </h2>

        <p class="text-xl text-slate-400 leading-relaxed max-w-2xl mx-auto">
          Expired passports before a flight. Auto-renewals you forgot to cancel. Scrambling to find your insurance policy. 
          <span class="text-slate-200 font-medium">It’s exhausting, expensive, and completely avoidable.</span>
        </p>
      </div>

      <!-- Problem Showcase Layout -->
      <div class="relative">
        
        <!-- Center Connecting Line (Desktop Only) -->
        <div class="hidden lg:block absolute left-1/2 top-0 bottom-0 w-px bg-gradient-to-b from-rose-500/0 via-rose-500/20 to-rose-500/0 -translate-x-1/2"></div>
        
        <div class="grid lg:grid-cols-2 gap-8 lg:gap-24">
          
          <!-- Column 1: The Costs (Problems) -->
          <div class="space-y-6">
            
            <div class="group flex items-start gap-5 p-6 rounded-2xl bg-slate-900/40 border border-rose-500/10 hover:border-rose-500/30 transition-colors">
              <div class="w-12 h-12 shrink-0 bg-rose-500/10 border border-rose-500/20 rounded-xl flex items-center justify-center text-rose-400 shadow-[0_0_15px_rgba(225,29,72,0.15)]">
                <AlertCircle :size="24" />
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-200 mb-2 group-hover:text-rose-300 transition-colors">Missing Critical Deadlines</h4>
                <p class="text-slate-400 leading-relaxed text-sm">Realizing your ID, passport, or visa expired the day before you need it. The stress of emergency renewals.</p>
              </div>
            </div>

            <div class="group flex items-start gap-5 p-6 rounded-2xl bg-slate-900/40 border border-orange-500/10 hover:border-orange-500/30 transition-colors">
              <div class="w-12 h-12 shrink-0 bg-orange-500/10 border border-orange-500/20 rounded-xl flex items-center justify-center text-orange-400 shadow-[0_0_15px_rgba(249,115,22,0.15)]">
                <DollarSign :size="24" />
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-200 mb-2 group-hover:text-orange-300 transition-colors">Paying the "Disorganization Tax"</h4>
                <p class="text-slate-400 leading-relaxed text-sm">Late fees for car registrations, paying for subscriptions you don't use, and expedited shipping fees.</p>
              </div>
            </div>

            <div class="group flex items-start gap-5 p-6 rounded-2xl bg-slate-900/40 border border-amber-500/10 hover:border-amber-500/30 transition-colors">
              <div class="w-12 h-12 shrink-0 bg-amber-500/10 border border-amber-500/20 rounded-xl flex items-center justify-center text-amber-400 shadow-[0_0_15px_rgba(245,158,11,0.15)]">
                <SearchX :size="24" />
              </div>
              <div>
                <h4 class="text-lg font-bold text-slate-200 mb-2 group-hover:text-amber-300 transition-colors">Scrambling for Documents</h4>
                <p class="text-slate-400 leading-relaxed text-sm">Digging through messy filing cabinets or thousands of emails just to find a simple medical record or warranty.</p>
              </div>
            </div>

          </div>

          <!-- Column 2: The Antidote (Visual break / Callout) -->
          <div class="flex flex-col justify-center">
            
            <div class="relative p-10 lg:p-12 rounded-[2rem] bg-gradient-to-br from-teal-500/10 to-cyan-500/5 border border-teal-500/20 overflow-hidden group">
              
              <!-- Subtle glow behind the shield -->
              <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-48 h-48 bg-teal-500/20 rounded-full blur-[60px] pointer-events-none"></div>

              <div class="relative z-10 text-center">
                <div class="w-20 h-20 mx-auto bg-slate-950 border border-teal-500/30 rounded-2xl flex items-center justify-center mb-8 shadow-[0_0_30px_rgba(45,212,191,0.2)] group-hover:scale-110 transition-transform duration-500">
                  <ShieldCheck :size="40" class="text-teal-400 drop-shadow-[0_0_8px_rgba(45,212,191,0.5)]" />
                </div>
                
                <h3 class="text-2xl md:text-3xl font-bold text-white mb-4 tracking-tight">
                  Bring calm to the chaos.
                </h3>
                
                <p class="text-slate-300 leading-relaxed mb-8">
                  Stop reacting to deadlines. Let LifeAdmin handle the mental load so you can focus on simply living.
                </p>

                <!-- Small inline CTA -->
                <RouterLink to="/register" class="inline-flex items-center gap-2 text-teal-400 font-semibold hover:text-teal-300 transition-colors">
                  Take back control
                  <TrendingUp :size="18" class="group-hover:translate-x-1 transition-transform" />
                </RouterLink>
              </div>

            </div>

          </div>

        </div>
      </div>

    </div>
  </section>
</template>