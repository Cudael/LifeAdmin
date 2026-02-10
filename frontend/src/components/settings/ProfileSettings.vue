<template>
  <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-200">

    <h2 class="text-xl font-semibold mb-4">Profile</h2>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

      <div>
        <label class="block text-sm font-medium mb-1">Full Name</label>
        <input
          v-model="form.name"
          type="text"
          class="w-full px-3 py-2 border rounded-lg"
        />
      </div>

      <div>
        <label class="block text-sm font-medium mb-1">Email</label>
        <input
          v-model="form.email"
          type="email"
          class="w-full px-3 py-2 border rounded-lg"
        />
      </div>

    </div>

    <button
      @click="save"
      class="mt-6 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
    >
      Save Changes
    </button>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"

const form = ref({
  name: "",
  email: ""
})

onMounted(async () => {
  const res = await fetch("http://localhost:8000/auth/me", {
    headers: {
      Authorization: `Bearer ${localStorage.getItem("token")}`
    }
  })
  const data = await res.json()
  form.value.name = data.name
  form.value.email = data.email
})

async function save() {
  await fetch("http://localhost:8000/auth/me", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("token")}`
    },
    body: JSON.stringify(form.value)
  })
}
</script>