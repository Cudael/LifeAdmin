<script setup>
import { Shield, Lock, Cloud, CheckCircle2 } from "lucide-vue-next"
</script>

<template>
  <section class="py-28 bg-white relative overflow-hidden">
    
    <!-- Decorative shapes -->
    <div class="absolute top-10 left-10 w-64 h-64 bg-teal-100 rounded-full opacity-20 blur-3xl"></div>
    <div class="absolute bottom-10 right-10 w-80 h-80 bg-cyan-100 rounded-full opacity-20 blur-3xl"></div>

    <div class="max-w-screen-xl mx-auto px-6 relative z-10">

      <div class="text-center mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
          <Shield :size="16" />
          Security First
        </div>

        <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
          Security & Trust
        </h2>
        <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-6"></div>
        <p class="text-lg text-gray-600 max-w-2xl mx-auto">
          Your privacy and security are our top priorities. We use industry-leading practices to keep your data safe.
        </p>
      </div>

      <div class="grid md:grid-cols-3 gap-12">

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Lock :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Bank‑Level Encryption</h3>
          <p class="text-gray-600 leading-relaxed">Your documents and data are encrypted at rest and in transit using AES-256 encryption.</p>
        </div>

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Shield :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Privacy First</h3>
          <p class="text-gray-600 leading-relaxed">We never sell your data. Your information stays yours, always.</p>
        </div>

        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
            <Cloud :size="32" class="text-teal-600" />
          </div>
          <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Secure Cloud Storage</h3>
          <p class="text-gray-600 leading-relaxed">Your files are stored safely with industry‑leading infrastructure and automatic backups.</p>
        </div>

      </div>

      <!-- Trust badges -->
      <div class="mt-16 flex flex-wrap justify-center items-center gap-8 text-gray-400 text-sm">
        <div class="flex items-center gap-2">
          <CheckCircle2 :size="20" class="text-teal-500" />
          <span>GDPR Compliant</span>
        </div>
        <div class="flex items-center gap-2">
          <CheckCircle2 :size="20" class="text-teal-500" />
          <span>ISO 27001 Certified</span>
        </div>
        <div class="flex items-center gap-2">
          <CheckCircle2 :size="20" class="text-teal-500" />
          <span>SOC 2 Type II</span>
        </div>
      </div>

    </div>
  </section>
</template>
