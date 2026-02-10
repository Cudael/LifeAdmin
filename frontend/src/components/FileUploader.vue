<script setup>
import { ref, watch } from "vue"

const props = defineProps({
  modelValue: File,
  existingFile: String
})

const emit = defineEmits(["update:modelValue"])

const dragOver = ref(false)
const fileName = ref(props.modelValue?.name || null)

function handleFile(e) {
  const file = e.target.files[0]
  if (file) {
    emit("update:modelValue", file)
    fileName.value = file.name
  }
}

function handleDrop(e) {
  e.preventDefault()
  dragOver.value = false

  const file = e.dataTransfer.files[0]
  if (file) {
    emit("update:modelValue", file)
    fileName.value = file.name
  }
}

function removeFile() {
  emit("update:modelValue", null)
  fileName.value = null
}

watch(() => props.modelValue, (newFile) => {
  fileName.value = newFile?.name || null
})
</script>

<template>
  <div>
    <!-- Upload Zone -->
    <label
      class="block border-2 border-dashed rounded-xl p-6 text-center cursor-pointer transition
             hover:border-teal-400 hover:bg-teal-50
             flex flex-col items-center justify-center gap-2"
      :class="dragOver ? 'border-teal-500 bg-teal-50' : 'border-gray-300'"
      @dragover.prevent="dragOver = true"
      @dragleave.prevent="dragOver = false"
      @drop="handleDrop"
    >
      <input type="file" class="hidden" @change="handleFile" />

      <div class="text-gray-600">
        <strong class="text-teal-600">Click to upload</strong> or drag & drop
      </div>

      <div class="text-xs text-gray-400">
        PDF, JPG, PNG — up to 10MB
      </div>
    </label>

    <!-- File Preview -->
    <div v-if="fileName || existingFile" class="mt-4 flex items-center justify-between bg-gray-50 p-3 rounded-lg border">
      <div>
        <p class="text-gray-800 font-medium">{{ fileName || existingFile }}</p>
      </div>

      <button
        @click="removeFile"
        class="text-red-500 text-sm font-medium hover:underline"
      >
        Remove
      </button>
    </div>
  </div>
</template>