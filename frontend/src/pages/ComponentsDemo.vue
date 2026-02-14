<template>
  <div class="p-8 space-y-8 bg-gray-50 min-h-screen">
    <h1 class="text-3xl font-bold text-gray-900 mb-8">Common Components Demo</h1>

    <!-- Button Demo -->
    <section class="bg-white rounded-2xl p-6 shadow">
      <h2 class="text-xl font-bold mb-4">Button Component</h2>
      <div class="space-y-4">
        <div class="flex flex-wrap gap-3">
          <Button variant="primary" size="sm">Primary Small</Button>
          <Button variant="primary" size="md">Primary Medium</Button>
          <Button variant="primary" size="lg">Primary Large</Button>
        </div>
        <div class="flex flex-wrap gap-3">
          <Button variant="secondary">Secondary</Button>
          <Button variant="danger">Danger</Button>
          <Button variant="ghost">Ghost</Button>
        </div>
        <div class="flex flex-wrap gap-3">
          <Button :loading="true">Loading</Button>
          <Button :disabled="true">Disabled</Button>
        </div>
      </div>
    </section>

    <!-- Card Demo -->
    <section class="bg-white rounded-2xl p-6 shadow">
      <h2 class="text-xl font-bold mb-4">Card Component</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card title="Card with Title">
          <p class="text-gray-600">This is a card with a title prop.</p>
        </Card>
        
        <Card :noPadding="true">
          <template #header>
            <div class="p-4 bg-gradient-to-r from-teal-50 to-cyan-50">
              <h3 class="font-bold">Custom Header Slot</h3>
            </div>
          </template>
          <div class="p-4">
            <p class="text-gray-600">Card with custom header and no padding</p>
          </div>
          <template #footer>
            <div class="p-4 bg-gray-50 text-sm text-gray-500">
              Footer content
            </div>
          </template>
        </Card>
      </div>
    </section>

    <!-- Alert Demo -->
    <section class="bg-white rounded-2xl p-6 shadow">
      <h2 class="text-xl font-bold mb-4">Alert Component</h2>
      <div class="space-y-3">
        <Alert type="success" message="Operation completed successfully!" :dismissible="true" />
        <Alert type="error" message="An error occurred. Please try again." :dismissible="true" />
        <Alert type="warning" message="This action may have consequences." :dismissible="true" />
        <Alert type="info" message="Here's some helpful information." :dismissible="true" />
      </div>
    </section>

    <!-- Loading Spinner Demo -->
    <section class="bg-white rounded-2xl p-6 shadow">
      <h2 class="text-xl font-bold mb-4">Loading Spinner Component</h2>
      <div class="flex items-center gap-8">
        <div>
          <p class="text-sm text-gray-600 mb-2">Small</p>
          <LoadingSpinner size="sm" />
        </div>
        <div>
          <p class="text-sm text-gray-600 mb-2">Medium</p>
          <LoadingSpinner size="md" />
        </div>
        <div>
          <p class="text-sm text-gray-600 mb-2">Large</p>
          <LoadingSpinner size="lg" />
        </div>
        <div>
          <p class="text-sm text-gray-600 mb-2">Different Colors</p>
          <div class="flex gap-3">
            <LoadingSpinner color="teal" />
            <LoadingSpinner color="red" />
            <LoadingSpinner color="blue" />
          </div>
        </div>
      </div>
    </section>

    <!-- Empty State Demo -->
    <section class="bg-white rounded-2xl p-6 shadow">
      <h2 class="text-xl font-bold mb-4">Empty State Component</h2>
      <Card>
        <EmptyState
          :icon="FileText"
          title="No documents found"
          message="Start by uploading your first document to get organized."
          actionText="Upload Document"
          @action="handleAction"
        />
      </Card>
    </section>

    <!-- Modal Demo -->
    <section class="bg-white rounded-2xl p-6 shadow">
      <h2 class="text-xl font-bold mb-4">Base Modal Component</h2>
      <Button @click="showModal = true">Open Modal</Button>
      
      <BaseModal
        :show="showModal"
        title="Example Modal"
        :closeable="true"
        @close="showModal = false"
      >
        <p class="text-gray-600 mb-4">
          This is a simple modal dialog. It can contain any content you want.
        </p>
        <p class="text-gray-600">
          Click the X button or outside the modal to close it.
        </p>
        
        <template #footer>
          <div class="flex gap-3 justify-end">
            <Button variant="secondary" @click="showModal = false">Cancel</Button>
            <Button variant="primary" @click="handleModalAction">Confirm</Button>
          </div>
        </template>
      </BaseModal>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { FileText } from 'lucide-vue-next'
import { Button, Card, BaseModal, Alert, LoadingSpinner, EmptyState } from '../components/common'

const showModal = ref(false)

function handleAction() {
  alert('Action button clicked!')
}

function handleModalAction() {
  alert('Modal confirmed!')
  showModal.value = false
}
</script>
