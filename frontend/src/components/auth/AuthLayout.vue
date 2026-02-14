<template>
  <div class="relative min-h-screen flex items-center justify-center px-4 overflow-hidden bg-gradient-to-br from-gray-50 via-teal-50/30 to-cyan-50/30">
    
    <!-- Decorative background elements -->
    <div class="absolute inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-20 left-10 w-72 h-72 bg-teal-200 rounded-full opacity-20 blur-3xl animate-pulse-slow"></div>
      <div class="absolute bottom-20 right-10 w-96 h-96 bg-cyan-200 rounded-full opacity-20 blur-3xl animate-pulse-slower"></div>
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-blue-200 rounded-full opacity-10 blur-3xl"></div>
    </div>

    <!-- Content Card -->
    <div class="relative z-10 w-full max-w-md">
      
      <!-- Logo/Brand -->
      <div class="text-center mb-8 animate-fade-in-down">
        <RouterLink to="/" class="inline-block">
          <div class="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl flex items-center justify-center shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110">
            <Lock :size="32" class="text-white" />
          </div>
          <h1 class="text-2xl font-bold bg-gradient-to-r from-teal-600 to-cyan-600 bg-clip-text text-transparent">
            LifeAdmin
          </h1>
        </RouterLink>
      </div>

      <!-- Main Card -->
      <div class="bg-white/80 backdrop-blur-xl p-8 md:p-10 rounded-3xl shadow-2xl border-2 border-white/50 animate-fade-in-up">
        
        <!-- Title -->
        <div class="text-center mb-8">
          <h2 class="text-3xl font-bold text-gray-900 mb-2">{{ title }}</h2>
          <p class="text-gray-600">{{ subtitle }}</p>
        </div>

        <!-- Slot for content -->
        <slot></slot>

      </div>

      <!-- Back to Home -->
      <div v-if="showBackToHome" class="text-center mt-6 animate-fade-in-up animation-delay-200">
        <RouterLink
          to="/"
          class="inline-flex items-center gap-2 text-gray-600 hover:text-gray-900 transition-colors group"
        >
          <ArrowLeft :size="16" class="group-hover:-translate-x-1 transition-transform" />
          Back to home
        </RouterLink>
      </div>

    </div>
  </div>
</template>

<script setup>
import { Lock, ArrowLeft } from "lucide-vue-next"

defineProps({
  title: {
    type: String,
    required: true
  },
  subtitle: {
    type: String,
    default: ""
  },
  showBackToHome: {
    type: Boolean,
    default: true
  }
})
</script>

<style scoped>
@keyframes fade-in-down {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse-slow {
  0%, 100% {
    opacity: 0.2;
  }
  50% {
    opacity: 0.3;
  }
}

@keyframes pulse-slower {
  0%, 100% {
    opacity: 0.2;
  }
  50% {
    opacity: 0.25;
  }
}

.animate-fade-in-down {
  animation: fade-in-down 0.6s ease-out;
}

.animate-fade-in-up {
  animation: fade-in-up 0.6s ease-out;
}

.animation-delay-200 {
  animation-delay: 0.2s;
  opacity: 0;
  animation-fill-mode: forwards;
}

.animate-pulse-slow {
  animation: pulse-slow 4s ease-in-out infinite;
}

.animate-pulse-slower {
  animation: pulse-slower 6s ease-in-out infinite;
}
</style>
