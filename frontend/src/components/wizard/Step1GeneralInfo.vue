<template>
  <div class="space-y-6">
    
    <!-- CATEGORY -->
    <div class="space-y-2">
      <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
        <FolderOpen :size="16" class="text-teal-600" />
        Category
        <span class="text-red-500">*</span>
      </label>
      <select
        :value="category"
        @input="$emit('update:category', $event.target.value)"
        class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white appearance-none cursor-pointer"
        required
        :disabled="loading"
      >
        <option value="" disabled>Select a category</option>
        <option v-for="cat in categories" :key="cat" :value="cat">
          {{ cat }}
        </option>
      </select>
    </div>

    <!-- ITEM TYPE -->
    <div class="space-y-2">
      <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
        <FileType :size="16" class="text-teal-600" />
        Document/Subscription Type
        <span class="text-red-500">*</span>
      </label>
      <div v-if="!category" class="p-4 bg-gray-50 border-2 border-gray-200 rounded-xl text-sm text-gray-600">
        Please select a category first
      </div>
      <div v-else-if="itemTypes.length === 0" class="p-4 bg-gray-50 border-2 border-gray-200 rounded-xl text-sm text-gray-600">
        No types available for this category
      </div>
      <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <button
          v-for="type in itemTypes"
          :key="type.id"
          type="button"
          @click="$emit('update:itemTypeName', type.name)"
          :class="[
            'p-4 rounded-xl border-2 text-left transition-all duration-200',
            itemTypeName === type.name
              ? 'border-teal-500 bg-teal-50 shadow-md'
              : 'border-gray-200 bg-white hover:border-teal-300 hover:shadow-sm'
          ]"
          :disabled="loading"
        >
          <div class="flex items-start gap-3">
            <span class="text-2xl">{{ type.icon || '📄' }}</span>
            <div class="flex-1">
              <div class="font-semibold text-gray-900">{{ type.name }}</div>
              <div class="text-xs text-gray-600 mt-1">{{ type.description }}</div>
            </div>
            <CheckCircle2 
              v-if="itemTypeName === type.name" 
              :size="20" 
              class="text-teal-600 flex-shrink-0" 
            />
          </div>
        </button>
      </div>
    </div>

    <!-- ITEM NAME -->
    <div class="space-y-2">
      <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
        <Edit3 :size="16" class="text-teal-600" />
        Item Name
        <span class="text-red-500">*</span>
      </label>
      <input
        type="text"
        :value="name"
        @input="$emit('update:name', $event.target.value)"
        class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white"
        placeholder="e.g., My Personal Passport"
        required
        :disabled="loading"
        maxlength="200"
      />
      <p class="text-xs text-gray-600">Give this item a personalized name to easily identify it</p>
    </div>

  </div>
</template>

<script setup>
import { FolderOpen, FileType, Edit3, CheckCircle2 } from "lucide-vue-next"

defineProps({
  category: String,
  itemTypeName: String,
  name: String,
  categories: Array,
  itemTypes: Array,
  loading: Boolean
})

defineEmits(['update:category', 'update:itemTypeName', 'update:name'])
</script>
