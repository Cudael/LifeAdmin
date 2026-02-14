<template>
  <div class="space-y-6">
    
    <!-- Review Header -->
    <div class="p-6 bg-gradient-to-br from-teal-50 to-cyan-50 rounded-2xl border-2 border-teal-200">
      <div class="flex items-start gap-4">
        <div class="w-12 h-12 rounded-xl bg-teal-500 flex items-center justify-center flex-shrink-0">
          <CheckCircle2 :size="24" class="text-white" />
        </div>
        <div>
          <h3 class="font-semibold text-gray-900 text-lg">Review Your Item</h3>
          <p class="text-sm text-gray-700 mt-1">Please verify all information before creating your item</p>
        </div>
      </div>
    </div>

    <!-- General Information -->
    <div class="space-y-4">
      <h4 class="font-semibold text-gray-900 flex items-center gap-2">
        <Info :size="18" class="text-teal-600" />
        General Information
      </h4>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="p-4 bg-gray-50 rounded-xl">
          <div class="text-xs text-gray-600 mb-1">Category</div>
          <div class="font-medium text-gray-900">{{ formData.category }}</div>
        </div>
        
        <div class="p-4 bg-gray-50 rounded-xl">
          <div class="text-xs text-gray-600 mb-1">Type</div>
          <div class="font-medium text-gray-900 flex items-center gap-2">
            <span>{{ selectedItemType?.icon || '📄' }}</span>
            {{ formData.itemTypeName }}
          </div>
        </div>
      </div>

      <div class="p-4 bg-gray-50 rounded-xl">
        <div class="text-xs text-gray-600 mb-1">Item Name</div>
        <div class="font-medium text-gray-900">{{ formData.name }}</div>
      </div>
    </div>

    <!-- Dynamic Fields -->
    <div v-if="selectedItemType && Object.keys(formData.dynamicFields).length > 0" class="space-y-4">
      <h4 class="font-semibold text-gray-900 flex items-center gap-2">
        <FileText :size="18" class="text-teal-600" />
        {{ selectedItemType.name }} Details
      </h4>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div 
          v-for="field in selectedItemType.fields"
          :key="field.name"
          class="p-4 bg-gray-50 rounded-xl"
        >
          <div class="text-xs text-gray-600 mb-1">{{ field.label }}</div>
          <div class="font-medium text-gray-900">
            {{ formatFieldValue(field, formData.dynamicFields[field.name]) }}
          </div>
        </div>
      </div>
    </div>

    <!-- File Upload -->
    <div v-if="formData.file" class="space-y-4">
      <h4 class="font-semibold text-gray-900 flex items-center gap-2">
        <Upload :size="18" class="text-teal-600" />
        Attached File
      </h4>
      
      <div class="p-4 bg-gray-50 rounded-xl flex items-center gap-3">
        <Paperclip :size="20" class="text-gray-600" />
        <div class="flex-1">
          <div class="font-medium text-gray-900">{{ formData.file.name }}</div>
          <div class="text-xs text-gray-600">{{ formatFileSize(formData.file.size) }}</div>
        </div>
      </div>
    </div>

    <!-- Notes -->
    <div v-if="formData.notes" class="space-y-4">
      <h4 class="font-semibold text-gray-900 flex items-center gap-2">
        <FileText :size="18" class="text-teal-600" />
        Notes
      </h4>
      
      <div class="p-4 bg-gray-50 rounded-xl">
        <div class="text-sm text-gray-700 whitespace-pre-wrap">{{ formData.notes }}</div>
      </div>
    </div>

    <!-- Reminder Settings -->
    <div class="space-y-4">
      <h4 class="font-semibold text-gray-900 flex items-center gap-2">
        <Bell :size="18" class="text-teal-600" />
        Reminder Settings
      </h4>
      
      <div class="p-4 bg-gray-50 rounded-xl">
        <div class="text-xs text-gray-600 mb-1">Notification Days Before</div>
        <div class="font-medium text-gray-900">
          {{ formData.reminderDaysBefore === null ? 'Default' : `${formData.reminderDaysBefore} days` }}
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { CheckCircle2, Info, FileText, Upload, Bell, Paperclip } from "lucide-vue-next"

defineProps({
  formData: Object,
  selectedItemType: Object
})

function formatFieldValue(field, value) {
  if (!value) return 'Not specified'
  
  if (field.field_type === 'date') {
    try {
      const date = new Date(value)
      return date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
    } catch {
      return value
    }
  }
  
  if (field.field_type === 'number') {
    return parseFloat(value).toFixed(2)
  }
  
  return value
}

function formatFileSize(bytes) {
  if (bytes < 1024) return bytes + ' B'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(2) + ' KB'
  return (bytes / (1024 * 1024)).toFixed(2) + ' MB'
}
</script>
