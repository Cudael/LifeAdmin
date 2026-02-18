<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div
      v-for="item in items"
      :key="item.id"
      class="group relative bg-gray-900/80 backdrop-blur-sm rounded-2xl border border-gray-800 shadow-lg hover:shadow-2xl hover:border-teal-300 transition-all duration-300 overflow-hidden flex flex-col"
    >
      
      <!-- Status Ribbon (top-right corner) -->
      <div class="absolute top-4 right-4 z-10">
        <div
          :class="[
            'flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-bold shadow-lg backdrop-blur-sm',
            expirationStatus(item).bgClass
          ]"
        >
          <span :class="expirationStatus(item).iconClass">
            {{ expirationStatus(item).icon }}
          </span>
          <span>{{ expirationStatus(item).label }}</span>
        </div>
      </div>

      <!-- IMAGE -->
      <div class="relative w-full h-48 overflow-hidden bg-gradient-to-br from-gray-100 to-gray-200">
        
        <!-- Overlay gradient for better text contrast -->
        <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent z-10"></div>

        <!-- Subscription icon -->
        <img
          v-if="item.type === 'subscription' && getSubscriptionIcon(item.name)"
          :src="getSubscriptionIcon(item.name)"
          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
          :alt="item.name"
        />

        <!-- Uploaded file -->
        <img
          v-else-if="item.file_path"
          :src="`${BASE_URL}${item.file_path}`"
          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
          :alt="item.name"
        />

        <!-- Category fallback -->
        <img
          v-else
          :src="defaultImages[item.category] || defaultImages.default"
          class="w-full h-full object-cover opacity-80 group-hover:scale-110 transition-transform duration-500"
          :alt="item.category"
        />

        <!-- Type Badge (bottom-left of image) -->
        <div class="absolute bottom-3 left-3 z-20">
          <span
            :class="[
              'inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-semibold backdrop-blur-md shadow-lg',
              item.type === 'subscription' 
                ? 'bg-purple-500/90 text-white' 
                : 'bg-teal-500/90 text-white'
            ]"
          >
            <component :is="item.type === 'subscription' ? CreditCard : FileText" :size="14" />
            {{ item.type === 'subscription' ? 'Subscription' : 'Document' }}
          </span>
        </div>
      </div>

      <!-- CONTENT SECTION -->
      <div class="flex-1 p-5 flex flex-col gap-3">
        
        <!-- TITLE + DELETE -->
        <div class="flex justify-between items-start gap-3">
          <div class="flex-1">
            <h3 class="font-bold text-lg text-white leading-tight group-hover:text-teal-600 transition-colors">
              {{ item.name }}
            </h3>

            <!-- CATEGORY BADGE -->
            <div class="mt-2">
              <span
                :class="[
                  'inline-flex items-center gap-1 px-2.5 py-1 rounded-lg text-xs font-semibold',
                  categoryColors[item.category] || 'bg-gray-100 text-gray-700'
                ]"
              >
                <component :is="getCategoryIcon(item.category)" :size="12" />
                {{ item.category }}
              </span>
            </div>
          </div>

          <!-- DELETE BUTTON -->
          <button
            @click.stop="handleDelete(item)"
            class="flex-shrink-0 w-8 h-8 rounded-lg bg-gray-800 text-gray-400 hover:bg-red-500 hover:text-white transition-all duration-200 flex items-center justify-center opacity-0 group-hover:opacity-100"
            title="Delete item"
          >
            <Trash2 :size="16" />
          </button>
        </div>

        <!-- NOTES -->
        <p class="text-gray-300 text-sm line-clamp-2 leading-relaxed">
          {{ item.notes || "No notes added" }}
        </p>

        <!-- DIVIDER -->
        <div class="border-t border-gray-800"></div>

        <!-- DATE + DAYS SECTION -->
        <div class="space-y-2">

          <!-- SUBSCRIPTIONS -->
          <template v-if="item.type === 'subscription'">
            
            <!-- Renewal Date -->
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-400 flex items-center gap-1.5">
                <Calendar :size="14" />
                Renews:
              </span>
              <span class="font-semibold text-white">
                {{ formatDate(item.renewal_date) }}
              </span>
            </div>

            <!-- Days until renewal -->
            <div class="flex items-center gap-2">
              <div class="flex-1 bg-gray-800/50 rounded-full h-1.5 overflow-hidden">
                <div 
                  :class="[
                    'h-full transition-all duration-500',
                    daysLeft(item.renewal_date) < 0 ? 'bg-red-500' : 
                    daysLeft(item.renewal_date) < 7 ? 'bg-orange-500' : 
                    daysLeft(item.renewal_date) < 30 ? 'bg-yellow-500' : 'bg-green-500'
                  ]"
                  :style="{ width: getProgressWidth(daysLeft(item.renewal_date)) }"
                ></div>
              </div>
              <span class="text-xs font-medium text-gray-300 whitespace-nowrap">
                {{ Math.abs(daysLeft(item.renewal_date)) }} days {{ daysLeft(item.renewal_date) < 0 ? 'overdue' : 'left' }}
              </span>
            </div>

            <!-- Optional expiration -->
            <div v-if="item.expiration_date" class="pt-2 border-t border-gray-800">
              <div class="flex items-center justify-between text-sm">
                <span class="text-gray-400 flex items-center gap-1.5">
                  <AlertTriangle :size="14" />
                  Ends:
                </span>
                <span class="font-semibold text-orange-400">
                  {{ formatDate(item.expiration_date) }}
                </span>
              </div>
            </div>

          </template>

          <!-- DOCUMENTS -->
          <template v-else>
            
            <!-- Expiration Date -->
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-400 flex items-center gap-1.5">
                <Calendar :size="14" />
                Expires:
              </span>
              <span class="font-semibold text-white">
                {{ formatDate(item.expiration_date) }}
              </span>
            </div>

            <!-- Days left progress -->
            <div class="flex items-center gap-2">
              <div class="flex-1 bg-gray-800/50 rounded-full h-1.5 overflow-hidden">
                <div 
                  :class="[
                    'h-full transition-all duration-500',
                    daysLeft(item.expiration_date) < 0 ? 'bg-red-500' : 
                    daysLeft(item.expiration_date) < 7 ? 'bg-orange-500' : 
                    daysLeft(item.expiration_date) < 30 ? 'bg-yellow-500' : 'bg-green-500'
                  ]"
                  :style="{ width: getProgressWidth(daysLeft(item.expiration_date)) }"
                ></div>
              </div>
              <span class="text-xs font-medium text-gray-300 whitespace-nowrap">
                {{ Math.abs(daysLeft(item.expiration_date)) }} days {{ daysLeft(item.expiration_date) < 0 ? 'overdue' : 'left' }}
              </span>
            </div>

          </template>

        </div>

        <!-- ACTIONS ROW -->
        <div class="flex items-center gap-2 pt-2 mt-auto">
          
          <!-- View Document Button -->
          <a
            v-if="item.file_path"
            :href="`${BASE_URL}${item.file_path}`"
            target="_blank"
            class="flex-1 flex items-center justify-center gap-2 px-4 py-2.5 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl text-sm font-semibold hover:shadow-lg hover:shadow-teal-500/30 transition-all duration-200"
            @click.stop
          >
            <ExternalLink :size="16" />
            View Document
          </a>

          <!-- Edit Button -->
          <RouterLink
            :to="`/items/${item.id}/edit`"
            class="flex items-center justify-center gap-2 px-4 py-2.5 bg-gray-800 border-2 border-gray-700 text-gray-300 rounded-xl text-sm font-semibold hover:border-teal-500 hover:text-teal-600 transition-all duration-200"
            @click.stop
          >
            <Edit2 :size="16" />
            Edit
          </RouterLink>

          <!-- View Details Button -->
          <RouterLink
            :to="`/items/${item.id}`"
            class="flex items-center justify-center p-2.5 bg-gray-800 text-gray-300 rounded-xl hover:bg-gray-700 transition-colors"
            title="View details"
            @click.stop
          >
            <Eye :size="18" />
          </RouterLink>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { BASE_URL } from "../utils/api"
