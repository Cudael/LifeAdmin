<script setup>
import { 
  FileUp, 
  Lock, 
  Bell, 
  Sparkles,
  ArrowRight
} from "lucide-vue-next"
</script>

<template>
  <section class="py-24 md:py-32 relative overflow-hidden z-10 bg-slate-950">
    
    <!-- Seamless blend from the Hero section above -->
    <div class="absolute top-0 left-0 w-full h-32 bg-gradient-to-b from-slate-950 via-slate-950 to-transparent z-10"></div>

    <div class="max-w-screen-xl mx-auto px-6 relative z-20">

      <!-- Header Area -->
      <div class="text-center max-w-2xl mx-auto mb-20">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-slate-900 border border-white/5 text-slate-300 rounded-full mb-6 text-sm font-semibold tracking-wide shadow-sm">
          <Sparkles :size="14" class="text-teal-400" />
          Autopilot for your documents
        </div>

        <h2 class="text-4xl md:text-5xl font-extrabold text-slate-50 tracking-tight mb-6">
          Set it. Forget it. <br class="hidden sm:block" />
          <span class="text-slate-500">We'll handle the rest.</span>
        </h2>
        
        <p class="text-lg text-slate-400">
          A seamless pipeline that takes your chaotic paperwork and turns it into timely, actionable intelligence.
        </p>
      </div>

      <!-- The Pipeline Flow -->
      <div class="relative max-w-5xl mx-auto">

        <!-- Animated Laser Line (Desktop) -->
        <div class="hidden md:block absolute top-[140px] left-[10%] right-[10%] h-px bg-white/5 z-0">
          <div class="absolute top-0 left-0 h-full w-[20%] bg-gradient-to-r from-transparent via-teal-400 to-transparent animate-data-flow opacity-70"></div>
        </div>

        <!-- Vertical Line (Mobile) -->
        <div class="md:hidden absolute top-10 bottom-10 left-8 w-px bg-white/5 z-0">
          <div class="absolute top-0 left-0 w-full h-[20%] bg-gradient-to-b from-transparent via-teal-400 to-transparent animate-data-flow-vertical opacity-70"></div>
        </div>

        <div class="grid md:grid-cols-3 gap-8 md:gap-12 relative z-10">

          <!-- STEP 1: Input -->
          <div class="group flex flex-col items-center md:items-start pl-16 md:pl-0 relative">
            <!-- Mobile Step Node -->
            <div class="md:hidden absolute left-[1.125rem] top-12 w-3 h-3 bg-slate-950 border-2 border-teal-500 rounded-full -translate-x-1/2 z-10 shadow-[0_0_10px_rgba(45,212,191,0.5)]"></div>

            <div class="w-full bg-slate-900/40 backdrop-blur-md rounded-3xl border border-white/5 p-2 mb-8 hover:border-teal-500/30 transition-all duration-500 shadow-lg group-hover:-translate-y-2">
              <!-- CSS-only Mini Illustration -->
              <div class="h-40 rounded-2xl bg-slate-950 border border-dashed border-white/10 flex flex-col items-center justify-center relative overflow-hidden group-hover:border-teal-500/30 transition-colors duration-500">
                <div class="absolute inset-0 bg-gradient-to-b from-teal-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="w-12 h-12 bg-slate-800 rounded-xl flex items-center justify-center mb-3 transform group-hover:-translate-y-2 transition-transform duration-500 border border-white/5 shadow-xl group-hover:shadow-teal-500/20">
                  <FileUp class="text-teal-400" size="24" />
                </div>
                <div class="text-xs text-slate-500 font-medium font-mono tracking-widest uppercase">Drop Zone</div>
              </div>
            </div>
            
            <div class="flex items-center gap-4 mb-4">
              <span class="text-4xl font-extrabold text-white/5 group-hover:text-teal-500/20 transition-colors">01</span>
              <h3 class="text-2xl font-bold text-slate-100">Drop it in.</h3>
            </div>
            <p class="text-slate-400 leading-relaxed text-left md:text-left">
              Upload PDFs, snap a photo, or forward an email. Our AI automatically extracts expiration dates and critical details in seconds.
            </p>
          </div>

          <!-- STEP 2: Process -->
          <div class="group flex flex-col items-center md:items-start pl-16 md:pl-0 relative md:mt-12">
            <div class="md:hidden absolute left-[1.125rem] top-12 w-3 h-3 bg-slate-950 border-2 border-cyan-500 rounded-full -translate-x-1/2 z-10 shadow-[0_0_10px_rgba(34,211,238,0.5)]"></div>

            <div class="w-full bg-slate-900/40 backdrop-blur-md rounded-3xl border border-white/5 p-2 mb-8 hover:border-cyan-500/30 transition-all duration-500 shadow-lg group-hover:-translate-y-2">
              <div class="h-40 rounded-2xl bg-slate-950 border border-white/5 flex items-center justify-center relative overflow-hidden">
                <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(34,211,238,0.05),transparent_60%)]"></div>
                
                <!-- Spinning Radar Effect -->
                <div class="relative w-20 h-20 flex items-center justify-center group-hover:scale-110 transition-transform duration-700">
                  <div class="absolute inset-0 border border-cyan-500/20 rounded-full animate-[spin_4s_linear_infinite]"></div>
                  <div class="absolute inset-2 border border-cyan-500/40 rounded-full border-t-transparent animate-[spin_3s_linear_infinite_reverse]"></div>
                  <div class="absolute inset-4 bg-cyan-500/10 rounded-full blur-sm"></div>
                  <Lock class="text-cyan-400 relative z-10" size="24" />
                </div>
              </div>
            </div>
            
            <div class="flex items-center gap-4 mb-4">
              <span class="text-4xl font-extrabold text-white/5 group-hover:text-cyan-500/20 transition-colors">02</span>
              <h3 class="text-2xl font-bold text-slate-100">The vault secures it.</h3>
            </div>
            <p class="text-slate-400 leading-relaxed text-left md:text-left">
              Your documents are encrypted and actively monitored 24/7. No more digging through messy filing cabinets or crowded inboxes.
            </p>
          </div>

          <!-- STEP 3: Alert -->
          <div class="group flex flex-col items-center md:items-start pl-16 md:pl-0 relative md:mt-24">
            <div class="md:hidden absolute left-[1.125rem] top-12 w-3 h-3 bg-slate-950 border-2 border-blue-500 rounded-full -translate-x-1/2 z-10 shadow-[0_0_10px_rgba(59,130,246,0.5)]"></div>

            <div class="w-full bg-slate-900/40 backdrop-blur-md rounded-3xl border border-white/5 p-2 mb-8 hover:border-blue-500/30 transition-all duration-500 shadow-lg group-hover:-translate-y-2">
              <div class="h-40 rounded-2xl bg-slate-950 border border-white/5 flex items-center justify-center relative overflow-hidden group-hover:bg-slate-900 transition-colors duration-500">
                
                <!-- Background ambient pulse -->
                <div class="absolute right-4 top-4 w-20 h-20 bg-blue-500/10 rounded-full blur-xl group-hover:bg-blue-500/20 transition-colors"></div>

                <!-- Floating Notification Pill -->
                <div class="absolute bottom-6 right-6 bg-slate-800 border border-blue-500/30 rounded-xl p-3.5 shadow-2xl transform translate-y-4 opacity-50 group-hover:-translate-y-2 group-hover:opacity-100 transition-all duration-500 z-10 flex items-center gap-3">
                  <div class="w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center">
                    <Bell class="text-blue-400" size="14" />
                  </div>
                  <div>
                    <div class="h-1.5 w-16 bg-slate-300 rounded mb-1.5"></div>
                    <div class="h-1.5 w-10 bg-slate-600 rounded"></div>
                  </div>
                </div>

                <Bell class="text-blue-400/50 mb-4 transform group-hover:scale-90 group-hover:text-blue-400 transition-all duration-500" size="40" />
              </div>
            </div>
            
            <div class="flex items-center gap-4 mb-4">
              <span class="text-4xl font-extrabold text-white/5 group-hover:text-blue-500/20 transition-colors">03</span>
              <h3 class="text-2xl font-bold text-slate-100">Get pinged.</h3>
            </div>
            <p class="text-slate-400 leading-relaxed text-left md:text-left">
              Receive timely alerts on your phone or email right before you need to act. Never pay a late fee or miss a deadline again.
            </p>
          </div>

        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
@keyframes data-flow {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(500%);
  }
}

@keyframes data-flow-vertical {
  0% {
    transform: translateY(-100%);
  }
  100% {
    transform: translateY(500%);
  }
}

.animate-data-flow {
  animation: data-flow 3s linear infinite;
}

.animate-data-flow-vertical {
  animation: data-flow-vertical 3s linear infinite;
}
</style>