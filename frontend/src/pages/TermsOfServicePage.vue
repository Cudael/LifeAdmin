<script setup>
import AppHeader from "../components/layout/AppHeader.vue"
import AppFooter from "../components/layout/AppFooter.vue"
import { FileText, AlertTriangle, Shield, Ban, Scale, Mail } from "lucide-vue-next"
</script>

<template>
  <div class="bg-slate-950 min-h-screen flex flex-col text-slate-300 font-sans selection:bg-teal-500/30 selection:text-teal-200">
    <AppHeader />

    <main class="flex-1 pt-24 md:pt-32 relative z-10">
      
      <!-- Abstract Background Elements -->
      <div class="absolute top-0 left-0 w-full h-[500px] bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px] [mask-image:linear-gradient(to_bottom,black_40%,transparent_100%)] pointer-events-none z-0"></div>
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-2xl h-[400px] bg-blue-500/10 blur-[120px] rounded-full pointer-events-none z-0"></div>

      <!-- Header Section -->
      <section class="relative py-16 md:py-24 z-10 border-b border-white/5">
        <div class="max-w-4xl mx-auto px-6">
          <div class="text-left md:text-center flex flex-col md:items-center">
            <div class="inline-flex items-center justify-center w-16 h-16 bg-blue-500/10 border border-blue-500/20 rounded-2xl mb-8 shadow-[0_0_15px_rgba(59,130,246,0.15)]">
              <FileText :size="32" class="text-blue-400 drop-shadow-[0_0_8px_rgba(59,130,246,0.5)]" />
            </div>
            <h1 class="text-4xl md:text-6xl font-extrabold text-white mb-6 tracking-tight">
              Terms of Service
            </h1>
            <p class="text-lg text-slate-400 font-medium">
              Last updated: <span class="text-slate-300">February 13, 2026</span>
            </p>
          </div>
        </div>
      </section>

      <!-- Content Section -->
      <section class="py-16 md:py-24 relative z-10">
        <div class="max-w-3xl mx-auto px-6 prose prose-invert prose-slate prose-a:text-blue-400 hover:prose-a:text-blue-300 prose-headings:text-white prose-p:leading-relaxed">
          
          <!-- Introduction -->
          <div class="mb-16">
            <p class="text-lg text-slate-400">
              Welcome to LifeAdmin. By accessing or using our service, you agree to be bound by these Terms of Service. Please read them carefully. If you do not agree to these terms, please do not use our service.
            </p>
          </div>

          <!-- Acceptance of Terms -->
          <div class="mb-16">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <Scale :size="20" class="text-blue-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">Acceptance of Terms</h2>
            </div>
            <p class="text-slate-400">
              By creating an account or using LifeAdmin, you agree to these Terms of Service and our Privacy Policy. These terms constitute a legally binding agreement between you and LifeAdmin.
            </p>
          </div>

          <!-- User Accounts -->
          <div class="mb-16">
            <h2 class="text-3xl font-bold text-white mb-6">User Accounts</h2>
            <p class="text-slate-400 mb-4">To use LifeAdmin, you must create an account. You agree to:</p>
            <ul class="list-disc pl-5 space-y-2 text-slate-400 marker:text-blue-500">
              <li>Provide accurate, current, and complete information during registration</li>
              <li>Maintain and promptly update your account information</li>
              <li>Keep your password secure and confidential</li>
              <li>Be responsible for all activities that occur under your account</li>
            </ul>
          </div>

          <!-- Acceptable Use -->
          <div class="mb-16">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <Shield :size="20" class="text-emerald-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">Acceptable Use</h2>
            </div>
            <p class="text-slate-400 mb-4">You agree to use LifeAdmin only for lawful purposes. You agree NOT to:</p>
            <ul class="list-disc pl-5 space-y-2 text-slate-400 marker:text-emerald-500">
              <li>Violate any applicable laws or regulations</li>
              <li>Infringe on the intellectual property rights of others</li>
              <li>Upload viruses, malware, or other malicious code</li>
              <li>Attempt to gain unauthorized access to any part of the service</li>
              <li>Use automated systems (bots, scrapers) to access the service without permission</li>
            </ul>
          </div>

          <!-- Prohibited Content -->
          <div class="mb-16 p-8 bg-rose-500/5 border border-rose-500/20 rounded-3xl relative overflow-hidden">
            <!-- Background accent -->
            <div class="absolute top-0 right-0 w-32 h-32 bg-rose-500/10 blur-3xl rounded-full pointer-events-none"></div>
            
            <div class="flex items-center gap-4 mb-6 relative z-10">
              <div class="w-12 h-12 bg-slate-900 border border-rose-500/30 rounded-xl flex items-center justify-center shadow-inner">
                <Ban :size="20" class="text-rose-400" />
              </div>
              <h2 class="text-2xl font-bold text-white m-0">Prohibited Content</h2>
            </div>
            <p class="text-rose-200/80 mb-4 relative z-10">You may not upload content that:</p>
            <ul class="list-disc pl-5 space-y-2 text-rose-200/80 marker:text-rose-500 relative z-10">
              <li>Is illegal, harmful, threatening, abusive, or harassing</li>
              <li>Contains explicit or adult content</li>
              <li>Contains personal information of others without consent</li>
              <li>Promotes violence, discrimination, or hatred</li>
            </ul>
          </div>

          <!-- Disclaimers -->
          <div class="mb-16">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <AlertTriangle :size="20" class="text-amber-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">Disclaimers</h2>
            </div>
            <div class="p-6 bg-amber-500/10 border border-amber-500/20 rounded-2xl mb-6">
              <p class="uppercase font-bold text-amber-400 text-sm tracking-widest m-0">
                The service is provided "as is" and "as available" without warranties of any kind.
              </p>
            </div>
            <p class="text-slate-400">
              We do not warrant that the service will be uninterrupted, secure, or error-free. You use the service at your own risk. We are not responsible for any data loss, so we recommend maintaining your own backups of important information.
            </p>
          </div>

          <!-- Contact Us -->
          <div class="mb-16 border-t border-white/10 pt-16">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <Mail :size="20" class="text-blue-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">Contact Us</h2>
            </div>
            <p class="text-slate-400 mb-6">
              If you have any questions about these Terms of Service, please contact us:
            </p>
            <div class="flex flex-col sm:flex-row gap-4">
              <a href="mailto:legal@lifeadmin.com" class="px-6 py-3 bg-white/5 border border-white/10 rounded-xl font-medium text-white hover:bg-white/10 transition-colors flex items-center justify-center gap-2 no-underline">
                <Mail :size="16" class="text-blue-400" />
                legal@lifeadmin.com
              </a>
            </div>
          </div>

        </div>
      </section>
    </main>

    <AppFooter />
  </div>
</template>