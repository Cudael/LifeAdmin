<template>
  <!-- Deep slate background with a very crisp, subtle top border to separate from the CTA section -->
  <footer class="relative bg-slate-950 pt-20 pb-10 border-t border-white/5 overflow-hidden z-10">
    
    <!-- Ambient background glow anchoring the bottom of the page -->
    <div class="absolute bottom-0 left-1/2 -translate-x-1/2 w-full max-w-3xl h-[300px] bg-teal-500/5 blur-[120px] rounded-full pointer-events-none z-0"></div>

    <div class="relative z-10 max-w-7xl mx-auto px-6">
      
      <!-- Top Grid: Brand & Links -->
      <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-10 lg:gap-12 mb-16">
        
        <!-- Brand Column (Takes up 2 columns on large screens) -->
        <div class="col-span-2 lg:col-span-2 space-y-6 pr-0 lg:pr-8">
          <RouterLink to="/" class="flex items-center gap-3 group inline-flex">
            <div class="w-8 h-8 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-lg flex items-center justify-center shadow-[0_0_15px_rgba(45,212,191,0.2)]">
              <Sparkles :size="16" class="text-slate-950" />
            </div>
            <span class="text-xl font-extrabold text-white tracking-tight">
              Life<span class="text-slate-500">Admin</span>
            </span>
          </RouterLink>
          
          <p class="text-slate-400 text-sm leading-relaxed max-w-sm">
            The intelligent vault that monitors your documents, tracks your subscriptions, and eliminates missed deadlines effortlessly.
          </p>
          
          <!-- Glassmorphic Social Links -->
          <div class="flex items-center gap-3 pt-2">
            <a href="https://twitter.com" target="_blank" class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-slate-400 hover:text-teal-400 hover:bg-white/10 hover:border-teal-500/30 transition-all duration-300">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/>
              </svg>
            </a>
            <a href="https://github.com" target="_blank" class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-slate-400 hover:text-teal-400 hover:bg-white/10 hover:border-teal-500/30 transition-all duration-300">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.17 6.839 9.49.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.463-1.11-1.463-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.167 22 16.418 22 12c0-5.523-4.477-10-10-10z"/>
              </svg>
            </a>
            <a href="https://linkedin.com" target="_blank" class="w-10 h-10 rounded-full bg-white/5 border border-white/10 flex items-center justify-center text-slate-400 hover:text-teal-400 hover:bg-white/10 hover:border-teal-500/30 transition-all duration-300">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
              </svg>
            </a>
          </div>
        </div>

        <!-- Product Links -->
        <div>
          <h3 class="text-sm font-bold text-slate-100 uppercase tracking-wider mb-5">Product</h3>
          <ul class="space-y-3">
            <li><a href="/#features" class="footer-link">Features</a></li>
            <li><a href="/#pricing" class="footer-link">Pricing</a></li>
            <li><RouterLink to="/security" class="footer-link">Security</RouterLink></li>
            <li><RouterLink to="/changelog" class="footer-link">Changelog</RouterLink></li>
          </ul>
        </div>

        <!-- Resources Links -->
        <div>
          <h3 class="text-sm font-bold text-slate-100 uppercase tracking-wider mb-5">Resources</h3>
          <ul class="space-y-3">
            <li><a href="/#faq" class="footer-link">FAQ</a></li>
            <li><RouterLink to="/help" class="footer-link">Help Center</RouterLink></li>
            <li><RouterLink to="/guides" class="footer-link">User Guides</RouterLink></li>
            <li><RouterLink to="/community" class="footer-link">Community</RouterLink></li>
          </ul>
        </div>

        <!-- Company Links -->
        <div>
          <h3 class="text-sm font-bold text-slate-100 uppercase tracking-wider mb-5">Company</h3>
          <ul class="space-y-3">
            <li><RouterLink to="/about" class="footer-link">About Us</RouterLink></li>
            <li><RouterLink to="/blog" class="footer-link">Blog</RouterLink></li>
            <li><RouterLink to="/careers" class="footer-link">Careers</RouterLink></li>
            <li><RouterLink to="/contact" class="footer-link">Contact</RouterLink></li>
          </ul>
        </div>

        <!-- Legal Links -->
        <div>
          <h3 class="text-sm font-bold text-slate-100 uppercase tracking-wider mb-5">Legal</h3>
          <ul class="space-y-3">
            <li><RouterLink to="/privacy" class="footer-link">Privacy Policy</RouterLink></li>
            <li><RouterLink to="/terms" class="footer-link">Terms of Service</RouterLink></li>
            <li><RouterLink to="/cookies" class="footer-link">Cookie Policy</RouterLink></li>
          </ul>
        </div>

      </div>

      <!-- Divider -->
      <div class="border-t border-white/10 mb-8"></div>

      <!-- Bottom Bar -->
      <div class="flex flex-col md:flex-row items-center justify-between gap-6">
        
        <div class="flex items-center gap-6">
          <p class="text-slate-500 text-sm">
            &copy; {{ currentYear }} LifeAdmin. All rights reserved.
          </p>

          <!-- System Status Indicator (High-end SaaS signal) -->
          <a href="/status" class="hidden sm:flex items-center gap-2 text-sm text-slate-400 hover:text-slate-300 transition-colors px-3 py-1 rounded-full bg-white/5 border border-white/5">
            <span class="relative flex h-2 w-2">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
            </span>
            All systems operational
          </a>
        </div>

        <!-- Sleek Custom Language Selector -->
        <div class="relative group">
          <div class="flex items-center gap-2 text-slate-400 bg-slate-900 border border-white/10 rounded-lg px-3 py-1.5 hover:border-white/20 transition-colors cursor-pointer">
            <Globe :size="16" />
            <select class="bg-transparent text-sm text-slate-300 focus:outline-none appearance-none pr-6 cursor-pointer w-24">
              <option value="en">English</option>
              <option value="de">Deutsch</option>
              <option value="es">Español</option>
              <option value="fr">Français</option>
            </select>
            <ChevronDown :size="14" class="absolute right-3 pointer-events-none text-slate-500 group-hover:text-slate-300 transition-colors" />
          </div>
        </div>

      </div>

    </div>

    <!-- Back to Top Button (Sleek Glassmorphic styling) -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 translate-y-4"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-300 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 translate-y-4"
    >
      <button
        v-if="showBackToTop"
        @click="scrollToTop"
        class="fixed bottom-8 right-8 w-12 h-12 bg-slate-800/80 backdrop-blur-md border border-white/10 rounded-full flex items-center justify-center shadow-2xl hover:border-teal-500/50 hover:bg-slate-800 text-slate-400 hover:text-teal-400 transition-all duration-300 hover:-translate-y-1 z-50 group"
        aria-label="Back to top"
      >
        <ArrowUp :size="20" class="group-hover:animate-bounce" />
      </button>
    </Transition>

  </footer>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue"
import {
  Sparkles,
  Globe,
  ArrowUp,
  ChevronDown
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
  @apply text-sm text-slate-400 hover:text-teal-400 transition-colors duration-200;
}

/* Hide default select arrow in IE/Edge/Firefox */
select::-ms-expand {
  display: none;
}
</style>