<template>
  <div>
    <div class="space-y-8">

      <!-- PROFILE PHOTO SECTION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-teal-100 flex items-center justify-center flex-shrink-0">
            <User :size="20" class="text-teal-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Profile Photo</h3>
            <p class="text-sm text-gray-600 mt-1">Update your profile picture</p>
          </div>
        </div>

        <div class="flex items-center gap-6">
          <!-- Avatar Display -->
          <div class="relative group">
            <div v-if="form.avatar" class="w-24 h-24 rounded-2xl overflow-hidden border-4 border-gray-200 shadow-lg">
              <img :src="form.avatar" alt="Profile" class="w-full h-full object-cover" />
            </div>
            <div v-else class="w-24 h-24 rounded-2xl bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center shadow-lg border-4 border-gray-200">
              <span class="text-3xl font-bold text-white">{{ initials }}</span>
            </div>
            
            <!-- Overlay on hover -->
            <div class="absolute inset-0 bg-black/50 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-200 flex items-center justify-center">
              <Camera :size="24" class="text-white" />
            </div>
          </div>

          <!-- Upload Buttons -->
          <div class="flex-1">
            <div class="flex flex-wrap gap-3">
              <label class="cursor-pointer px-4 py-2 bg-teal-500 text-white rounded-xl font-medium hover:bg-teal-600 transition-all duration-200 shadow-md hover:shadow-lg flex items-center gap-2">
                <Upload :size="18" />
                Upload Photo
                <input
                  type="file"
                  accept="image/*"
                  class="hidden"
                  @change="handleAvatarUpload"
                />
              </label>
              
              <button
                v-if="form.avatar"
                @click="removeAvatar"
                class="px-4 py-2 bg-red-50 text-red-600 border border-red-200 rounded-xl font-medium hover:bg-red-100 transition-all duration-200"
              >
                Remove
              </button>
            </div>
            <p class="text-xs text-gray-500 mt-2">
              JPG, PNG or GIF. Max size 5MB.
            </p>
          </div>
        </div>
      </div>

      <!-- DIVIDER -->
      <div class="border-t border-gray-200"></div>

      <!-- PERSONAL INFORMATION -->
      <div>
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-lg bg-blue-100 flex items-center justify-center flex-shrink-0">
            <FileText :size="20" class="text-blue-600" />
          </div>
          <div>
            <h3 class="text-lg font-bold text-gray-900">Personal Information</h3>
            <p class="text-sm text-gray-600 mt-1">Update your personal details</p>
          </div>
        </div>

        <form @submit.prevent="save" class="space-y-6">
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            <!-- Full Name -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Full Name *
              </label>
              <div class="relative">
                <input
                  v-model="form.full_name"
                  type="text"
                  class="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                  placeholder="John Doe"
                  required
                />
                <User :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
              </div>
            </div>

            <!-- Username -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Username
              </label>
              <div class="relative">
                <input
                  v-model="form.username"
                  type="text"
                  class="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                  placeholder="johndoe"
                />
                <AtSign :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
              </div>
            </div>

          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            <!-- Email (Read-only, change in Account settings) -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Email Address
              </label>
              <div class="relative">
                <input
                  :value="form.email"
                  type="email"
                  class="w-full pl-11 pr-4 py-3 border border-gray-200 bg-gray-50 rounded-xl text-gray-500 cursor-not-allowed"
                  readonly
                />
                <Mail :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
              </div>
              <p class="text-xs text-gray-500 mt-2 flex items-center gap-1">
                <Info :size="12" />
                Change your email in Account Settings
              </p>
            </div>

            <!-- Phone -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                Phone Number
              </label>
              <div class="relative">
                <input
                  v-model="form.phone"
                  type="tel"
                  class="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                  placeholder="+1 (555) 000-0000"
                />
                <Phone :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
              </div>
            </div>

          </div>

          <!-- Bio -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">
              Bio
            </label>
            <textarea
              v-model="form.bio"
              rows="4"
              class="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all resize-none"
              placeholder="Tell us a bit about yourself..."
            ></textarea>
            <p class="text-xs text-gray-500 mt-2">
              {{ form.bio?.length || 0 }} / 500 characters
            </p>
          </div>

          <!-- DIVIDER -->
          <div class="border-t border-gray-200"></div>

          <!-- ADDITIONAL INFORMATION -->
          <div>
            <h4 class="text-md font-bold text-gray-900 mb-4">Additional Information</h4>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              
              <!-- Date of Birth -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">
                  Date of Birth
                </label>
                <div class="relative">
                  <input
                    v-model="form.date_of_birth"
                    type="date"
                    class="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                  />
                  <Calendar :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
                </div>
              </div>

              <!-- Location -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">
                  Location
                </label>
                <div class="relative">
                  <input
                    v-model="form.location"
                    type="text"
                    class="w-full pl-11 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
                    placeholder="City, Country"
                  />
                  <MapPin :size="18" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400" />
                </div>
              </div>

            </div>
          </div>

          <!-- DIVIDER -->
          <div class="border-t border-gray-200"></div>

          <!-- ACCOUNT INFO (Read-only) -->
          <div>
            <h4 class="text-md font-bold text-gray-900 mb-4">Account Information</h4>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              
              <!-- Member Since -->
              <div class="p-4 bg-gray-50 rounded-xl">
                <div class="flex items-center gap-2 mb-1">
                  <Clock :size="16" class="text-gray-500" />
                  <p class="text-sm font-medium text-gray-600">Member Since</p>
                </div>
                <p class="text-lg font-semibold text-gray-900">
                  {{ formatDate(form.created_at) }}
                </p>
              </div>

              <!-- Last Updated -->
              <div class="p-4 bg-gray-50 rounded-xl">
                <div class="flex items-center gap-2 mb-1">
                  <RefreshCw :size="16" class="text-gray-500" />
                  <p class="text-sm font-medium text-gray-600">Last Updated</p>
                </div>
                <p class="text-lg font-semibold text-gray-900">
                  {{ formatDate(form.updated_at) }}
                </p>
              </div>

            </div>
          </div>

          <!-- ACTION BUTTONS -->
          <div class="flex items-center gap-3 pt-4">
            <button
              type="submit"
              :disabled="saving || !hasChanges"
              class="px-6 py-3 bg-gradient-to-r from-teal-500 to-cyan-500 text-white rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              <Loader2 :size="18" class="animate-spin" v-if="saving" />
              <Check :size="18" v-else />
              {{ saving ? 'Saving...' : 'Save Changes' }}
            </button>

            <button
              v-if="hasChanges"
              type="button"
              @click="resetForm"
              :disabled="saving"
              class="px-6 py-3 bg-gray-100 text-gray-700 rounded-xl font-semibold hover:bg-gray-200 transition-all duration-200"
            >
              Cancel
            </button>
          </div>

          <!-- Success Message -->
          <Transition
            enter-active-class="transition-all duration-200 ease-out"
            enter-from-class="opacity-0 translate-y-2"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition-all duration-150 ease-in"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 translate-y-2"
          >
            <div v-if="saveSuccess" class="flex items-center gap-2 p-4 bg-green-50 border border-green-200 rounded-xl text-green-800 text-sm">
              <CheckCircle2 :size="18" class="text-green-600" />
              <span>Profile updated successfully!</span>
            </div>
          </Transition>

          <!-- Error Message -->
          <Transition
            enter-active-class="transition-all duration-200 ease-out"
            enter-from-class="opacity-0 translate-y-2"
            enter-to-class="opacity-100 translate-y-0"
            leave-active-class="transition-all duration-150 ease-in"
            leave-from-class="opacity-100 translate-y-0"
            leave-to-class="opacity-0 translate-y-2"
          >
            <div v-if="error" class="flex items-center gap-2 p-4 bg-red-50 border border-red-200 rounded-xl text-red-800 text-sm">
              <AlertCircle :size="18" class="text-red-600" />
              <span>{{ error }}</span>
            </div>
          </Transition>

        </form>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { apiFetch } from "../../utils/api"
