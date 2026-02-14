<template>
  <AuthLayout 
    title="Welcome Back" 
    subtitle="Sign in to your account to continue"
  >
    <!-- Error Message -->
    <AuthErrorAlert :message="errorMessage" />

    <!-- Google Sign In Button -->
    <GoogleSignInButton 
      :disabled="loading" 
      @click="signInWithGoogle"
      class="mb-6"
    />

    <!-- Divider -->
    <OrDivider />

    <!-- Login Form -->
    <LoginForm
      v-model:email="email"
      v-model:password="password"
      v-model:remember-me="rememberMe"
      :loading="loading"
      @submit="handleLogin"
    />

    <!-- Register Link -->
    <p class="text-center text-sm text-gray-600 mt-8">
      Don't have an account?
      <RouterLink
        to="/register"
        class="text-teal-600 hover:text-teal-700 font-semibold hover:underline transition-colors"
      >
        Create an account
      </RouterLink>
    </p>
  </AuthLayout>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRouter, useRoute } from "vue-router"
import { apiFetch } from "../utils/api"
import { setTokens } from "../utils/auth"
import AuthLayout from "../components/auth/AuthLayout.vue"
import AuthErrorAlert from "../components/auth/AuthErrorAlert.vue"
import GoogleSignInButton from "../components/auth/GoogleSignInButton.vue"
import OrDivider from "../components/auth/OrDivider.vue"
import LoginForm from "../components/auth/LoginForm.vue"

const router = useRouter()
const route = useRoute()

const email = ref("")
const password = ref("")
const rememberMe = ref(false)
const loading = ref(false)
const errorMessage = ref("")

onMounted(() => {
  if (route.query.error === 'oauth_failed') {
    errorMessage.value = 'Google sign-in failed. Please try again.'
  }
})

async function handleLogin() {
  loading.value = true
  errorMessage.value = ""

  try {
    const res = await apiFetch("/auth/login", {
      method: "POST",
      body: JSON.stringify({
        email: email.value,
        password: password.value,
        remember_me: rememberMe.value
      })
    })

    if (!res.ok) {
      const data = await res.json()
      errorMessage.value = data.detail || "Invalid email or password"
      loading.value = false
      return
    }

    const data = await res.json()
    setTokens(data.access_token, data.refresh_token)

    setTimeout(() => {
      router.push("/dashboard")
    }, 300)

  } catch (err) {
    console.error(err)
    errorMessage.value = "Something went wrong. Please try again."
    loading.value = false
  }
}

function signInWithGoogle() {
  loading.value = true
  errorMessage.value = ""
  window.location.href = 'http://localhost:8000/auth/google'
}
</script>
