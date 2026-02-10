<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
    <div
      v-for="item in items"
      :key="item.id"
      class="bg-white p-5 rounded-xl border shadow-sm hover:shadow-md hover:border-gray-300 transition-all duration-200 flex flex-col gap-4"
    >

      <!-- IMAGE -->
      <div class="w-full h-40 rounded-lg overflow-hidden bg-gray-100 shadow-sm flex items-center justify-center">

        <!-- Subscription icon -->
        <img
          v-if="item.type === 'subscription' && getSubscriptionIcon(item.name)"
          :src="getSubscriptionIcon(item.name)"
          class="w-full h-full object-cover"
        />

        <!-- Uploaded file -->
        <img
          v-else-if="item.file_path"
          :src="`http://localhost:8000${item.file_path}`"
          class="w-full h-full object-cover"
        />

        <!-- Category fallback -->
        <img
          v-else
          :src="defaultImages[item.category] || defaultImages.default"
          class="w-full h-full object-cover opacity-80"
        />

      </div>

      <!-- TITLE + DELETE -->
      <div class="flex justify-between items-start">
        <div>
          <h3 class="font-semibold text-lg text-gray-900 leading-tight">
            {{ item.name }}
          </h3>

          <!-- CATEGORY BADGE -->
          <span
            :class="[
              'inline-block mt-1 px-2 py-0.5 rounded-full text-xs font-medium',
              categoryColors[item.category] || 'bg-gray-100 text-gray-700'
            ]"
          >
            {{ item.category }}
          </span>
        </div>

        <!-- DELETE ICON -->
        <button
          @click="$emit('delete', item)"
          class="text-gray-400 hover:text-red-600 transition"
          title="Delete"
        >
          ✕
        </button>
      </div>

      <!-- NOTES -->
      <p class="text-gray-500 text-sm line-clamp-2">
        {{ item.notes || "No notes added" }}
      </p>

      <!-- STATUS BADGE -->
      <div class="flex items-center gap-2">
        <span
          :class="[
            'px-2 py-0.5 rounded-full text-xs font-semibold',
            expirationStatus(item).color
          ]"
        >
          {{ expirationStatus(item).label }}
        </span>

        <span class="text-lg">
          <template v-if="expirationStatus(item).label === 'Expired'">❗</template>
          <template v-else-if="expirationStatus(item).label.includes('Soon')">⚠️</template>
          <template v-else>✔️</template>
        </span>
      </div>

      <!-- DATE + DAYS SECTION -->
      <div class="text-sm text-gray-700 font-medium">

        <!-- SUBSCRIPTIONS -->
        <template v-if="item.type === 'subscription'">

          <!-- Renewal -->
          <div>
            Renews: {{ item.renewal_date }}
          </div>

          <div class="text-xs text-gray-500">
            {{ daysLeft(item) < 0
              ? Math.abs(daysLeft(item)) + ' days overdue'
              : daysLeft(item) + ' days until renewal'
            }}
          </div>

          <!-- Optional expiration -->
          <div v-if="item.expiration_date" class="mt-2">
            Ends: {{ item.expiration_date }}
            <div class="text-xs text-gray-400">
              {{ expirationDays(item) < 0
                ? Math.abs(expirationDays(item)) + ' days overdue'
                : expirationDays(item) + ' days left'
              }}
            </div>
          </div>

        </template>

        <!-- DOCUMENTS -->
        <template v-else>
          Expires: {{ item.expiration_date }}
          <div class="text-xs text-gray-500">
            {{ daysLeft(item) < 0
              ? Math.abs(daysLeft(item)) + ' days overdue'
              : daysLeft(item) + ' days left'
            }}
          </div>
        </template>

      </div>

      <!-- VIEW DOCUMENT -->
      <div v-if="item.file_path" class="mt-2">
        <a
          :href="`http://localhost:8000${item.file_path}`"
          target="_blank"
          class="text-blue-600 hover:underline text-sm"
        >
          View Document
        </a>
      </div>

    </div>
  </div>
</template>

<script setup>
defineProps({
  items: Array
})

/* -----------------------------
   STATUS LOGIC (DOCUMENT + SUBSCRIPTION)
----------------------------- */
function expirationStatus(item) {
  const today = new Date()

  // SUBSCRIPTIONS
  if (item.type === "subscription") {
    if (!item.renewal_date) {
      return { label: "Active", color: "bg-blue-100 text-blue-700" }
    }

    const renewal = new Date(item.renewal_date)
    const diff = (renewal - today) / (1000 * 60 * 60 * 24)

    if (diff < 0) return { label: "Expired", color: "bg-red-100 text-red-700" }
    if (diff < 30) return { label: "Renewing Soon", color: "bg-yellow-100 text-yellow-700" }

    return { label: "Active", color: "bg-green-100 text-green-700" }
  }

  // DOCUMENTS
  if (!item.expiration_date) {
    return { label: "Valid", color: "bg-green-100 text-green-700" }
  }

  const exp = new Date(item.expiration_date)
  const diff = (exp - today) / (1000 * 60 * 60 * 24)

  if (diff < 0) return { label: "Expired", color: "bg-red-100 text-red-700" }
  if (diff < 30) return { label: "Expiring Soon", color: "bg-yellow-100 text-yellow-700" }

  return { label: "Valid", color: "bg-green-100 text-green-700" }
}

/* -----------------------------
   DAYS LEFT (DOCUMENT + SUBSCRIPTION)
----------------------------- */
function daysLeft(item) {
  const today = new Date()

  if (item.type === "subscription") {
    if (!item.renewal_date) return 0
    const renewal = new Date(item.renewal_date)
    return Math.ceil((renewal - today) / (1000 * 60 * 60 * 24))
  }

  if (!item.expiration_date) return 0

  const exp = new Date(item.expiration_date)
  return Math.ceil((exp - today) / (1000 * 60 * 60 * 24))
}

/* -----------------------------
   EXPIRATION DAYS (SUBSCRIPTION END DATE)
----------------------------- */
function expirationDays(item) {
  if (!item.expiration_date) return 0
  const today = new Date()
  const exp = new Date(item.expiration_date)
  return Math.ceil((exp - today) / (1000 * 60 * 60 * 24))
}

/* -----------------------------
   CATEGORY COLORS + DEFAULT IMAGES
----------------------------- */
const categoryColors = {
  Travel: "bg-blue-100 text-blue-700",
  Health: "bg-red-100 text-red-700",
  Finance: "bg-green-100 text-green-700",
  Work: "bg-yellow-100 text-yellow-700",
  Personal: "bg-purple-100 text-purple-700",
  Subscriptions: "bg-indigo-100 text-indigo-700"
}

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