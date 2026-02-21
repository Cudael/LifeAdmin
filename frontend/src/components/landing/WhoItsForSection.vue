<script setup>
import { Users, Briefcase, Home, Building2, Globe } from "lucide-vue-next"
</script>

<template>
  <section class="py-24 relative z-10">
    <div class="max-w-6xl mx-auto px-6 relative z-10">

      <div class="text-center max-w-2xl mx-auto mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-slate-900 ring-1 ring-white/10 text-slate-300 rounded-full mb-6 text-sm font-bold tracking-wide shadow-lg">
          <Users :size="16" class="text-indigo-400" />
          Tailored For You
        </div>

        <h2 class="text-4xl md:text-5xl font-extrabold text-white tracking-tight mb-6 text-balance">
          Built for your <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-cyan-400">peace of mind.</span>
        </h2>
        
        <p class="text-lg text-slate-400 text-balance">
          Whether you're managing a busy household or a growing business, LifeAdmin adapts to what matters most to you.
        </p>
      </div>

      <!-- Enhanced Bento Grid -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

        <!-- Households -->
        <div class="group md:col-span-2 relative overflow-hidden p-10 rounded-[2rem] bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-white/10 transition-all duration-500 flex flex-col justify-end min-h-[320px] shadow-2xl">
          <Home :size="240" stroke-width="1" class="absolute -right-10 -bottom-10 text-white/[0.02] group-hover:text-white/[0.04] group-hover:scale-105 group-hover:-rotate-3 transition-all duration-700 pointer-events-none" />
          <div class="absolute inset-0 bg-gradient-to-br from-teal-500/0 via-transparent to-teal-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center mb-6 text-teal-400 group-hover:bg-teal-500/10 transition-colors shadow-inner">
              <Home :size="28" />
            </div>
            <h3 class="text-3xl font-bold mb-3 text-white">Busy Households</h3>
            <p class="text-slate-400 leading-relaxed max-w-md text-lg text-balance">
              Manage passports, warranties, pet vaccinations, and medical documents for the entire family in one unified hub.
            </p>
          </div>
        </div>

        <!-- Professionals -->
        <div class="group md:col-span-1 relative overflow-hidden p-10 rounded-[2rem] bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-white/10 transition-all duration-500 flex flex-col justify-end min-h-[320px] shadow-2xl">
          <Briefcase :size="200" stroke-width="1" class="absolute -right-8 -bottom-8 text-white/[0.02] group-hover:text-white/[0.04] group-hover:scale-105 group-hover:rotate-3 transition-all duration-700 pointer-events-none" />
          <div class="absolute inset-0 bg-gradient-to-br from-indigo-500/0 via-transparent to-indigo-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center mb-6 text-indigo-400 group-hover:bg-indigo-500/10 transition-colors shadow-inner">
              <Briefcase :size="28" />
            </div>
            <h3 class="text-2xl font-bold mb-3 text-white">Professionals</h3>
            <p class="text-slate-400 leading-relaxed text-balance">
              Never miss a certification renewal, work visa expiry, or important contract deadline again.
            </p>
          </div>
        </div>

        <!-- Expats -->
        <div class="group md:col-span-1 relative overflow-hidden p-10 rounded-[2rem] bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-white/10 transition-all duration-500 flex flex-col justify-end min-h-[320px] shadow-2xl">
          <Globe :size="200" stroke-width="1" class="absolute -right-8 -top-8 text-white/[0.02] group-hover:text-white/[0.04] group-hover:scale-105 group-hover:-rotate-3 transition-all duration-700 pointer-events-none" />
          <div class="absolute inset-0 bg-gradient-to-tr from-cyan-500/0 via-transparent to-cyan-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center mb-6 text-cyan-400 group-hover:bg-cyan-500/10 transition-colors shadow-inner">
              <Globe :size="28" />
            </div>
            <h3 class="text-2xl font-bold mb-3 text-white">Expats & Nomads</h3>
            <p class="text-slate-400 leading-relaxed text-balance">
              Keep visas, passports, and travel insurance sorted across borders without the constant stress.
            </p>
          </div>
        </div>

        <!-- Small Businesses -->
        <div class="group md:col-span-2 relative overflow-hidden p-10 rounded-[2rem] bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-white/10 transition-all duration-500 flex flex-col justify-end min-h-[320px] shadow-2xl">
          <Building2 :size="240" stroke-width="1" class="absolute -right-10 -bottom-6 text-white/[0.02] group-hover:text-white/[0.04] group-hover:scale-105 group-hover:-rotate-2 transition-all duration-700 pointer-events-none" />
          <div class="absolute inset-0 bg-gradient-to-br from-blue-500/0 via-transparent to-blue-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          <div class="relative z-10">
            <div class="w-14 h-14 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center mb-6 text-blue-400 group-hover:bg-blue-500/10 transition-colors shadow-inner">
              <Building2 :size="28" />
            </div>
            <h3 class="text-3xl font-bold mb-3 text-white">Small Businesses</h3>
            <p class="text-slate-400 leading-relaxed max-w-md text-lg text-balance">
              Track business licenses, compliance documents, domain renewals, and employee records effortlessly.
            </p>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>