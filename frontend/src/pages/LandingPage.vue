<script setup>
import AppHeader from "../components/layout/AppHeader.vue"
import AppFooter from "../components/layout/AppFooter.vue"
import HeroSection from "../components/landing/HeroSection.vue"
import HowItWorksSection from "../components/landing/HowItWorksSection.vue"
import WhoItsForSection from "../components/landing/WhoItsForSection.vue"
import WhyItMattersSection from "../components/landing/WhyItMattersSection.vue"
import SecuritySection from "../components/landing/SecuritySection.vue"
import FeaturesSection from "../components/landing/FeaturesSection.vue"
import PricingSection from "../components/landing/PricingSection.vue"
import FAQSection from "../components/landing/FAQSection.vue"
import CTASection from "../components/landing/CTASection.vue"
</script>

<template>
  <!-- 
    Global Dark Theme Wrapper
    - bg-slate-950: Deep, rich dark background
    - text-slate-300: Soft off-white text to prevent eye strain
    - antialiased: Crisper font rendering for dark themes
    - selection: Custom highlight color when users select text
  -->
  <div class="min-h-screen flex flex-col bg-slate-950 text-slate-300 antialiased selection:bg-indigo-500 selection:text-white relative overflow-hidden">
    
    <!-- 
      Modern UI Improvement: Subtle Background Glows 
      These sit fixed in the background to give the page a premium, layered dark-mode feel.
    -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-3xl h-[600px] bg-indigo-600/10 blur-[120px] rounded-full pointer-events-none z-0"></div>
    <div class="absolute bottom-0 right-0 w-3/4 h-[500px] bg-blue-900/10 blur-[150px] rounded-full pointer-events-none z-0"></div>

    <!-- 
      Content needs relative and z-10 so it sits on top of the background glows 
    -->
    <AppHeader class="relative z-10" />

    <main class="flex-1 flex flex-col relative z-10">
      <HeroSection />
      <HowItWorksSection />
      <WhoItsForSection />
      <WhyItMattersSection />
      <SecuritySection />
      <FeaturesSection />
      <PricingSection />
      <FAQSection />
      <CTASection />
    </main>

    <AppFooter class="relative z-10" />
  </div>
</template>