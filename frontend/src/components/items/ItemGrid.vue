<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
    <div
      v-for="item in items"
      :key="item.id"
      class="group relative bg-slate-900/60 backdrop-blur-xl rounded-[2rem] border border-white/5 shadow-2xl hover:shadow-[0_0_40px_rgba(45,212,191,0.1)] hover:border-teal-500/30 transition-all duration-500 overflow-hidden flex flex-col cursor-pointer"
      @click="$router.push(`/items/${item.id}`)"
    >
      
      <!-- Top Glowing Edge -->
      <div class="absolute top-0 left-0 right-0 h-px z-30 flex justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-500">
        <div class="h-full w-1/2 bg-gradient-to-r from-transparent via-teal-400 to-transparent"></div>
      </div>

      <!-- STATUS RIBBON (Floating Frosted Glass) -->
      <div class="absolute top-4 right-4 z-20">
        <div
          class="flex items-center gap-1.5 px-3 py-1.5 rounded-full text-[10px] font-bold tracking-widest uppercase shadow-[0_4px_12px_rgba(0,0,0,0.3)] backdrop-blur-md border"
          :class="expirationStatus(item).bgClass"
        >
          <span :class="expirationStatus(item).iconClass">{{ expirationStatus(item).icon }}</span>
          <span>{{ expirationStatus(item).label }}</span>
        </div>
      </div>

      <!-- IMAGE AREA -->
      <div class="relative w-full h-48 overflow-hidden bg-slate-950">
        <!-- Deep Gradient Overlay -->
        <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent z-10 pointer-events-none"></div>

        <img
          v-if="item.file_path"
          :src="`${BASE_URL}${item.file_path}`"
          class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-60 group-hover:opacity-90 mix-blend-luminosity"
          :alt="item.name"
        />
        <img
          v-else
          :src="getItemTypeImage(item.item_type_name || item.name)"
          class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 opacity-80 group-hover:opacity-100"
          :alt="item.name"
        />

        <!-- Type Badge (Bottom Left) -->
        <div class="absolute bottom-4 left-5 z-20">
          <span
            class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-[10px] font-bold uppercase tracking-wider backdrop-blur-xl border border-white/10 shadow-lg"
            :class="item.type === 'subscription' ? 'bg-indigo-500/20 text-indigo-300' : 'bg-teal-500/20 text-teal-300'"
          >
            <component :is="item.type === 'subscription' ? CreditCard : FileText" :size="12" />
            {{ item.type === 'subscription' ? 'Subscription' : 'Document' }}
          </span>
        </div>
      </div>

      <!-- CONTENT SECTION -->
      <div class="flex-1 p-6 pt-2 flex flex-col gap-4 relative z-20">
        
        <!-- TITLE + CATEGORY -->
        <div>
          <div class="flex justify-between items-start gap-2 mb-2">
            <h3 class="font-bold text-xl text-white leading-tight tracking-tight group-hover:text-teal-400 transition-colors truncate pr-2">
              {{ item.name }}
            </h3>
            <!-- Delete Button (Reveals on hover) -->
            <button
              @click.stop="$emit('delete', item)"
              class="flex-shrink-0 w-8 h-8 rounded-lg bg-rose-500/10 border border-rose-500/20 text-rose-400 hover:bg-rose-500 hover:text-white transition-all duration-200 flex items-center justify-center opacity-0 group-hover:opacity-100 -translate-y-1 group-hover:translate-y-0"
              title="Delete item"
            >
              <Trash2 :size="14" />
            </button>
          </div>

          <span
            class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-[10px] font-bold uppercase tracking-widest border"
            :class="categoryColors[item.category] || 'bg-slate-800/60 border-white/5 text-slate-400'"
          >
            <component :is="getCategoryIcon(item.category)" :size="10" />
            {{ item.category || 'Uncategorized' }}
          </span>
        </div>

        <div class="h-px bg-white/5 w-full"></div>

        <!-- TIMELINE & PROGRESS -->
        <div class="space-y-3 mt-auto">
          <div class="flex items-center justify-between text-sm">
            <span class="text-slate-500 flex items-center gap-1.5 text-[10px] font-bold uppercase tracking-widest">
              <Calendar :size="14" />
              {{ item.type === 'subscription' ? 'Renews' : 'Expires' }}
            </span>
            <span class="font-bold text-slate-200">
              {{ formatDate(item.type === 'subscription' ? item.renewal_date : item.expiration_date) }}
            </span>
          </div>

          <!-- Progress Bar -->
          <div class="flex items-center gap-3">
            <div class="flex-1 bg-slate-950 rounded-full h-1 overflow-hidden shadow-inner">
              <div 
                class="h-full transition-all duration-1000 ease-out shadow-[0_0_10px_currentColor]"
                :class="[
                  daysLeft(item.type === 'subscription' ? item.renewal_date : item.expiration_date) < 0 ? 'bg-rose-500 text-rose-500' : 
                  daysLeft(item.type === 'subscription' ? item.renewal_date : item.expiration_date) < 7 ? 'bg-orange-500 text-orange-500' : 
                  daysLeft(item.type === 'subscription' ? item.renewal_date : item.expiration_date) < 30 ? 'bg-amber-400 text-amber-400' : 'bg-teal-500 text-teal-500'
                ]"
                :style="{ width: getProgressWidth(daysLeft(item.type === 'subscription' ? item.renewal_date : item.expiration_date)) }"
              ></div>
            </div>
            <span class="text-[10px] font-bold text-slate-500 uppercase tracking-widest whitespace-nowrap">
              {{ Math.abs(daysLeft(item.type === 'subscription' ? item.renewal_date : item.expiration_date)) }}d {{ daysLeft(item.type === 'subscription' ? item.renewal_date : item.expiration_date) < 0 ? 'overdue' : 'left' }}
            </span>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { BASE_URL } from "../../utils/api"
