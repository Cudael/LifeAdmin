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
  <div class="min-h-screen flex flex-col bg-slate-950 text-slate-300 subpixel-antialiased selection:bg-teal-500/30 selection:text-teal-200 relative overflow-hidden font-sans">
    
    <!-- Premium UI: Fixed subtle grain/noise overlay for a tactile, expensive feel -->
    <div class="fixed inset-0 opacity-[0.025] pointer-events-none mix-blend-overlay z-[100]" style="background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.8%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E');"></div>
    
    <!-- Deep, cinematic background lighting -->
    <div class="absolute top-[-10%] left-1/2 -translate-x-1/2 w-full max-w-[1000px] h-[800px] bg-[radial-gradient(ellipse_at_top,rgba(20,184,166,0.15),transparent_70%)] pointer-events-none z-0"></div>
    <div class="absolute bottom-0 right-[-10%] w-3/4 h-[800px] bg-[radial-gradient(ellipse_at_bottom_right,rgba(6,182,212,0.1),transparent_70%)] pointer-events-none z-0"></div>

    <AppHeader class="relative z-50" />

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