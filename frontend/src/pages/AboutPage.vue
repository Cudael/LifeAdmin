<template>
  <div class="min-h-screen bg-gradient-to-b from-gray-50 to-white">
    <AppHeader />
    
    <main class="max-w-5xl mx-auto px-6 py-16 pt-36">
      <!-- Header -->
      <div class="text-center mb-16">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          About LifeAdmin
        </h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Simplifying life administration through intelligent organization and timely reminders.
        </p>
      </div>

      <!-- Mission Section -->
      <div class="bg-white rounded-2xl shadow-xl p-8 md:p-12 mb-12">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
          </div>
          <h2 class="text-3xl font-bold text-gray-900">Our Mission</h2>
        </div>
        <p class="text-lg text-gray-700 leading-relaxed mb-4">
          Life's administrative tasks shouldn't be overwhelming. At LifeAdmin, we believe everyone deserves peace of mind when it comes to managing important documents, subscriptions, and deadlines.
        </p>
        <p class="text-lg text-gray-700 leading-relaxed">
          Our mission is to provide an intelligent, user-friendly platform that helps you stay on top of life's essential details—so you can focus on what truly matters.
        </p>
      </div>

      <!-- Story Section -->
      <div class="bg-gradient-to-br from-teal-50 to-cyan-50 rounded-2xl p-8 md:p-12 mb-12">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-12 h-12 bg-white rounded-xl flex items-center justify-center shadow-md">
            <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
            </svg>
          </div>
          <h2 class="text-3xl font-bold text-gray-900">Our Story</h2>
        </div>
        <p class="text-lg text-gray-700 leading-relaxed mb-4">
          LifeAdmin was born from a simple realization: missed deadlines, expired documents, and forgotten subscriptions are universal pain points that cost people time, money, and stress.
        </p>
        <p class="text-lg text-gray-700 leading-relaxed">
          We built this platform to solve these everyday challenges with smart tracking, automated reminders, and secure document storage—all in one beautiful, easy-to-use dashboard.
        </p>
      </div>

      <!-- Values Section -->
      <div class="mb-12">
        <h2 class="text-3xl font-bold text-gray-900 mb-8 text-center">Our Values</h2>
        <div class="grid md:grid-cols-3 gap-8">
          <!-- Value 1 -->
          <div class="bg-white rounded-xl shadow-lg p-6">
            <div class="w-14 h-14 bg-teal-100 rounded-xl flex items-center justify-center mb-4">
              <svg class="w-7 h-7 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Privacy First</h3>
            <p class="text-gray-600">
              Your data is yours. We use bank-level encryption and never sell your information to third parties.
            </p>
          </div>

          <!-- Value 2 -->
          <div class="bg-white rounded-xl shadow-lg p-6">
            <div class="w-14 h-14 bg-cyan-100 rounded-xl flex items-center justify-center mb-4">
              <svg class="w-7 h-7 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Simplicity</h3>
            <p class="text-gray-600">
              Complex features wrapped in an intuitive interface. Organization shouldn't require a learning curve.
            </p>
          </div>

          <!-- Value 3 -->
          <div class="bg-white rounded-xl shadow-lg p-6">
            <div class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center mb-4">
              <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">Reliability</h3>
            <p class="text-gray-600">
              Never miss another deadline. Our platform ensures you're always notified in time, every time.
            </p>
          </div>
        </div>
      </div>

      <!-- Features Overview -->
      <div class="bg-white rounded-2xl shadow-xl p-8 md:p-12 mb-12">
        <h2 class="text-3xl font-bold text-gray-900 mb-8 text-center">What We Offer</h2>
        <div class="grid md:grid-cols-2 gap-6">
          <div class="flex gap-4">
            <div class="flex-shrink-0">
              <div class="w-10 h-10 bg-teal-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
              </div>
            </div>
            <div>
              <h3 class="font-semibold text-gray-900 mb-1">Document Management</h3>
              <p class="text-gray-600 text-sm">Securely store and organize all your important documents in one place.</p>
            </div>
          </div>

          <div class="flex gap-4">
            <div class="flex-shrink-0">
              <div class="w-10 h-10 bg-cyan-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
                </svg>
              </div>
            </div>
            <div>
              <h3 class="font-semibold text-gray-900 mb-1">Smart Reminders</h3>
              <p class="text-gray-600 text-sm">Get notified before important deadlines and renewal dates.</p>
            </div>
          </div>

          <div class="flex gap-4">
            <div class="flex-shrink-0">
              <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                </svg>
              </div>
            </div>
            <div>
              <h3 class="font-semibold text-gray-900 mb-1">Subscription Tracking</h3>
              <p class="text-gray-600 text-sm">Monitor all your subscriptions and renewals in one dashboard.</p>
            </div>
          </div>

          <div class="flex gap-4">
            <div class="flex-shrink-0">
              <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                </svg>
              </div>
            </div>
            <div>
              <h3 class="font-semibold text-gray-900 mb-1">Analytics & Insights</h3>
              <p class="text-gray-600 text-sm">Get a clear overview of upcoming renewals and spending patterns.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- CTA Section -->
      <div class="bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl p-8 md:p-12 text-center text-white">
        <h2 class="text-3xl font-bold mb-4">Ready to Get Organized?</h2>
        <p class="text-xl mb-8 text-teal-50">
          Join thousands of users who never miss a deadline.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <RouterLink
            to="/register"
            class="inline-flex items-center justify-center px-8 py-4 bg-white text-teal-600 font-semibold rounded-lg hover:bg-gray-50 transition-all duration-200 transform hover:scale-105 shadow-lg"
          >
            Get Started Free
            <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"/>
            </svg>
          </RouterLink>
          <RouterLink
            to="/contact"
            class="inline-flex items-center justify-center px-8 py-4 bg-white/10 text-white font-semibold rounded-lg hover:bg-white/20 transition-all duration-200 border-2 border-white/30"
          >
            Contact Us
          </RouterLink>
        </div>
      </div>
    </main>

    <AppFooter />
  </div>
</template>

<script setup>
import AppHeader from '../components/layout/AppHeader.vue'
import AppFooter from '../components/layout/AppFooter.vue'
</script>