import { getItemTypeImage } from "../../utils/itemTypeImages"
import { useItemStatus } from "../../composables/useItemStatus"
import { Calendar, FileText, CreditCard, Trash2, Plane, Heart, DollarSign, Briefcase, User, Repeat } from "lucide-vue-next"

defineProps({ items: Array })
defineEmits(['delete'])

const { daysLeft } = useItemStatus()

function expirationStatus(item) {
  const today = new Date()
  const targetDate = item.type === 'subscription' ? item.renewal_date : item.expiration_date

  if (!targetDate) return { label: "Active", bgClass: "bg-emerald-500/10 border-emerald-500/20 text-emerald-400", iconClass: "", icon: "●" }

  const diff = (new Date(targetDate) - today) / (1000 * 60 * 60 * 24)

  if (diff < 0) return { label: "Expired", bgClass: "bg-rose-500/10 border-rose-500/20 text-rose-400", iconClass: "animate-pulse", icon: "●" }
  if (diff < 30) return { label: "Soon", bgClass: "bg-orange-500/10 border-orange-500/20 text-orange-400", iconClass: "", icon: "●" }
  return { label: "Active", bgClass: "bg-emerald-500/10 border-emerald-500/20 text-emerald-400", iconClass: "", icon: "●" }
}

function getProgressWidth(days) {
  if (days < 0) return '100%'
  if (days > 365) return '100%'
  return `${Math.min((days / 365) * 100, 100)}%`
}

function formatDate(date) {
  if (!date) return 'N/A'
  return new Date(date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

const categoryColors = {
  Travel: "bg-blue-500/10 border-blue-500/20 text-blue-400",
  Health: "bg-rose-500/10 border-rose-500/20 text-rose-400",
  Finance: "bg-emerald-500/10 border-emerald-500/20 text-emerald-400",
  Work: "bg-amber-500/10 border-amber-500/20 text-amber-400",
  Personal: "bg-purple-500/10 border-purple-500/20 text-purple-400",
  Subscriptions: "bg-indigo-500/10 border-indigo-500/20 text-indigo-400"
}

function getCategoryIcon(category) {
  const icons = { Travel: Plane, Health: Heart, Finance: DollarSign, Work: Briefcase, Personal: User, Subscriptions: Repeat }
  return icons[category] || FileText
}

</script>
