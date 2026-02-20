<script setup>
import { ArrowRight, CheckCircle2, Sparkles } from "lucide-vue-next"
</script>

<template>
  <section class="py-24 md:py-32 relative overflow-hidden z-10">
    
    <!-- Ambient glowing backgrounds for depth -->
    <div class="absolute inset-0 bg-slate-950"></div>
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-teal-600/10 rounded-full blur-[150px] pointer-events-none z-0"></div>

    <div class="max-w-screen-xl mx-auto px-4 sm:px-6 relative z-10">
      
      <!-- The Main CTA Container (Massive Glass/Gradient Card) -->
      <div class="relative p-12 md:p-20 lg:p-24 bg-gradient-to-br from-teal-500/10 via-slate-900/80 to-cyan-500/10 backdrop-blur-xl rounded-[3rem] border border-white/10 shadow-[0_0_50px_rgba(45,212,191,0.1)] overflow-hidden text-center group">
        
        <!-- Stunning Abstract Lighting Effects inside the card -->
        <div class="absolute -top-40 -right-40 w-96 h-96 bg-teal-500/30 rounded-full blur-[100px] mix-blend-screen group-hover:bg-teal-500/40 transition-colors duration-700 pointer-events-none"></div>
        <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-cyan-500/20 rounded-full blur-[100px] mix-blend-screen group-hover:bg-cyan-500/30 transition-colors duration-700 pointer-events-none"></div>
        
        <!-- Faint grid pattern over the gradient -->
        <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px] [mask-image:radial-gradient(ellipse_80%_80%_at_50%_50%,#000_20%,transparent_100%)] pointer-events-none"></div>

        <div class="relative z-10">
          
          <div class="inline-flex items-center justify-center w-16 h-16 bg-teal-500/20 border border-teal-500/30 rounded-2xl mb-8 shadow-inner text-teal-400 drop-shadow-[0_0_15px_rgba(45,212,191,0.5)]">
            <Sparkles :size="32" />
          </div>

          <h2 class="text-5xl md:text-6xl lg:text-7xl font-extrabold text-white tracking-tight mb-8 leading-[1.1]">
            Stop remembering. <br class="hidden sm:block" />
            <span class="bg-gradient-to-r from-teal-400 to-cyan-400 bg-clip-text text-transparent drop-shadow-sm">Start living.</span>
          </h2>

          <p class="text-xl md:text-2xl text-slate-300 max-w-3xl mx-auto mb-12 leading-relaxed">
            Join thousands of users who never miss a deadline. 
            Offload your mental clutter today — it's completely free to get started.
          </p>

          <div class="flex flex-col sm:flex-row gap-5 justify-center items-center">
            
            <!-- Primary Pulse Button -->
            <div class="relative group/btn w-full sm:w-auto">
              <div class="absolute -inset-1 bg-gradient-to-r from-teal-500 to-cyan-500 rounded-full blur opacity-75 group-hover/btn:opacity-100 transition duration-300 group-hover/btn:duration-200"></div>
              <RouterLink
                to="/register"
                class="relative px-10 py-5 bg-slate-950 text-white rounded-full text-xl font-bold border border-white/10 hover:bg-slate-900 transition-all duration-300 flex items-center justify-center gap-3 w-full"
              >
                Get Started Free
                <ArrowRight :size="22" class="group-hover/btn:translate-x-1.5 transition-transform text-teal-400" />
              </RouterLink>
            </div>

            <!-- Secondary Outline Button -->
            <RouterLink
              to="/login"
              class="px-10 py-5 bg-white/5 backdrop-blur-md border border-white/10 text-white rounded-full text-xl font-semibold hover:bg-white/10 transition-all duration-300 w-full sm:w-auto flex justify-center"
            >
              Sign In
            </RouterLink>
          </div>

          <!-- Micro-copy assurances -->
          <div class="mt-14 pt-8 border-t border-white/10 flex flex-wrap justify-center gap-x-8 gap-y-4 text-slate-400 text-sm font-medium">
            <div class="flex items-center gap-2">
              <CheckCircle2 :size="16" class="text-teal-500/70" />
              <span>No credit card required</span>
            </div>
            <div class="hidden md:block w-1.5 h-1.5 rounded-full bg-slate-700"></div>
            <div class="flex items-center gap-2">
              <CheckCircle2 :size="16" class="text-teal-500/70" />
              <span>Cancel anytime</span>
            </div>
            <div class="hidden md:block w-1.5 h-1.5 rounded-full bg-slate-700"></div>
            <div class="flex items-center gap-2">
              <CheckCircle2 :size="16" class="text-teal-500/70" />
              <span>Free forever plan</span>
            </div>
          </div>
          
        </div>
      </div>

    </div>
  </section>
</template>