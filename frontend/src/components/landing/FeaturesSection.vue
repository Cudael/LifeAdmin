<script setup>
import { 
  Calendar,
  Bell,
  FileText,
  TrendingUp,
  Users,
  Zap,
  Sparkles
} from "lucide-vue-next"
</script>

<template>
  <section id="features" class="py-24 md:py-32 relative overflow-hidden z-10">
    
    <!-- Ambient Background Depth -->
    <div class="absolute top-0 right-1/4 w-[500px] h-[500px] bg-teal-600/10 rounded-full blur-[150px] pointer-events-none"></div>
    <div class="absolute bottom-0 left-1/4 w-[500px] h-[500px] bg-cyan-600/10 rounded-full blur-[150px] pointer-events-none"></div>

    <div class="max-w-screen-xl mx-auto px-6 relative z-10">

      <!-- Section Header -->
      <div class="text-center max-w-2xl mx-auto mb-20">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-500/10 border border-teal-500/20 text-teal-400 rounded-full mb-6 text-sm font-semibold tracking-wide">
          <Sparkles :size="16" class="fill-current/20" />
          Powerful Arsenal
        </div>

        <h2 class="text-4xl md:text-5xl font-extrabold text-slate-50 tracking-tight mb-6">
          Everything you need, <br class="hidden sm:block" />
          <span class="text-slate-500">nothing you don't.</span>
        </h2>
        
        <p class="text-lg text-slate-400 leading-relaxed">
          A carefully curated set of tools designed to keep your life organized without adding unnecessary complexity.
        </p>
      </div>

      <!-- Features 3x2 Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 lg:gap-8">

        <!-- Feature 1: Expiration Tracking -->
        <div class="group relative p-8 rounded-3xl bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-teal-500/30 transition-all duration-500 hover:-translate-y-1 overflow-hidden">
          <!-- Hidden hover gradient reveal -->
          <div class="absolute inset-0 bg-gradient-to-br from-teal-500/0 via-transparent to-teal-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-teal-500/10 border border-teal-500/20 rounded-2xl flex items-center justify-center text-teal-400 group-hover:scale-110 group-hover:bg-teal-500/20 transition-all duration-500 shadow-inner">
              <Calendar :size="28" class="drop-shadow-[0_0_8px_rgba(45,212,191,0.5)]" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-slate-100 group-hover:text-teal-300 transition-colors">Expiration Tracking</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base">
              Never miss a renewal again — passports, IDs, insurance, subscriptions, and more.
            </p>
          </div>
        </div>

        <!-- Feature 2: Smart Reminders -->
        <div class="group relative p-8 rounded-3xl bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-cyan-500/30 transition-all duration-500 hover:-translate-y-1 overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-br from-cyan-500/0 via-transparent to-cyan-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-cyan-500/10 border border-cyan-500/20 rounded-2xl flex items-center justify-center text-cyan-400 group-hover:scale-110 group-hover:bg-cyan-500/20 transition-all duration-500 shadow-inner">
              <Bell :size="28" class="drop-shadow-[0_0_8px_rgba(34,211,238,0.5)]" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-slate-100 group-hover:text-cyan-300 transition-colors">Smart Reminders</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base">
              Get notified weeks before something expires. Customize reminder timing to your needs.
            </p>
          </div>
        </div>

        <!-- Feature 3: Document Storage -->
        <div class="group relative p-8 rounded-3xl bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-teal-500/30 transition-all duration-500 hover:-translate-y-1 overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-br from-teal-500/0 via-transparent to-teal-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-teal-500/10 border border-teal-500/20 rounded-2xl flex items-center justify-center text-teal-400 group-hover:scale-110 group-hover:bg-teal-500/20 transition-all duration-500 shadow-inner">
              <FileText :size="28" class="drop-shadow-[0_0_8px_rgba(45,212,191,0.5)]" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-slate-100 group-hover:text-teal-300 transition-colors">Document Vault</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base">
              Upload PDFs, receipts, warranties, and keep them safe and organized in one place.
            </p>
          </div>
        </div>

        <!-- Feature 4: Analytics -->
        <div class="group relative p-8 rounded-3xl bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-cyan-500/30 transition-all duration-500 hover:-translate-y-1 overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-br from-cyan-500/0 via-transparent to-cyan-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-cyan-500/10 border border-cyan-500/20 rounded-2xl flex items-center justify-center text-cyan-400 group-hover:scale-110 group-hover:bg-cyan-500/20 transition-all duration-500 shadow-inner">
              <TrendingUp :size="28" class="drop-shadow-[0_0_8px_rgba(34,211,238,0.5)]" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-slate-100 group-hover:text-cyan-300 transition-colors">Advanced Analytics</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base">
              See patterns, track spending on subscriptions, and get insights into your renewals.
            </p>
          </div>
        </div>

        <!-- Feature 5: Family Sharing -->
        <div class="group relative p-8 rounded-3xl bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-teal-500/30 transition-all duration-500 hover:-translate-y-1 overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-br from-teal-500/0 via-transparent to-teal-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-teal-500/10 border border-teal-500/20 rounded-2xl flex items-center justify-center text-teal-400 group-hover:scale-110 group-hover:bg-teal-500/20 transition-all duration-500 shadow-inner">
              <Users :size="28" class="drop-shadow-[0_0_8px_rgba(45,212,191,0.5)]" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-slate-100 group-hover:text-teal-300 transition-colors">Family Sharing</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base">
              Share documents and reminders with family members. Perfect for household management.
            </p>
          </div>
        </div>

        <!-- Feature 6: Quick Actions -->
        <div class="group relative p-8 rounded-3xl bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-cyan-500/30 transition-all duration-500 hover:-translate-y-1 overflow-hidden">
          <div class="absolute inset-0 bg-gradient-to-br from-cyan-500/0 via-transparent to-cyan-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-cyan-500/10 border border-cyan-500/20 rounded-2xl flex items-center justify-center text-cyan-400 group-hover:scale-110 group-hover:bg-cyan-500/20 transition-all duration-500 shadow-inner">
              <Zap :size="28" class="drop-shadow-[0_0_8px_rgba(34,211,238,0.5)]" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-slate-100 group-hover:text-cyan-300 transition-colors">Quick Actions</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base">
              Bulk operations, smart filters, and shortcuts to manage hundreds of items effortlessly.
            </p>
          </div>
        </div>

      </div>

    </div>
  </section>
</template>