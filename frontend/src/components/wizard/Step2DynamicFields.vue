<template>
  <div class="space-y-8">

    <!-- Dynamic Fields Based on Item Type -->
    <div v-if="selectedItemType" class="space-y-6">
      
      <div class="flex items-center gap-3 px-4 py-3 bg-indigo-500/10 border border-indigo-500/20 rounded-xl shadow-inner">
        <div class="w-8 h-8 rounded-lg bg-indigo-500/20 flex items-center justify-center shrink-0">
          <Layers :size="16" class="text-indigo-400" />
        </div>
        <div>
          <p class="text-sm font-bold text-indigo-300">{{ selectedItemType.name }} Metadata</p>
          <p class="text-[10px] font-bold uppercase tracking-widest text-indigo-400/70">Required system fields</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Render each field dynamically -->
        <div 
          v-for="field in selectedItemType.fields" 
          :key="field.name" 
          class="space-y-3"
          :class="field.field_type === 'textarea' ? 'md:col-span-2' : ''"
        >
          <label class="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
            <component :is="getFieldIcon(field.field_type)" :size="14" class="text-teal-400" />
            {{ field.label }}
            <span v-if="field.required" class="text-rose-400">*</span>
          </label>

          <!-- Standard Inputs (Text, Date, Number) -->
          <input
            v-if="['text', 'date', 'number'].includes(field.field_type)"
            :type="field.field_type"
            :step="field.field_type === 'number' ? 'any' : null"
            :value="dynamicFields[field.name]"
            @input="updateField(field.name, $event.target.value)"
            :placeholder="field.placeholder || `Enter ${field.label.toLowerCase()}...`"
            :required="field.required"
            :disabled="loading"
            class="w-full bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl px-4 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300 hover:border-white/20 font-medium"
          />

          <!-- Select Dropdown -->
          <div v-else-if="field.field_type === 'select'" class="relative group/select">
            <select
              :value="dynamicFields[field.name]"
              @input="updateField(field.name, $event.target.value)"
              :required="field.required"
              :disabled="loading"
              class="w-full bg-slate-950/50 border border-white/10 text-white rounded-xl pl-4 pr-10 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300 appearance-none cursor-pointer hover:border-white/20 font-medium"
            >
              <option value="" disabled class="bg-slate-900 text-slate-500">Select {{ field.label }}...</option>
              <option v-for="option in field.options" :key="option" :value="option" class="bg-slate-900 text-white">
                {{ option }}
              </option>
            </select>
            <div class="absolute inset-y-0 right-4 flex items-center pointer-events-none text-slate-500 group-hover/select:text-white transition-colors">
              <ChevronDown :size="16" />
            </div>
          </div>

          <!-- Textarea -->
          <textarea
            v-else-if="field.field_type === 'textarea'"
            :value="dynamicFields[field.name]"
            @input="updateField(field.name, $event.target.value)"
            :placeholder="field.placeholder || `Enter ${field.label.toLowerCase()}...`"
            :required="field.required"
            :disabled="loading"
            rows="3"
            class="w-full bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl px-4 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300 hover:border-white/20 font-medium resize-none"
          ></textarea>
        </div>
      </div>
    </div>

    <div class="h-px w-full bg-white/5"></div>

    <!-- FILE UPLOADER -->
    <div class="space-y-3">
      <div class="flex items-center justify-between">
        <label class="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
          <Upload :size="14" class="text-teal-400" />
          Secure Attachment
        </label>
        <span class="text-[10px] font-bold text-slate-600 uppercase tracking-widest">Optional</span>
      </div>
      <!-- Wrap file uploader in a nice container -->
      <div class="bg-slate-950/30 rounded-2xl p-2 border border-white/5 border-dashed">
        <FileUploader :modelValue="file" @update:modelValue="$emit('update:file', $event)" />
      </div>
    </div>

    <!-- REMINDER DAYS (Segmented Control) -->
    <div class="space-y-3">
      <div class="flex items-center justify-between">
        <label class="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
          <Bell :size="14" class="text-teal-400" />
          Alert Schedule
        </label>
        <span class="text-[10px] font-bold text-slate-600 uppercase tracking-widest">Optional</span>
      </div>
      
      <div class="p-1.5 bg-slate-950/80 rounded-2xl border border-white/5 flex flex-wrap gap-1 shadow-inner">
        <button
          type="button"
          @click="$emit('update:reminderDaysBefore', null)"
          :class="[
            'flex-1 min-w-[80px] py-2.5 rounded-xl font-bold transition-all duration-300 text-xs flex flex-col items-center justify-center gap-0.5',
            reminderDaysBefore === null
              ? 'bg-slate-800 text-white shadow-sm border border-white/10'
              : 'text-slate-500 hover:text-slate-300 hover:bg-white/5 border border-transparent'
          ]"
          :disabled="loading"
        >
          <span>Default</span>
          <span class="text-[9px] uppercase tracking-widest opacity-60">{{ userDefaultReminderDays }} days</span>
        </button>
        <button
          type="button"
          v-for="days in [7, 14, 30, 60]"
          :key="days"
          @click="$emit('update:reminderDaysBefore', days)"
          :class="[
            'flex-1 min-w-[80px] py-2.5 rounded-xl font-bold transition-all duration-300 text-xs flex items-center justify-center',
            reminderDaysBefore === days
              ? 'bg-teal-500 text-slate-950 shadow-[0_0_15px_rgba(45,212,191,0.3)] border border-teal-400'
              : 'text-slate-500 hover:text-slate-300 hover:bg-white/5 border border-transparent'
          ]"
          :disabled="loading"
        >
          {{ days }} Days
        </button>
      </div>
    </div>

    <!-- NOTES -->
    <div class="space-y-3">
      <div class="flex items-center justify-between">
        <label class="flex items-center gap-2 text-[10px] font-bold uppercase tracking-widest text-slate-500">
          <FileText :size="14" class="text-teal-400" />
          Internal Notes
        </label>
        <span class="text-[10px] font-bold text-slate-600 uppercase tracking-widest">Optional</span>
      </div>
      <textarea
        :value="notes"
        @input="$emit('update:notes', $event.target.value)"
        rows="3"
        class="w-full bg-slate-950/50 border border-white/10 text-white placeholder:text-slate-600 rounded-xl px-4 py-3.5 focus:outline-none focus:ring-1 focus:ring-teal-500/50 focus:border-teal-500/50 transition-all duration-300 hover:border-white/20 font-medium resize-none"
        placeholder="Add encrypted notes, account numbers, or extra context..."
        :disabled="loading"
      ></textarea>
    </div>

  </div>
</template>

<script setup>
import { FileText, Upload, Bell, Calendar, Hash, DollarSign, ChevronDown, Layers } from "lucide-vue-next"
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