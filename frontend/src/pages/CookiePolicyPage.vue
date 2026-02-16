<script setup>
import AppHeader from "../components/layout/AppHeader.vue"
import AppFooter from "../components/layout/AppFooter.vue"
import { Cookie, Settings, BarChart, Shield, CheckCircle, Mail } from "lucide-vue-next"
</script>

<template>
  <div class="bg-white min-h-screen flex flex-col">
    <AppHeader />

    <main class="flex-1 pt-20">
      <!-- Header Section -->
      <section class="bg-gradient-to-br from-purple-50 via-pink-50 to-white py-20">
        <div class="max-w-4xl mx-auto px-6">
          <div class="text-center">
            <div class="inline-flex items-center justify-center w-20 h-20 bg-gradient-to-br from-purple-500 to-pink-500 rounded-2xl mb-6 shadow-lg">
              <Cookie :size="40" class="text-white" />
            </div>
            <h1 class="text-5xl font-extrabold text-gray-900 mb-4">
              Cookie Policy
            </h1>
            <p class="text-lg text-gray-600">
              Last updated: February 13, 2026
            </p>
          </div>
        </div>
      </section>

      <!-- Content Section -->
      <section class="py-16">
        <div class="max-w-4xl mx-auto px-6">
          
          <!-- Introduction -->
          <div class="mb-12">
            <p class="text-lg text-gray-700 leading-relaxed mb-6">
              This Cookie Policy explains how Remindes uses cookies and similar tracking technologies when you visit our website. By using our service, you consent to the use of cookies as described in this policy.
            </p>
          </div>

          <!-- What Are Cookies -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
                <Cookie :size="24" class="text-purple-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">What Are Cookies?</h2>
            </div>

            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                Cookies are small text files that are placed on your device when you visit a website. They are widely used to make websites work more efficiently and provide information to website owners.
              </p>
              <p>
                Cookies can be "persistent" or "session" cookies:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li><strong>Session Cookies:</strong> Temporary cookies that are deleted when you close your browser</li>
                <li><strong>Persistent Cookies:</strong> Remain on your device until they expire or you delete them</li>
              </ul>
            </div>
          </div>

          <!-- How We Use Cookies -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">How We Use Cookies</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                We use cookies and similar technologies for several purposes:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>To enable certain functions of the service</li>
                <li>To remember your preferences and settings</li>
                <li>To authenticate and secure your account</li>
                <li>To analyze how you use our service and improve performance</li>
                <li>To understand user behavior and optimize user experience</li>
              </ul>
            </div>
          </div>

          <!-- Types of Cookies We Use -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Types of Cookies We Use</h2>

            <!-- Essential Cookies -->
            <div class="mb-8 p-6 bg-green-50 border-l-4 border-green-500 rounded-r-lg">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                  <CheckCircle :size="20" class="text-green-600" />
                </div>
                <h3 class="text-xl font-semibold text-gray-900">Essential Cookies</h3>
              </div>
              <p class="text-gray-700 leading-relaxed mb-3">
                These cookies are necessary for the website to function properly. They enable core functionality such as security, authentication, and accessibility.
              </p>
              <p class="text-sm text-gray-600 italic">
                Examples: Authentication tokens, session management, security features
              </p>
              <p class="text-sm text-green-700 font-medium mt-3">
                ✓ Required - Cannot be disabled
              </p>
            </div>

            <!-- Functional Cookies -->
            <div class="mb-8 p-6 bg-blue-50 border-l-4 border-blue-500 rounded-r-lg">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                  <Settings :size="20" class="text-blue-600" />
                </div>
                <h3 class="text-xl font-semibold text-gray-900">Functional Cookies</h3>
              </div>
              <p class="text-gray-700 leading-relaxed mb-3">
                These cookies enable enhanced functionality and personalization, such as remembering your preferences and settings.
              </p>
              <p class="text-sm text-gray-600 italic">
                Examples: Language preferences, theme settings, remembered filters
              </p>
              <p class="text-sm text-blue-700 font-medium mt-3">
                ⚙ Optional - Can be disabled in settings
              </p>
            </div>

            <!-- Analytics Cookies -->
            <div class="mb-8 p-6 bg-purple-50 border-l-4 border-purple-500 rounded-r-lg">
              <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                  <BarChart :size="20" class="text-purple-600" />
                </div>
                <h3 class="text-xl font-semibold text-gray-900">Analytics Cookies</h3>
              </div>
              <p class="text-gray-700 leading-relaxed mb-3">
                These cookies help us understand how visitors interact with our website by collecting and reporting information anonymously.
              </p>
              <p class="text-sm text-gray-600 italic">
                Examples: Page views, time on site, user journey, feature usage
              </p>
              <p class="text-sm text-purple-700 font-medium mt-3">
                ⚙ Optional - Can be disabled in settings
              </p>
            </div>

          </div>

          <!-- Specific Cookies -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Specific Cookies We Use</h2>
            <div class="overflow-x-auto">
              <table class="w-full border-collapse">
                <thead>
                  <tr class="bg-gray-100">
                    <th class="border border-gray-300 px-4 py-3 text-left font-semibold text-gray-900">Cookie Name</th>
                    <th class="border border-gray-300 px-4 py-3 text-left font-semibold text-gray-900">Purpose</th>
                    <th class="border border-gray-300 px-4 py-3 text-left font-semibold text-gray-900">Type</th>
                    <th class="border border-gray-300 px-4 py-3 text-left font-semibold text-gray-900">Duration</th>
                  </tr>
                </thead>
                <tbody class="text-gray-700">
                  <tr class="hover:bg-gray-50">
                    <td class="border border-gray-300 px-4 py-3 font-mono text-sm">access_token</td>
                    <td class="border border-gray-300 px-4 py-3">Authentication and session management</td>
                    <td class="border border-gray-300 px-4 py-3">Essential</td>
                    <td class="border border-gray-300 px-4 py-3">30 minutes</td>
                  </tr>
                  <tr class="hover:bg-gray-50">
                    <td class="border border-gray-300 px-4 py-3 font-mono text-sm">refresh_token</td>
                    <td class="border border-gray-300 px-4 py-3">Maintaining login session</td>
                    <td class="border border-gray-300 px-4 py-3">Essential</td>
                    <td class="border border-gray-300 px-4 py-3">7 days</td>
                  </tr>
                  <tr class="hover:bg-gray-50">
                    <td class="border border-gray-300 px-4 py-3 font-mono text-sm">user_preferences</td>
                    <td class="border border-gray-300 px-4 py-3">Storing user settings and preferences</td>
                    <td class="border border-gray-300 px-4 py-3">Functional</td>
                    <td class="border border-gray-300 px-4 py-3">1 year</td>
                  </tr>
                  <tr class="hover:bg-gray-50">
                    <td class="border border-gray-300 px-4 py-3 font-mono text-sm">theme</td>
                    <td class="border border-gray-300 px-4 py-3">Remembering light/dark mode preference</td>
                    <td class="border border-gray-300 px-4 py-3">Functional</td>
                    <td class="border border-gray-300 px-4 py-3">1 year</td>
                  </tr>
                  <tr class="hover:bg-gray-50">
                    <td class="border border-gray-300 px-4 py-3 font-mono text-sm">analytics_id</td>
                    <td class="border border-gray-300 px-4 py-3">Anonymous usage analytics</td>
                    <td class="border border-gray-300 px-4 py-3">Analytics</td>
                    <td class="border border-gray-300 px-4 py-3">2 years</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Third-Party Cookies -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Third-Party Cookies</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                We may use third-party services that set their own cookies. These services include:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li><strong>Authentication Providers:</strong> For Google OAuth and other login services</li>
                <li><strong>Analytics Services:</strong> To understand how users interact with our service</li>
                <li><strong>Content Delivery Networks (CDN):</strong> To improve performance and load times</li>
              </ul>
              <p class="mt-4">
                These third parties have their own privacy and cookie policies, which we encourage you to review.
              </p>
            </div>
          </div>

          <!-- Managing Cookies -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                <Settings :size="24" class="text-blue-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">Managing Your Cookie Preferences</h2>
            </div>

            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                You have several options to manage or delete cookies:
              </p>
              
              <div class="p-6 bg-blue-50 border border-blue-200 rounded-lg">
                <h3 class="text-lg font-semibold text-gray-900 mb-3">Browser Settings</h3>
                <p class="mb-3">
                  Most web browsers allow you to control cookies through their settings. You can:
                </p>
                <ul class="list-disc pl-6 space-y-2">
                  <li>Block all cookies</li>
                  <li>Block third-party cookies</li>
                  <li>Delete cookies after each session</li>
                  <li>Manage cookies on a site-by-site basis</li>
                </ul>
                <p class="mt-3 text-sm text-gray-600">
                  Note: Blocking essential cookies may affect the functionality of our service.
                </p>
              </div>

              <div class="p-6 bg-purple-50 border border-purple-200 rounded-lg">
                <h3 class="text-lg font-semibold text-gray-900 mb-3">Our Cookie Settings</h3>
                <p class="mb-3">
                  You can manage your cookie preferences in your account settings. This allows you to:
                </p>
                <ul class="list-disc pl-6 space-y-2">
                  <li>Disable functional cookies</li>
                  <li>Opt-out of analytics cookies</li>
                  <li>Review what cookies are currently active</li>
                </ul>
              </div>

              <div class="mt-6">
                <h3 class="text-lg font-semibold text-gray-900 mb-3">Browser-Specific Instructions</h3>
                <ul class="space-y-2">
                  <li><strong>Chrome:</strong> Settings → Privacy and security → Cookies and other site data</li>
                  <li><strong>Firefox:</strong> Settings → Privacy & Security → Cookies and Site Data</li>
                  <li><strong>Safari:</strong> Preferences → Privacy → Manage Website Data</li>
                  <li><strong>Edge:</strong> Settings → Cookies and site permissions → Manage and delete cookies</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Do Not Track -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Do Not Track Signals</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                Some browsers include a "Do Not Track" (DNT) feature that signals to websites that you do not want to be tracked. Because there is no common understanding of how to interpret DNT signals, we do not currently respond to DNT browser signals.
              </p>
            </div>
          </div>

          <!-- Local Storage -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Local Storage and Similar Technologies</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                In addition to cookies, we may use other technologies like Local Storage and Session Storage to store information on your device. These technologies serve similar purposes to cookies but can store more data and are not automatically sent to our servers.
              </p>
              <p>
                We use these technologies to:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Cache data for improved performance</li>
                <li>Store user preferences locally</li>
                <li>Enable offline functionality</li>
              </ul>
            </div>
          </div>

          <!-- Updates to This Policy -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Updates to This Cookie Policy</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                We may update this Cookie Policy from time to time to reflect changes in technology, legislation, or our practices. We will post any updates on this page with a new "Last updated" date.
              </p>
            </div>
          </div>

          <!-- More Information -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-teal-100 rounded-xl flex items-center justify-center">
                <Shield :size="24" class="text-teal-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">More Information</h2>
            </div>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                For more information about how we handle your personal data, please see our <RouterLink to="/privacy" class="text-purple-600 hover:text-purple-700 font-medium">Privacy Policy</RouterLink>.
              </p>
              <p>
                To learn more about cookies in general, visit <a href="https://www.allaboutcookies.org" target="_blank" class="text-purple-600 hover:text-purple-700 font-medium">allaboutcookies.org</a>.
              </p>
            </div>
          </div>

          <!-- Contact Us -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                <Mail :size="24" class="text-blue-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">Contact Us</h2>
            </div>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                If you have any questions about our use of cookies, please contact us:
              </p>
              <ul class="space-y-2">
                <li>Email: <a href="mailto:privacy@remindes.com" class="text-purple-600 hover:text-purple-700 font-medium">privacy@remindes.com</a></li>
                <li>Email: <a href="mailto:support@remindes.com" class="text-purple-600 hover:text-purple-700 font-medium">support@remindes.com</a></li>
              </ul>
            </div>
          </div>

        </div>
      </section>
    </main>

    <AppFooter />
  </div>
</template>
