<script setup>
import { Star, MessageCircle } from "lucide-vue-next"
</script>

<template>
  <section class="py-28 bg-gradient-to-b from-[#f7fdfc] to-white relative overflow-hidden">
    
    <!-- Decorative shapes -->
    <div class="absolute top-20 right-20 w-72 h-72 bg-cyan-100 rounded-full opacity-20 blur-3xl"></div>
    <div class="absolute bottom-20 left-20 w-64 h-64 bg-teal-100 rounded-full opacity-20 blur-3xl"></div>

    <div class="max-w-screen-xl mx-auto px-6 text-center relative z-10">

      <div class="inline-flex items-center gap-2 px-4 py-2 bg-teal-100 text-teal-700 rounded-full mb-4 text-sm font-semibold">
        <MessageCircle :size="16" />
        Reviews
      </div>

      <h2 class="text-5xl font-extrabold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent mb-4">
        What People Say
      </h2>
      <div class="w-16 h-1 bg-gradient-to-r from-teal-400 to-cyan-400 mx-auto mb-16"></div>

      <div class="grid md:grid-cols-3 gap-12">

        <div class="group p-8 bg-white rounded-3xl shadow-lg border-2 border-teal-200 hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <!-- Star rating -->
          <div class="flex justify-center gap-1 mb-4">
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
          </div>
          <p class="text-gray-700 mb-6 leading-relaxed italic">"I used to forget renewals constantly. Now everything is handled automatically. This app is a lifesaver!"</p>
          <div class="flex items-center justify-center gap-3">
            <div class="w-12 h-12 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center text-white font-bold text-lg">
              A
            </div>
            <div class="text-left">
              <div class="font-semibold text-gray-900">Anna K.</div>
              <div class="text-sm text-gray-500">Marketing Manager</div>
            </div>
          </div>
        </div>

        <div class="group p-8 bg-white rounded-3xl shadow-lg border-2 border-teal-200 hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <!-- Star rating -->
          <div class="flex justify-center gap-1 mb-4">
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
          </div>
          <p class="text-gray-700 mb-6 leading-relaxed italic">"The reminders saved me from a €300 fine. Worth it instantly. Best investment I made this year."</p>
          <div class="flex items-center justify-center gap-3">
            <div class="w-12 h-12 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center text-white font-bold text-lg">
              M
            </div>
            <div class="text-left">
              <div class="font-semibold text-gray-900">Markus L.</div>
              <div class="text-sm text-gray-500">Freelance Designer</div>
            </div>
          </div>
        </div>

        <div class="group p-8 bg-white rounded-3xl shadow-lg border-2 border-teal-200 hover:shadow-2xl hover:border-teal-400 transition-all duration-300 hover:-translate-y-2">
          <!-- Star rating -->
          <div class="flex justify-center gap-1 mb-4">
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            <Star :size="20" class="fill-yellow-400 text-yellow-400" />
          </div>
          <p class="text-gray-700 mb-6 leading-relaxed italic">"Clean, simple, and surprisingly powerful. I use it every week to stay organized. Highly recommended!"</p>
          <div class="flex items-center justify-center gap-3">
            <div class="w-12 h-12 rounded-full bg-gradient-to-br from-teal-400 to-cyan-400 flex items-center justify-center text-white font-bold text-lg">
              S
            </div>
            <div class="text-left">
              <div class="font-semibold text-gray-900">Sofia R.</div>
              <div class="text-sm text-gray-500">Small Business Owner</div>
            </div>
          </div>
        </div>

      </div>

      <!-- Overall rating -->
      <div class="mt-16 p-8 bg-gradient-to-r from-teal-50 to-cyan-50 rounded-3xl border border-teal-200">
        <div class="flex flex-col md:flex-row items-center justify-center gap-6">
          <div class="text-center md:text-left">
            <div class="text-5xl font-bold text-teal-600 mb-2">4.9/5</div>
            <div class="flex gap-1 justify-center md:justify-start mb-2">
              <Star :size="20" class="fill-yellow-400 text-yellow-400" />
              <Star :size="20" class="fill-yellow-400 text-yellow-400" />
              <Star :size="20" class="fill-yellow-400 text-yellow-400" />
              <Star :size="20" class="fill-yellow-400 text-yellow-400" />
              <Star :size="20" class="fill-yellow-400 text-yellow-400" />
            </div>
            <p class="text-gray-600">Based on 500+ reviews</p>
          </div>
          <div class="hidden md:block w-px h-16 bg-teal-300"></div>
          <div class="text-center">
            <p class="text-gray-700 text-lg font-medium">Trusted by thousands of users worldwide</p>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>
