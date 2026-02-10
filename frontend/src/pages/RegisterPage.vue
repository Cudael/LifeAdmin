<template>
  <div class="bg-gray-50 min-h-screen flex items-center justify-center px-4">
    <div class="w-full max-w-md bg-white p-8 rounded-xl shadow">

      <h2 class="text-2xl font-bold text-center mb-6">Create Your Account</h2>

      <!-- Error Message -->
      <div
        v-if="errorMessage"
        class="bg-red-100 text-red-700 p-3 rounded mb-4"
      >
        {{ errorMessage }}
      </div>

      <!-- Success Message -->
      <div
        v-if="successMessage"
        class="bg-green-100 text-green-700 p-3 rounded mb-4"
      >
        {{ successMessage }}
      </div>

      <form @submit.prevent="handleRegister" class="space-y-6">

        <!-- Full Name -->
        <div>
          <label class="block mb-1 text-sm font-medium">Full Name</label>
          <input
            v-model="fullName"
            type="text"
            class="w-full p-3 border rounded-lg"
            placeholder="John Doe"
            required
          />
        </div>

        <!-- Email -->
        <div>
          <label class="block mb-1 text-sm font-medium">Email</label>
          <input
            v-model="email"
            type="email"
            class="w-full p-3 border rounded-lg"
            placeholder="you@example.com"
            required
          />
        </div>

        <!-- Password -->
        <div>
          <label class="block mb-1 text-sm font-medium">Password</label>
          <div class="relative">
            <input
              :type="showPassword ? 'text' : 'password'"
              v-model="password"
              class="w-full p-3 border rounded-lg"
              required
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-3 top-3 text-sm text-gray-500"
            >
              {{ showPassword ? 'Hide' : 'Show' }}
            </button>
          </div>
        </div>

        <!-- Confirm Password -->
        <div>
          <label class="block mb-1 text-sm font-medium">Confirm Password</label>
          <div class="relative">
            <input
              :type="showConfirmPassword ? 'text' : 'password'"
              v-model="confirmPassword"
              class="w-full p-3 border rounded-lg"
              required
            />
            <button
              type="button"
              @click="showConfirmPassword = !showConfirmPassword"
              class="absolute right-3 top-3 text-sm text-gray-500"
            >
              {{ showConfirmPassword ? 'Hide' : 'Show' }}
            </button>
          </div>
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition"
        >
          Create Account
        </button>

      </form>

      <p class="text-center text-sm text-gray-600 mt-4">
        Already have an account?
        <RouterLink to="/login" class="text-blue-600 hover:underline">
          Login
        </RouterLink>
      </p>

    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import { apiFetch } from "../utils/api"

const router = useRouter()

const fullName = ref("")
const email = ref("")
const password = ref("")
const confirmPassword = ref("")

const showPassword = ref(false)
const showConfirmPassword = ref(false)
const errorMessage = ref("")
const successMessage = ref("")

async function handleRegister() {
  errorMessage.value = ""
  successMessage.value = ""

  if (password.value !== confirmPassword.value) {
    errorMessage.value = "Passwords do not match"
    return
  }

  try {
    const data = await apiFetch("/auth/register", {
      method: "POST",
      body: JSON.stringify({
        full_name: fullName.value,
        email: email.value,
        password: password.value
      })
    })

    successMessage.value = "Account created successfully!"

    setTimeout(() => {
      router.push("/login")
    }, 1000)

  } catch (err) {
    console.error(err)
    errorMessage.value = "Registration failed"
  }
}
</script>