<script setup>
import AppHeader from "../components/layout/AppHeader.vue"
import AppFooter from "../components/layout/AppFooter.vue"
import { FileText, AlertTriangle, Shield, Ban, Scale, Mail } from "lucide-vue-next"
</script>

<template>
  <div class="bg-white min-h-screen flex flex-col">
    <AppHeader />

    <main class="flex-1 pt-20">
      <!-- Header Section -->
      <section class="bg-gradient-to-br from-cyan-50 via-blue-50 to-white py-20">
        <div class="max-w-4xl mx-auto px-6">
          <div class="text-center">
            <div class="inline-flex items-center justify-center w-20 h-20 bg-gradient-to-br from-cyan-500 to-blue-500 rounded-2xl mb-6 shadow-lg">
              <FileText :size="40" class="text-white" />
            </div>
            <h1 class="text-5xl font-extrabold text-gray-900 mb-4">
              Terms of Service
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
              Welcome to LifeAdmin. By accessing or using our service, you agree to be bound by these Terms of Service. Please read them carefully. If you do not agree to these terms, please do not use our service.
            </p>
          </div>

          <!-- Acceptance of Terms -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                <Scale :size="24" class="text-blue-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">Acceptance of Terms</h2>
            </div>

            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                By creating an account or using LifeAdmin, you agree to these Terms of Service and our Privacy Policy. These terms constitute a legally binding agreement between you and LifeAdmin.
              </p>
              <p>
                If you are using the service on behalf of an organization, you represent that you have the authority to bind that organization to these terms.
              </p>
            </div>
          </div>

          <!-- Description of Service -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Description of Service</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                LifeAdmin is a document and subscription management platform that helps you:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Store and organize important documents</li>
                <li>Track subscription renewals and expiration dates</li>
                <li>Receive reminders about upcoming deadlines</li>
                <li>Manage various life admin tasks in one place</li>
              </ul>
              <p class="mt-4">
                We reserve the right to modify, suspend, or discontinue any part of the service at any time with or without notice.
              </p>
            </div>
          </div>

          <!-- User Accounts -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">User Accounts</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                To use LifeAdmin, you must create an account. You agree to:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Provide accurate, current, and complete information during registration</li>
                <li>Maintain and promptly update your account information</li>
                <li>Keep your password secure and confidential</li>
                <li>Notify us immediately of any unauthorized use of your account</li>
                <li>Be responsible for all activities that occur under your account</li>
              </ul>
              <p class="mt-4">
                You must be at least 13 years old to use LifeAdmin. If you are under 18, you must have permission from a parent or guardian.
              </p>
            </div>
          </div>

          <!-- Acceptable Use -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
                <Shield :size="24" class="text-green-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">Acceptable Use</h2>
            </div>

            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>You agree to use LifeAdmin only for lawful purposes and in accordance with these Terms. You agree NOT to:</p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Violate any applicable laws or regulations</li>
                <li>Infringe on the intellectual property rights of others</li>
                <li>Upload viruses, malware, or other malicious code</li>
                <li>Attempt to gain unauthorized access to any part of the service</li>
                <li>Interfere with or disrupt the service or servers</li>
                <li>Collect or harvest information about other users</li>
                <li>Use the service to send spam or unsolicited communications</li>
                <li>Impersonate any person or entity</li>
                <li>Engage in any activity that could harm minors</li>
                <li>Use automated systems (bots, scrapers) to access the service without permission</li>
              </ul>
            </div>
          </div>

          <!-- User Content -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">User Content</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                You retain all rights to the content you upload to LifeAdmin, including documents, notes, and other materials ("User Content"). By uploading User Content, you grant us a limited license to:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Store, process, and display your User Content to provide the service</li>
                <li>Make backups to prevent data loss</li>
                <li>Analyze usage patterns to improve the service (in anonymized form)</li>
              </ul>
              <p class="mt-4">
                You are solely responsible for your User Content and represent that:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>You own or have the necessary rights to upload the content</li>
                <li>Your content does not violate any laws or third-party rights</li>
                <li>Your content does not contain any viruses or harmful code</li>
              </ul>
            </div>
          </div>

          <!-- Prohibited Content -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-red-100 rounded-xl flex items-center justify-center">
                <Ban :size="24" class="text-red-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">Prohibited Content</h2>
            </div>

            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>You may not upload content that:</p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Is illegal, harmful, threatening, abusive, or harassing</li>
                <li>Contains explicit or adult content</li>
                <li>Infringes on intellectual property rights</li>
                <li>Contains personal information of others without consent</li>
                <li>Promotes violence, discrimination, or hatred</li>
                <li>Is false, misleading, or fraudulent</li>
              </ul>
              <p class="mt-4">
                We reserve the right to remove any content that violates these terms without prior notice.
              </p>
            </div>
          </div>

          <!-- Intellectual Property -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Intellectual Property</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                The LifeAdmin service, including its design, features, text, graphics, logos, and software, is owned by LifeAdmin and protected by copyright, trademark, and other intellectual property laws.
              </p>
              <p>
                You may not copy, modify, distribute, sell, or lease any part of our service without our express written permission.
              </p>
            </div>
          </div>

          <!-- Payment and Subscriptions -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Payment and Subscriptions</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                Some features of LifeAdmin may require a paid subscription. By purchasing a subscription, you agree to:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Provide accurate and current billing information</li>
                <li>Pay all fees associated with your subscription</li>
                <li>Accept automatic renewal unless you cancel before the renewal date</li>
              </ul>
              <p class="mt-4">
                <strong>Refunds:</strong> Subscription fees are generally non-refundable, except where required by law. You may cancel your subscription at any time, and you will retain access until the end of your billing period.
              </p>
              <p>
                <strong>Free Trial:</strong> If we offer a free trial, you may cancel at any time during the trial without being charged.
              </p>
            </div>
          </div>

          <!-- Termination -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Termination</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                You may terminate your account at any time by contacting us or using the account deletion feature in your settings.
              </p>
              <p>
                We reserve the right to suspend or terminate your account if you violate these Terms of Service, without prior notice or liability. Upon termination:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Your right to access the service will cease immediately</li>
                <li>We may delete your account and User Content after a reasonable period</li>
                <li>You remain responsible for any outstanding fees</li>
              </ul>
            </div>
          </div>

          <!-- Disclaimers -->
          <div class="mb-12">
            <div class="flex items-center gap-3 mb-6">
              <div class="w-12 h-12 bg-yellow-100 rounded-xl flex items-center justify-center">
                <AlertTriangle :size="24" class="text-yellow-600" />
              </div>
              <h2 class="text-3xl font-bold text-gray-900">Disclaimers</h2>
            </div>

            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p class="uppercase font-semibold">
                The service is provided "as is" and "as available" without warranties of any kind, either express or implied.
              </p>
              <p>
                We do not warrant that:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>The service will be uninterrupted, secure, or error-free</li>
                <li>The results obtained from using the service will be accurate or reliable</li>
                <li>Any errors in the service will be corrected</li>
              </ul>
              <p class="mt-4">
                You use the service at your own risk. We are not responsible for any data loss, so we recommend maintaining your own backups of important information.
              </p>
            </div>
          </div>

          <!-- Limitation of Liability -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Limitation of Liability</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p class="uppercase font-semibold">
                To the maximum extent permitted by law, LifeAdmin shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including loss of profits, data, or other intangible losses.
              </p>
              <p>
                Our total liability to you for any claims arising from these terms or your use of the service shall not exceed the amount you paid us in the 12 months before the claim, or $100, whichever is greater.
              </p>
            </div>
          </div>

          <!-- Indemnification -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Indemnification</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                You agree to indemnify, defend, and hold harmless LifeAdmin and its officers, directors, employees, and agents from any claims, liabilities, damages, losses, and expenses (including legal fees) arising from:
              </p>
              <ul class="list-disc pl-6 space-y-2">
                <li>Your use of the service</li>
                <li>Your violation of these Terms of Service</li>
                <li>Your violation of any rights of another party</li>
                <li>Your User Content</li>
              </ul>
            </div>
          </div>

          <!-- Dispute Resolution -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Dispute Resolution</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                If you have any dispute with us, you agree to first contact us and attempt to resolve the dispute informally.
              </p>
              <p>
                Any disputes arising from these terms shall be governed by the laws of your jurisdiction, without regard to conflict of law principles.
              </p>
            </div>
          </div>

          <!-- Changes to Terms -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Changes to These Terms</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                We may update these Terms of Service from time to time. We will notify you of any material changes by posting the new terms on this page and updating the "Last updated" date.
              </p>
              <p>
                Your continued use of the service after any changes constitutes your acceptance of the new terms.
              </p>
            </div>
          </div>

          <!-- Severability -->
          <div class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Severability</h2>
            <div class="space-y-4 text-gray-700 leading-relaxed">
              <p>
                If any provision of these Terms is found to be unenforceable or invalid, that provision will be limited or eliminated to the minimum extent necessary, and the remaining provisions will remain in full force and effect.
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
                If you have any questions about these Terms of Service, please contact us:
              </p>
              <ul class="space-y-2">
                <li>Email: <a href="mailto:legal@lifeadmin.com" class="text-cyan-600 hover:text-cyan-700 font-medium">legal@lifeadmin.com</a></li>
                <li>Email: <a href="mailto:support@lifeadmin.com" class="text-cyan-600 hover:text-cyan-700 font-medium">support@lifeadmin.com</a></li>
              </ul>
            </div>
          </div>

        </div>
      </section>
    </main>

    <AppFooter />
  </div>
</template>
