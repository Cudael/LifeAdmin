<script setup>
import { FileText, Zap, Bell } from "lucide-vue-next"
</script>

<template>
  <section class="py-28 bg-white relative overflow-hidden">
    
    <!-- Decorative background -->
    <div class="absolute inset-0 bg-gradient-to-b from-teal-50/30 to-transparent"></div>

    <div class="max-w-screen-xl mx-auto px-6 text-center relative z-10">

      <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
        <Zap :size="16" />
        Simple Process
      </div>

      <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
        How It Works
      </h2>
      <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-6"></div>
      <p class="text-lg text-gray-600 max-w-2xl mx-auto mb-16">
        A simple, powerful workflow that keeps your life organized without effort.
      </p>

      <div class="grid md:grid-cols-3 gap-12">

        <div class="group relative p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          
          <!-- Step number badge -->
          <div class="absolute -top-4 -right-4 w-12 h-12 bg-gradient-to-br from-teal-400 to-cyan-400 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg">
            1
          </div>

          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <FileText :size="32" class="text-teal-600" />
          </div>
          
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Add Your Items</h3>
          <p class="text-gray-600 leading-relaxed">Upload documents, add subscriptions, or enter expiry dates manually in seconds.</p>
        </div>

        <div class="group relative p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2 md:mt-8">
          
          <!-- Step number badge -->
          <div class="absolute -top-4 -right-4 w-12 h-12 bg-gradient-to-br from-teal-400 to-cyan-400 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg">
            2
          </div>

          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Zap :size="32" class="text-teal-600" />
          </div>
          
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">We Track Everything</h3>
          <p class="text-gray-600 leading-relaxed">Our system monitors renewals, deadlines, and important dates 24/7.</p>
        </div>

        <div class="group relative p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          
          <!-- Step number badge -->
          <div class="absolute -top-4 -right-4 w-12 h-12 bg-gradient-to-br from-teal-400 to-cyan-400 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg">
            3
          </div>

          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Bell :size="32" class="text-teal-600" />
          </div>
          
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Get Smart Reminders</h3>
          <p class="text-gray-600 leading-relaxed">Receive notifications weeks before something expires — never miss a thing.</p>
        </div>

      </div>

    </div>
  </section>
</template>