import { useItemStatus } from "../composables/useItemStatus"
import { 
  Calendar, 
  AlertTriangle, 
  FileText, 
  CreditCard, 
  Trash2, 
  ExternalLink, 
  Edit2, 
  Eye,
  Plane,
  Heart,
  DollarSign,
  Briefcase,
  User,
  Repeat
} from "lucide-vue-next"

defineProps({
  items: Array
})

// ✅ Define the emit
const emit = defineEmits(['delete'])

// ✅ Add handler function
function handleDelete(item) {
  emit('delete', item)
}

const { daysLeft } = useItemStatus()

/* -----------------------------
   STATUS LOGIC (ENHANCED)
----------------------------- */
function expirationStatus(item) {
  const today = new Date()

  // SUBSCRIPTIONS
  if (item.type === "subscription") {
    if (!item.renewal_date) {
      return { 
        label: "Active", 
        bgClass: "bg-green-500/90 text-white",
        iconClass: "",
        icon: "✓"
      }
    }

    const renewal = new Date(item.renewal_date)
    const diff = (renewal - today) / (1000 * 60 * 60 * 24)

    if (diff < 0) {
      return { 
        label: "Expired", 
        bgClass: "bg-red-500/90 text-white",
        iconClass: "animate-pulse",
        icon: "⚠"
      }
    }
    if (diff < 30) {
      return { 
        label: "Soon", 
        bgClass: "bg-orange-500/90 text-white",
        iconClass: "",
        icon: "⏰"
      }
    }

    return { 
      label: "Active", 
      bgClass: "bg-green-500/90 text-white",
      iconClass: "",
      icon: "✓"
    }
  }

  // DOCUMENTS
  if (!item.expiration_date) {
    return { 
      label: "Valid", 
      bgClass: "bg-green-500/90 text-white",
      iconClass: "",
      icon: "✓"
    }
  }

  const exp = new Date(item.expiration_date)
  const diff = (exp - today) / (1000 * 60 * 60 * 24)

  if (diff < 0) {
    return { 
      label: "Expired", 
      bgClass: "bg-red-500/90 text-white",
      iconClass: "animate-pulse",
      icon: "⚠"
    }
  }
  if (diff < 30) {
    return { 
      label: "Soon", 
      bgClass: "bg-orange-500/90 text-white",
      iconClass: "",
      icon: "⏰"
    }
  }

  return { 
    label: "Valid", 
    bgClass: "bg-green-500/90 text-white",
    iconClass: "",
    icon: "✓"
  }
}

