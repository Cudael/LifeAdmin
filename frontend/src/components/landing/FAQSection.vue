<script setup>
import { MessageCircle, Mail, ArrowRight, ChevronDown } from "lucide-vue-next"
</script>

<template>
  <section id="faq" class="py-24 md:py-32 relative overflow-hidden z-10">
    
    <!-- Ambient glowing backgrounds -->
    <div class="absolute top-1/4 left-0 w-96 h-96 bg-teal-600/10 rounded-full blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-1/4 right-0 w-96 h-96 bg-cyan-600/10 rounded-full blur-[120px] pointer-events-none"></div>

    <div class="max-w-screen-xl mx-auto px-6 relative z-10">

      <!-- Section Header -->
      <div class="text-center mb-16 max-w-2xl mx-auto">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-500/10 border border-teal-500/20 text-teal-400 rounded-full mb-6 text-sm font-semibold tracking-wide">
          <MessageCircle :size="16" class="fill-current/20" />
          Got Questions?
        </div>

        <h2 class="text-4xl md:text-5xl font-extrabold text-slate-50 tracking-tight mb-6">
          Frequently asked <span class="bg-gradient-to-r from-teal-400 to-cyan-400 bg-clip-text text-transparent">questions.</span>
        </h2>
        
        <p class="text-lg text-slate-400">
          Everything you need to know about the product and billing.
        </p>
      </div>

      <!-- FAQ Accordions Container -->
      <div class="max-w-3xl mx-auto space-y-4">

        <!-- FAQ ITEM 1 -->
        <details class="group bg-slate-900/40 backdrop-blur-md border border-white/5 rounded-2xl overflow-hidden shadow-sm hover:border-teal-500/30 transition-colors duration-300">
          <summary class="flex justify-between items-center cursor-pointer p-6 text-lg font-semibold text-slate-100 list-none outline-none select-none">
            <span class="pr-6">How does Remindes remind me about upcoming expirations?</span>
            <div class="w-8 h-8 rounded-full bg-slate-800 border border-white/10 flex items-center justify-center flex-shrink-0 group-open:bg-teal-500/20 group-open:border-teal-500/40 transition-all duration-300">
              <ChevronDown :size="18" class="text-slate-400 group-open:text-teal-400 group-open:rotate-180 transition-transform duration-300" />
            </div>
          </summary>
          <div class="px-6 pb-6 text-slate-400 leading-relaxed text-base">
            Remindes sends you smart reminders days or weeks before something expires. 
            You choose how early you want to be notified via email, push notifications, or both.
          </div>
        </details>

        <!-- FAQ ITEM 2 -->
        <details class="group bg-slate-900/40 backdrop-blur-md border border-white/5 rounded-2xl overflow-hidden shadow-sm hover:border-teal-500/30 transition-colors duration-300">
          <summary class="flex justify-between items-center cursor-pointer p-6 text-lg font-semibold text-slate-100 list-none outline-none select-none">
            <span class="pr-6">Is my data secure?</span>
            <div class="w-8 h-8 rounded-full bg-slate-800 border border-white/10 flex items-center justify-center flex-shrink-0 group-open:bg-teal-500/20 group-open:border-teal-500/40 transition-all duration-300">
              <ChevronDown :size="18" class="text-slate-400 group-open:text-teal-400 group-open:rotate-180 transition-transform duration-300" />
            </div>
          </summary>
          <div class="px-6 pb-6 text-slate-400 leading-relaxed text-base">
            Yes — all your data is encrypted at rest and in transit using bank-level AES-256 encryption. 
            We never sell your information, and you stay in full control of your documents.
          </div>
        </details>

        <!-- FAQ ITEM 3 -->
        <details class="group bg-slate-900/40 backdrop-blur-md border border-white/5 rounded-2xl overflow-hidden shadow-sm hover:border-teal-500/30 transition-colors duration-300">
          <summary class="flex justify-between items-center cursor-pointer p-6 text-lg font-semibold text-slate-100 list-none outline-none select-none">
            <span class="pr-6">What's included in the free plan?</span>
            <div class="w-8 h-8 rounded-full bg-slate-800 border border-white/10 flex items-center justify-center flex-shrink-0 group-open:bg-teal-500/20 group-open:border-teal-500/40 transition-all duration-300">
              <ChevronDown :size="18" class="text-slate-400 group-open:text-teal-400 group-open:rotate-180 transition-transform duration-300" />
            </div>
          </summary>
          <div class="px-6 pb-6 text-slate-400 leading-relaxed text-base">
            The free plan includes tracking for up to 20 items, smart reminders, and secure document storage up to 100MB.
            It's perfect for getting started and seeing if Remindes is right for you.
          </div>
        </details>

        <!-- FAQ ITEM 4 -->
        <details class="group bg-slate-900/40 backdrop-blur-md border border-white/5 rounded-2xl overflow-hidden shadow-sm hover:border-teal-500/30 transition-colors duration-300">
          <summary class="flex justify-between items-center cursor-pointer p-6 text-lg font-semibold text-slate-100 list-none outline-none select-none">
            <span class="pr-6">Can I cancel my Premium subscription anytime?</span>
            <div class="w-8 h-8 rounded-full bg-slate-800 border border-white/10 flex items-center justify-center flex-shrink-0 group-open:bg-teal-500/20 group-open:border-teal-500/40 transition-all duration-300">
              <ChevronDown :size="18" class="text-slate-400 group-open:text-teal-400 group-open:rotate-180 transition-transform duration-300" />
            </div>
          </summary>
          <div class="px-6 pb-6 text-slate-400 leading-relaxed text-base">
            Absolutely. You can cancel anytime with a single click from your account settings — no hidden steps, no hassle.
            Your data remains accessible even after cancellation.
          </div>
        </details>

        <!-- FAQ ITEM 5 -->
        <details class="group bg-slate-900/40 backdrop-blur-md border border-white/5 rounded-2xl overflow-hidden shadow-sm hover:border-teal-500/30 transition-colors duration-300">
          <summary class="flex justify-between items-center cursor-pointer p-6 text-lg font-semibold text-slate-100 list-none outline-none select-none">
            <span class="pr-6">Do you offer refunds?</span>
            <div class="w-8 h-8 rounded-full bg-slate-800 border border-white/10 flex items-center justify-center flex-shrink-0 group-open:bg-teal-500/20 group-open:border-teal-500/40 transition-all duration-300">
              <ChevronDown :size="18" class="text-slate-400 group-open:text-teal-400 group-open:rotate-180 transition-transform duration-300" />
            </div>
          </summary>
          <div class="px-6 pb-6 text-slate-400 leading-relaxed text-base">
            Yes — all Premium plans come with a 30‑day money‑back guarantee. 
            If you're not satisfied for any reason, we'll refund you with no questions asked.
          </div>
        </details>

        <!-- FAQ ITEM 6 -->
        <details class="group bg-slate-900/40 backdrop-blur-md border border-white/5 rounded-2xl overflow-hidden shadow-sm hover:border-teal-500/30 transition-colors duration-300">
          <summary class="flex justify-between items-center cursor-pointer p-6 text-lg font-semibold text-slate-100 list-none outline-none select-none">
            <span class="pr-6">What types of items can I track?</span>
            <div class="w-8 h-8 rounded-full bg-slate-800 border border-white/10 flex items-center justify-center flex-shrink-0 group-open:bg-teal-500/20 group-open:border-teal-500/40 transition-all duration-300">
              <ChevronDown :size="18" class="text-slate-400 group-open:text-teal-400 group-open:rotate-180 transition-transform duration-300" />
            </div>
          </summary>
          <div class="px-6 pb-6 text-slate-400 leading-relaxed text-base">
            Anything with an expiration date — IDs, passports, warranties, subscriptions, insurance policies, 
            contracts, certifications, licenses, memberships, and more. If it expires, you can track it.
          </div>
        </details>

        <!-- FAQ ITEM 7 -->
        <details class="group bg-slate-900/40 backdrop-blur-md border border-white/5 rounded-2xl overflow-hidden shadow-sm hover:border-teal-500/30 transition-colors duration-300">
          <summary class="flex justify-between items-center cursor-pointer p-6 text-lg font-semibold text-slate-100 list-none outline-none select-none">
            <span class="pr-6">Can I share items with family members?</span>
            <div class="w-8 h-8 rounded-full bg-slate-800 border border-white/10 flex items-center justify-center flex-shrink-0 group-open:bg-teal-500/20 group-open:border-teal-500/40 transition-all duration-300">
              <ChevronDown :size="18" class="text-slate-400 group-open:text-teal-400 group-open:rotate-180 transition-transform duration-300" />
            </div>
          </summary>
          <div class="px-6 pb-6 text-slate-400 leading-relaxed text-base">
            Yes! Premium users can share documents and reminders with family members. 
            Perfect for managing household documents, kids' school forms, or family insurance policies.
          </div>
        </details>

        <!-- FAQ ITEM 8 -->
        <details class="group bg-slate-900/40 backdrop-blur-md border border-white/5 rounded-2xl overflow-hidden shadow-sm hover:border-teal-500/30 transition-colors duration-300">
          <summary class="flex justify-between items-center cursor-pointer p-6 text-lg font-semibold text-slate-100 list-none outline-none select-none">
            <span class="pr-6">Do you have a mobile app?</span>
            <div class="w-8 h-8 rounded-full bg-slate-800 border border-white/10 flex items-center justify-center flex-shrink-0 group-open:bg-teal-500/20 group-open:border-teal-500/40 transition-all duration-300">
              <ChevronDown :size="18" class="text-slate-400 group-open:text-teal-400 group-open:rotate-180 transition-transform duration-300" />
            </div>
          </summary>
          <div class="px-6 pb-6 text-slate-400 leading-relaxed text-base">
            Our web app is fully responsive and works great on mobile browsers. 
            Native iOS and Android apps are currently in development. Join our waitlist to be notified!
          </div>
        </details>

      </div>

    </div>

    <!-- Contact Support Banner -->
    <div class="max-w-4xl mx-auto px-6 mt-24 relative z-10">
      <div class="relative p-10 md:p-14 bg-gradient-to-br from-slate-900 to-slate-950 rounded-[2.5rem] border border-white/10 shadow-2xl overflow-hidden text-center">
        
        <!-- Background Banner Gradients -->
        <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,rgba(45,212,191,0.15),transparent_70%)]"></div>
        <div class="absolute top-0 left-0 w-full h-px bg-gradient-to-r from-transparent via-teal-500/50 to-transparent"></div>

        <div class="relative z-10">
          <div class="w-16 h-16 mx-auto bg-teal-500/10 border border-teal-500/20 rounded-2xl flex items-center justify-center mb-6 text-teal-400 shadow-[0_0_15px_rgba(45,212,191,0.15)]">
            <Mail :size="32" />
          </div>
          
          <h3 class="text-3xl font-bold text-white mb-4 tracking-tight">
            Still have questions?
          </h3>

          <p class="text-lg text-slate-400 mb-10 max-w-xl mx-auto">
            We're here to help. If you didn't find the answer you were looking for, reach out and we'll get back to you as soon as possible.
          </p>

          <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <RouterLink
              to="/contact"
              class="group px-8 py-3.5 bg-white text-slate-900 rounded-full text-lg font-bold shadow-[0_0_20px_rgba(255,255,255,0.1)] hover:bg-slate-200 transition-all duration-300 flex items-center gap-2 w-full sm:w-auto justify-center"
            >
              Contact Support
              <ArrowRight :size="18" class="group-hover:translate-x-1 transition-transform" />
            </RouterLink>

            <a
              href="mailto:support@remindes.com"
              class="px-8 py-3.5 bg-white/5 hover:bg-white/10 border border-white/10 text-white rounded-full text-lg font-medium transition-all duration-300 w-full sm:w-auto justify-center flex"
            >
              support@remindes.com
            </a>
          </div>

          <p class="text-sm text-slate-500 mt-8 font-medium">
            Average response time: <span class="text-teal-400">under 24 hours</span>
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Remove default arrow from <details> tag in Webkit browsers */
details > summary::-webkit-details-marker {
  display: none;
}
</style>