<script setup>
import { Shield, CheckCircle2 } from "lucide-vue-next"
</script>

<template>
  <section class="py-16 bg-white relative overflow-hidden">
    
    <!-- Decorative shapes -->
    <div class="absolute top-10 left-10 w-64 h-64 bg-teal-100 rounded-full opacity-20 blur-3xl"></div>
    <div class="absolute bottom-10 right-10 w-80 h-80 bg-cyan-100 rounded-full opacity-20 blur-3xl"></div>

    <div class="max-w-screen-xl mx-auto px-6 relative z-10">

      <div class="text-center mb-12">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
          <Shield :size="16" />
          Security First
        </div>

        <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
          Security & Trust
        </h2>
        <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto"></div>
      </div>

      <div class="max-w-3xl mx-auto space-y-4">
        <div class="flex items-start gap-3 p-4 bg-white rounded-xl border border-teal-200 hover:border-teal-400 transition-colors">
          <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
          <p class="text-gray-700 leading-relaxed">Your data is encrypted in transit (HTTPS)</p>
        </div>
        
        <div class="flex items-start gap-3 p-4 bg-white rounded-xl border border-teal-200 hover:border-teal-400 transition-colors">
          <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
          <p class="text-gray-700 leading-relaxed">Only you can access your documents</p>
        </div>
        
        <div class="flex items-start gap-3 p-4 bg-white rounded-xl border border-teal-200 hover:border-teal-400 transition-colors">
          <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
          <p class="text-gray-700 leading-relaxed">We never sell or share your information</p>
        </div>
        
        <div class="flex items-start gap-3 p-4 bg-white rounded-xl border border-teal-200 hover:border-teal-400 transition-colors">
          <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
          <p class="text-gray-700 leading-relaxed">You control your data at all times</p>
        </div>
        
        <div class="flex items-start gap-3 p-4 bg-white rounded-xl border border-teal-200 hover:border-teal-400 transition-colors">
          <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
          <p class="text-gray-700 leading-relaxed">Built with modern security best practices</p>
        </div>
      </div>

    </div>
  </section>
</template>
