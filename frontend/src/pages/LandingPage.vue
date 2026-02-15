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
  <div class="bg-white text-gray-800 min-h-screen flex flex-col">
    <AppHeader />

    <main class="flex-1">
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

    <AppFooter />
  </div>
</template>
