<script setup>
import { Users, Briefcase, Home, Award } from "lucide-vue-next"
</script>

<template>
  <section class="py-16 bg-gradient-to-b from-white to-[#f7fdfc] relative overflow-hidden">
    
    <!-- Decorative shapes -->
    <div class="absolute top-20 right-10 w-72 h-72 bg-teal-100 rounded-full opacity-20 blur-3xl"></div>
    <div class="absolute bottom-20 left-10 w-96 h-96 bg-cyan-100 rounded-full opacity-20 blur-3xl"></div>

    <div class="max-w-screen-xl mx-auto px-6 text-center relative z-10">

      <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
        <Users :size="16" />
        For Everyone
      </div>

      <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
        Who It's For
      </h2>
      <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-12"></div>

      <div class="grid md:grid-cols-3 gap-12">

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Briefcase :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 text-teal-600">Busy Professionals</h3>
          <p class="text-gray-600 leading-relaxed">Keep track of IDs, insurance, certifications, and work documents without the stress.</p>
        </div>

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Home :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 text-teal-600">Families</h3>
          <p class="text-gray-600 leading-relaxed">Manage passports, warranties, medical documents, and school deadlines all in one place.</p>
        </div>

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Award :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 text-teal-600">Small Business Owners</h3>
          <p class="text-gray-600 leading-relaxed">Track licenses, contracts, receipts, and compliance documents effortlessly.</p>
        </div>

      </div>

    </div>
  </section>
</template>
