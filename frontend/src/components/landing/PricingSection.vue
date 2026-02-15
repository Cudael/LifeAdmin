<script setup>
import { 
  CheckCircle2, 
  ArrowRight,
  Star,
  Shield,
  Zap,
  TrendingUp,
  Award
} from "lucide-vue-next"
</script>

<template>
  <section id="pricing" class="py-16 bg-gradient-to-b from-white to-[#f7fdfc] relative overflow-hidden">
    
    <!-- Decorative gradient -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(20,184,166,0.05),transparent_70%)]"></div>

    <div class="max-w-screen-xl mx-auto px-6 text-center relative z-10">

      <!-- Section Label -->
      <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
        <Award :size="16" />
        Simple Pricing
      </div>

      <!-- Title -->
      <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
        Choose the Plan That Fits You
      </h2>

      <!-- Underline -->
      <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-12"></div>

      <!-- Pricing Grid -->
      <div class="grid md:grid-cols-3 gap-12 max-w-6xl mx-auto">

        <!-- FREE PLAN -->
        <div class="group p-10 bg-white rounded-3xl border-2 border-gray-200 shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2 text-left">
          <div class="inline-block px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm font-semibold mb-4">
            Free Forever
          </div>
          <h3 class="text-3xl font-semibold mb-2">Free</h3>
          <p class="text-gray-600 mb-6">Perfect for getting started.</p>

          <p class="text-5xl font-bold text-gray-900 mb-2">€0</p>
          <p class="text-gray-500 mb-8">No credit card required</p>

          <ul class="space-y-4 text-gray-700 mb-10">
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Track up to 20 items</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Smart reminders</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Document uploads (100MB)</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Secure cloud storage</span>
            </li>
          </ul>

          <RouterLink
            to="/register"
            class="block text-center px-7 py-4 bg-gray-100 text-gray-900 rounded-xl text-lg font-semibold hover:bg-gray-200 transition group-hover:shadow-lg"
          >
            Start Free
          </RouterLink>
        </div>

        <!-- PREMIUM MONTHLY -->
        <div class="relative p-10 bg-gradient-to-br from-white to-teal-50 rounded-3xl border-2 border-teal-400 shadow-2xl hover:shadow-3xl transition-all duration-300 hover:-translate-y-2 text-left transform scale-105">

          <!-- Most Popular Badge -->
          <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-gradient-to-r from-teal-500 to-cyan-500 text-white text-sm font-bold px-6 py-2 rounded-full shadow-lg flex items-center gap-2">
            <Star :size="16" class="fill-white" />
            Most Popular
          </div>

          <div class="inline-block px-3 py-1 bg-teal-100 text-teal-700 rounded-full text-sm font-semibold mb-4">
            Best Value
          </div>
          <h3 class="text-3xl font-semibold mb-2 text-teal-600">Premium Monthly</h3>
          <p class="text-gray-600 mb-6">Full access. No limits.</p>

          <div class="flex items-baseline gap-2 mb-2">
            <p class="text-5xl font-bold text-gray-900">€2.99</p>
            <span class="text-xl text-gray-500">/mo</span>
          </div>
          <p class="text-teal-600 font-medium mb-8">Billed monthly</p>

          <ul class="space-y-4 text-gray-700 mb-10">
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span><strong>Unlimited items</strong></span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Priority reminders</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Unlimited document uploads</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Advanced insights & analytics</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Priority support</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Early access to new features</span>
            </li>
          </ul>

          <RouterLink
            to="/register"
            class="group block text-center px-7 py-4 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl text-lg font-bold shadow-lg hover:shadow-2xl hover:from-teal-400 hover:to-cyan-400 transition-all items-center justify-center gap-2"
          >
            Upgrade Monthly
            <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
          </RouterLink>
        </div>

        <!-- PREMIUM YEARLY -->
        <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2 text-left">
          <div class="inline-block px-3 py-1 bg-teal-100 text-teal-700 rounded-full text-sm font-semibold mb-4">
            Save 33%
          </div>
          <h3 class="text-3xl font-semibold mb-2 text-teal-600">Premium Yearly</h3>
          <p class="text-gray-600 mb-6">Save money with the yearly plan.</p>

          <div class="flex items-baseline gap-2 mb-2">
            <p class="text-5xl font-bold text-gray-900">€24</p>
            <span class="text-xl text-gray-500">/yr</span>
          </div>
          <p class="text-teal-600 font-semibold mb-8">€2/month · Save €12/year</p>

          <ul class="space-y-4 text-gray-700 mb-10">
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Everything in Monthly</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span><strong>33% discount</strong></span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Priority support</span>
            </li>
            <li class="flex items-start gap-3">
              <CheckCircle2 :size="20" class="text-teal-500 flex-shrink-0 mt-0.5" />
              <span>Exclusive yearly-only perks</span>
            </li>
          </ul>

          <RouterLink
            to="/register"
            class="block text-center px-7 py-4 bg-teal-500 text-white rounded-xl text-lg font-semibold shadow-lg hover:bg-teal-600 hover:shadow-xl transition group-hover:scale-105"
          >
            Upgrade Yearly
          </RouterLink>
        </div>

      </div>

      <!-- Money Back Guarantee -->
      <div class="mt-16 p-6 bg-gradient-to-r from-teal-50 to-cyan-50 rounded-2xl border border-teal-200 inline-flex items-center gap-3">
        <div class="w-12 h-12 rounded-full bg-teal-500 flex items-center justify-center">
          <Shield :size="24" class="text-white" />
        </div>
        <div class="text-left">
          <p class="font-semibold text-gray-900">30-day money-back guarantee</p>
          <p class="text-sm text-gray-600">No questions asked. Full refund if you're not satisfied.</p>
        </div>
      </div>

    </div>
  </section>
</template>
