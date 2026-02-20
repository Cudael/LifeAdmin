<script setup>
import { Users, Briefcase, Home, Building2, Globe, Sparkles } from "lucide-vue-next"
</script>

<template>
  <section class="py-24 relative overflow-hidden z-10">
    
    <!-- Deep background radial glows for depth -->
    <div class="absolute top-1/2 left-0 w-96 h-96 bg-indigo-600/10 rounded-full blur-[120px] -translate-y-1/2 pointer-events-none"></div>
    <div class="absolute top-1/2 right-0 w-96 h-96 bg-teal-600/10 rounded-full blur-[120px] -translate-y-1/2 pointer-events-none"></div>

    <div class="max-w-5xl mx-auto px-6 relative z-10">

      <!-- Header Area -->
      <div class="text-center max-w-2xl mx-auto mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 rounded-full mb-6 text-sm font-semibold tracking-wide">
          <Users :size="16" class="fill-current/20" />
          Tailored For You
        </div>

        <h2 class="text-4xl md:text-5xl font-extrabold text-slate-50 tracking-tight mb-6">
          Built for your <span class="bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent">peace of mind.</span>
        </h2>
        
        <p class="text-lg text-slate-400">
          Whether you're managing a household or a business, LifeAdmin adapts to what matters most to you.
        </p>
      </div>

      <!-- Bento Box Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

        <!-- Bento Card 1: Families (Spans 2 columns) -->
        <div class="group md:col-span-2 relative overflow-hidden p-8 sm:p-10 rounded-[2rem] bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-white/10 transition-all duration-500 flex flex-col justify-end min-h-[300px]">
          <!-- Decorative Watermark Icon -->
          <Home :size="200" class="absolute -right-10 -bottom-10 text-white/[0.03] group-hover:text-white/[0.05] group-hover:scale-110 group-hover:-rotate-6 transition-all duration-700 pointer-events-none" />
          <!-- Glow Reveal on Hover -->
          <div class="absolute inset-0 bg-gradient-to-br from-teal-500/0 via-transparent to-teal-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 bg-teal-500/10 border border-teal-500/20 rounded-2xl flex items-center justify-center mb-6 text-teal-400 shadow-[0_0_15px_rgba(45,212,191,0.15)]">
              <Home :size="28" />
            </div>
            <h3 class="text-3xl font-bold mb-3 text-slate-100">Busy Households</h3>
            <p class="text-slate-400 leading-relaxed max-w-md text-lg">
              Manage passports, warranties, pet vaccinations, and medical documents for the entire family in one unified hub.
            </p>
          </div>
        </div>

        <!-- Bento Card 2: Professionals (Spans 1 column) -->
        <div class="group md:col-span-1 relative overflow-hidden p-8 sm:p-10 rounded-[2rem] bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-white/10 transition-all duration-500 flex flex-col justify-end min-h-[300px]">
          <Briefcase :size="180" class="absolute -right-8 -bottom-8 text-white/[0.03] group-hover:text-white/[0.05] group-hover:scale-110 group-hover:rotate-6 transition-all duration-700 pointer-events-none" />
          <div class="absolute inset-0 bg-gradient-to-br from-indigo-500/0 via-transparent to-indigo-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 bg-indigo-500/10 border border-indigo-500/20 rounded-2xl flex items-center justify-center mb-6 text-indigo-400 shadow-[0_0_15px_rgba(99,102,241,0.15)]">
              <Briefcase :size="28" />
            </div>
            <h3 class="text-2xl font-bold mb-3 text-slate-100">Professionals</h3>
            <p class="text-slate-400 leading-relaxed">
              Never miss a certification renewal, work visa expiry, or important contract deadline again.
            </p>
          </div>
        </div>

        <!-- Bento Card 3: Travelers & Expats (Spans 1 column) -->
        <div class="group md:col-span-1 relative overflow-hidden p-8 sm:p-10 rounded-[2rem] bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-white/10 transition-all duration-500 flex flex-col justify-end min-h-[300px]">
          <Globe :size="180" class="absolute -right-8 -top-8 text-white/[0.03] group-hover:text-white/[0.05] group-hover:scale-110 group-hover:-rotate-6 transition-all duration-700 pointer-events-none" />
          <div class="absolute inset-0 bg-gradient-to-tr from-cyan-500/0 via-transparent to-cyan-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 bg-cyan-500/10 border border-cyan-500/20 rounded-2xl flex items-center justify-center mb-6 text-cyan-400 shadow-[0_0_15px_rgba(34,211,238,0.15)]">
              <Globe :size="28" />
            </div>
            <h3 class="text-2xl font-bold mb-3 text-slate-100">Expats & Nomads</h3>
            <p class="text-slate-400 leading-relaxed">
              Keep visas, passports, and travel insurance sorted across borders without the stress.
            </p>
          </div>
        </div>

        <!-- Bento Card 4: Small Business (Spans 2 columns) -->
        <div class="group md:col-span-2 relative overflow-hidden p-8 sm:p-10 rounded-[2rem] bg-slate-900/40 backdrop-blur-md border border-white/5 hover:border-white/10 transition-all duration-500 flex flex-col justify-end min-h-[300px]">
          <Building2 :size="200" class="absolute -right-10 -bottom-6 text-white/[0.03] group-hover:text-white/[0.05] group-hover:scale-110 group-hover:-rotate-3 transition-all duration-700 pointer-events-none" />
          <div class="absolute inset-0 bg-gradient-to-br from-blue-500/0 via-transparent to-blue-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 bg-blue-500/10 border border-blue-500/20 rounded-2xl flex items-center justify-center mb-6 text-blue-400 shadow-[0_0_15px_rgba(59,130,246,0.15)]">
              <Building2 :size="28" />
            </div>
            <h3 class="text-3xl font-bold mb-3 text-slate-100">Small Businesses</h3>
            <p class="text-slate-400 leading-relaxed max-w-md text-lg">
              Track business licenses, compliance documents, domain renewals, and employee records effortlessly.
            </p>
          </div>
        </div>

      </div>

    </div>
  </section>
</template>