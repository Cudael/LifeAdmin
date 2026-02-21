<script setup>
import AppHeader from "../components/layout/AppHeader.vue"
import AppFooter from "../components/layout/AppFooter.vue"
import { Shield, Lock, Eye, Database, Mail, UserCheck } from "lucide-vue-next"
</script>

<template>
  <div class="bg-slate-950 min-h-screen flex flex-col text-slate-300 font-sans selection:bg-teal-500/30 selection:text-teal-200">
    <AppHeader />

    <main class="flex-1 pt-24 md:pt-32 relative z-10">
      
      <!-- Abstract Background Elements -->
      <div class="absolute top-0 left-0 w-full h-[500px] bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px] [mask-image:linear-gradient(to_bottom,black_40%,transparent_100%)] pointer-events-none z-0"></div>
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-2xl h-[400px] bg-teal-500/10 blur-[120px] rounded-full pointer-events-none z-0"></div>

      <!-- Header Section -->
      <section class="relative py-16 md:py-24 z-10 border-b border-white/5">
        <div class="max-w-4xl mx-auto px-6">
          <div class="text-left md:text-center flex flex-col md:items-center">
            <div class="inline-flex items-center justify-center w-16 h-16 bg-teal-500/10 border border-teal-500/20 rounded-2xl mb-8 shadow-[0_0_15px_rgba(45,212,191,0.15)]">
              <Shield :size="32" class="text-teal-400 drop-shadow-[0_0_8px_rgba(45,212,191,0.5)]" />
            </div>
            <h1 class="text-4xl md:text-6xl font-extrabold text-white mb-6 tracking-tight">
              Privacy Policy
            </h1>
            <p class="text-lg text-slate-400 font-medium">
              Last updated: <span class="text-slate-300">February 13, 2026</span>
            </p>
          </div>
        </div>
      </section>

      <!-- Content Section -->
      <section class="py-16 md:py-24 relative z-10">
        <div class="max-w-3xl mx-auto px-6 prose prose-invert prose-slate prose-a:text-teal-400 hover:prose-a:text-teal-300 prose-headings:text-white prose-p:leading-relaxed">
          
          <!-- Introduction -->
          <div class="mb-16">
            <p class="text-lg text-slate-400">
              At Remindes, we take your privacy seriously. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our service. Please read this privacy policy carefully. If you do not agree with the terms of this privacy policy, please do not access the site.
            </p>
          </div>

          <!-- Information We Collect -->
          <div class="mb-16 scroll-mt-32">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <Database :size="20" class="text-teal-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">Information We Collect</h2>
            </div>

            <div class="space-y-8 text-slate-400">
              <div class="p-6 bg-slate-900/50 border border-white/5 rounded-2xl">
                <h3 class="text-xl font-bold text-slate-100 mb-3 mt-0">Personal Information</h3>
                <p class="mb-4">We collect information that you voluntarily provide to us when you register on the service, including:</p>
                <ul class="list-disc pl-5 space-y-2 marker:text-teal-500">
                  <li>Name and email address</li>
                  <li>Account credentials (encrypted password)</li>
                  <li>Profile information you choose to provide</li>
                </ul>
              </div>

              <div class="p-6 bg-slate-900/50 border border-white/5 rounded-2xl">
                <h3 class="text-xl font-bold text-slate-100 mb-3 mt-0">Document and Data Information</h3>
                <p class="mb-4">When you use our service, we collect:</p>
                <ul class="list-disc pl-5 space-y-2 marker:text-teal-500">
                  <li>Documents and files you upload</li>
                  <li>Subscription details and expiration dates</li>
                  <li>Reminder preferences and settings</li>
                  <li>Notes and custom fields you add to items</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- How We Use Your Information -->
          <div class="mb-16 scroll-mt-32">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <UserCheck :size="20" class="text-cyan-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">How We Use Your Information</h2>
            </div>
            <ul class="list-disc pl-5 space-y-2 text-slate-400 marker:text-cyan-500">
              <li>Create and manage your account</li>
              <li>Provide, operate, and maintain our service</li>
              <li>Send you reminders about upcoming expirations</li>
              <li>Improve, personalize, and expand our service</li>
              <li>Understand and analyze how you use our service</li>
              <li>Prevent fraud and enhance security</li>
              <li>Comply with legal obligations</li>
            </ul>
          </div>

          <!-- Data Security -->
          <div class="mb-16 scroll-mt-32">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <Lock :size="20" class="text-emerald-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">Data Security</h2>
            </div>
            <p class="text-slate-400 mb-6">
              We implement appropriate technical and organizational security measures to protect your personal information, including:
            </p>
            <ul class="list-disc pl-5 space-y-3 text-slate-400 marker:text-emerald-500">
              <li><strong class="text-slate-200">Encryption:</strong> All data is encrypted in transit using TLS/SSL and at rest using AES-256.</li>
              <li><strong class="text-slate-200">Access Controls:</strong> Strict access controls and authentication mechanisms.</li>
              <li><strong class="text-slate-200">Secure Infrastructure:</strong> Industry-leading cloud infrastructure with automatic backups.</li>
              <li><strong class="text-slate-200">Password Protection:</strong> Passwords are hashed using bcrypt before storage.</li>
            </ul>
          </div>

          <!-- Sharing Your Information -->
          <div class="mb-16 scroll-mt-32">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <Eye :size="20" class="text-indigo-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">Sharing Your Information</h2>
            </div>
            <div class="p-6 bg-indigo-500/10 border border-indigo-500/20 rounded-2xl mb-6">
              <p class="font-bold text-indigo-300 m-0">We do not sell, trade, or rent your personal information to third parties.</p>
            </div>
            <p class="text-slate-400 mb-4">We may share your information only in the following situations:</p>
            <ul class="list-disc pl-5 space-y-2 text-slate-400 marker:text-indigo-500">
              <li><strong class="text-slate-200">With Your Consent:</strong> When you give us explicit permission.</li>
              <li><strong class="text-slate-200">Service Providers:</strong> With trusted third-party providers who assist us (e.g., AWS, Stripe).</li>
              <li><strong class="text-slate-200">Legal Requirements:</strong> If required by law or in response to valid legal requests.</li>
            </ul>
          </div>

          <!-- Contact Us -->
          <div class="mb-16 scroll-mt-32 border-t border-white/10 pt-16">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <Mail :size="20" class="text-teal-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">Contact Us</h2>
            </div>
            <p class="text-slate-400 mb-6">
              If you have any questions about this Privacy Policy, please contact us:
            </p>
            <div class="flex flex-col sm:flex-row gap-4">
              <a href="mailto:info@remindes.com" class="px-6 py-3 bg-white/5 border border-white/10 rounded-xl font-medium text-white hover:bg-white/10 transition-colors flex items-center justify-center gap-2 no-underline">
                <Mail :size="16" class="text-teal-400" />
                info@remindes.com
              </a>
              <a href="mailto:support@remindes.com" class="px-6 py-3 bg-white/5 border border-white/10 rounded-xl font-medium text-white hover:bg-white/10 transition-colors flex items-center justify-center gap-2 no-underline">
                <Mail :size="16" class="text-teal-400" />
                support@remindes.com
              </a>
            </div>
          </div>

        </div>
      </section>
    </main>

    <AppFooter />
  </div>
</template>