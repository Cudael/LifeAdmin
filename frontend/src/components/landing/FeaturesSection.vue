<script setup>
import { Calendar, Bell, FileText, TrendingUp, Users, Zap, Sparkles } from "lucide-vue-next"
</script>

<template>
  <section id="features" class="py-24 md:py-32 relative z-10">
    <div class="max-w-screen-xl mx-auto px-6 relative z-10">

      <div class="text-center max-w-2xl mx-auto mb-20">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-slate-900 ring-1 ring-white/10 text-slate-300 rounded-full mb-6 text-sm font-bold tracking-wide shadow-lg">
          <Sparkles :size="16" class="text-teal-400" />
          Powerful Arsenal
        </div>

        <h2 class="text-4xl md:text-5xl font-extrabold text-white tracking-tight mb-6 text-balance">
          Everything you need, <span class="text-slate-500">nothing you don't.</span>
        </h2>
        
        <p class="text-lg text-slate-400 leading-relaxed text-balance">
          A carefully curated set of tools designed to keep your life organized without adding unnecessary complexity to your day.
        </p>
      </div>

      <!-- Sleek Bento-style Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">

        <div class="group relative p-8 rounded-3xl bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-teal-500/50 transition-all duration-300 overflow-hidden shadow-xl hover:shadow-teal-500/10">
          <div class="absolute inset-0 bg-gradient-to-br from-teal-500/0 via-transparent to-teal-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center text-teal-400 group-hover:bg-teal-500/10 group-hover:ring-teal-500/30 transition-all duration-300 shadow-inner">
              <Calendar :size="26" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-white">Expiration Tracking</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base text-balance">
              Never miss a renewal again — passports, IDs, insurance, subscriptions, and more.
            </p>
          </div>
        </div>

        <div class="group relative p-8 rounded-3xl bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-cyan-500/50 transition-all duration-300 overflow-hidden shadow-xl hover:shadow-cyan-500/10">
          <div class="absolute inset-0 bg-gradient-to-br from-cyan-500/0 via-transparent to-cyan-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center text-cyan-400 group-hover:bg-cyan-500/10 group-hover:ring-cyan-500/30 transition-all duration-300 shadow-inner">
              <Bell :size="26" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-white">Smart Reminders</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base text-balance">
              Get notified weeks before something expires. Customize reminder timing to your exact needs.
            </p>
          </div>
        </div>

        <div class="group relative p-8 rounded-3xl bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-emerald-500/50 transition-all duration-300 overflow-hidden shadow-xl hover:shadow-emerald-500/10">
          <div class="absolute inset-0 bg-gradient-to-br from-emerald-500/0 via-transparent to-emerald-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center text-emerald-400 group-hover:bg-emerald-500/10 group-hover:ring-emerald-500/30 transition-all duration-300 shadow-inner">
              <FileText :size="26" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-white">Document Vault</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base text-balance">
              Upload PDFs, receipts, warranties, and keep them completely safe and organized in one place.
            </p>
          </div>
        </div>

        <div class="group relative p-8 rounded-3xl bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-indigo-500/50 transition-all duration-300 overflow-hidden shadow-xl hover:shadow-indigo-500/10">
          <div class="absolute inset-0 bg-gradient-to-br from-indigo-500/0 via-transparent to-indigo-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center text-indigo-400 group-hover:bg-indigo-500/10 group-hover:ring-indigo-500/30 transition-all duration-300 shadow-inner">
              <TrendingUp :size="26" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-white">Advanced Analytics</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base text-balance">
              See patterns, track spending on auto-renewals, and get deep insights into your subscriptions.
            </p>
          </div>
        </div>

        <div class="group relative p-8 rounded-3xl bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-purple-500/50 transition-all duration-300 overflow-hidden shadow-xl hover:shadow-purple-500/10">
          <div class="absolute inset-0 bg-gradient-to-br from-purple-500/0 via-transparent to-purple-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center text-purple-400 group-hover:bg-purple-500/10 group-hover:ring-purple-500/30 transition-all duration-300 shadow-inner">
              <Users :size="26" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-white">Family Sharing</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base text-balance">
              Share documents and reminders with family members. Perfect for modern household management.
            </p>
          </div>
        </div>

        <div class="group relative p-8 rounded-3xl bg-slate-900/50 backdrop-blur-xl ring-1 ring-white/5 hover:ring-rose-500/50 transition-all duration-300 overflow-hidden shadow-xl hover:shadow-rose-500/10">
          <div class="absolute inset-0 bg-gradient-to-br from-rose-500/0 via-transparent to-rose-500/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div class="relative z-10">
            <div class="w-14 h-14 mb-6 bg-slate-800 ring-1 ring-white/10 rounded-2xl flex items-center justify-center text-rose-400 group-hover:bg-rose-500/10 group-hover:ring-rose-500/30 transition-all duration-300 shadow-inner">
              <Zap :size="26" />
            </div>
            <h3 class="text-xl font-bold mb-3 text-white">Quick Actions</h3>
            <p class="text-slate-400 leading-relaxed text-sm md:text-base text-balance">
              Bulk operations, smart filters, and AI shortcuts to manage hundreds of items effortlessly.
            </p>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>