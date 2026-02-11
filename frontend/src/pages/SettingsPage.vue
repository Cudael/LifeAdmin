<template>
  <DashboardLayout pageTitle="Settings">

    <template #actions>
      <!-- Optional: Add a save all button if you have unsaved changes -->
      <button
        v-if="hasUnsavedChanges"
        class="px-5 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl transition-all duration-200"
      >
        Save All Changes
      </button>
    </template>

    <!-- SETTINGS HEADER -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900 mb-2">Settings</h1>
      <p class="text-gray-600">Manage your account settings and preferences</p>
    </div>

    <!-- SETTINGS LAYOUT -->
    <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">

      <!-- LEFT SIDEBAR -->
      <aside class="lg:col-span-1">
        <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-2 sticky top-24">
          <nav class="flex flex-col gap-1">

            <button
              v-for="item in menu"
              :key="item.key"
              @click="active = item.key"
              :class="[
                'group flex items-center gap-3 text-left px-4 py-3 rounded-xl transition-all duration-200 font-medium',
                active === item.key
                  ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white shadow-md'
                  : 'text-gray-700 hover:bg-gray-50 hover:text-gray-900'
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
        <div class="bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden">
          
          <!-- Section Header -->
          <div class="bg-gradient-to-r from-teal-50 to-cyan-50 border-b border-gray-200 px-8 py-6">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-teal-500 to-cyan-500 flex items-center justify-center shadow-md">
                <component :is="activeMenu.icon" :size="20" class="text-white" />
              </div>
              <div>
                <h2 class="text-2xl font-bold text-gray-900">{{ activeMenu.label }}</h2>
                <p class="text-sm text-gray-600 mt-1">{{ activeMenu.description }}</p>
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
import ProfileSettings from "../components/settings/ProfileSettings.vue"
import AccountSettings from "../components/settings/AccountSettings.vue"
import SecuritySettings from "../components/settings/SecuritySettings.vue"
import PreferencesSettings from "../components/settings/PreferencesSettings.vue"
import DashboardLayout from "../layouts/DashboardLayout.vue"

import {
  User,
  Settings,
  Shield,
  Sliders
} from "lucide-vue-next"

const menu = [
  {
    key: "profile",
    label: "Profile",
    description: "Manage your personal information",
    icon: User,
    component: ProfileSettings
  },
  {
    key: "account",
    label: "Account",
    description: "Update your account settings",
    icon: Settings,
    component: AccountSettings
  },
  {
    key: "security",
    label: "Security",
    description: "Password and authentication settings",
    icon: Shield,
    component: SecuritySettings
  },
  {
    key: "preferences",
    label: "Preferences",
    description: "Customize your experience",
    icon: Sliders,
    component: PreferencesSettings
  },
]

const active = ref("profile")
const hasUnsavedChanges = ref(false) // You can connect this to actual form state

const activeMenu = computed(() => {
  return menu.find(m => m.key === active.value)
})
</script>