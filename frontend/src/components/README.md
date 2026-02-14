# Component Organization

This document describes the component structure of the LifeAdmin frontend.

## Overview

All components are organized by feature/domain for better maintainability and scalability.

## Directory Structure

```
components/
├── common/          # Reusable UI components
├── auth/            # Authentication components
├── items/           # Item management components
├── landing/         # Landing page sections
├── layout/          # Layout components (headers, footers)
├── profile/         # User profile components
├── settings/        # Settings page components
└── wizard/          # Item creation wizard steps
```

## Component Categories

### Common Components (`common/`)

Reusable UI primitives used throughout the application.

**Components:**
- `Button.vue` - Button with variants (primary, secondary, danger, ghost)
- `Card.vue` - Base card component with header/footer slots
- `BaseModal.vue` - Generic modal component
- `Alert.vue` - Alert/notification display (success, error, warning, info)
- `LoadingSpinner.vue` - Loading indicator
- `EmptyState.vue` - Empty state display

**Usage:**
```vue
<script setup>
import { Button, Card, Alert } from '@/components/common'
</script>

<template>
  <Card title="Welcome">
    <Alert type="success" message="Login successful!" />
    <Button variant="primary" @click="handleClick">
      Get Started
    </Button>
  </Card>
</template>
```

### Auth Components (`auth/`)

Authentication-related components.

**Components:**
- `AuthLayout.vue` - Shared layout wrapper for auth pages
- `LoginForm.vue` - Email/password login form
- `AuthErrorAlert.vue` - Error display for auth pages
- `GoogleSignInButton.vue` - Google OAuth button
- `OrDivider.vue` - "OR" divider with lines

**Used by:** LoginPage, RegisterPage, ForgotPasswordPage

### Items Components (`items/`)

Item management components.

**Components:**
- `ItemsHeader.vue` - Page header with "Add Item" button
- `ItemsInsights.vue` - Statistics cards
- `ItemsFilters.vue` - Filter controls (category, status)
- `ItemsEmptyState.vue` - Empty state display
- `ItemGrid.vue` - Grid display of items (existing)
- `FilterBar.vue` - Category filter bar (existing)

**Used by:** ItemsPage

### Landing Components (`landing/`)

Landing page section components.

**Components:**
- `HeroSection.vue` - Hero with animated stats
- `FeaturesSection.vue` - Features grid
- `HowItWorksSection.vue` - Process steps
- `WhoItsForSection.vue` - Target audience
- `WhyItMattersSection.vue` - Problem statement
- `SecuritySection.vue` - Security features
- `TestimonialsSection.vue` - Customer reviews
- `PricingSection.vue` - Pricing tiers
- `FAQSection.vue` - FAQ accordion
- `CTASection.vue` - Call-to-action

**Used by:** LandingPage

### Layout Components (`layout/`)

Page layout components (existing).

**Components:**
- `AppHeader.vue` - Main application header
- `AppFooter.vue` - Footer
- `DashboardHeader.vue` - Dashboard-specific header
- `MobileHeader.vue` - Mobile navigation
- `MobileDrawer.vue` - Mobile menu drawer

### Profile & Settings (`profile/`, `settings/`)

User profile and settings components (existing).

**Components:**
- `ProfileSettings.vue` - Profile information form
- `SecuritySettings.vue` - Password change form
- `AccountSettings.vue` - Account preferences
- `PreferencesSettings.vue` - Display preferences
- `DangerZone.vue` - Account deletion

## Component Guidelines

### Size Limits

- ✅ Keep components **under 300 lines**
- ✅ Extract reusable parts into smaller components
- ✅ Use composables for complex logic

### Composition API

All new components use Vue 3 Composition API with `<script setup>`:

```vue
<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  title: String,
  items: Array
})

const emit = defineEmits(['update', 'delete'])

const count = computed(() => props.items.length)
</script>
```

### Props and Events

- Use **props** for data flow down
- Use **emits** for data flow up
- Avoid prop mutation

```vue
<script setup>
// Good ✅
const props = defineProps({
  modelValue: String
})
const emit = defineEmits(['update:modelValue'])

const updateValue = (newValue) => {
  emit('update:modelValue', newValue)
}
</script>
```

### Styling

- Use **Tailwind CSS** utility classes
- Follow design system:
  - Primary gradient: `from-teal-500 to-cyan-500`
  - Border radius: `rounded-xl`, `rounded-2xl`
  - Shadows: `shadow-lg`, `shadow-xl`

### Accessibility

- Use semantic HTML
- Add ARIA labels where needed
- Ensure keyboard navigation

```vue
<button
  aria-label="Close modal"
  @click="close"
  @keydown.esc="close"
>
  <XIcon />
</button>
```

## Using Composables

Extract complex logic into composables:

```vue
<script setup>
import { useAuth, useModal } from '@/composables'

const { user, isAuthenticated, login } = useAuth()
const { isOpen, open, close } = useModal()
</script>
```

Available composables:
- `useAuth` - Authentication state
- `useApi` - API calls
- `useModal` - Modal state
- `useForm` - Form validation
- `usePagination` - Pagination logic

## Best Practices

1. **Single Responsibility** - Each component should do one thing well
2. **Composition over Inheritance** - Use composables and slots
3. **Props Validation** - Always validate prop types
4. **Event Naming** - Use kebab-case for events
5. **File Naming** - Use PascalCase for component files
6. **Extract Logic** - Move complex logic to composables
7. **Keep Templates Simple** - Extract complex conditionals to computed

## Creating New Components

1. Choose the appropriate directory
2. Create a new `.vue` file in PascalCase
3. Use `<script setup>` syntax
4. Define props and emits
5. Extract logic to composables if needed
6. Add to the directory's `index.js` if creating a collection

## Testing

(TODO: Add testing guidelines once testing infrastructure is set up)

## Performance

- Use `v-show` for frequently toggled elements
- Use `v-if` for conditionally rendered elements
- Lazy load heavy components with `defineAsyncComponent`
- Use `v-once` for static content

## Future Improvements

- [ ] Add Storybook for component documentation
- [ ] Add component unit tests
- [ ] Create design tokens for theming
- [ ] Add component performance monitoring
