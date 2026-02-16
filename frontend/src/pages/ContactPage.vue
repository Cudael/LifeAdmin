<template>
  <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white">
    <AppHeader />
    
    <main class="max-w-4xl mx-auto px-6 py-16 pt-36">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          Get in Touch
        </h1>
        <p class="text-xl text-gray-600">
          Have questions or need support? We're here to help.
        </p>
      </div>

      <!-- Contact Form -->
      <div class="bg-white rounded-2xl shadow-xl p-8 md:p-12">
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- Name -->
          <div>
            <label for="name" class="block text-sm font-medium text-gray-700 mb-2">
              Name
            </label>
            <input
              id="name"
              v-model="form.name"
              type="text"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
              placeholder="Your name"
            />
          </div>

          <!-- Email -->
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
              Email
            </label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
              placeholder="your@email.com"
            />
          </div>

          <!-- Subject -->
          <div>
            <label for="subject" class="block text-sm font-medium text-gray-700 mb-2">
              Subject
            </label>
            <input
              id="subject"
              v-model="form.subject"
              type="text"
              required
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all"
              placeholder="How can we help?"
            />
          </div>

          <!-- Message -->
          <div>
            <label for="message" class="block text-sm font-medium text-gray-700 mb-2">
              Message
            </label>
            <textarea
              id="message"
              v-model="form.message"
              required
              rows="6"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all resize-none"
              placeholder="Tell us more about your inquiry..."
            ></textarea>
          </div>

          <!-- Success Message -->
          <div
            v-if="showSuccess"
            class="bg-green-50 border border-green-200 text-green-800 px-4 py-3 rounded-lg"
          >
            Thank you for contacting us! We'll get back to you soon.
          </div>

          <!-- Error Message -->
          <div
            v-if="showError"
            class="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg"
          >
            {{ errorMessage }}
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="isSubmitting"
            class="w-full bg-gradient-to-r from-teal-500 to-cyan-500 text-white font-semibold py-4 px-6 rounded-lg hover:from-teal-600 hover:to-cyan-600 transition-all duration-200 transform hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
          >
            {{ isSubmitting ? 'Sending...' : 'Send Message' }}
          </button>
        </form>
      </div>

      <!-- Alternative Contact Methods -->
      <div class="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="text-center p-6 bg-white rounded-xl shadow-sm">
          <div class="w-12 h-12 bg-teal-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
            </svg>
          </div>
          <h3 class="font-semibold text-gray-900 mb-2">Email</h3>
          <a href="mailto:support@remindes.com" class="text-teal-600 hover:text-teal-700">
            support@remindes.com
          </a>
        </div>

        <div class="text-center p-6 bg-white rounded-xl shadow-sm">
          <div class="w-12 h-12 bg-cyan-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg class="w-6 h-6 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <h3 class="font-semibold text-gray-900 mb-2">FAQ</h3>
          <a href="/#faq" class="text-cyan-600 hover:text-cyan-700">
            Check our FAQ
          </a>
        </div>

        <div class="text-center p-6 bg-white rounded-xl shadow-sm">
          <div class="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
          </div>
          <h3 class="font-semibold text-gray-900 mb-2">Response Time</h3>
          <p class="text-gray-600">
            Within 24 hours
          </p>
        </div>
      </div>
    </main>

    <AppFooter />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import AppHeader from '../components/layout/AppHeader.vue'
import AppFooter from '../components/layout/AppFooter.vue'

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const isSubmitting = ref(false)
const showSuccess = ref(false)
const showError = ref(false)
const errorMessage = ref('')

const handleSubmit = async () => {
  isSubmitting.value = true
  showSuccess.value = false
  showError.value = false

  try {
    // TODO: Implement actual backend integration for contact form
    // For now, just show success message (simulate form submission)
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    showSuccess.value = true
    
    // Reset form
    form.value = {
      name: '',
      email: '',
      subject: '',
      message: ''
    }
    
    // Hide success message after 5 seconds
    setTimeout(() => {
      showSuccess.value = false
    }, 5000)
  } catch (error) {
    showError.value = true
    errorMessage.value = 'Something went wrong. Please try again or email us directly.'
  } finally {
    isSubmitting.value = false
  }
}
</script>