import {
  User,
  Camera,
  Upload,
  FileText,
  Mail,
  Phone,
  Calendar,
  MapPin,
  AtSign,
  Clock,
  RefreshCw,
  Check,
  CheckCircle2,
  AlertCircle,
  Info,
  Loader2
} from "lucide-vue-next"

const form = ref({
  full_name: "",
  username: "",
  email: "",
  phone: "",
  bio: "",
  date_of_birth: "",
  location: "",
  avatar: "",
  created_at: "",
  updated_at: ""
})

const originalForm = ref({})
const saving = ref(false)
const saveSuccess = ref(false)
const error = ref("")
const loading = ref(true)

const initials = computed(() => {
  if (!form.value.full_name) return "?"
  return form.value.full_name
    .split(" ")
    .map(n => n[0])
    .join("")
    .toUpperCase()
    .slice(0, 2)
})

const hasChanges = computed(() => {
  return JSON.stringify(form.value) !== JSON.stringify(originalForm.value)
})

onMounted(async () => {
  try {
    const res = await apiFetch("/auth/me")
    
    if (!res.ok) {
      throw new Error("Failed to fetch profile")
    }
    
    const data = await res.json()
    
    form.value = {
      full_name: data.full_name || data.name || "",
      username: data.username || "",
      email: data.email || "",
      phone: data.phone || "",
      bio: data.bio || "",
      date_of_birth: data.date_of_birth || "",
      location: data.location || "",
      avatar: data.avatar || "",
      created_at: data.created_at || new Date().toISOString(),
      updated_at: data.updated_at || new Date().toISOString()
    }
    
    // Store original form state
    originalForm.value = JSON.parse(JSON.stringify(form.value))
    
  } catch (err) {
    console.error("Error fetching profile:", err)
    error.value = "Failed to load profile data"
  } finally {
    loading.value = false
  }
})

