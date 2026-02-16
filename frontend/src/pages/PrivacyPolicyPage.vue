<script setup>
import AppHeader from "../components/layout/AppHeader.vue"
import AppFooter from "../components/layout/AppFooter.vue"
import { Shield, Lock, Eye, Database, Mail, UserCheck } from "lucide-vue-next"
</script>

<template>
  <div class="bg-white min-h-screen flex flex-col">
    <AppHeader />

    <main class="flex-1 pt-20">
      <!-- Header Section -->
      <section class="bg-gradient-to-br from-teal-50 via-cyan-50 to-white py-20">
        <div class="max-w-4xl mx-auto px-6">
          <div class="text-center">
            <div class="inline-flex items-center justify-center w-20 h-20 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl mb-6 shadow-lg">
              <Shield :size="40" class="text-white" />
            </div>
            <h1 class="text-5xl font-extrabold text-gray-900 mb-4">
              Privacy Policy
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
              At Remindes, we take your privacy seriously. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our service. Please read this privacy policy carefully. If you do not agree with the terms of this privacy policy, please do not access the site.
            </p>
          </div>

          <!-- Information We Collect -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-teal-100 rounded-xl flex items-center justify-center">
                <Database :size="24" class="text-teal-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">Information We Collect</h2>
            </div>

            <div class="space-y-6 text-gray-700 leading-relaxed">
              <div>
                <h3 class="text-xl font-semibold text-gray-800 mb-3">Personal Information</h3>
                <p class="mb-3">We collect information that you voluntarily provide to us when you register on the service, including:</p>
                <ul class="list-disc pl-6 space-y-2">
                  <li>Name and email address</li>
                  <li>Account credentials (encrypted password)</li>
                  <li>Profile information you choose to provide</li>
                </ul>
              </div>

              <div>
                <h3 class="text-xl font-semibold text-gray-800 mb-3">Document and Data Information</h3>
                <p class="mb-3">When you use our service, we collect:</p>
                <ul class="list-disc pl-6 space-y-2">
                  <li>Documents and files you upload</li>
                  <li>Subscription details and expiration dates</li>
                  <li>Reminder preferences and settings</li>
                  <li>Notes and custom fields you add to items</li>
                </ul>
              </div>

              <div>
                <h3 class="text-xl font-semibold text-gray-800 mb-3">Automatically Collected Information</h3>
                <p class="mb-3">We may automatically collect certain information about your device, including:</p>
                <ul class="list-disc pl-6 space-y-2">
                  <li>IP address and location data</li>
                  <li>Browser type and version</li>
                  <li>Operating system</li>
                  <li>Access times and pages viewed</li>
                  <li>Links clicked and other usage data</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- How We Use Your Information -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-cyan-100 rounded-xl flex items-center justify-center">
                <UserCheck :size="24" class="text-cyan-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">How We Use Your Information</h2>
            </div>

            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>We use the information we collect to:</p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Create and manage your account</li>
                <li>Provide, operate, and maintain our service</li>
                <li>Send you reminders about upcoming expirations</li>
                <li>Improve, personalize, and expand our service</li>
                <li>Understand and analyze how you use our service</li>
                <li>Develop new products, services, features, and functionality</li>
                <li>Communicate with you for customer service and support</li>
                <li>Send you updates, security alerts, and administrative messages</li>
                <li>Prevent fraud and enhance security</li>
                <li>Comply with legal obligations</li>
              </ul>
            </div>
          </div>

          <!-- Data Security -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
                <Lock :size="24" class="text-green-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">Data Security</h2>
            </div>

            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                We implement appropriate technical and organizational security measures to protect your personal information, including:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li><strong>Encryption:</strong> All data is encrypted in transit using TLS/SSL and at rest using AES-256 encryption</li>
                <li><strong>Access Controls:</strong> Strict access controls and authentication mechanisms</li>
                <li><strong>Regular Audits:</strong> Regular security audits and vulnerability assessments</li>
                <li><strong>Secure Infrastructure:</strong> Industry-leading cloud infrastructure with automatic backups</li>
                <li><strong>Password Protection:</strong> Passwords are hashed using bcrypt before storage</li>
              </ul>
              <p class="mt-4">
                However, no method of transmission over the Internet or electronic storage is 100% secure. While we strive to use commercially acceptable means to protect your personal information, we cannot guarantee its absolute security.
              </p>
            </div>
          </div>

          <!-- Sharing Your Information -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
                <Eye :size="24" class="text-purple-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">Sharing Your Information</h2>
            </div>

            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p class="font-semibold text-gray-900">We do not sell, trade, or rent your personal information to third parties.</p>
              <p>We may share your information in the following situations:</p>
              <ul class="list-disc pl-6 space-y-2">
                <li><strong>With Your Consent:</strong> We may share your information when you give us explicit permission</li>
                <li><strong>Service Providers:</strong> We may share information with trusted third-party service providers who assist us in operating our service (e.g., hosting, email delivery)</li>
                <li><strong>Legal Requirements:</strong> We may disclose your information if required by law or in response to valid legal requests</li>
                <li><strong>Business Transfers:</strong> In the event of a merger, acquisition, or sale of assets, your information may be transferred</li>
              </ul>
            </div>
          </div>

          <!-- Your Rights -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Your Rights</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>Depending on your location, you may have the following rights:</p>
              <ul class="list-disc pl-6 space-y-2">
                <li><strong>Access:</strong> Request access to your personal information</li>
                <li><strong>Correction:</strong> Request correction of inaccurate or incomplete information</li>
                <li><strong>Deletion:</strong> Request deletion of your personal information</li>
                <li><strong>Data Portability:</strong> Request a copy of your data in a structured format</li>
                <li><strong>Opt-Out:</strong> Opt-out of marketing communications</li>
                <li><strong>Withdraw Consent:</strong> Withdraw consent where processing is based on consent</li>
              </ul>
              <p class="mt-4">
                To exercise these rights, please contact us at <a href="mailto:privacy@remindes.com" class="text-teal-600 hover:text-teal-700 font-medium">privacy@remindes.com</a>.
              </p>
            </div>
          </div>

          <!-- Data Retention -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Data Retention</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                We retain your personal information for as long as necessary to provide you with our services and as described in this Privacy Policy. When you delete your account, we will delete your personal information within 30 days, except where we are required to retain it for legal or regulatory purposes.
              </p>
            </div>
          </div>

          <!-- Cookies and Tracking -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Cookies and Tracking Technologies</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                We use cookies and similar tracking technologies to track activity on our service and store certain information. For more information about how we use cookies, please see our <RouterLink to="/cookies" class="text-teal-600 hover:text-teal-700 font-medium">Cookie Policy</RouterLink>.
              </p>
            </div>
          </div>

          <!-- International Data Transfers -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">International Data Transfers</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                Your information may be transferred to and maintained on servers located outside of your state, province, country, or other governmental jurisdiction where data protection laws may differ. By using our service, you consent to such transfers.
              </p>
            </div>
          </div>

          <!-- Children's Privacy -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Children's Privacy</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                Our service is not intended for children under the age of 13. We do not knowingly collect personal information from children under 13. If you are a parent or guardian and believe your child has provided us with personal information, please contact us, and we will delete such information.
              </p>
            </div>
          </div>

          <!-- Changes to This Policy -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Changes to This Privacy Policy</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page and updating the "Last updated" date. You are advised to review this Privacy Policy periodically for any changes.
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
                If you have any questions about this Privacy Policy, please contact us:
              </p>
              <ul class="space-y-2">
                <li>Email: <a href="mailto:privacy@remindes.com" class="text-teal-600 hover:text-teal-700 font-medium">privacy@remindes.com</a></li>
                <li>Email: <a href="mailto:support@remindes.com" class="text-teal-600 hover:text-teal-700 font-medium">support@remindes.com</a></li>
              </ul>
            </div>
          </div>

        </div>
      </section>
    </main>

    <AppFooter />
  </div>
</template>
