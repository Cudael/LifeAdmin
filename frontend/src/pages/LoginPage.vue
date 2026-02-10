<template>
  <div class="bg-gray-50 min-h-screen flex items-center justify-center px-4">
    <div class="w-full max-w-md bg-white p-8 rounded-xl shadow">

      <h2 class="text-2xl font-bold text-center mb-6">Welcome Back</h2>

      <form @submit.prevent="handleLogin" class="space-y-6">

        <!-- EMAIL -->
        <div>
          <label class="block mb-1 text-sm font-medium">Email</label>
          <input
            v-model="email"
            type="email"
            class="w-full p-3 border rounded-lg focus:ring-blue-500 focus:border-blue-500"
            placeholder="you@example.com"
            required
          />
        </div>

        <!-- PASSWORD -->
        <div>
          <label class="block mb-1 text-sm font-medium">Password</label>
          <input
            v-model="password"
            type="password"
            class="w-full p-3 border rounded-lg focus:ring-blue-500 focus:border-blue-500"
            placeholder="••••••••"
            required
          />
        </div>

        <!-- SUBMIT -->
        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition"
        >
          Login
        </button>

      </form>

      <p class="text-center text-sm text-gray-600 mt-4">
        Don’t have an account?
        <RouterLink to="/register" class="text-blue-600 hover:underline">
          Register
        </RouterLink>
      </p>

    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import { apiFetch } from "../utils/api"   // <-- use your API wrapper
import { setTokens } from "../utils/auth" // <-- function to save tokens

const router = useRouter()

const email = ref("")
const password = ref("")

async function handleLogin() {
  try {
    const res = await apiFetch("/auth/login", {
      method: "POST",
      body: JSON.stringify({
        email: email.value,
        password: password.value
      })
    })

    const data = await res.json()
    setTokens(data.access_token, data.refresh_token)

    router.push("/dashboard")

  } catch (err) {
    console.error(err)
    alert("Invalid email or password")
  }
}
</script>