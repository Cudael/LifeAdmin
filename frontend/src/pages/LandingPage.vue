<script setup>
import { computed, ref, onMounted } from "vue"
import AppHeader from "../components/layout/AppHeader.vue"
import AppFooter from "../components/layout/AppFooter.vue"
import { accessToken } from "../utils/auth"
import { 
  ArrowRight, 
  CheckCircle2, 
  Shield, 
  Cloud, 
  Lock,
  Bell,
  FileText,
  Calendar,
  Sparkles,
  Zap,
  Users,
  TrendingUp,
  Award,
  Star,
  MessageCircle,
  Mail,
  Briefcase,
  Home,
  AlertCircle,
  DollarSign,
  FolderOpen
} from "lucide-vue-next"

const isLoggedIn = computed(() => !!accessToken.value)

// Stats counter animation
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
  <div class="bg-white text-gray-800 min-h-screen flex flex-col">

    <AppHeader />

    <main class="flex-1">

      <!-- HERO -->
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

      <!-- HOW IT WORKS -->
      <section class="py-28 bg-white relative overflow-hidden">
        
        <!-- Decorative background -->
        <div class="absolute inset-0 bg-gradient-to-b from-teal-50/30 to-transparent"></div>

        <div class="max-w-screen-xl mx-auto px-6 text-center relative z-10">

          <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
            <Zap :size="16" />
            Simple Process
          </div>

          <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
            How It Works
          </h2>
          <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-6"></div>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto mb-16">
            A simple, powerful workflow that keeps your life organized without effort.
          </p>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="group relative p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              
              <!-- Step number badge -->
              <div class="absolute -top-4 -right-4 w-12 h-12 bg-gradient-to-br from-teal-400 to-cyan-400 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg">
                1
              </div>

              <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <FileText :size="32" class="text-teal-600" />
              </div>
              
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Add Your Items</h3>
              <p class="text-gray-600 leading-relaxed">Upload documents, add subscriptions, or enter expiry dates manually in seconds.</p>
            </div>

            <div class="group relative p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2 md:mt-8">
              
              <!-- Step number badge -->
              <div class="absolute -top-4 -right-4 w-12 h-12 bg-gradient-to-br from-teal-400 to-cyan-400 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg">
                2
              </div>

              <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Zap :size="32" class="text-teal-600" />
              </div>
              
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">We Track Everything</h3>
              <p class="text-gray-600 leading-relaxed">Our system monitors renewals, deadlines, and important dates 24/7.</p>
            </div>

            <div class="group relative p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              
              <!-- Step number badge -->
              <div class="absolute -top-4 -right-4 w-12 h-12 bg-gradient-to-br from-teal-400 to-cyan-400 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg">
                3
              </div>

              <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Bell :size="32" class="text-teal-600" />
              </div>
              
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Get Smart Reminders</h3>
              <p class="text-gray-600 leading-relaxed">Receive notifications weeks before something expires — never miss a thing.</p>
            </div>

          </div>

        </div>
      </section>

      <!-- WHO IT'S FOR -->
      <section class="py-28 bg-gradient-to-b from-white to-[#f7fdfc] relative overflow-hidden">
        
        <!-- Decorative shapes -->
        <div class="absolute top-20 right-10 w-72 h-72 bg-teal-100 rounded-full opacity-20 blur-3xl"></div>
        <div class="absolute bottom-20 left-10 w-96 h-96 bg-cyan-100 rounded-full opacity-20 blur-3xl"></div>

        <div class="max-w-screen-xl mx-auto px-6 text-center relative z-10">

          <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
            <Users :size="16" />
            For Everyone
          </div>

          <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
            Who It's For
          </h2>
          <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-6"></div>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto mb-16">
            LifeAdmin is built for anyone who wants clarity, control, and peace of mind.
          </p>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Briefcase :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 text-teal-600">Busy Professionals</h3>
              <p class="text-gray-600 leading-relaxed">Keep track of IDs, insurance, certifications, and work documents without the stress.</p>
            </div>

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Home :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 text-teal-600">Families</h3>
              <p class="text-gray-600 leading-relaxed">Manage passports, warranties, medical documents, and school deadlines all in one place.</p>
            </div>

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Award :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 text-teal-600">Small Business Owners</h3>
              <p class="text-gray-600 leading-relaxed">Track licenses, contracts, receipts, and compliance documents effortlessly.</p>
            </div>

          </div>

        </div>
      </section>

      <!-- WHY THIS MATTERS -->
      <section class="py-28 bg-gradient-to-b from-[#f7fdfc] to-white relative overflow-hidden">
        
        <!-- Decorative gradient -->
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(20,184,166,0.05),transparent_70%)]"></div>

        <div class="max-w-screen-lg mx-auto px-6 text-center relative z-10">

          <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
            <TrendingUp :size="16" />
            The Problem
          </div>

          <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-6">
            Why It Matters
          </h2>
          <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-8"></div>

          <p class="text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed mb-12">
            Life admin sneaks up on everyone — expired IDs, forgotten subscriptions, missing documents.
            We built this tool to bring <span class="text-teal-600 font-semibold">calm to the chaos</span> and help you stay on top of the things that matter.
          </p>

          <!-- Problem cards -->
          <div class="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <div class="p-6 bg-white rounded-2xl border border-red-200 shadow-sm hover:shadow-md transition-shadow">
              <div class="w-12 h-12 mx-auto mb-3 bg-red-100 rounded-xl flex items-center justify-center">
                <AlertCircle :size="24" class="text-red-600" />
              </div>
              <p class="text-gray-700 font-medium">Missing renewal deadlines</p>
            </div>

            <div class="p-6 bg-white rounded-2xl border border-orange-200 shadow-sm hover:shadow-md transition-shadow">
              <div class="w-12 h-12 mx-auto mb-3 bg-orange-100 rounded-xl flex items-center justify-center">
                <DollarSign :size="24" class="text-orange-600" />
              </div>
              <p class="text-gray-700 font-medium">Paying fines for late renewals</p>
            </div>

            <div class="p-6 bg-white rounded-2xl border border-yellow-200 shadow-sm hover:shadow-md transition-shadow">
              <div class="w-12 h-12 mx-auto mb-3 bg-yellow-100 rounded-xl flex items-center justify-center">
                <FolderOpen :size="24" class="text-yellow-600" />
              </div>
              <p class="text-gray-700 font-medium">Lost or disorganized documents</p>
            </div>
          </div>

        </div>
      </section>

      <!-- SECURITY & TRUST -->
      <section class="py-28 bg-white relative overflow-hidden">
        
        <!-- Decorative shapes -->
        <div class="absolute top-10 left-10 w-64 h-64 bg-teal-100 rounded-full opacity-20 blur-3xl"></div>
        <div class="absolute bottom-10 right-10 w-80 h-80 bg-cyan-100 rounded-full opacity-20 blur-3xl"></div>

        <div class="max-w-screen-xl mx-auto px-6 relative z-10">

          <div class="text-center mb-16">
            <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
              <Shield :size="16" />
              Security First
            </div>

            <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
              Security & Trust
            </h2>
            <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-6"></div>
            <p class="text-lg text-gray-600 max-w-2xl mx-auto">
              Your privacy and security are our top priorities. We use industry-leading practices to keep your data safe.
            </p>
          </div>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Lock :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Bank‑Level Encryption</h3>
              <p class="text-gray-600 leading-relaxed">Your documents and data are encrypted at rest and in transit using AES-256 encryption.</p>
            </div>

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Shield :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Privacy First</h3>
              <p class="text-gray-600 leading-relaxed">We never sell your data. Your information stays yours, always.</p>
            </div>

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mx-auto mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Cloud :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Secure Cloud Storage</h3>
              <p class="text-gray-600 leading-relaxed">Your files are stored safely with industry‑leading infrastructure and automatic backups.</p>
            </div>

          </div>

          <!-- Trust badges -->
          <div class="mt-16 flex flex-wrap justify-center items-center gap-8 text-gray-400 text-sm">
            <div class="flex items-center gap-2">
              <CheckCircle2 :size="20" class="text-teal-500" />
              <span>GDPR Compliant</span>
            </div>
            <div class="flex items-center gap-2">
              <CheckCircle2 :size="20" class="text-teal-500" />
              <span>ISO 27001 Certified</span>
            </div>
            <div class="flex items-center gap-2">
              <CheckCircle2 :size="20" class="text-teal-500" />
              <span>SOC 2 Type II</span>
            </div>
          </div>

        </div>
      </section>

      <!-- FEATURES -->
      <section id="features" class="py-28 bg-gradient-to-b from-white to-[#f7fdfc] relative overflow-hidden">
        
        <!-- Decorative gradient -->
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,rgba(20,184,166,0.05),transparent_50%)]"></div>

        <div class="max-w-screen-xl mx-auto px-6 relative z-10">

          <div class="text-center mb-20">
            <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
              <Sparkles :size="16" />
              Powerful Features
            </div>

            <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
              Everything You Need
            </h2>
            <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-6"></div>
            <p class="text-lg text-gray-600 max-w-2xl mx-auto">
              A complete toolkit to manage every aspect of your life admin, all in one beautiful dashboard.
            </p>
          </div>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Calendar :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Expiration Tracking</h3>
              <p class="text-gray-600 leading-relaxed">Never miss a renewal again — passports, IDs, insurance, subscriptions, and more.</p>
            </div>

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Bell :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Smart Reminders</h3>
              <p class="text-gray-600 leading-relaxed">Get notified weeks before something expires. Customize reminder timing to your needs.</p>
            </div>

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <FileText :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Document Storage</h3>
              <p class="text-gray-600 leading-relaxed">Upload PDFs, receipts, warranties, and keep them safe and organized in one place.</p>
            </div>

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <TrendingUp :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Advanced Analytics</h3>
              <p class="text-gray-600 leading-relaxed">See patterns, track spending on subscriptions, and get insights into your renewals.</p>
            </div>

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Users :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Family Sharing</h3>
              <p class="text-gray-600 leading-relaxed">Share documents and reminders with family members. Perfect for household management.</p>
            </div>

            <div class="group p-10 bg-white rounded-3xl border-2 border-teal-200 shadow-lg hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <div class="w-16 h-16 mb-6 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-2xl flex items-center justify-center group-hover:scale-110 transition-transform">
                <Zap :size="32" class="text-teal-600" />
              </div>
              <h3 class="text-2xl font-semibold mb-3 group-hover:text-teal-600 transition-colors">Quick Actions</h3>
              <p class="text-gray-600 leading-relaxed">Bulk operations, smart filters, and shortcuts to manage hundreds of items effortlessly.</p>
            </div>

          </div>

        </div>
      </section>

      <!-- TESTIMONIALS -->
      <section class="py-28 bg-gradient-to-b from-[#f7fdfc] to-white relative overflow-hidden">
        
        <!-- Decorative shapes -->
        <div class="absolute top-20 right-20 w-72 h-72 bg-cyan-100 rounded-full opacity-20 blur-3xl"></div>
        <div class="absolute bottom-20 left-20 w-64 h-64 bg-teal-100 rounded-full opacity-20 blur-3xl"></div>

        <div class="max-w-screen-xl mx-auto px-6 text-center relative z-10">

          <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
            <MessageCircle :size="16" />
            Reviews
          </div>

          <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
            What People Say
          </h2>
          <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-16"></div>

          <div class="grid md:grid-cols-3 gap-12">

            <div class="group p-8 bg-white rounded-3xl shadow-lg border-2 border-teal-200 hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <!-- Star rating -->
              <div class="flex justify-center gap-1 mb-4">
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
              </div>
              <p class="text-gray-700 mb-6 leading-relaxed italic">"I used to forget renewals constantly. Now everything is handled automatically. This app is a lifesaver!"</p>
              <div class="flex items-center justify-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center text-white font-bold text-lg">
                  A
                </div>
                <div class="text-left">
                  <div class="font-semibold text-gray-900">Anna K.</div>
                  <div class="text-sm text-gray-500">Marketing Manager</div>
                </div>
              </div>
            </div>

            <div class="group p-8 bg-white rounded-3xl shadow-lg border-2 border-teal-200 hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <!-- Star rating -->
              <div class="flex justify-center gap-1 mb-4">
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
              </div>
              <p class="text-gray-700 mb-6 leading-relaxed italic">"The reminders saved me from a €300 fine. Worth it instantly. Best investment I made this year."</p>
              <div class="flex items-center justify-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center text-white font-bold text-lg">
                  M
                </div>
                <div class="text-left">
                  <div class="font-semibold text-gray-900">Markus L.</div>
                  <div class="text-sm text-gray-500">Freelance Designer</div>
                </div>
              </div>
            </div>

            <div class="group p-8 bg-white rounded-3xl shadow-lg border-2 border-teal-200 hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
              <!-- Star rating -->
              <div class="flex justify-center gap-1 mb-4">
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                <Star :size="20" class="fill-yellow-400 text-yellow-400" />
              </div>
              <p class="text-gray-700 mb-6 leading-relaxed italic">"Clean, simple, and surprisingly powerful. I use it every week to stay organized. Highly recommended!"</p>
              <div class="flex items-center justify-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center text-white font-bold text-lg">
                  S
                </div>
                <div class="text-left">
                  <div class="font-semibold text-gray-900">Sofia R.</div>
                  <div class="text-sm text-gray-500">Small Business Owner</div>
                </div>
              </div>
            </div>

          </div>

          <!-- Overall rating -->
          <div class="mt-16 p-8 bg-gradient-to-r from-teal-50 to-cyan-50 rounded-3xl border border-teal-200">
            <div class="flex flex-col md:flex-row items-center justify-center gap-6">
              <div class="text-center md:text-left">
                <div class="text-5xl font-bold text-teal-600 mb-2">4.9/5</div>
                <div class="flex gap-1 justify-center md:justify-start mb-2">
                  <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                  <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                  <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                  <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                  <Star :size="20" class="fill-yellow-400 text-yellow-400" />
                </div>
                <p class="text-gray-600">Based on 500+ reviews</p>
              </div>
              <div class="hidden md:block w-px h-16 bg-teal-300"></div>
              <div class="text-center">
                <p class="text-gray-700 text-lg font-medium">Trusted by thousands of users worldwide</p>
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- PRICING -->
      <section id="pricing" class="py-32 bg-gradient-to-b from-white to-[#f7fdfc] relative overflow-hidden">
        
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

          <p class="text-lg text-gray-600 max-w-2xl mx-auto mb-20">
            Simple, transparent pricing. No hidden fees. Cancel anytime.
          </p>

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

          <!-- WHY PREMIUM -->
          <div class="mt-24 max-w-3xl mx-auto text-center">
            <h3 class="text-4xl font-bold text-gray-900 mb-6">Why Go Premium?</h3>
            <p class="text-lg text-gray-600 leading-relaxed mb-10">
              Premium gives you unlimited tracking, faster reminders, and powerful insights that help you stay ahead of every deadline. 
              If you rely on LifeAdmin to manage important documents, subscriptions, or IDs — Premium pays for itself instantly.
            </p>

            <div class="grid md:grid-cols-3 gap-10">

              <div class="group p-6 bg-white rounded-2xl border-2 border-teal-200 shadow-lg hover:shadow-xl hover:border-teal-400 transition-all duration-300">
                <div class="w-14 h-14 mx-auto mb-4 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform">
                  <Zap :size="28" class="text-teal-600" />
                </div>
                <p class="font-semibold text-gray-900 mb-2 text-lg">Faster Reminders</p>
                <p class="text-gray-600 text-sm">Get notified earlier so you never miss a renewal.</p>
              </div>

              <div class="group p-6 bg-white rounded-2xl border-2 border-teal-200 shadow-lg hover:shadow-xl hover:border-teal-400 transition-all duration-300">
                <div class="w-14 h-14 mx-auto mb-4 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform">
                  <TrendingUp :size="28" class="text-teal-600" />
                </div>
                <p class="font-semibold text-gray-900 mb-2 text-lg">Advanced Insights</p>
                <p class="text-gray-600 text-sm">See patterns, upcoming renewals, and risk areas.</p>
              </div>

              <div class="group p-6 bg-white rounded-2xl border-2 border-teal-200 shadow-lg hover:shadow-xl hover:border-teal-400 transition-all duration-300">
                <div class="w-14 h-14 mx-auto mb-4 bg-gradient-to-br from-teal-100 to-cyan-100 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform">
                  <CheckCircle2 :size="28" class="text-teal-600" />
                </div>
                <p class="font-semibold text-gray-900 mb-2 text-lg">Unlimited Everything</p>
                <p class="text-gray-600 text-sm">No limits on items, uploads, or reminders.</p>
              </div>

            </div>
          </div>

        </div>
      </section>

      <!-- FAQ -->
      <section id="faq" class="py-32 bg-gradient-to-b from-[#f7fdfc] to-white relative overflow-hidden">
        
        <!-- Decorative shapes -->
        <div class="absolute top-10 left-10 w-96 h-96 bg-teal-100 rounded-full opacity-10 blur-3xl"></div>
        <div class="absolute bottom-10 right-10 w-80 h-80 bg-cyan-100 rounded-full opacity-10 blur-3xl"></div>

        <div class="max-w-screen-xl mx-auto px-6 relative z-10">

          <!-- Label -->
          <div class="text-center mb-16">
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
                  <span class="text-teal-600 text-2xl group-open:text-white group-open:rotate-180 transition-transform">⌄</span>
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
                  <span class="text-teal-600 text-2xl group-open:text-white group-open:rotate-180 transition-transform">⌄</span>
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
                  <span class="text-teal-600 text-2xl group-open:text-white group-open:rotate-180 transition-transform">⌄</span>
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
                  <span class="text-teal-600 text-2xl group-open:text-white group-open:rotate-180 transition-transform">⌄</span>
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
                  <span class="text-teal-600 text-2xl group-open:text-white group-open:rotate-180 transition-transform">⌄</span>
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
                  <span class="text-teal-600 text-2xl group-open:text-white group-open:rotate-180 transition-transform">⌄</span>
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
                  <span class="text-teal-600 text-2xl group-open:text-white group-open:rotate-180 transition-transform">⌄</span>
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
                  <span class="text-teal-600 text-2xl group-open:text-white group-open:rotate-180 transition-transform">⌄</span>
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
        <div class="max-w-screen-md mx-auto px-6 text-center mt-24 relative z-10">

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

            <p class="text-sm text-white/70 mt-8 flex items-center justify-center gap-2">
              <Clock :size="16" />
              Average response time: <span class="text-white font-semibold">under 24 hours</span>
            </p>
          </div>

        </div>
      </section>

      <!-- FINAL CTA -->
      <section class="py-28 bg-gradient-to-b from-white to-gray-50 relative overflow-hidden">
        
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

    </main>

    <AppFooter />

  </div>
</template>

<style scoped>
/* Custom animations */
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

/* Smooth hover transitions */
.group:hover .group-hover\:scale-110 {
  transform: scale(1.1);
}

.group:hover .group-hover\:translate-x-1 {
  transform: translateX(0.25rem);
}

.group:hover .group-hover\:translate-x-2 {
  transform: translateX(0.5rem);
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(to bottom, #14b8a6, #06b6d4);
  border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(to bottom, #0d9488, #0891b2);
}
</style>