/* -----------------------------
   PROGRESS BAR WIDTH
----------------------------- */
function getProgressWidth(days) {
  if (days < 0) return '100%'
  if (days > 365) return '100%'
  
  const maxDays = 365
  const percentage = Math.min((days / maxDays) * 100, 100)
  return `${percentage}%`
}

/* -----------------------------
   FORMAT DATE
----------------------------- */
function formatDate(date) {
  if (!date) return 'N/A'
  return new Date(date).toLocaleDateString('en-US', { 
    month: 'short', 
    day: 'numeric', 
    year: 'numeric' 
  })
}

/* -----------------------------
   CATEGORY COLORS + ICONS
----------------------------- */
const categoryColors = {
  Travel: "bg-blue-100 text-blue-700",
  Health: "bg-red-100 text-red-700",
  Finance: "bg-green-100 text-green-700",
  Work: "bg-yellow-100 text-yellow-700",
  Personal: "bg-purple-100 text-purple-700",
  Subscriptions: "bg-indigo-100 text-indigo-700"
}

function getCategoryIcon(category) {
  const icons = {
    Travel: Plane,
    Health: Heart,
    Finance: DollarSign,
    Work: Briefcase,
    Personal: User,
    Subscriptions: Repeat
  }
  return icons[category] || FileText
}

/* -----------------------------
   DEFAULT IMAGES
----------------------------- */
const defaultImages = {
  Travel: "/src/assets/category-defaults/travel.jpg",
  Health: "/src/assets/category-defaults/health.jpg",
  Finance: "/src/assets/category-defaults/finance.jpg",
  Work: "/src/assets/category-defaults/work.jpg",
  Personal: "/src/assets/category-defaults/personal.jpg",
  Subscriptions: "/src/assets/category-defaults/subscriptions.jpg",
  default: "/src/assets/category-defaults/default.jpg"
}

const subscriptionIcons = {
  netflix: "/src/assets/subscription-icons/netflix.jpg",
  spotify: "/src/assets/subscription-icons/spotify.jpg",
  youtube: "/src/assets/subscription-icons/youtube.jpg",
}

function getSubscriptionIcon(name) {
  if (!name) return null

  const key = name.toLowerCase()

  for (const brand in subscriptionIcons) {
    if (key.includes(brand)) {
      return subscriptionIcons[brand]
    }
  }

  return null
}
</script>