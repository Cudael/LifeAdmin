<template>
  <DashboardLayout pageTitle="Add Subscription">

    <!-- Header Section -->
    <div class="text-center mt-4">
      <h2 class="text-2xl font-bold text-gray-800">Add New Subscription</h2>
      <p class="text-gray-500 text-sm mt-1">
        Track and organize your recurring subscriptions
      </p>
    </div>

    <!-- Back Button -->
    <div class="flex justify-center mt-6">
      <button
        @click="$router.back()"
        class="inline-flex items-center gap-2 px-4 py-2 
               bg-white border border-gray-300 rounded-lg shadow-sm
               hover:bg-gray-50 hover:shadow transition-all"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4"
             fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 19l-7-7 7-7" />
        </svg>
        Back
      </button>
    </div>

    <!-- Centered container -->
    <div class="flex justify-center mt-6 px-4">
      <div class="w-full max-w-2xl bg-white p-8 rounded-2xl shadow border border-teal-100">

        <!-- SUCCESS MESSAGE -->
        <div
          v-if="successMessage"
          class="mb-4 p-3 rounded bg-green-100 text-green-700"
        >
          {{ successMessage }}
        </div>

        <!-- ERROR MESSAGE -->
        <div
          v-if="errorMessage"
          class="mb-4 p-3 rounded bg-red-100 text-red-700"
        >
          {{ errorMessage }}
        </div>

        <!-- FORM -->
        <form @submit.prevent="handleSubmit" class="space-y-8">

          <!-- NAME -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Subscription Name</label>
            <input
              v-model="name"
              type="text"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              placeholder="Netflix, Spotify, Gym Membership..."
              required
            />
          </div>

          <!-- PROVIDER (NEW FIELD) -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Provider (optional)</label>
            <input
              v-model="provider"
              type="text"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              placeholder="Netflix, Apple, Local Gym..."
            />
          </div>

          <!-- SUBSCRIPTION URL (NEW FIELD) -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Subscription URL (optional)</label>
            <input
              v-model="subscriptionUrl"
              type="url"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              placeholder="https://account.netflix.com"
            />
          </div>

          <!-- PRICE -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Price (optional)</label>
            <input
              v-model="price"
              type="number"
              step="0.01"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              placeholder="9.99"
            />
          </div>

          <!-- BILLING CYCLE -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Billing Cycle</label>
            <select
              v-model="billingCycle"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              required
            >
              <option disabled value="">Select cycle</option>
              <option>Weekly</option>
              <option>Monthly</option>
              <option>Quarterly</option>
              <option>Yearly</option>
            </select>
          </div>

          <!-- NEXT RENEWAL DATE -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Next Renewal Date</label>
            <input
              v-model="renewalDate"
              type="date"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              required
            />
          </div>

          <!-- EXPIRATION TOGGLE -->
          <div class="flex items-center justify-between mt-4">
            <label class="text-gray-700 font-medium">Has an expiration date?</label>

            <label class="relative inline-flex items-center cursor-pointer">
              <input type="checkbox" v-model="hasExpiration" class="sr-only peer" />
              <div
                class="w-11 h-6 bg-gray-300 rounded-full peer peer-checked:bg-teal-500 transition-all"
              ></div>
              <div
                class="absolute left-1 top-1 w-4 h-4 bg-white rounded-full shadow
                       peer-checked:translate-x-5 transition-all"
              ></div>
            </label>
          </div>

          <!-- EXPIRATION DATE -->
          <div v-if="hasExpiration">
            <label class="block mb-1 font-medium text-gray-700">Expiration Date</label>
            <input
              v-model="expirationDate"
              type="date"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
            />
          </div>

          <!-- FILE UPLOADER -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Upload File (optional)</label>

            <FileUploader v-model="file" />
          </div>

          <!-- NOTES -->
          <div>
            <label class="block mb-1 font-medium text-gray-700">Notes (optional)</label>
            <textarea
              v-model="notes"
              rows="3"
              class="w-full p-3 border rounded-lg focus:ring-teal-400 focus:border-teal-400"
              placeholder="Any extra details..."
            ></textarea>
          </div>

          <!-- SUBMIT -->
          <button
            type="submit"
            class="w-full bg-teal-500 text-white py-3 rounded-lg font-semibold hover:bg-teal-600 transition"
          >
            Add Subscription
          </button>

        </form>
      </div>
    </div>

  </DashboardLayout>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import FileUploader from "../components/FileUploader.vue"
import { apiFetch } from "../utils/api"

const router = useRouter()

// Form fields
const name = ref("")
const provider = ref("") // NEW
const subscriptionUrl = ref("") // NEW
const price = ref("")
const billingCycle = ref("")
const renewalDate = ref("")
const notes = ref("")
const file = ref(null)

// Expiration toggle
const hasExpiration = ref(false)
const expirationDate = ref(null)

// Messages
const successMessage = ref("")
const errorMessage = ref("")

async function handleSubmit() {
  if (!billingCycle.value) {
    errorMessage.value = "Please select a billing cycle"
    return
  }

  if (!renewalDate.value) {
    errorMessage.value = "Please select a renewal date"
    return
  }

  if (hasExpiration.value && !expirationDate.value) {
    errorMessage.value = "Please select an expiration date"
    return
  }

  try {
    const formData = new FormData()
    formData.append("name", name.value)
    formData.append("provider", provider.value)
    formData.append("subscription_url", subscriptionUrl.value)
    formData.append("price", price.value)
    formData.append("billing_cycle", billingCycle.value)
    formData.append("renewal_date", renewalDate.value)
    formData.append("notes", notes.value)
    formData.append("category", "Subscriptions")
    formData.append("type", "subscription")

    if (hasExpiration.value && expirationDate.value) {
      formData.append("expiration_date", expirationDate.value)
    }

    if (file.value) {
      formData.append("file", file.value)
    }

    const res = await apiFetch("/items/upload", {
      method: "POST",
      body: formData
    })

    if (!res.ok) {
      const data = await res.json()
      errorMessage.value = data.detail || "Failed to add subscription"
      return
    }

    successMessage.value = "Subscription added successfully!"

    setTimeout(() => {
      router.push("/items")
    }, 1000)

  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong"
  }
}
</script>