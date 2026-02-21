<script setup>
import { 
  Shield, 
  Lock, 
  EyeOff, 
  UserCheck, 
  Database,
  Fingerprint
} from "lucide-vue-next"
</script>

<template>
  <section class="py-24 md:py-32 relative overflow-hidden z-10">
    
    <!-- High-tech dotted background pattern -->
    <div class="absolute inset-0 bg-[radial-gradient(rgba(16,185,129,0.05)_1.5px,transparent_1.5px)] bg-[size:24px_24px] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_60%,transparent_100%)] pointer-events-none"></div>

    <div class="max-w-screen-xl mx-auto px-6 relative z-10">

      <div class="grid lg:grid-cols-2 gap-16 items-center">

        <!-- Left Column: Visual & Header -->
        <div class="text-left">
          
          <div class="inline-flex items-center gap-2 px-4 py-2 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 rounded-full mb-6 text-sm font-semibold tracking-wide">
            <Shield :size="16" class="fill-current/20" />
            Bank-Grade Security
          </div>

          <h2 class="text-4xl md:text-5xl font-extrabold text-slate-50 tracking-tight mb-6 leading-tight">
            Private by design. <br />
            <span class="bg-gradient-to-r from-emerald-400 to-teal-400 bg-clip-text text-transparent">Fort Knox for your data.</span>
          </h2>
          
          <p class="text-lg text-slate-400 leading-relaxed mb-10 max-w-lg">
            Your life’s most important documents shouldn't sit in an unsecure email folder. We built Remindes with modern encryption standards so your data stays exactly where it belongs: with you.
          </p>

          <!-- Glowing Security Visual Anchor -->
          <div class="relative w-32 h-32 hidden md:flex items-center justify-center group">
            <!-- Pulsing rings -->
            <div class="absolute inset-0 bg-emerald-500/20 rounded-full blur-xl animate-pulse-slow"></div>
            <div class="absolute inset-2 border border-emerald-500/30 rounded-full animate-[spin_10s_linear_infinite]"></div>
            <div class="absolute inset-4 border border-dashed border-emerald-500/40 rounded-full animate-[spin_15s_linear_infinite_reverse]"></div>
            
            <div class="relative w-16 h-16 bg-slate-900 border border-emerald-500/50 rounded-2xl flex items-center justify-center shadow-[0_0_30px_rgba(16,185,129,0.3)] group-hover:scale-110 transition-transform duration-500">
              <Fingerprint :size="32" class="text-emerald-400 drop-shadow-[0_0_8px_rgba(16,185,129,0.8)]" />
            </div>
          </div>

        </div>

        <!-- Right Column: Security Features List -->
        <div class="space-y-4 relative">
          
          <!-- Subtle background glow behind the list -->
          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full bg-emerald-900/10 rounded-full blur-[100px] pointer-events-none"></div>

          <!-- Feature 1 -->
          <div class="group relative flex items-center gap-5 p-5 bg-slate-900/60 backdrop-blur-md rounded-2xl border border-white/5 hover:border-emerald-500/30 hover:bg-slate-800/60 transition-all duration-300">
            <div class="w-12 h-12 shrink-0 bg-emerald-500/10 border border-emerald-500/20 rounded-xl flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform duration-300 shadow-inner">
              <Lock :size="22" />
            </div>
            <div>
              <h4 class="text-slate-200 font-semibold mb-1 group-hover:text-emerald-300 transition-colors">Encrypted in transit</h4>
              <p class="text-slate-400 text-sm leading-relaxed">All data moving between you and our servers is secured with 256-bit TLS encryption.</p>
            </div>
          </div>

          <!-- Feature 2 -->
          <div class="group relative flex items-center gap-5 p-5 bg-slate-900/60 backdrop-blur-md rounded-2xl border border-white/5 hover:border-emerald-500/30 hover:bg-slate-800/60 transition-all duration-300">
            <div class="w-12 h-12 shrink-0 bg-emerald-500/10 border border-emerald-500/20 rounded-xl flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform duration-300 shadow-inner">
              <EyeOff :size="22" />
            </div>
            <div>
              <h4 class="text-slate-200 font-semibold mb-1 group-hover:text-emerald-300 transition-colors">Only you have access</h4>
              <p class="text-slate-400 text-sm leading-relaxed">Your documents are strictly private. Nobody else can view, read, or access your files.</p>
            </div>
          </div>

          <!-- Feature 3 -->
          <div class="group relative flex items-center gap-5 p-5 bg-slate-900/60 backdrop-blur-md rounded-2xl border border-white/5 hover:border-emerald-500/30 hover:bg-slate-800/60 transition-all duration-300">
            <div class="w-12 h-12 shrink-0 bg-emerald-500/10 border border-emerald-500/20 rounded-xl flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform duration-300 shadow-inner">
              <Shield :size="22" />
            </div>
            <div>
              <h4 class="text-slate-200 font-semibold mb-1 group-hover:text-emerald-300 transition-colors">We never sell your data</h4>
              <p class="text-slate-400 text-sm leading-relaxed">You are our customer, not the product. We strictly prohibit selling or sharing user information.</p>
            </div>
          </div>

          <!-- Feature 4 -->
          <div class="group relative flex items-center gap-5 p-5 bg-slate-900/60 backdrop-blur-md rounded-2xl border border-white/5 hover:border-emerald-500/30 hover:bg-slate-800/60 transition-all duration-300">
            <div class="w-12 h-12 shrink-0 bg-emerald-500/10 border border-emerald-500/20 rounded-xl flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform duration-300 shadow-inner">
              <UserCheck :size="22" />
            </div>
            <div>
              <h4 class="text-slate-200 font-semibold mb-1 group-hover:text-emerald-300 transition-colors">Total data control</h4>
              <p class="text-slate-400 text-sm leading-relaxed">Export, download, or permanently delete your entire account and all associated data at any time.</p>
            </div>
          </div>

          <!-- Feature 5 -->
          <div class="group relative flex items-center gap-5 p-5 bg-slate-900/60 backdrop-blur-md rounded-2xl border border-white/5 hover:border-emerald-500/30 hover:bg-slate-800/60 transition-all duration-300">
            <div class="w-12 h-12 shrink-0 bg-emerald-500/10 border border-emerald-500/20 rounded-xl flex items-center justify-center text-emerald-400 group-hover:scale-110 transition-transform duration-300 shadow-inner">
              <Database :size="22" />
            </div>
            <div>
              <h4 class="text-slate-200 font-semibold mb-1 group-hover:text-emerald-300 transition-colors">Modern infrastructure</h4>
              <p class="text-slate-400 text-sm leading-relaxed">Built on industry-leading cloud infrastructure utilizing the latest security best practices.</p>
            </div>
          </div>

        </div>

      </div>

    </div>
  </section>
</template>

<style scoped>
@keyframes pulse-slow {
  0%, 100% {
    opacity: 0.5;
    transform: scale(1);
  }
  50% {
    opacity: 0.8;
    transform: scale(1.05);
  }
}

.animate-pulse-slow {
  animation: pulse-slow 4s ease-in-out infinite;
}
</style>