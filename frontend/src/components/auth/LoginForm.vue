<template>
  <form @submit.prevent="handleSubmit" class="space-y-6">

    <!-- EMAIL -->
    <div class="space-y-2">
      <label class="block text-sm font-semibold text-gray-700 items-center gap-2">
        <Mail :size="16" class="text-teal-600" />
        Email Address
      </label>
      <div class="relative">
        <input
          :value="email"
          @input="$emit('update:email', $event.target.value)"
          type="email"
          class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 backdrop-blur-sm"
          placeholder="you@example.com"
          required
          :disabled="loading"
        />
      </div>
    </div>

    <!-- PASSWORD -->
    <div class="space-y-2">
      <label class="block text-sm font-semibold text-gray-700 items-center gap-2">
        <Lock :size="16" class="text-teal-600" />
        Password
      </label>
      <div class="relative">
        <input
          :value="password"
          @input="$emit('update:password', $event.target.value)"
          :type="showPassword ? 'text' : 'password'"
          class="w-full px-4 py-3 pr-12 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white/50 backdrop-blur-sm"
          placeholder="••••••••"
          required
          :disabled="loading"
        />
        <button
          type="button"
          @click="togglePasswordVisibility"
          class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 transition-colors"
          tabindex="-1"
        >
          <Eye v-if="!showPassword" :size="20" />
          <EyeOff v-if="showPassword" :size="20" />
        </button>
      </div>
    </div>

    <!-- Remember Me & Forgot Password -->
    <div class="flex items-center justify-between text-sm">
      <label class="flex items-center gap-2 cursor-pointer group">
        <input
          type="checkbox"
          :checked="rememberMe"
          @change="$emit('update:rememberMe', $event.target.checked)"
          class="w-4 h-4 text-teal-600 border-gray-300 rounded focus:ring-teal-500 cursor-pointer"
        />
        <span class="text-gray-600 group-hover:text-gray-900 transition-colors">Remember me</span>
      </label>
      <RouterLink
        to="/forgot-password"
        class="text-teal-600 hover:text-teal-700 font-medium hover:underline transition-colors"
      >
        Forgot password?
      </RouterLink>
    </div>

    <!-- SUBMIT BUTTON -->
    <button
      type="submit"
      :disabled="loading"
      class="group relative w-full bg-gradient-to-r from-teal-500 to-cyan-500 text-white py-4 rounded-xl font-semibold shadow-lg hover:shadow-xl hover:from-teal-600 hover:to-cyan-600 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
    >
      <span v-if="!loading" class="flex items-center gap-2">
        Sign In
        <ArrowRight :size="20" class="group-hover:translate-x-1 transition-transform" />
      </span>
      <span v-else class="flex items-center gap-3">
        <Loader2 :size="20" class="animate-spin" />
        Signing in...
      </span>
    </button>

  </form>
</template>

<script setup>
import { ref } from "vue"
import { Lock, Mail, Eye, EyeOff, ArrowRight, Loader2 } from "lucide-vue-next"

const props = defineProps({
  email: {
    type: String,
    required: true
  },
  password: {
    type: String,
    required: true
  },
  rememberMe: {
    type: Boolean,
    default: false
  },
  loading: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:email', 'update:password', 'update:rememberMe', 'submit'])

const showPassword = ref(false)

function togglePasswordVisibility() {
  showPassword.value = !showPassword.value
}

function handleSubmit() {
  emit('submit')
}
</script>