async function save() {
  saving.value = true
  error.value = ""
  saveSuccess.value = false
  
  try {
    const res = await apiFetch("/auth/me", {
      method: "PUT",
      body: JSON.stringify(form.value)
    })
    
    if (!res.ok) {
      throw new Error("Failed to update profile")
    }
    
    const data = await res.json()
    
    // Update form with server response
    form.value.updated_at = data.updated_at || new Date().toISOString()
    
    // Update original form state
    originalForm.value = JSON.parse(JSON.stringify(form.value))
    
    saveSuccess.value = true
    setTimeout(() => {
      saveSuccess.value = false
    }, 3000)
    
  } catch (err) {
    console.error("Error saving profile:", err)
    error.value = "Failed to update profile. Please try again."
    setTimeout(() => {
      error.value = ""
    }, 5000)
  } finally {
    saving.value = false
  }
}

function resetForm() {
  form.value = JSON.parse(JSON.stringify(originalForm.value))
}

function handleAvatarUpload(event) {
  const file = event.target.files[0]
  if (!file) return
  
  // Check file size (5MB max)
  if (file.size > 5 * 1024 * 1024) {
    error.value = "Image size must be less than 5MB"
    setTimeout(() => {
      error.value = ""
    }, 5000)
    return
  }
  
  // Create preview
  const reader = new FileReader()
  reader.onload = (e) => {
    form.value.avatar = e.target.result
  }
  reader.readAsDataURL(file)
  
  // TODO: Upload to server
  // uploadAvatar(file)
}

function removeAvatar() {
  form.value.avatar = ""
  // TODO: Delete from server
}

function formatDate(dateString) {
  if (!dateString) return "N/A"
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>

<style scoped>
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>