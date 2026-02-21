<script setup>
import { ArrowRight, CheckCircle2, Sparkles } from "lucide-vue-next"
</script>

<template>
  <section class="py-24 md:py-32 relative z-10">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 relative z-10">
      
      <!-- Premium Glass/Gradient Card -->
      <div class="relative p-12 md:p-20 lg:p-24 bg-slate-900/80 backdrop-blur-3xl rounded-[3rem] ring-1 ring-white/10 shadow-[0_40px_100px_rgba(0,0,0,0.8)] overflow-hidden text-center group">
        
        <!-- Deep internal glow effects -->
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-[radial-gradient(ellipse_at_top,rgba(45,212,191,0.2),transparent_70%)] pointer-events-none"></div>
        <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-[800px] h-[400px] bg-[radial-gradient(ellipse_at_bottom,rgba(6,182,212,0.15),transparent_70%)] pointer-events-none"></div>

        <div class="relative z-10 flex flex-col items-center">
          
          <div class="inline-flex items-center justify-center w-16 h-16 bg-slate-950 ring-1 ring-teal-500/30 rounded-2xl mb-8 shadow-2xl shadow-teal-500/20 text-teal-400">
            <Sparkles :size="32" class="drop-shadow-[0_0_8px_rgba(45,212,191,0.8)]" />
          </div>

          <h2 class="text-5xl md:text-6xl lg:text-[4.5rem] font-extrabold text-white tracking-tighter mb-8 leading-[1.05] text-balance">
            Stop remembering. <br />
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal-300 via-cyan-300 to-emerald-300">Start living.</span>
          </h2>

          <p class="text-xl md:text-2xl text-slate-400 max-w-2xl mx-auto mb-12 leading-relaxed text-balance">
            Join thousands of users who never miss a deadline. 
            Offload your mental clutter today — it's completely free to get started.
          </p>

          <div class="flex flex-col sm:flex-row gap-5 justify-center items-center w-full sm:w-auto">
            <RouterLink
              to="/register"
              class="group relative px-10 py-5 bg-white text-slate-950 rounded-full text-xl font-bold shadow-[0_0_40px_rgba(255,255,255,0.2)] hover:shadow-[0_0_60px_rgba(255,255,255,0.3)] hover:scale-[1.02] transition-all duration-300 flex items-center justify-center gap-3 w-full sm:w-auto ring-1 ring-white/50"
            >
              Get Started Free
              <ArrowRight :size="22" class="group-hover:translate-x-1.5 transition-transform" />
            </RouterLink>

            <RouterLink
              to="/login"
              class="px-10 py-5 bg-slate-800/50 backdrop-blur-xl ring-1 ring-white/10 text-white rounded-full text-xl font-bold hover:bg-slate-700 transition-all duration-300 w-full sm:w-auto flex justify-center shadow-xl"
            >
              Sign In
            </RouterLink>
          </div>

          <!-- Micro-copy -->
          <div class="mt-14 pt-8 border-t border-white/5 flex flex-wrap justify-center gap-x-8 gap-y-4 text-slate-400 text-sm font-bold">
            <div class="flex items-center gap-2"><CheckCircle2 :size="18" class="text-teal-400" /><span>No credit card required</span></div>
            <div class="hidden md:block w-1.5 h-1.5 rounded-full bg-slate-700"></div>
            <div class="flex items-center gap-2"><CheckCircle2 :size="18" class="text-teal-400" /><span>Cancel anytime</span></div>
            <div class="hidden md:block w-1.5 h-1.5 rounded-full bg-slate-700"></div>
            <div class="flex items-center gap-2"><CheckCircle2 :size="18" class="text-teal-400" /><span>Free forever plan</span></div>
          </div>
          
        </div>
      </div>
    </div>
  </section>
</template>