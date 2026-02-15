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
  <section id="features" class="py-16 bg-gradient-to-b from-white to-[#f7fdfc] relative overflow-hidden">
    
    <!-- Decorative gradient -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(20,184,166,0.05),transparent_50%)]"></div>

    <div class="max-w-screen-xl mx-auto px-6 relative z-10">

      <div class="text-center mb-12">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
          <Sparkles :size="16" />
          Powerful Features
        </div>

        <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4 pb-1">
          Everything You Need
        </h2>
        <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto"></div>
      </div>

      <div class="grid md:grid-cols-3 gap-12">

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Calendar :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Expiration Tracking</h3>
          <p class="text-gray-600 leading-relaxed">Never miss a renewal again — passports, IDs, insurance, subscriptions, and more.</p>
        </div>

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Bell :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Smart Reminders</h3>
          <p class="text-gray-600 leading-relaxed">Get notified weeks before something expires. Customize reminder timing to your needs.</p>
        </div>

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <FileText :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Document Storage</h3>
          <p class="text-gray-600 leading-relaxed">Upload PDFs, receipts, warranties, and keep them safe and organized in one place.</p>
        </div>

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <TrendingUp :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Advanced Analytics</h3>
          <p class="text-gray-600 leading-relaxed">See patterns, track spending on subscriptions, and get insights into your renewals.</p>
        </div>

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Users :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Family Sharing</h3>
          <p class="text-gray-600 leading-relaxed">Share documents and reminders with family members. Perfect for household management.</p>
        </div>

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Zap :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Quick Actions</h3>
          <p class="text-gray-600 leading-relaxed">Bulk operations, smart filters, and shortcuts to manage hundreds of items effortlessly.</p>
        </div>

      </div>

    </div>
  </section>
</template>
