<script setup>
import { TrendingUp, AlertCircle, DollarSign, FolderOpen } from "lucide-vue-next"
</script>

<template>
  <section class="py-16 bg-gradient-to-b from-[#f7fdfc] to-white relative overflow-hidden">
    
    <!-- Decorative gradient -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(20,184,166,0.05),transparent_70%)]"></div>

    <div class="max-w-screen-lg mx-auto px-6 text-center relative z-10">

      <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
        <TrendingUp :size="16" />
        The Problem
      </div>

      <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4 pb-1">
        Why It Matters
      </h2>
      <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-8"></div>

      <p class="text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed mb-12">
        Life admin sneaks up on everyone — expired IDs, forgotten subscriptions, missing documents.
        We built this tool to bring <span class="text-teal-600 font-semibold">calm to the chaos</span> and help you stay on top of the things that matter.
      </p>

      <!-- Problem cards -->
      <div class="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
        <div class="p-6 bg-white rounded-2xl border border-red-200 shadow-sm hover:shadow-md transition-shadow">
          <div class="w-12 h-12 mx-auto mb-3 bg-red-100 rounded-xl flex items-center justify-center">
            <AlertCircle :size="24" class="text-red-600" />
          </div>
          <p class="text-gray-700 font-medium">Missing renewal deadlines</p>
        </div>

        <div class="p-6 bg-white rounded-2xl border border-orange-200 shadow-sm hover:shadow-md transition-shadow">
          <div class="w-12 h-12 mx-auto mb-3 bg-orange-100 rounded-xl flex items-center justify-center">
            <DollarSign :size="24" class="text-orange-600" />
          </div>
          <p class="text-gray-700 font-medium">Paying fines for late renewals</p>
        </div>

        <div class="p-6 bg-white rounded-2xl border border-yellow-200 shadow-sm hover:shadow-md transition-shadow">
          <div class="w-12 h-12 mx-auto mb-3 bg-yellow-100 rounded-xl flex items-center justify-center">
            <FolderOpen :size="24" class="text-yellow-600" />
          </div>
          <p class="text-gray-700 font-medium">Lost or disorganized documents</p>
        </div>
      </div>

    </div>
  </section>
</template>
