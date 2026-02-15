<script setup>
import { ArrowRight, CheckCircle2 } from "lucide-vue-next"
</script>

<template>
  <section class="py-16 bg-gradient-to-b from-white to-gray-50 relative overflow-hidden">
    
    <!-- Decorative gradient -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(20,184,166,0.1),transparent_70%)]"></div>

    <div class="max-w-screen-lg mx-auto px-6 text-center relative z-10">
      
      <div class="p-16 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-3xl shadow-2xl text-white relative overflow-hidden">
        
        <!-- Decorative elements -->
        <div class="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2"></div>
        <div class="absolute bottom-0 left-0 w-48 h-48 bg-white/10 rounded-full translate-y-1/2 -translate-x-1/2"></div>

        <div class="relative z-10">
          <h2 class="text-4xl md:text-5xl font-extrabold mb-6">
            Ready to Take Control?
          </h2>

          <p class="text-xl text-white/90 max-w-2xl mx-auto mb-10">
            Join thousands of users who never miss a deadline. 
            Start organizing your life today — it's free to get started.
          </p>

          <div class="flex flex-col sm:flex-row gap-6 justify-center items-center">
            <RouterLink
              to="/register"
              class="group px-12 py-5 bg-white text-teal-600 rounded-full text-xl font-bold shadow-2xl hover:shadow-3xl hover:scale-105 transition-all duration-300 flex items-center gap-3"
            >
              Get Started Free
              <ArrowRight :size="24" class="group-hover:translate-x-2 transition-transform" />
            </RouterLink>

            <RouterLink
              to="/login"
              class="px-12 py-5 bg-white/10 backdrop-blur-sm border-2 border-white/30 text-white rounded-full text-xl font-medium hover:bg-white/20 transition-all duration-300"
            >
              Sign In
            </RouterLink>
          </div>

          <p class="text-white/80 mt-8 flex items-center justify-center gap-2 flex-wrap">
            <CheckCircle2 :size="20" />
            <span>No credit card required</span>
            <span class="hidden sm:inline">•</span>
            <span>Cancel anytime</span>
            <span class="hidden sm:inline">•</span>
            <span>Free forever plan available</span>
          </p>
        </div>

      </div>

    </div>
  </section>
</template>
