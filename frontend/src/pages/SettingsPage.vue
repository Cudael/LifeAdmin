<template>
  <DashboardLayout pageTitle="Settings">

    <template #actions>
      <button
        v-if="hasUnsavedChanges"
        @click="saveAllChanges"
        class="px-5 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl transition-all duration-200"
      >
        Save Changes
      </button>
    </template>

    <!-- SETTINGS HEADER -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-white mb-2">Settings</h1>
      <p class="text-gray-300">Manage your app preferences and configurations</p>
    </div>

    <!-- SETTINGS LAYOUT -->
    <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">

      <!-- LEFT SIDEBAR -->
      <aside class="lg:col-span-1">
        <div class="bg-gray-900 rounded-2xl shadow-sm border border-gray-800 p-2 sticky top-24">
          <nav class="flex flex-col gap-1">

            <button
              v-for="item in menu"
              :key="item.key"
              @click="active = item.key"
              :class="[
                'group flex items-center gap-3 text-left px-4 py-3 rounded-xl transition-all duration-200 font-medium',
                active === item.key
                  ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white shadow-md'
                  : 'text-gray-300 hover:bg-gray-800 hover:text-white'
              ]"
            >
              <component
                :is="item.icon"
                :size="20"
                :class="[
                  'transition-transform duration-200',
                  active === item.key ? 'scale-110' : 'group-hover:scale-105'
                ]"
              />
              <span>{{ item.label }}</span>
            </button>

          </nav>
        </div>
      </aside>

      <!-- RIGHT CONTENT -->
      <section class="lg:col-span-3">
        <div class="bg-gray-900 rounded-2xl shadow-sm border border-gray-800 overflow-hidden">
          
          <!-- Section Header -->
          <div class="bg-teal-900/20 border-b border-gray-800 px-8 py-6">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-500 flex items-center justify-center shadow-md">
                <component :is="activeMenu.icon" :size="20" class="text-white" />
              </div>
              <div>
                <h2 class="text-2xl font-bold text-white">{{ activeMenu.label }}</h2>
                <p class="text-sm text-gray-300 mt-1">{{ activeMenu.description }}</p>
              </div>
            </div>
          </div>

          <!-- Section Content with Transition -->
          <div class="p-8">
            <Transition
              mode="out-in"
              enter-active-class="transition-all duration-200 ease-out"
              enter-from-class="opacity-0 translate-y-4"
              enter-to-class="opacity-100 translate-y-0"
              leave-active-class="transition-all duration-150 ease-in"
              leave-from-class="opacity-100 translate-y-0"
              leave-to-class="opacity-0 -translate-y-4"
            >
              <component :is="activeMenu.component" :key="active" />
            </Transition>
          </div>

        </div>
      </section>

    </div>

  </DashboardLayout>
</template>

<script setup>
import { ref, computed } from "vue"
import AccountSettings from "../components/settings/AccountSettings.vue"
import PreferencesSettings from "../components/settings/PreferencesSettings.vue"
import DashboardLayout from "../layouts/DashboardLayout.vue"

import {
  Settings,
  Sliders
} from "lucide-vue-next"

const menu = [
  {
    key: "account",
    label: "Account",
    description: "Manage your account settings",
    icon: Settings,
    component: AccountSettings
  },
  {
    key: "preferences",
    label: "Preferences",
    description: "Customize your app experience",
    icon: Sliders,
    component: PreferencesSettings
  }
]

const active = ref("account")
const hasUnsavedChanges = ref(false)

const activeMenu = computed(() => {
  return menu.find(m => m.key === active.value)
})

function saveAllChanges() {
  // This will be implemented when we add real save functionality
  console.log('Saving changes...')
  hasUnsavedChanges.value = false
}
</script>