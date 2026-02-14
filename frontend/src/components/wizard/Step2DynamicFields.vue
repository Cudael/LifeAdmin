<template>
  <div class="space-y-6">

    <!-- Dynamic Fields Based on Item Type -->
    <div v-if="selectedItemType" class="space-y-6">
      
      <div class="p-4 bg-blue-50 border-2 border-blue-200 rounded-xl">
        <div class="flex items-start gap-3">
          <Info :size="20" class="text-blue-600 flex-shrink-0 mt-0.5" />
          <div>
            <p class="text-sm font-semibold text-blue-900">{{ selectedItemType.name }} Fields</p>
            <p class="text-xs text-blue-700 mt-1">Fill in the relevant information for this type of item</p>
          </div>
        </div>
      </div>

      <!-- Render each field dynamically -->
      <div 
        v-for="field in selectedItemType.fields" 
        :key="field.name" 
        class="space-y-2"
      >
        <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
          <component :is="getFieldIcon(field.field_type)" :size="16" class="text-teal-600" />
          {{ field.label }}
          <span v-if="field.required" class="text-red-500">*</span>
        </label>

        <!-- Text Input -->
        <input
          v-if="field.field_type === 'text'"
          type="text"
          :value="dynamicFields[field.name]"
          @input="updateField(field.name, $event.target.value)"
          :placeholder="field.placeholder || `Enter ${field.label.toLowerCase()}`"
          :required="field.required"
          :disabled="loading"
          class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white"
        />

        <!-- Date Input -->
        <input
          v-else-if="field.field_type === 'date'"
          type="date"
          :value="dynamicFields[field.name]"
          @input="updateField(field.name, $event.target.value)"
          :required="field.required"
          :disabled="loading"
          class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white"
        />

        <!-- Number Input -->
        <input
          v-else-if="field.field_type === 'number'"
          type="number"
          step="any"
          :value="dynamicFields[field.name]"
          @input="updateField(field.name, $event.target.value)"
          :placeholder="field.placeholder || `Enter ${field.label.toLowerCase()}`"
          :required="field.required"
          :disabled="loading"
          class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white"
        />

        <!-- Select Dropdown -->
        <select
          v-else-if="field.field_type === 'select'"
          :value="dynamicFields[field.name]"
          @input="updateField(field.name, $event.target.value)"
          :required="field.required"
          :disabled="loading"
          class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white appearance-none cursor-pointer"
        >
          <option value="">Select {{ field.label }}</option>
          <option v-for="option in field.options" :key="option" :value="option">
            {{ option }}
          </option>
        </select>

        <!-- Textarea -->
        <textarea
          v-else-if="field.field_type === 'textarea'"
          :value="dynamicFields[field.name]"
          @input="updateField(field.name, $event.target.value)"
          :placeholder="field.placeholder || `Enter ${field.label.toLowerCase()}`"
          :required="field.required"
          :disabled="loading"
          rows="4"
          class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white resize-none"
        ></textarea>
      </div>

    </div>

    <!-- FILE UPLOADER -->
    <div class="space-y-2">
      <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
        <Upload :size="16" class="text-teal-600" />
        Upload File
        <span class="text-gray-500 text-xs font-normal">(optional)</span>
      </label>
      <FileUploader :modelValue="file" @update:modelValue="$emit('update:file', $event)" />
    </div>

    <!-- REMINDER DAYS -->
    <div class="space-y-2">
      <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
        <Bell :size="16" class="text-teal-600" />
        Reminder Schedule
        <span class="text-gray-500 text-xs font-normal">(optional)</span>
      </label>
      <div class="space-y-3">
        <div class="flex items-center gap-2 p-3 bg-blue-50 border border-blue-200 rounded-lg">
          <Info :size="16" class="text-blue-600 flex-shrink-0" />
          <p class="text-xs text-blue-700">
            Set custom reminder days for this item, or leave blank to use your default setting ({{ userDefaultReminderDays }} days).
          </p>
        </div>
        
        <div class="flex gap-3">
          <button
            type="button"
            @click="$emit('update:reminderDaysBefore', null)"
            :class="[
              'flex-1 px-4 py-3 rounded-xl font-medium transition-all duration-200 border-2',
              reminderDaysBefore === null
                ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white border-teal-500 shadow-md'
                : 'bg-white text-gray-700 border-gray-200 hover:border-teal-300'
            ]"
            :disabled="loading"
          >
            <div class="text-sm">Use Default</div>
            <div class="text-xs opacity-75 mt-0.5">{{ userDefaultReminderDays }} days</div>
          </button>
          <button
            type="button"
            v-for="days in [7, 14, 30, 60]"
            :key="days"
            @click="$emit('update:reminderDaysBefore', days)"
            :class="[
              'flex-1 px-4 py-3 rounded-xl font-medium transition-all duration-200 border-2',
              reminderDaysBefore === days
                ? 'bg-gradient-to-r from-teal-500 to-cyan-500 text-white border-teal-500 shadow-md'
                : 'bg-white text-gray-700 border-gray-200 hover:border-teal-300'
            ]"
            :disabled="loading"
          >
            {{ days }} days
          </button>
        </div>
      </div>
    </div>

    <!-- NOTES -->
    <div class="space-y-2">
      <label class="flex items-center gap-2 text-sm font-semibold text-gray-700">
        <FileText :size="16" class="text-teal-600" />
        Notes
        <span class="text-gray-500 text-xs font-normal">(optional)</span>
      </label>
      <textarea
        :value="notes"
        @input="$emit('update:notes', $event.target.value)"
        rows="4"
        class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-teal-500 transition-all duration-200 bg-white resize-none"
        placeholder="Add any additional details or reminders..."
        :disabled="loading"
      ></textarea>
    </div>

  </div>
</template>

<script setup>
import { FileText, Upload, Bell, Info, Calendar, Hash, DollarSign } from "lucide-vue-next"
import FileUploader from "../FileUploader.vue"

const props = defineProps({
  dynamicFields: Object,
  file: Object,
  notes: String,
  reminderDaysBefore: Number,
  selectedItemType: Object,
  userDefaultReminderDays: Number,
  loading: Boolean
})

const emit = defineEmits([
  'update:dynamicFields',
  'update:file',
  'update:notes',
  'update:reminderDaysBefore'
])

function updateField(fieldName, value) {
  const updated = { ...props.dynamicFields, [fieldName]: value }
  emit('update:dynamicFields', updated)
}

function getFieldIcon(fieldType) {
  switch (fieldType) {
    case 'date': return Calendar
    case 'number': return DollarSign
    case 'text': return Hash
    case 'textarea': return FileText
    default: return Hash
  }
}
</script>
