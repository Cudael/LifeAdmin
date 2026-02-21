<template>
  <DashboardLayout pageTitle="App Settings">

    <!-- Ambient Background Mesh -->
    <div class="fixed inset-0 z-0 bg-[linear-gradient(to_right,#80808008_1px,transparent_1px),linear-gradient(to_bottom,#80808008_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none"></div>
    <div class="fixed bottom-0 right-1/4 w-[600px] h-[500px] bg-cyan-500/10 blur-[150px] rounded-full pointer-events-none z-0 mix-blend-screen"></div>

    <div class="relative z-10 max-w-[1400px] mx-auto pb-12 animate-fade-in-up">

      <!-- SETTINGS HEADER -->
      <div class="mb-8">
        <h1 class="text-3xl font-extrabold text-white mb-2 tracking-tight">App Preferences</h1>
        <p class="text-slate-400 font-medium">Configure notifications, localization, and display settings.</p>
      </div>

      <!-- SETTINGS LAYOUT -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">

        <!-- LEFT SIDEBAR NAVIGATION -->
        <aside class="lg:col-span-3">
          <div class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] shadow-2xl border border-white/5 p-3 sticky top-24">
            <nav class="flex flex-col gap-1">
              <button
                v-for="item in menu"
                :key="item.key"
                @click="active = item.key"
                class="group flex items-center gap-3 text-left px-4 py-3.5 rounded-xl transition-all duration-300 font-bold text-sm relative overflow-hidden"
                :class="[
                  active === item.key
                    ? 'text-white bg-white/10 shadow-inner'
                    : 'text-slate-500 hover:bg-white/5 hover:text-slate-300'
                ]"
              >
                <!-- Active glowing left bar -->
                <div 
                  class="absolute left-0 top-1/2 -translate-y-1/2 w-1 h-1/2 bg-cyan-400 rounded-r-full transition-all duration-300 shadow-[0_0_10px_rgba(34,211,238,0.8)]"
                  :class="active === item.key ? 'opacity-100 translate-x-0' : 'opacity-0 -translate-x-full'"
                ></div>

                <component
                  :is="item.icon"
                  :size="18"
                  class="transition-colors duration-300 relative z-10"
                  :class="active === item.key ? 'text-cyan-400' : 'group-hover:text-slate-400'"
                />
                <span class="relative z-10">{{ item.label }}</span>
              </button>
            </nav>
          </div>
        </aside>

        <!-- RIGHT CONTENT AREA -->
        <section class="lg:col-span-9">
          <div class="bg-slate-900/60 backdrop-blur-xl rounded-[2rem] shadow-2xl border border-white/5 overflow-hidden min-h-[600px] flex flex-col">
            
            <!-- Section Header -->
            <div class="bg-white/[0.02] border-b border-white/5 px-8 py-6 flex items-center gap-4 relative overflow-hidden">
              <div class="absolute top-0 right-0 w-64 h-64 bg-cyan-500/5 blur-[50px] rounded-full pointer-events-none"></div>
              
              <div class="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center shadow-inner relative z-10">
                <component :is="activeMenu.icon" :size="24" class="text-cyan-400" />
              </div>
              <div class="relative z-10">
                <h2 class="text-xl font-extrabold text-white tracking-tight">{{ activeMenu.label }}</h2>
                <p class="text-xs font-bold uppercase tracking-widest text-slate-500 mt-1">{{ activeMenu.description }}</p>
              </div>
            </div>

            <!-- Section Content -->
            <div class="p-8 flex-1">
              <Transition
                mode="out-in"
                enter-active-class="transition-all duration-300 ease-out"
                enter-from-class="opacity-0 translate-y-4 scale-[0.98]"
                enter-to-class="opacity-100 translate-y-0 scale-100"
                leave-active-class="transition-all duration-200 ease-in"
                leave-from-class="opacity-100 translate-y-0 scale-100"
                leave-to-class="opacity-0 -translate-y-4 scale-[0.98]"
              >
                <component :is="activeMenu.component" :key="active" />
              </Transition>
            </div>

          </div>
        </section>

      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref, computed } from "vue"
import AccountSettings from "../components/settings/AccountSettings.vue"
import PreferencesSettings from "../components/settings/PreferencesSettings.vue"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import { Bell, Sliders } from "lucide-vue-next"

const menu = [
  {
    key: "notifications",
    label: "Alerts & Notifications", // Relabeled for UI clarity
    description: "Manage how Remindes contacts you",
    icon: Bell,
    component: AccountSettings
  },
  {
    key: "preferences",
    label: "Localization & Display",
    description: "Customize your dashboard experience",
    icon: Sliders,
    component: PreferencesSettings
  }
]

const active = ref("notifications")

const activeMenu = computed(() => {
  return menu.find(m => m.key === active.value)
})
</script>

<style scoped>
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up {
  animation: fade-in-up 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>