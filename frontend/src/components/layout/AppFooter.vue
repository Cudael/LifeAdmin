<template>
  <footer class="relative bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-white overflow-hidden">
    
    <!-- Decorative background elements -->
    <div class="absolute inset-0 opacity-10">
      <div class="absolute top-10 left-10 w-64 h-64 bg-teal-500 rounded-full blur-3xl"></div>
      <div class="absolute bottom-10 right-10 w-80 h-80 bg-cyan-500 rounded-full blur-3xl"></div>
    </div>

    <!-- Main Footer Content -->
    <div class="relative z-10 max-w-7xl mx-auto px-6 py-16">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12 mb-12">
        
        <!-- Brand Section -->
        <div class="space-y-4">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-xl flex items-center justify-center shadow-lg">
              <Sparkles :size="24" class="text-white" />
            </div>
            <span class="text-2xl font-bold bg-gradient-to-r from-teal-400 to-cyan-400 bg-clip-text text-transparent">
              LifeAdmin
            </span>
          </div>
          <p class="text-gray-400 leading-relaxed">
            The intelligent dashboard that keeps your documents, subscriptions, and deadlines organized — effortlessly.
          </p>
          
          <!-- Social Links -->
          <div class="flex items-center gap-3">
            <a
              href="https://twitter.com"
              target="_blank"
              class="w-10 h-10 rounded-lg bg-white/10 hover:bg-white/20 flex items-center justify-center transition-all duration-200 hover:scale-110"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/>
              </svg>
            </a>
            <a
              href="https://github.com"
              target="_blank"
              class="w-10 h-10 rounded-lg bg-white/10 hover:bg-white/20 flex items-center justify-center transition-all duration-200 hover:scale-110"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.17 6.839 9.49.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.463-1.11-1.463-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.167 22 16.418 22 12c0-5.523-4.477-10-10-10z"/>
              </svg>
            </a>
            <a
              href="https://linkedin.com"
              target="_blank"
              class="w-10 h-10 rounded-lg bg-white/10 hover:bg-white/20 flex items-center justify-center transition-all duration-200 hover:scale-110"
            >
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
              </svg>
            </a>
          </div>
        </div>

        <!-- Product -->
        <div>
          <h3 class="text-lg font-semibold mb-4 flex items-center gap-2">
            <Package :size="20" class="text-teal-400" />
            Product
          </h3>
          <ul class="space-y-3">
            <li>
              <a href="/#features" class="footer-link">Features</a>
            </li>
            <li>
              <a href="/#pricing" class="footer-link">Pricing</a>
            </li>
            <li>
              <a href="/#faq" class="footer-link">FAQ</a>
            </li>
          </ul>
        </div>

        <!-- Company & Support -->
        <div>
          <h3 class="text-lg font-semibold mb-4 flex items-center gap-2">
            <HelpCircle :size="20" class="text-blue-400" />
            Company & Support
          </h3>
          <ul class="space-y-3">
            <li>
              <RouterLink to="/about" class="footer-link">About Us</RouterLink>
            </li>
            <li>
              <RouterLink to="/contact" class="footer-link">Contact Support</RouterLink>
            </li>
            <li>
              <RouterLink to="/privacy" class="footer-link">Privacy Policy</RouterLink>
            </li>
            <li>
              <RouterLink to="/terms" class="footer-link">Terms of Service</RouterLink>
            </li>
            <li>
              <RouterLink to="/cookies" class="footer-link">Cookie Policy</RouterLink>
            </li>
          </ul>
        </div>

      </div>

      <!-- Divider -->
      <div class="border-t border-white/10 mb-8"></div>

      <!-- Bottom Section -->
      <div class="flex flex-col md:flex-row items-center justify-between gap-4 text-gray-400 text-sm">
        <div class="flex items-center gap-2">
          <Copyright :size="16" />
          <span>{{ currentYear }} LifeAdmin. All rights reserved.</span>
        </div>

        <!-- Language Selector -->
        <div class="flex items-center gap-2">
          <Globe :size="16" />
          <select class="bg-white/10 border border-white/20 rounded-lg px-3 py-1 text-sm text-white focus:outline-none focus:ring-2 focus:ring-teal-500">
            <option value="en">English</option>
            <option value="de">Deutsch</option>
            <option value="es">Español</option>
            <option value="fr">Français</option>
          </select>
        </div>
      </div>

    </div>

    <!-- Back to Top Button -->
    <button
      v-if="showBackToTop"
      @click="scrollToTop"
      class="fixed bottom-8 right-8 w-12 h-12 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-full flex items-center justify-center shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-110 z-40"
    >
      <ArrowUp :size="20" class="text-white" />
    </button>

  </footer>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue"
import {
  Sparkles,
  Package,
  HelpCircle,
  Copyright,
  Globe,
  ArrowUp
} from "lucide-vue-next"

const currentYear = computed(() => new Date().getFullYear())
const showBackToTop = ref(false)

// Handle scroll for back-to-top button
function handleScroll() {
  showBackToTop.value = window.scrollY > 500
}

// Scroll to top smoothly
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.footer-link {
  @apply text-gray-400 hover:text-white transition-colors duration-200;
}
</style>