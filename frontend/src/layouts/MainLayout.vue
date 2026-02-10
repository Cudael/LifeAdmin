<template>
  <div class="min-h-screen flex bg-gray-100">
    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-md p-4">
      <h2 class="text-xl font-semibold mb-4">Life Admin</h2>
      <nav class="space-y-2">
        <a class="block p-2 rounded hover:bg-gray-200 cursor-pointer">Dashboard</a>
        <a class="block p-2 rounded hover:bg-gray-200 cursor-pointer">Documents</a>
        <a class="block p-2 rounded hover:bg-gray-200 cursor-pointer">Subscriptions</a>
      </nav>
    </aside>

    <!-- Main content -->
    <div class="flex-1 p-6">
      <header class="mb-6">
        <h1 class="text-3xl font-bold">Dashboard</h1>
      </header>

      <slot />
    </div>
  </div>
</template>