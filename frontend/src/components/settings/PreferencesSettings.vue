<template>
  <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-200">

    <h2 class="text-xl font-semibold mb-4">Preferences</h2>

    <div class="mb-6">
      <label class="block text-sm font-medium mb-1">Theme</label>
      <select class="w-full px-3 py-2 border rounded-lg">
        <option>Light</option>
        <option>Dark</option>
      </select>
    </div>

    <div class="mb-6">
      <label class="block text-sm font-medium mb-1">Notifications</label>
      <select class="w-full px-3 py-2 border rounded-lg">
        <option>All</option>
        <option>Important Only</option>
        <option>None</option>
      </select>
    </div>

  </div>
</template>