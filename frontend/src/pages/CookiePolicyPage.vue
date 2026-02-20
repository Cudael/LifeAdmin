<script setup>
import AppHeader from "../components/layout/AppHeader.vue"
import AppFooter from "../components/layout/AppFooter.vue"
import { Cookie, Settings, BarChart, Shield, CheckCircle, Mail } from "lucide-vue-next"
</script>

<template>
  <div class="bg-slate-950 min-h-screen flex flex-col text-slate-300 font-sans selection:bg-teal-500/30 selection:text-teal-200">
    <AppHeader />

    <main class="flex-1 pt-24 md:pt-32 relative z-10">
      
      <!-- Abstract Background Elements -->
      <div class="absolute top-0 left-0 w-full h-[500px] bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px] [mask-image:linear-gradient(to_bottom,black_40%,transparent_100%)] pointer-events-none z-0"></div>
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-2xl h-[400px] bg-indigo-500/10 blur-[120px] rounded-full pointer-events-none z-0"></div>

      <!-- Header Section -->
      <section class="relative py-16 md:py-24 z-10 border-b border-white/5">
        <div class="max-w-4xl mx-auto px-6">
          <div class="text-left md:text-center flex flex-col md:items-center">
            <div class="inline-flex items-center justify-center w-16 h-16 bg-indigo-500/10 border border-indigo-500/20 rounded-2xl mb-8 shadow-[0_0_15px_rgba(99,102,241,0.15)]">
              <Cookie :size="32" class="text-indigo-400 drop-shadow-[0_0_8px_rgba(99,102,241,0.5)]" />
            </div>
            <h1 class="text-4xl md:text-6xl font-extrabold text-white mb-6 tracking-tight">
              Cookie Policy
            </h1>
            <p class="text-lg text-slate-400 font-medium">
              Last updated: <span class="text-slate-300">February 13, 2026</span>
            </p>
          </div>
        </div>
      </section>

      <!-- Content Section -->
      <section class="py-16 md:py-24 relative z-10">
        <div class="max-w-3xl mx-auto px-6 prose prose-invert prose-slate prose-a:text-indigo-400 hover:prose-a:text-indigo-300 prose-headings:text-white prose-p:leading-relaxed">
          
          <!-- Introduction -->
          <div class="mb-16">
            <p class="text-lg text-slate-400">
              This Cookie Policy explains how LifeAdmin uses cookies and similar tracking technologies when you visit our website. By using our service, you consent to the use of cookies as described in this policy.
            </p>
          </div>

          <!-- Types of Cookies We Use -->
          <div class="mb-16">
            <h2 class="text-3xl font-bold text-white mb-8">Types of Cookies We Use</h2>

            <!-- Essential Cookies -->
            <div class="mb-6 p-6 bg-slate-900/50 border border-white/5 border-l-4 border-l-emerald-500 rounded-r-2xl rounded-l-md shadow-sm">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 bg-slate-950 border border-white/10 rounded-lg flex items-center justify-center">
                  <CheckCircle :size="18" class="text-emerald-400" />
                </div>
                <h3 class="text-xl font-bold text-white m-0">Essential Cookies</h3>
              </div>
              <p class="text-slate-400 mb-3 m-0">
                Necessary for the website to function properly. They enable core functionality such as security, authentication, and accessibility.
              </p>
              <p class="text-sm text-emerald-400 font-bold tracking-wide uppercase mt-4 m-0">
                ✓ Required - Cannot be disabled
              </p>
            </div>

            <!-- Functional Cookies -->
            <div class="mb-6 p-6 bg-slate-900/50 border border-white/5 border-l-4 border-l-cyan-500 rounded-r-2xl rounded-l-md shadow-sm">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 bg-slate-950 border border-white/10 rounded-lg flex items-center justify-center">
                  <Settings :size="18" class="text-cyan-400" />
                </div>
                <h3 class="text-xl font-bold text-white m-0">Functional Cookies</h3>
              </div>
              <p class="text-slate-400 mb-3 m-0">
                Enable enhanced functionality and personalization, such as remembering your preferences and dark mode settings.
              </p>
              <p class="text-sm text-cyan-400 font-bold tracking-wide uppercase mt-4 m-0">
                ⚙ Optional - Configurable
              </p>
            </div>

            <!-- Analytics Cookies -->
            <div class="mb-6 p-6 bg-slate-900/50 border border-white/5 border-l-4 border-l-purple-500 rounded-r-2xl rounded-l-md shadow-sm">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 bg-slate-950 border border-white/10 rounded-lg flex items-center justify-center">
                  <BarChart :size="18" class="text-purple-400" />
                </div>
                <h3 class="text-xl font-bold text-white m-0">Analytics Cookies</h3>
              </div>
              <p class="text-slate-400 mb-3 m-0">
                Help us understand how visitors interact with our website by collecting and reporting information anonymously.
              </p>
              <p class="text-sm text-purple-400 font-bold tracking-wide uppercase mt-4 m-0">
                ⚙ Optional - Configurable
              </p>
            </div>
          </div>

          <!-- Specific Cookies Data Table -->
          <div class="mb-16">
            <h2 class="text-3xl font-bold text-white mb-6">Specific Cookies We Use</h2>
            <div class="overflow-x-auto rounded-2xl border border-white/10 bg-slate-900/50">
              <table class="w-full text-left border-collapse text-sm m-0">
                <thead>
                  <tr class="bg-white/5 border-b border-white/10 text-slate-300">
                    <th class="p-4 font-semibold">Cookie Name</th>
                    <th class="p-4 font-semibold">Purpose</th>
                    <th class="p-4 font-semibold">Type</th>
                    <th class="p-4 font-semibold">Duration</th>
                  </tr>
                </thead>
                <tbody class="text-slate-400">
                  <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                    <td class="p-4 font-mono text-indigo-300">access_token</td>
                    <td class="p-4">Authentication and session management</td>
                    <td class="p-4"><span class="px-2 py-1 bg-emerald-500/10 text-emerald-400 rounded-md text-xs font-bold">Essential</span></td>
                    <td class="p-4">30 minutes</td>
                  </tr>
                  <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                    <td class="p-4 font-mono text-indigo-300">refresh_token</td>
                    <td class="p-4">Maintaining login session</td>
                    <td class="p-4"><span class="px-2 py-1 bg-emerald-500/10 text-emerald-400 rounded-md text-xs font-bold">Essential</span></td>
                    <td class="p-4">7 days</td>
                  </tr>
                  <tr class="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                    <td class="p-4 font-mono text-indigo-300">theme</td>
                    <td class="p-4">Remembering light/dark mode preference</td>
                    <td class="p-4"><span class="px-2 py-1 bg-cyan-500/10 text-cyan-400 rounded-md text-xs font-bold">Functional</span></td>
                    <td class="p-4">1 year</td>
                  </tr>
                  <tr class="hover:bg-white/[0.02] transition-colors">
                    <td class="p-4 font-mono text-indigo-300">analytics_id</td>
                    <td class="p-4">Anonymous usage analytics</td>
                    <td class="p-4"><span class="px-2 py-1 bg-purple-500/10 text-purple-400 rounded-md text-xs font-bold">Analytics</span></td>
                    <td class="p-4">2 years</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Contact Us -->
          <div class="mb-16 border-t border-white/10 pt-16">
            <div class="flex items-center gap-4 mb-8">
              <div class="w-12 h-12 bg-slate-900 border border-white/10 rounded-xl flex items-center justify-center shadow-inner">
                <Shield :size="20" class="text-indigo-400" />
              </div>
              <h2 class="text-3xl font-bold text-white m-0">More Information</h2>
            </div>
            <p class="text-slate-400 mb-6">
              For more information about how we handle your personal data, please see our <RouterLink to="/privacy" class="text-indigo-400 hover:text-indigo-300 font-medium no-underline">Privacy Policy</RouterLink>. If you have any questions, reach out to us:
            </p>
            <div class="flex flex-col sm:flex-row gap-4">
              <a href="mailto:privacy@lifeadmin.com" class="px-6 py-3 bg-white/5 border border-white/10 rounded-xl font-medium text-white hover:bg-white/10 transition-colors flex items-center justify-center gap-2 no-underline">
                <Mail :size="16" class="text-indigo-400" />
                privacy@lifeadmin.com
              </a>
            </div>
          </div>

        </div>
      </section>
    </main>

    <AppFooter />
  </div>
</template>