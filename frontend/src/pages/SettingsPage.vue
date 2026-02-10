<template>
  <DashboardLayout pageTitle="Settings">

    <template #actions></template>

    <!-- SETTINGS LAYOUT -->
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10">

      <!-- LEFT SIDEBAR -->
      <aside class="md:col-span-1">
        <nav class="flex flex-col gap-1">

          <button
            v-for="item in menu"
            :key="item.key"
            @click="active = item.key"
            :class="[
              'text-left px-4 py-2 rounded-lg transition font-medium',
              active === item.key
                ? 'bg-gray-900 text-white shadow-sm'
                : 'text-gray-700 hover:bg-gray-100'
            ]"
          >
            {{ item.label }}
          </button>

        </nav>
      </aside>

      <!-- RIGHT CONTENT -->
      <section class="md:col-span-3">
        <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-200">
          <component :is="activeComponent" />
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

const menu = [
  { key: "profile", label: "Profile", component: ProfileSettings },
  { key: "account", label: "Account", component: AccountSettings },
  { key: "security", label: "Security", component: SecuritySettings },
  { key: "preferences", label: "Preferences", component: PreferencesSettings },
]

const active = ref("profile")

const activeComponent = computed(() => {
  return menu.find(m => m.key === active.value).component
})
</script>