# Common Reusable UI Components

This directory contains reusable UI components that follow the Remindes design system.

## Components

### Button
Reusable button component with multiple variants and sizes.

**Props:**
- `variant` - 'primary', 'secondary', 'danger', 'ghost' (default: 'primary')
- `size` - 'sm', 'md', 'lg' (default: 'md')
- `loading` - Boolean (default: false)
- `disabled` - Boolean (default: false)
- `type` - Button type (default: 'button')

**Emits:**
- `click` - Triggered when button is clicked

**Example:**
```vue
<Button variant="primary" size="md" @click="handleClick">
  Click Me
</Button>

<Button variant="danger" :loading="isLoading">
  Delete
</Button>
```

### Card
Base card component with header, content, and footer sections.

**Props:**
- `title` - Card title (optional)
- `noPadding` - Remove default padding (default: false)

**Slots:**
- `default` - Main content area
- `header` - Custom header content
- `footer` - Custom footer content

**Example:**
```vue
<Card title="My Card">
  <p>Card content goes here</p>
</Card>

<Card :noPadding="true">
  <template #header>
    <div class="p-4 bg-gray-50">Custom Header</div>
  </template>
  <div class="p-4">Content</div>
  <template #footer>
    <div class="p-4">Footer</div>
  </template>
</Card>
```

### BaseModal
Generic modal dialog component with teleport and transitions.

**Props:**
- `show` - Boolean to control modal visibility (default: false)
- `title` - Modal title
- `closeable` - Allow closing the modal (default: true)

**Slots:**
- `default` - Modal content
- `footer` - Modal footer (typically for actions)

**Emits:**
- `close` - Triggered when modal is closed

**Example:**
```vue
<BaseModal
  :show="showModal"
  title="Confirm Action"
  @close="showModal = false"
>
  <p>Are you sure you want to continue?</p>
  
  <template #footer>
    <div class="flex gap-3 justify-end">
      <Button variant="secondary" @click="showModal = false">Cancel</Button>
      <Button variant="primary" @click="confirm">Confirm</Button>
    </div>
  </template>
</BaseModal>
```

### Alert
Alert/notification component with different types and icons.

**Props:**
- `type` - 'success', 'error', 'warning', 'info' (default: 'info')
- `message` - Alert message text (required)
- `dismissible` - Show dismiss button (default: false)

**Emits:**
- `dismiss` - Triggered when alert is dismissed

**Example:**
```vue
<Alert
  type="success"
  message="Changes saved successfully!"
  :dismissible="true"
  @dismiss="handleDismiss"
/>

<Alert
  type="error"
  message="An error occurred. Please try again."
/>
```

### LoadingSpinner
Animated loading spinner component.

**Props:**
- `size` - 'sm', 'md', 'lg' (default: 'md')
- `color` - 'teal', 'gray', 'white', 'red', 'blue' (default: 'teal')

**Example:**
```vue
<LoadingSpinner size="md" color="teal" />

<div class="flex items-center gap-2">
  <LoadingSpinner size="sm" />
  <span>Loading...</span>
</div>
```

### EmptyState
Empty state component for when there's no data to display.

**Props:**
- `icon` - Lucide icon component (optional)
- `title` - Main heading (default: 'No items found')
- `message` - Description text (default: 'Get started by adding your first item.')
- `actionText` - Text for action button (optional)

**Slots:**
- `actions` - Custom action buttons

**Emits:**
- `action` - Triggered when action button is clicked

**Example:**
```vue
<EmptyState
  :icon="FileText"
  title="No documents found"
  message="Start by uploading your first document."
  actionText="Upload Document"
  @action="handleUpload"
/>

<EmptyState title="No results" message="Try adjusting your filters.">
  <template #actions>
    <Button @click="clearFilters">Clear Filters</Button>
  </template>
</EmptyState>
```

## Usage

Import components from the common directory:

```vue
<script setup>
import { Button, Card, BaseModal, Alert, LoadingSpinner, EmptyState } from '@/components/common'
</script>
```

Or import individually:

```vue
<script setup>
import Button from '@/components/common/Button.vue'
import Card from '@/components/common/Card.vue'
</script>
```

## Design System

All components follow the Remindes design system:

- **Primary Color:** Gradient from teal-500 to cyan-500
- **Border Radius:** Rounded corners (rounded-xl, rounded-2xl)
- **Shadows:** Subtle shadows for depth
- **Transitions:** Smooth transitions (duration-200, duration-300)
- **Typography:** Clear hierarchy with proper font weights

## Demo

See `ComponentsDemo.vue` for examples of all components in use.
