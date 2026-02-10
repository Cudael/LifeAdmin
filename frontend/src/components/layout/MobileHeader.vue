<template>
  <div class="md:hidden bg-white border-b border-gray-200 p-4 flex justify-between items-center w-full fixed top-0 left-0 z-20">
    <h2 class="text-lg font-bold">Life Admin</h2>
    <button @click="$emit('open-drawer')" class="p-2 rounded-lg border">
      ☰
    </button>
  </div>
</template>