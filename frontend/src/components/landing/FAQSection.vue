<script setup>
import { MessageCircle, Mail, ArrowRight, ChevronDown } from "lucide-vue-next"
</script>

<template>
  <section id="faq" class="py-16 bg-gradient-to-b from-[#f7fdfc] to-white relative overflow-hidden">
    
    <!-- Decorative shapes -->
    <div class="absolute top-10 left-10 w-96 h-96 bg-teal-100 rounded-full opacity-10 blur-3xl"></div>
    <div class="absolute bottom-10 right-10 w-80 h-80 bg-cyan-100 rounded-full opacity-10 blur-3xl"></div>

    <div class="max-w-screen-xl mx-auto px-6 relative z-10">

      <!-- Label -->
      <div class="text-center mb-12">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
          <MessageCircle :size="16" />
          FAQ
        </div>

        <!-- Title -->
        <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
          Frequently Asked Questions
        </h2>

        <!-- Underline -->
        <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto"></div>
      </div>

      <div class="max-w-3xl mx-auto space-y-4">

        <!-- FAQ ITEM -->
        <details class="group bg-white border-2 border-teal-200 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300">
          <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900 list-none">
            <span>How does LifeAdmin remind me about upcoming expirations?</span>
            <div class="w-8 h-8 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0 ml-4 group-open:bg-teal-500 transition-colors">
              <ChevronDown :size="20" class="text-teal-600 group-open:text-white group-open:rotate-180 transition-transform" />
            </div>
          </summary>

          <div class="mt-4 text-gray-600 leading-relaxed border-t border-gray-100 pt-4">
            LifeAdmin sends you smart reminders days or weeks before something expires. 
            You choose how early you want to be notified via email, push notifications, or both.
          </div>
        </details>

        <!-- FAQ ITEM -->
        <details class="group bg-white border-2 border-teal-200 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300">
          <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900 list-none">
            <span>Is my data secure?</span>
            <div class="w-8 h-8 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0 ml-4 group-open:bg-teal-500 transition-colors">
              <ChevronDown :size="20" class="text-teal-600 group-open:text-white group-open:rotate-180 transition-transform" />
            </div>
          </summary>
          <div class="mt-4 text-gray-600 leading-relaxed border-t border-gray-100 pt-4">
            Yes — all your data is encrypted at rest and in transit using bank-level AES-256 encryption. 
            We never sell your information, and you stay in full control of your documents.
          </div>
        </details>

        <!-- FAQ ITEM -->
        <details class="group bg-white border-2 border-teal-200 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300">
          <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900 list-none">
            <span>What's included in the free plan?</span>
            <div class="w-8 h-8 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0 ml-4 group-open:bg-teal-500 transition-colors">
              <ChevronDown :size="20" class="text-teal-600 group-open:text-white group-open:rotate-180 transition-transform" />
            </div>
          </summary>
          <div class="mt-4 text-gray-600 leading-relaxed border-t border-gray-100 pt-4">
            The free plan includes tracking for up to 20 items, smart reminders, and secure document storage up to 100MB.
            It's perfect for getting started and seeing if LifeAdmin is right for you.
          </div>
        </details>

        <!-- FAQ ITEM -->
        <details class="group bg-white border-2 border-teal-200 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300">
          <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900 list-none">
            <span>Can I cancel my Premium subscription anytime?</span>
            <div class="w-8 h-8 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0 ml-4 group-open:bg-teal-500 transition-colors">
              <ChevronDown :size="20" class="text-teal-600 group-open:text-white group-open:rotate-180 transition-transform" />
            </div>
          </summary>
          <div class="mt-4 text-gray-600 leading-relaxed border-t border-gray-100 pt-4">
            Absolutely. You can cancel anytime with a single click from your account settings — no hidden steps, no hassle.
            Your data remains accessible even after cancellation.
          </div>
        </details>

        <!-- FAQ ITEM -->
        <details class="group bg-white border-2 border-teal-200 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300">
          <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900 list-none">
            <span>Do you offer refunds?</span>
            <div class="w-8 h-8 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0 ml-4 group-open:bg-teal-500 transition-colors">
              <ChevronDown :size="20" class="text-teal-600 group-open:text-white group-open:rotate-180 transition-transform" />
            </div>
          </summary>
          <div class="mt-4 text-gray-600 leading-relaxed border-t border-gray-100 pt-4">
            Yes — all Premium plans come with a 30‑day money‑back guarantee. 
            If you're not satisfied for any reason, we'll refund you with no questions asked.
          </div>
        </details>

        <!-- FAQ ITEM -->
        <details class="group bg-white border-2 border-teal-200 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300">
          <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900 list-none">
            <span>What types of items can I track?</span>
            <div class="w-8 h-8 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0 ml-4 group-open:bg-teal-500 transition-colors">
              <ChevronDown :size="20" class="text-teal-600 group-open:text-white group-open:rotate-180 transition-transform" />
            </div>
          </summary>
          <div class="mt-4 text-gray-600 leading-relaxed border-t border-gray-100 pt-4">
            Anything with an expiration date — IDs, passports, warranties, subscriptions, insurance policies, 
            contracts, certifications, licenses, memberships, and more. If it expires, you can track it.
          </div>
        </details>

        <!-- FAQ ITEM -->
        <details class="group bg-white border-2 border-teal-200 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300">
          <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900 list-none">
            <span>Can I share items with family members?</span>
            <div class="w-8 h-8 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0 ml-4 group-open:bg-teal-500 transition-colors">
              <ChevronDown :size="20" class="text-teal-600 group-open:text-white group-open:rotate-180 transition-transform" />
            </div>
          </summary>
          <div class="mt-4 text-gray-600 leading-relaxed border-t border-gray-100 pt-4">
            Yes! Premium users can share documents and reminders with family members. 
            Perfect for managing household documents, kids' school forms, or family insurance policies.
          </div>
        </details>

        <!-- FAQ ITEM -->
        <details class="group bg-white border-2 border-teal-200 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300">
          <summary class="flex justify-between items-center cursor-pointer text-lg font-semibold text-gray-900 list-none">
            <span>Do you have a mobile app?</span>
            <div class="w-8 h-8 rounded-full bg-teal-100 flex items-center justify-center flex-shrink-0 ml-4 group-open:bg-teal-500 transition-colors">
              <ChevronDown :size="20" class="text-teal-600 group-open:text-white group-open:rotate-180 transition-transform" />
            </div>
          </summary>
          <div class="mt-4 text-gray-600 leading-relaxed border-t border-gray-100 pt-4">
            Our web app is fully responsive and works great on mobile browsers. 
            Native iOS and Android apps are coming in Q2 2026. Join our waitlist to be notified!
          </div>
        </details>

      </div>

    </div>

    <!-- Still have a question? -->
    <div class="max-w-screen-md mx-auto px-6 text-center mt-16 relative z-10">

      <div class="p-12 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-3xl shadow-2xl text-white">
        <Mail :size="48" class="mx-auto mb-6 opacity-90" />
        
        <h3 class="text-3xl font-bold mb-4">
          Still have a question?
        </h3>

        <p class="text-lg text-white/90 mb-10">
          We're here to help. If you didn't find the answer you were looking for, 
          reach out and we'll get back to you as soon as possible.
        </p>

        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <RouterLink
            to="/contact"
            class="group px-10 py-4 bg-white text-teal-600 rounded-full text-lg font-semibold shadow-xl hover:shadow-2xl hover:scale-105 transition-all duration-300 flex items-center gap-2"
          >
            Contact Support
            <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
          </RouterLink>

          <a
            href="mailto:support@lifeadmin.com"
            class="px-10 py-4 bg-white/10 backdrop-blur-sm border-2 border-white/30 text-white rounded-full text-lg font-medium hover:bg-white/20 transition-all duration-300"
          >
            support@lifeadmin.com
          </a>
        </div>

        <p class="text-sm text-white/70 mt-8">
          Average response time: <span class="text-white font-semibold">under 24 hours</span>
        </p>
      </div>

    </div>
  </section>
</template>
