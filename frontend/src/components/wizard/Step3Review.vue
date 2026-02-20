<template>
  <div class="space-y-6">
    
    <!-- Review Header -->
    <div class="flex items-center justify-center p-8 bg-teal-500/5 border border-teal-500/20 rounded-2xl relative overflow-hidden">
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-48 h-48 bg-teal-500/20 blur-[60px] rounded-full pointer-events-none"></div>
      
      <div class="text-center relative z-10">
        <div class="w-16 h-16 rounded-2xl bg-teal-500/10 border border-teal-500/30 flex items-center justify-center mx-auto mb-4 shadow-inner">
          <ShieldCheck :size="32" class="text-teal-400" />
        </div>
        <h3 class="font-extrabold text-white text-2xl tracking-tight">Ready to Encrypt</h3>
        <p class="text-sm font-medium text-slate-400 mt-2">Verify the payload before saving to your secure vault.</p>
      </div>
    </div>

    <!-- Bento Grid Summary -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      
      <!-- General Info -->
      <div class="p-6 bg-slate-950/50 rounded-2xl border border-white/5">
        <h4 class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-4 flex items-center gap-2">
          <FolderOpen :size="12" class="text-indigo-400" /> General
        </h4>
        <div class="space-y-4">
          <div>
            <p class="text-xs text-slate-500 font-medium mb-0.5">Asset Name</p>
            <p class="font-bold text-white text-lg">{{ formData.name }}</p>
          </div>
          <div class="flex gap-6">
            <div>
              <p class="text-xs text-slate-500 font-medium mb-1">Category</p>
              <span class="px-2.5 py-1 rounded-md bg-slate-800 text-slate-300 text-xs font-bold border border-white/5">{{ formData.category }}</span>
            </div>
            <div>
              <p class="text-xs text-slate-500 font-medium mb-1">Type</p>
              <span class="px-2.5 py-1 rounded-md bg-indigo-500/10 text-indigo-400 text-xs font-bold border border-indigo-500/20 flex items-center gap-1.5">
                {{ selectedItemType?.icon || '📄' }} {{ formData.itemTypeName }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Settings & Metadata -->
      <div class="p-6 bg-slate-950/50 rounded-2xl border border-white/5 flex flex-col justify-between space-y-4">
        <div>
          <h4 class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-4 flex items-center gap-2">
            <Settings2 :size="12" class="text-amber-400" /> Configuration
          </h4>
          
          <div class="flex items-center gap-3 p-3 bg-slate-900 rounded-xl border border-white/5">
            <Bell :size="16" class="text-amber-400 shrink-0" />
            <div>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-500">Alert Schedule</p>
              <p class="font-bold text-slate-200 text-sm">
                {{ formData.reminderDaysBefore === null ? 'System Default' : `${formData.reminderDaysBefore} Days Prior` }}
              </p>
            </div>
          </div>
        </div>

        <div v-if="formData.file" class="flex items-center gap-3 p-3 bg-teal-500/10 rounded-xl border border-teal-500/20">
          <Paperclip :size="16" class="text-teal-400 shrink-0" />
          <div class="min-w-0 flex-1">
            <p class="text-[10px] font-bold uppercase tracking-widest text-teal-400/70">Attached File</p>
            <p class="font-bold text-teal-300 text-sm truncate">{{ formData.file.name }}</p>
          </div>
          <p class="text-xs font-bold text-teal-500 shrink-0">{{ formatFileSize(formData.file.size) }}</p>
        </div>
        <div v-else class="flex items-center gap-3 p-3 bg-slate-900 rounded-xl border border-white/5 border-dashed">
          <Paperclip :size="16" class="text-slate-600 shrink-0" />
          <p class="text-xs font-medium text-slate-500 italic">No file attached</p>
        </div>
      </div>

      <!-- Dynamic Fields List -->
      <div v-if="selectedItemType && Object.keys(formData.dynamicFields).length > 0" class="md:col-span-2 p-6 bg-slate-950/50 rounded-2xl border border-white/5">
        <h4 class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-4 flex items-center gap-2">
          <Database :size="12" class="text-teal-400" /> Extracted Metadata
        </h4>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
          <div 
            v-for="field in selectedItemType.fields"
            :key="field.name"
            class="flex flex-col"
          >
            <span class="text-xs text-slate-500 font-medium mb-1">{{ field.label }}</span>
            <span class="font-bold text-slate-200 text-sm bg-slate-900 px-3 py-2 rounded-lg border border-white/5 truncate">
              {{ formatFieldValue(field, formData.dynamicFields[field.name]) }}
            </span>
          </div>
        </div>
      </div>

      <!-- Notes -->
      <div v-if="formData.notes" class="md:col-span-2 p-6 bg-slate-950/50 rounded-2xl border border-white/5">
        <h4 class="text-[10px] font-bold uppercase tracking-widest text-slate-500 mb-4 flex items-center gap-2">
          <FileText :size="12" class="text-slate-400" /> Internal Notes
        </h4>
        <div class="text-sm font-medium text-slate-300 whitespace-pre-wrap leading-relaxed bg-slate-900 p-4 rounded-xl border border-white/5">
          {{ formData.notes }}
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ShieldCheck, FolderOpen, Settings2, Bell, Paperclip, Database, FileText } from "lucide-vue-next"

defineProps({
  formData: Object,
  selectedItemType: Object
})

function formatFieldValue(field, value) {
  if (!value) return 'Not specified'
  
  if (field.field_type === 'date') {
    try {
      // Create date and account for timezone offsets to show intended local date
      const [year, month, day] = value.split('-')
      const date = new Date(year, month - 1, day)
      return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })
    } catch (error) {
      return value
    }
  }
  
  if (field.field_type === 'number') {
    try {
      return parseFloat(value).toLocaleString('en-US')
    } catch (error) {
      return value
    }
  }
  
  return value
}

function formatFileSize(bytes) {
  if (bytes < 1024) return bytes + ' B'
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB'
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB'
}
</script>