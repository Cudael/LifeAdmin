<script setup>
import { ref, onMounted } from "vue"
import { 
  ArrowRight, 
  Sparkles,
  Lock,
  Calendar,
  Bell
} from "lucide-vue-next"

const stats = ref({
  users: 0,
  documents: 0,
  reminders: 0
})

const animateStats = () => {
  const targets = { users: 500, documents: 5000, reminders: 2500 }
  const duration = 2000
  const steps = 60
  const increment = duration / steps

  let current = { users: 0, documents: 0, reminders: 0 }

  const interval = setInterval(() => {
    current.users += targets.users / steps
    current.documents += targets.documents / steps
    current.reminders += targets.reminders / steps

    stats.value = {
      users: Math.floor(current.users),
      documents: Math.floor(current.documents),
      reminders: Math.floor(current.reminders)
    }

    if (current.users >= targets.users) {
      clearInterval(interval)
      stats.value = targets
    }
  }, increment)
}

onMounted(() => {
  animateStats()
})
</script>

<template>
  <section class="relative min-h-screen flex items-center justify-center overflow-hidden bg-[#0a0c12] text-white">

    <!-- Base dark background -->
    <div class="absolute inset-0 z-0 bg-[#0a0c12]"></div>
    
    <!-- Simplified gradient overlays -->
    <div class="absolute inset-0 z-0 bg-[radial-gradient(circle_at_20%_30%,rgba(20,184,166,0.15),transparent_60%)] animate-pulse-slow"></div>
    <div class="absolute inset-0 z-0 bg-[radial-gradient(circle_at_80%_70%,rgba(6,182,212,0.12),transparent_65%)] animate-pulse-slower"></div>

    <!-- Subtle floating particles -->
    <div class="absolute inset-0 z-0">
      <div class="absolute top-1/4 left-1/4 w-2 h-2 bg-teal-400 rounded-full opacity-15 animate-float"></div>
      <div class="absolute top-1/3 right-1/4 w-2 h-2 bg-cyan-400 rounded-full opacity-20 animate-float-delayed"></div>
      <div class="absolute bottom-1/3 left-1/3 w-2 h-2 bg-blue-400 rounded-full opacity-15 animate-float"></div>
    </div>

    <!-- Content -->
    <div class="relative z-10 max-w-4xl mx-auto px-6 text-center">

      <!-- Animated badge -->
      <div class="inline-flex items-center gap-2 px-4 py-2 bg-white/10 backdrop-blur-md border border-white/20 rounded-full mb-8 animate-fade-in-down">
        <Sparkles :size="16" class="text-teal-400" />
        <span class="text-sm font-medium text-gray-200">Now with AI-powered reminders</span>
        <span class="px-2 py-0.5 bg-teal-400/20 text-teal-300 text-xs font-semibold rounded-full">NEW</span>
      </div>

      <h1 class="text-6xl md:text-7xl font-extrabold leading-tight mb-8 animate-fade-in-up">
        Stay Ahead.<br />
        <span class="bg-gradient-to-r from-teal-400 to-cyan-400 bg-clip-text text-transparent">
          Live With Clarity.
        </span>
      </h1>

      <p class="text-xl text-gray-300 max-w-2xl mx-auto mb-12 animate-fade-in-up animation-delay-200">
        A calm, intelligent dashboard that keeps your documents, subscriptions, and deadlines organized — effortlessly.
      </p>

      <!-- Centered CTA layout -->
      <div class="flex flex-col md:flex-row justify-center items-center gap-6 mb-14 animate-fade-in-up animation-delay-400">

        <RouterLink
          to="/register"
          class="group px-12 py-4 bg-gradient-to-r from-teal-400 to-cyan-400 hover:from-teal-300 hover:to-cyan-300 text-black rounded-full text-xl font-semibold shadow-xl hover:shadow-2xl hover:shadow-teal-500/30 transition-all duration-300 flex items-center gap-2 hover:gap-3"
        >
          Get Started Free
          <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
        </RouterLink>

        <RouterLink
          to="/demo"
          class="group px-12 py-4 bg-white/10 backdrop-blur-md border border-white/20 hover:bg-white/20 text-white rounded-full text-xl font-medium transition-all duration-300 flex items-center gap-2"
        >
          Watch Demo
          <svg class="w-5 h-5 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 20 20">
            <path d="M6.3 2.841A1.5 1.5 0 004 4.11V15.89a1.5 1.5 0 002.3 1.269l9.344-5.89a1.5 1.5 0 000-2.538L6.3 2.84z" />
          </svg>
        </RouterLink>

      </div>

      <!-- Micro-features with icons -->
      <div class="flex flex-wrap justify-center gap-10 text-gray-300 text-sm opacity-90 animate-fade-in-up animation-delay-600">

        <div class="flex items-center gap-2 hover:text-teal-300 transition-colors cursor-pointer">
          <Sparkles :size="18" class="text-teal-300" />
          <span>Beautiful interface</span>
        </div>

        <div class="flex items-center gap-2 hover:text-teal-300 transition-colors cursor-pointer">
          <Lock :size="18" class="text-teal-300" />
          <span>Secure cloud storage</span>
        </div>

        <div class="flex items-center gap-2 hover:text-teal-300 transition-colors cursor-pointer">
          <Calendar :size="18" class="text-teal-300" />
          <span>Smart expiry detection</span>
        </div>

        <div class="flex items-center gap-2 hover:text-teal-300 transition-colors cursor-pointer">
          <Bell :size="18" class="text-teal-300" />
          <span>Custom reminders</span>
        </div>

      </div>

      <!-- Social proof -->
      <div class="mt-16 flex flex-col sm:flex-row items-center justify-center gap-8 text-gray-400 text-sm animate-fade-in-up animation-delay-800">
        <div class="flex flex-col items-center">
          <p class="text-3xl font-bold text-white">{{ stats.users }}+</p>
          <p>Active Users</p>
        </div>
        <div class="hidden sm:block w-px h-12 bg-white/20"></div>
        <div class="flex flex-col items-center">
          <p class="text-3xl font-bold text-white">{{ stats.documents.toLocaleString() }}+</p>
          <p>Documents Tracked</p>
        </div>
        <div class="hidden sm:block w-px h-12 bg-white/20"></div>
        <div class="flex flex-col items-center">
          <p class="text-3xl font-bold text-white">{{ stats.reminders.toLocaleString() }}+</p>
          <p>Reminders Sent</p>
        </div>
      </div>

    </div>

    <!-- Scroll indicator -->
    <div class="absolute bottom-10 left-1/2 -translate-x-1/2 z-10 animate-bounce">
      <div class="w-6 h-10 border-2 border-white/30 rounded-full flex justify-center">
        <div class="w-1 h-3 bg-white/50 rounded-full mt-2 animate-scroll"></div>
      </div>
    </div>
  </section>
