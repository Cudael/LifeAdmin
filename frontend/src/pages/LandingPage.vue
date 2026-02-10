<script setup>
import { computed } from "vue"
import AppHeader from "../components/layout/AppHeader.vue"
import AppFooter from "../components/layout/AppFooter.vue"
import { accessToken } from "../utils/auth"

const isLoggedIn = computed(() => !!accessToken.value)
</script>

<template>
  <div class="bg-white text-gray-800 min-h-screen flex flex-col">

    <AppHeader />

    <main class="flex-1">

      <!-- HERO -->
      <section class="relative min-h-screen flex items-center justify-center overflow-hidden bg-[#0a0c12] text-white">

        <!-- Base dark background -->
        <div class="absolute inset-0 z-0 bg-[#0a0c12]"></div>

        <div class="absolute inset-0 z-0 opacity-[0.5] bg-[url('https://www.transparenttextures.com/patterns/axiom-pattern.png')]"></div>
        

        <!-- Teal atmospheric gradient (main accent) -->
        <div class="absolute inset-0 z-0 bg-[radial-gradient(circle_at_20%_30%,rgba(0,255,200,0.22),transparent_60%)]"></div>

        <!-- Soft blue-teal drift from the opposite side -->
        <div class="absolute inset-0 z-0 bg-[radial-gradient(circle_at_80%_70%,rgba(0,180,255,0.18),transparent_65%)]"></div>

        <!-- Fog layer (cinematic depth) -->
        <div class="absolute inset-0 z-0 bg-[radial-gradient(circle_at_center,rgba(255,255,255,0.02),transparent_75%)]"></div>

        <!-- Content -->
        <div class="relative z-10 max-w-4xl mx-auto px-6 text-center">

          <h1 class="text-6xl md:text-7xl font-extrabold leading-tight mb-8">
            Stay Ahead.<br />
            Live With Clarity.
          </h1>

          <p class="text-xl text-gray-300 max-w-2xl mx-auto mb-12">
            A calm, intelligent dashboard that keeps your documents, subscriptions, and deadlines organized — effortlessly.
          </p>

          <!-- Centered CTA layout -->
          <div class="flex flex-col md:flex-row justify-center items-center gap-6 mb-14">

            <RouterLink
              to="/register"
              class="px-12 py-4 bg-gradient-to-r from-teal-400 to-cyan-400 hover:from-teal-300 hover:to-cyan-300 text-black rounded-full text-xl font-semibold shadow-xl transition"
            >
              Get Started Free
            </RouterLink>

            <RouterLink
              to="/demo"
              class="px-12 py-4 bg-white/10 backdrop-blur-md border border-white/20 hover:bg-white/20 text-white rounded-full text-xl font-medium transition"
            >
              Watch Demo
            </RouterLink>

          </div>

          <!-- Micro-features -->
          <div class="flex flex-wrap justify-center gap-10 text-gray-300 text-sm opacity-90">

            <div class="flex items-center gap-2">
              <span class="text-teal-300 text-lg">✨</span> Beautiful interface
            </div>

            <div class="flex items-center gap-2">
              <span class="text-teal-300 text-lg">🔐</span> Secure cloud storage
            </div>

            <div class="flex items-center gap-2">
              <span class="text-teal-300 text-lg">📅</span> Smart expiry detection
            </div>

            <div class="flex items-center gap-2">
              <span class="text-teal-300 text-lg">⚙️</span> Custom reminders
            </div>

          </div>

        </div>
      </section>

      <!-- HOW IT WORKS -->
      <section class="py-28 bg-white">
        <div class="max-w-screen-xl mx-auto px-6 text-center">

          <h2 class="text-4xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">How It Works</h2>
          <div class="w-12 h-1 bg-teal-400 mx-auto mb-6"></div>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto mb-16">
            A simple, powerful workflow that keeps your life organized without effort.
          </p>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm hover:shadow-xl transition">
              <div class="text-4xl mb-4 text-teal-500">📥</div>
              <h3 class="text-xl font-semibold mb-3">1. Add Your Items</h3>
              <p class="text-gray-600">Upload documents, add subscriptions, or enter expiry dates manually.</p>
            </div>

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm hover:shadow-xl transition">
              <div class="text-4xl mb-4 text-teal-500">⚡</div>
              <h3 class="text-xl font-semibold mb-3">2. We Track Everything</h3>
              <p class="text-gray-600">Our system monitors renewals, deadlines, and important dates for you.</p>
            </div>

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm hover:shadow-xl transition">
              <div class="text-4xl mb-4 text-teal-500">🔔</div>
              <h3 class="text-xl font-semibold mb-3">3. Get Smart Reminders</h3>
              <p class="text-gray-600">Receive notifications weeks before something expires — never miss a thing.</p>
            </div>

          </div>

        </div>
      </section>

      <!-- WHO IT’S FOR -->
      <section class="py-28 bg-gradient-to-b from-white to-[#f7fdfc]">
        <div class="max-w-screen-xl mx-auto px-6 text-center">

          <h2 class="text-4xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">Who It’s For</h2>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto mb-16">
            LifeAdmin is built for anyone who wants clarity, control, and peace of mind.
          </p>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm">
              <h3 class="text-xl font-semibold mb-3 text-teal-600">Busy Professionals</h3>
              <p class="text-gray-600">Keep track of IDs, insurance, certifications, and work documents.</p>
            </div>

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm">
              <h3 class="text-xl font-semibold mb-3 text-teal-600">Families</h3>
              <p class="text-gray-600">Manage passports, warranties, medical documents, and school deadlines.</p>
            </div>

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm">
              <h3 class="text-xl font-semibold mb-3 text-teal-600">Small Business Owners</h3>
              <p class="text-gray-600">Track licenses, contracts, receipts, and compliance documents.</p>
            </div>

          </div>

        </div>
      </section>

      <!-- WHY THIS MATTERS -->
      <section class="py-28 bg-gradient-to-b from-[#f7fdfc] to-white">
        <div class="max-w-screen-lg mx-auto px-6 text-center">

          <h2 class="text-4xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">Why It Matters</h2>

          <p class="text-lg text-gray-600 max-w-2xl mx-auto leading-relaxed">
            Life admin sneaks up on everyone — expired IDs, forgotten subscriptions, missing documents.
            We built this tool to bring calm to the chaos and help you stay on top of the things that matter.
          </p>

        </div>
      </section>

      <!-- SECURITY & TRUST -->
      <section class="py-28 bg-white">
        <div class="max-w-screen-xl mx-auto px-6">

          <h2 class="text-4xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent text-center mb-16">Security & Trust</h2>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm">
              <div class="text-4xl mb-4 text-teal-500">🔒</div>
              <h3 class="text-xl font-semibold mb-3">Bank‑Level Encryption</h3>
              <p class="text-gray-600">Your documents and data are encrypted at rest and in transit.</p>
            </div>

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm">
              <div class="text-4xl mb-4 text-teal-500">🛡️</div>
              <h3 class="text-xl font-semibold mb-3">Privacy First</h3>
              <p class="text-gray-600">We never sell your data. Your information stays yours.</p>
            </div>

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm">
              <div class="text-4xl mb-4 text-teal-500">☁️</div>
              <h3 class="text-xl font-semibold mb-3">Secure Cloud Storage</h3>
              <p class="text-gray-600">Your files are stored safely with industry‑leading infrastructure.</p>
            </div>

          </div>

        </div>
      </section>

      <!-- FEATURES -->
      <section id="features" class="py-28 bg-gradient-to-b from-white to-[#f7fdfc]">
        <div class="max-w-screen-xl mx-auto px-6">

          <h2 class="text-4xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent text-center mb-20">Features</h2>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm hover:shadow-xl transition">
              <div class="text-4xl mb-4 text-teal-500">📅</div>
              <h3 class="text-xl font-semibold mb-3">Expiration Tracking</h3>
              <p class="text-gray-600">Never miss a renewal again — passports, IDs, insurance, subscriptions.</p>
            </div>

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm hover:shadow-xl transition">
              <div class="text-4xl mb-4 text-teal-500">⏰</div>
              <h3 class="text-xl font-semibold mb-3">Smart Reminders</h3>
              <p class="text-gray-600">Get notified weeks before something expires.</p>
            </div>

            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm hover:shadow-xl transition">
              <div class="text-4xl mb-4 text-teal-500">📄</div>
              <h3 class="text-xl font-semibold mb-3">Document Storage</h3>
              <p class="text-gray-600">Upload PDFs, receipts, warranties, and keep them safe.</p>
            </div>

          </div>

        </div>
      </section>

      <!-- TESTIMONIALS -->
      <section class="py-28 bg-gradient-to-b from-[#f7fdfc] to-white">
        <div class="max-w-screen-xl mx-auto px-6 text-center">

          <h2 class="text-4xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">What People Say</h2>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="p-8 bg-white rounded-3xl shadow-md border border-teal-200">
              <p class="text-gray-700 mb-4">“I used to forget renewals constantly. Now everything is handled automatically.”</p>
              <div class="font-semibold text-gray-900">— Anna K.</div>
            </div>

            <div class="p-8 bg-white rounded-3xl shadow-md border border-teal-200">
              <p class="text-gray-700 mb-4">“The reminders saved me from a €300 fine. Worth it instantly.”</p>
              <div class="font-semibold text-gray-900">— Markus L.</div>
            </div>

            <div class="p-8 bg-white rounded-3xl shadow-md border border-teal-200">
              <p class="text-gray-700 mb-4">“Clean, simple, and surprisingly powerful. I use it every week.”</p>
              <div class="font-semibold text-gray-900">— Sofia R.</div>
            </div>

          </div>

        </div>
      </section>

      <!-- PRICING -->
      <section id="pricing" class="py-32 bg-gradient-to-b from-white to-[#f7fdfc]">
        <div class="max-w-screen-xl mx-auto px-6 text-center">

          <!-- Section Label -->
          <p class="text-sm font-semibold text-teal-600 tracking-wide uppercase mb-3">
            Pricing
          </p>

          <!-- Title -->
          <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
            Choose the Plan That Fits You
          </h2>

          <!-- Underline -->
          <div class="w-16 h-1 bg-teal-400 mx-auto mb-12"></div>

          <p class="text-lg text-gray-600 max-w-2xl mx-auto mb-20">
            Simple, transparent pricing. No hidden fees. Cancel anytime.
          </p>

          <!-- Pricing Grid -->
          <div class="grid md:grid-cols-3 gap-12 max-w-6xl mx-auto">

            <!-- FREE PLAN -->
            <div class="p-10 bg-white rounded-3xl border border-gray-200 shadow-sm hover:shadow-xl transition text-left">
              <h3 class="text-2xl font-semibold mb-2">Free</h3>
              <p class="text-gray-600 mb-6">Perfect for getting started.</p>

              <p class="text-5xl font-bold text-gray-900 mb-8">€0</p>

              <ul class="space-y-3 text-gray-700 mb-10">
                <li>✔ Track up to 20 items</li>
                <li>✔ Smart reminders</li>
                <li>✔ Document uploads</li>
                <li>✔ Secure cloud storage</li>
              </ul>

              <RouterLink
                to="/register"
                class="block text-center px-7 py-3 bg-gray-100 text-gray-900 rounded-full text-lg font-medium hover:bg-gray-200 transition"
              >
                Start Free
              </RouterLink>
            </div>

            <!-- PREMIUM MONTHLY -->
            <div class="relative p-10 bg-white rounded-3xl border-2 border-teal-400 shadow-xl hover:shadow-2xl transition text-left">

              <!-- Most Popular Badge -->
              <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-teal-500 text-white text-sm font-semibold px-4 py-1 rounded-full shadow-md">
                Most Popular
              </div>

              <h3 class="text-2xl font-semibold mb-2 text-teal-600">Premium Monthly</h3>
              <p class="text-gray-600 mb-6">Full access. No limits.</p>

              <p class="text-5xl font-bold text-gray-900 mb-8">€2.99<span class="text-xl text-gray-500">/mo</span></p>

              <ul class="space-y-3 text-gray-700 mb-10">
                <li>✔ Unlimited items</li>
                <li>✔ Priority reminders</li>
                <li>✔ Unlimited document uploads</li>
                <li>✔ Advanced insights</li>
                <li>✔ Early access to new features</li>
              </ul>

              <RouterLink
                to="/register"
                class="block text-center px-7 py-3 bg-gradient-to-r from-teal-400 to-cyan-400 text-black rounded-full text-lg font-semibold shadow-md hover:from-teal-300 hover:to-cyan-300 transition"
              >
                Upgrade Monthly
              </RouterLink>
            </div>

            <!-- PREMIUM YEARLY -->
            <div class="p-10 bg-white rounded-3xl border border-teal-200 shadow-sm hover:shadow-xl transition text-left">
              <h3 class="text-2xl font-semibold mb-2 text-teal-600">Premium Yearly</h3>
              <p class="text-gray-600 mb-6">Save money with the yearly plan.</p>

              <p class="text-5xl font-bold text-gray-900 mb-2">€24<span class="text-xl text-gray-500">/yr</span></p>
              <p class="text-sm text-teal-600 font-semibold mb-8">Save 33%</p>

              <ul class="space-y-3 text-gray-700 mb-10">
                <li>✔ Everything in Monthly</li>
                <li>✔ Priority support</li>
                <li>✔ Exclusive yearly-only perks</li>
              </ul>

              <RouterLink
                to="/register"
                class="block text-center px-7 py-3 bg-teal-500 text-white rounded-full text-lg font-medium shadow-md hover:bg-teal-600 transition"
              >
                Upgrade Yearly
              </RouterLink>
            </div>

          </div>

          <!-- Money Back Guarantee -->
          <div class="mt-16 flex items-center justify-center gap-3 text-gray-600">
            <span class="text-teal-500 text-2xl">🛡️</span>
            <p class="text-md font-medium">30‑day money‑back guarantee. No questions asked.</p>
          </div>

          <!-- WHY PREMIUM -->
          <div class="mt-24 max-w-3xl mx-auto text-center">
            <h3 class="text-3xl font-bold text-gray-900 mb-6">Why Go Premium?</h3>
            <p class="text-lg text-gray-600 leading-relaxed mb-10">
              Premium gives you unlimited tracking, faster reminders, and powerful insights that help you stay ahead of every deadline. 
              If you rely on Expirel to manage important documents, subscriptions, or IDs — Premium pays for itself instantly.
            </p>

            <div class="grid md:grid-cols-3 gap-10">

              <div class="p-6 bg-white rounded-2xl border border-teal-200 shadow-sm">
                <div class="text-3xl mb-3 text-teal-500">⚡</div>
                <p class="font-semibold text-gray-900 mb-2">Faster Reminders</p>
                <p class="text-gray-600 text-sm">Get notified earlier so you never miss a renewal.</p>
              </div>

              <div class="p-6 bg-white rounded-2xl border border-teal-200 shadow-sm">
                <div class="text-3xl mb-3 text-teal-500">📈</div>
                <p class="font-semibold text-gray-900 mb-2">Advanced Insights</p>
                <p class="text-gray-600 text-sm">See patterns, upcoming renewals, and risk areas.</p>
              </div>

              <div class="p-6 bg-white rounded-2xl border border-teal-200 shadow-sm">
                <div class="text-3xl mb-3 text-teal-500">🔓</div>
                <p class="font-semibold text-gray-900 mb-2">Unlimited Everything</p>
                <p class="text-gray-600 text-sm">No limits on items, uploads, or reminders.</p>
              </div>

            </div>
          </div>

        </div>
      </section>

      <!-- FAQ -->
      <section id="faq" class="py-32 bg-gradient-to-b from-[#f7fdfc] to-white">
        <div class="max-w-screen-xl mx-auto px-6">

          <!-- Label -->
          <p class="text-sm font-semibold text-teal-600 tracking-wide uppercase mb-3 text-center">
            FAQ
          </p>

          <!-- Title -->
          <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent text-center mb-4">
            Frequently Asked Questions
          </h2>

          <!-- Underline -->
          <div class="w-16 h-1 bg-teal-400 mx-auto mb-16"></div>

          <div class="max-w-3xl mx-auto space-y-6">

            <!-- FAQ ITEM -->
            <details class="group bg-white border-b rounded-2xl p-6 shadow-sm">
              <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900">
                How does Expirel remind me about upcoming expirations?
                <span class="text-teal-500 text-2xl group-open:rotate-180 transition-transform">⌄</span>
              </summary>

              <div class="overflow-hidden transition-all duration-300 ease-in-out max-h-0 group-open:max-h-96">
                <p class="mt-4 text-gray-600 leading-relaxed">
                  Expirel sends you smart reminders days or weeks before something expires. 
                  You choose how early you want to be notified.
                </p>
              </div>
            </details>

            <!-- FAQ ITEM -->
            <details class="group bg-white border-b rounded-2xl p-6 shadow-sm">
              <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900">
                Is my data secure?
                <span class="text-teal-500 text-2xl group-open:rotate-180 transition-transform">⌄</span>
              </summary>
              <p class="mt-4 text-gray-600 leading-relaxed">
                Yes — all your data is encrypted at rest and in transit. 
                We never sell your information, and you stay in full control of your documents.
              </p>
            </details>

            <!-- FAQ ITEM -->
            <details class="group bg-white border-b rounded-2xl p-6 shadow-sm">
              <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900">
                What’s included in the free plan?
                <span class="text-teal-500 text-2xl group-open:rotate-180 transition-transform">⌄</span>
              </summary>
              <p class="mt-4 text-gray-600 leading-relaxed">
                The free plan includes tracking for up to 20 items, smart reminders, and secure document storage.
                It’s perfect for getting started.
              </p>
            </details>

            <!-- FAQ ITEM -->
            <details class="group bg-white border-b rounded-2xl p-6 shadow-sm">
              <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900">
                Can I cancel my Premium subscription anytime?
                <span class="text-teal-500 text-2xl group-open:rotate-180 transition-transform">⌄</span>
              </summary>
              <p class="mt-4 text-gray-600 leading-relaxed">
                Absolutely. You can cancel anytime with a single click — no hidden steps, no hassle.
              </p>
            </details>

            <!-- FAQ ITEM -->
            <details class="group bg-white border-b rounded-2xl p-6 shadow-sm">
              <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900">
                Do you offer refunds?
                <span class="text-teal-500 text-2xl group-open:rotate-180 transition-transform">⌄</span>
              </summary>
              <p class="mt-4 text-gray-600 leading-relaxed">
                Yes — all Premium plans come with a 30‑day money‑back guarantee. 
                If you’re not satisfied, we’ll refund you with no questions asked.
              </p>
            </details>

            <!-- FAQ ITEM -->
            <details class="group bg-white border-b rounded-2xl p-6 shadow-sm">
              <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900">
                What types of items can I track?
                <span class="text-teal-500 text-2xl group-open:rotate-180 transition-transform">⌄</span>
              </summary>
              <p class="mt-4 text-gray-600 leading-relaxed">
                Anything with an expiration date — IDs, passports, warranties, subscriptions, insurance, 
                contracts, certifications, and more.
              </p>
            </details>

          </div>

        </div>


        <!-- Still have a question? -->
        <div class="max-w-screen-md mx-auto px-6 text-center mt-24">

          <h3 class="text-3xl font-bold text-gray-900 mb-4">
            Still have a question?
          </h3>

          <p class="text-lg text-gray-600 mb-10">
            We’re here to help. If you didn’t find the answer you were looking for, 
            reach out and we’ll get back to you as soon as possible.
          </p>

          <RouterLink
            to="/contact"
            class="inline-block px-10 py-4 bg-gradient-to-r from-teal-400 to-cyan-400 text-black rounded-full text-lg font-semibold shadow-md hover:from-teal-300 hover:to-cyan-300 transition"
          >
            Contact Support
          </RouterLink>

          <p class="text-sm text-gray-500 mt-6">
            Average response time: <span class="text-teal-600 font-semibold">under 24 hours</span>
          </p>

        </div>
      </section>
    </main>

    <AppFooter />

  </div>
</template>