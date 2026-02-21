<template>
  <div class="min-h-screen bg-slate-950 text-slate-300 selection:bg-teal-500/30 selection:text-teal-200 flex flex-col">
    <AppHeader />
    
    <main class="flex-1 relative pt-32 pb-24 lg:pt-40 lg:pb-32 overflow-hidden">
      <!-- Ambient Background Elements -->
      <div class="absolute top-0 left-1/4 w-[800px] h-[500px] bg-teal-500/10 blur-[150px] rounded-full pointer-events-none mix-blend-screen z-0"></div>
      <div class="absolute bottom-0 right-1/4 w-[600px] h-[400px] bg-cyan-500/10 blur-[120px] rounded-full pointer-events-none mix-blend-screen z-0"></div>
      <div class="absolute inset-0 z-0 bg-[linear-gradient(to_right,#80808008_1px,transparent_1px),linear-gradient(to_bottom,#80808008_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none"></div>

      <div class="max-w-7xl mx-auto px-6 relative z-10">
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-start">
          
          <!-- LEFT COLUMN: Copy & Contact Methods -->
          <div class="animate-fade-in-up">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-teal-500/10 border border-teal-500/20 text-teal-400 text-[10px] font-bold uppercase tracking-widest mb-6 shadow-inner">
              <span class="relative flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-teal-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-teal-500"></span>
              </span>
              Support Online
            </div>

            <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white tracking-tight mb-6 leading-tight">
              Let's build your <br />
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-cyan-400">secure future.</span>
            </h1>
            
            <p class="text-lg text-slate-400 leading-relaxed mb-12 max-w-xl font-medium">
              Whether you have a question about security protocols, pricing, or need technical support, our engineering and support teams are ready to help.
            </p>

            <!-- Bento Box Contact Methods -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <!-- Email Card -->
              <div class="p-6 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 hover:border-teal-500/30 transition-colors group">
                <div class="w-12 h-12 rounded-2xl bg-teal-500/10 border border-teal-500/20 flex items-center justify-center text-teal-400 mb-4 group-hover:scale-110 transition-transform shadow-inner">
                  <Mail :size="20" />
                </div>
                <h3 class="text-sm font-bold text-white mb-1">Email Support</h3>
                <a href="mailto:support@remindes.com" class="text-xs font-medium text-slate-400 hover:text-teal-400 transition-colors">
                  support@remindes.com
                </a>
              </div>

              <!-- FAQ Card -->
              <div class="p-6 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 hover:border-cyan-500/30 transition-colors group">
                <div class="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400 mb-4 group-hover:scale-110 transition-transform shadow-inner">
                  <HelpCircle :size="20" />
                </div>
                <h3 class="text-sm font-bold text-white mb-1">Documentation</h3>
                <RouterLink to="/#faq" class="text-xs font-medium text-slate-400 hover:text-cyan-400 transition-colors">
                  Browse the FAQ
                </RouterLink>
              </div>

              <!-- Location Card (Spans full width) -->
              <div class="sm:col-span-2 p-6 bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 flex items-center gap-4 group">
                <div class="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 shrink-0 group-hover:scale-110 transition-transform shadow-inner">
                  <MapPin :size="20" />
                </div>
                <div>
                  <h3 class="text-sm font-bold text-white mb-1">Headquarters</h3>
                  <p class="text-xs font-medium text-slate-400">San Francisco, CA • Response within 24h</p>
                </div>
              </div>
            </div>
          </div>

          <!-- RIGHT COLUMN: Glassmorphic Form -->
          <div class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 shadow-2xl p-8 md:p-10 relative overflow-hidden animate-fade-in-up animation-delay-100">
            
            <!-- Top Edge Glow -->
            <div class="absolute top-0 left-0 right-0 h-px flex justify-center opacity-50">
              <div class="h-full w-1/2 bg-gradient-to-r from-transparent via-teal-400 to-transparent"></div>
            </div>

            <form @submit.prevent="handleSubmit" class="space-y-6">
              
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <!-- Name -->
                <div class="space-y-2">
                  <label for="name" class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
                    Full Name <span class="text-rose-400">*</span>
                  </label>
                  <input
                    id="name"
                    v-model="form.name"
                    type="text"
                    required
                    :disabled="isSubmitting"
                    class="w-full bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl px-4 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all hover:border-white/20 font-medium"
                    placeholder="John Doe"
                  />
                </div>

                <!-- Email -->
                <div class="space-y-2">
                  <label for="email" class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
                    Email Address <span class="text-rose-400">*</span>
                  </label>
                  <input
                    id="email"
                    v-model="form.email"
                    type="email"
                    required
                    :disabled="isSubmitting"
                    class="w-full bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl px-4 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all hover:border-white/20 font-medium"
                    placeholder="john@company.com"
                  />
                </div>
              </div>

              <!-- Inquiry Type (Dropdown instead of generic Subject) -->
              <div class="space-y-2">
                <label for="type" class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
                  Inquiry Type <span class="text-rose-400">*</span>
                </label>
                <div class="relative group/select">
                  <select
                    id="type"
                    v-model="form.type"
                    required
                    :disabled="isSubmitting"
                    class="w-full bg-slate-950/50 border border-white/10 text-white rounded-xl pl-4 pr-10 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all appearance-none cursor-pointer hover:border-white/20 font-medium"
                  >
                    <option value="" disabled class="bg-slate-900 text-slate-500">How can we help you?</option>
                    <option v-for="type in inquiryTypes" :key="type" :value="type" class="bg-slate-900 text-white">
                      {{ type }}
                    </option>
                  </select>
                  <div class="absolute inset-y-0 right-4 flex items-center pointer-events-none text-slate-500 group-hover/select:text-white transition-colors">
                    <ChevronDown :size="16" />
                  </div>
                </div>
              </div>

              <!-- Message -->
              <div class="space-y-2">
                <label for="message" class="block text-[10px] font-bold uppercase tracking-widest text-slate-500 ml-1">
                  Message <span class="text-rose-400">*</span>
                </label>
                <textarea
                  id="message"
                  v-model="form.message"
                  required
                  rows="5"
                  :disabled="isSubmitting"
                  class="w-full bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl px-4 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all hover:border-white/20 font-medium resize-none"
                  placeholder="Provide any details that will help us assist you better..."
                ></textarea>
              </div>

              <!-- Success Alert -->
              <Transition enter-active-class="transition-all duration-300" enter-from-class="opacity-0 -translate-y-2 scale-95" leave-active-class="transition-all duration-200" leave-to-class="opacity-0 -translate-y-2 scale-95">
                <div v-if="showSuccess" class="flex items-center gap-3 p-4 bg-emerald-500/10 border border-emerald-500/20 rounded-xl shadow-inner">
                  <div class="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400 shrink-0"><CheckCircle2 :size="16" /></div>
                  <span class="text-sm font-bold text-emerald-300">Message dispatched successfully. We'll be in touch.</span>
                </div>
              </Transition>

              <!-- Error Alert -->
              <Transition enter-active-class="transition-all duration-300" enter-from-class="opacity-0 -translate-y-2 scale-95" leave-active-class="transition-all duration-200" leave-to-class="opacity-0 -translate-y-2 scale-95">
                <div v-if="showError" class="flex items-center gap-3 p-4 bg-rose-500/10 border border-rose-500/20 rounded-xl shadow-inner">
                  <div class="w-8 h-8 rounded-full bg-rose-500/20 flex items-center justify-center text-rose-400 shrink-0"><AlertCircle :size="16" /></div>
                  <span class="text-sm font-bold text-rose-300">{{ errorMessage }}</span>
                </div>
              </Transition>

              <!-- Submit Button -->
              <button
                type="submit"
                :disabled="isSubmitting"
                class="group w-full px-6 py-4 bg-gradient-to-r from-teal-500 to-cyan-500 text-slate-950 rounded-xl font-bold shadow-[0_0_20px_rgba(45,212,191,0.2)] hover:shadow-[0_0_30px_rgba(45,212,191,0.4)] transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
              >
                <Loader2 v-if="isSubmitting" :size="20" class="animate-spin" />
                <Send v-else :size="18" class="group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
                {{ isSubmitting ? 'Transmitting...' : 'Send Transmission' }}
              </button>
            </form>
          </div>

        </div>
      </div>
    </main>

    <AppFooter />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import AppHeader from '../components/layout/AppHeader.vue'
import AppFooter from '../components/layout/AppFooter.vue'
import { Mail, HelpCircle, MapPin, ChevronDown, Send, CheckCircle2, AlertCircle, Loader2 } from 'lucide-vue-next'

const inquiryTypes = [
  'Technical Support',
  'Billing Question',
  'Enterprise Sales',
  'Feature Request',
  'Other'
]

const form = ref({
  name: '',
  email: '',
  type: '',
  message: ''
})

const isSubmitting = ref(false)
const showSuccess = ref(false)
const showError = ref(false)
const errorMessage = ref('')

const handleSubmit = async () => {
  isSubmitting.value = true
  showSuccess.value = false
  showError.value = false

  try {
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 1500))
    
    showSuccess.value = true
    
    // Reset form
    form.value = {
      name: '',
      email: '',
      type: '',
      message: ''
    }
    
    setTimeout(() => {
      showSuccess.value = false
    }, 5000)
  } catch (error) {
    showError.value = true
    errorMessage.value = 'Transmission failed. Please try again or email us directly.'
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in-up {
  animation: fade-in-up 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.animation-delay-100 {
  animation-delay: 0.15s;
}
</style>