</template>

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

@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes pulse-slow {
  0%, 100% {
    opacity: 0.5;
  }
  50% {
    opacity: 0.7;
  }
}

@keyframes pulse-slower {
  0%, 100% {
    opacity: 0.3;
  }
  50% {
    opacity: 0.5;
  }
}

@keyframes scroll {
  0% {
    opacity: 0;
    transform: translateY(0);
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: translateY(12px);
  }
}

.animate-fade-in-down {
  animation: fade-in-down 0.8s ease-out;
}

.animate-fade-in-up {
  animation: fade-in-up 0.8s ease-out;
}

.animation-delay-200 {
  animation-delay: 0.2s;
  opacity: 0;
  animation-fill-mode: forwards;
}

.animation-delay-400 {
  animation-delay: 0.4s;
  opacity: 0;
  animation-fill-mode: forwards;
}

.animation-delay-600 {
  animation-delay: 0.6s;
  opacity: 0;
  animation-fill-mode: forwards;
}

.animation-delay-800 {
  animation-delay: 0.8s;
  opacity: 0;
  animation-fill-mode: forwards;
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-float-delayed {
  animation: float 8s ease-in-out infinite 2s;
}

.animate-pulse-slow {
  animation: pulse-slow 4s ease-in-out infinite;
}

.animate-pulse-slower {
  animation: pulse-slower 6s ease-in-out infinite;
}

.animate-scroll {
  animation: scroll 2s ease-in-out infinite;
}
</style>
