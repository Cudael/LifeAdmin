<template>
  <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-200">

    <h2 class="text-xl font-semibold mb-4">Account</h2>

    <div class="mb-6">
      <label class="block text-sm font-medium mb-1">New Password</label>
      <input type="password" class="w-full px-3 py-2 border rounded-lg" />
    </div>

    <button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
      Update Password
    </button>

    <hr class="my-8" />

    <h3 class="text-lg font-semibold text-red-600 mb-2">Danger Zone</h3>

    <button class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700">
      Delete Account
    </button>

  </div>
</template>