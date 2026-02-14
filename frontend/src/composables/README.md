# Vue 3 Composables

This directory contains reusable composable functions following the Vue 3 Composition API patterns.

## Available Composables

### useAuth
Authentication state and methods.

```js
import { useAuth } from '@/composables'

const { user, isAuthenticated, loading, login, logout, register, checkAuthStatus } = useAuth()

// Login
await login('user@example.com', 'password')

// Register
await register('user@example.com', 'password')

// Logout
logout()

// Check auth status
const isValid = await checkAuthStatus()
```

### useApi
API call wrapper with built-in error handling.

```js
import { useApi } from '@/composables'

const { api } = useApi()

// GET request
const data = await api.get('/items')

// POST request
const newItem = await api.post('/items', { name: 'Item' })

// PUT request
const updated = await api.put('/items/1', { name: 'Updated' })

// PATCH request
const patched = await api.patch('/items/1', { status: 'done' })

// DELETE request
await api.delete('/items/1')
```

### useModal
Modal state management.

```js
import { useModal } from '@/composables'

const { isOpen, open, close, toggle } = useModal()

// Open modal
open()

// Close modal
close()

// Toggle modal
toggle()

// Use in template
<div v-if="isOpen">Modal content</div>
```

### useForm
Form validation helpers.

```js
import { useForm } from '@/composables'

const { errors, setError, clearError, clearErrors, hasErrors, getError } = useForm()

// Set an error
setError('email', 'Email is required')

// Get an error
const emailError = getError('email')

// Clear specific error
clearError('email')

// Clear all errors
clearErrors()

// Check if there are any errors
if (hasErrors.value) {
  console.log('Form has errors')
}

// Use in template
<span v-if="errors.email">{{ errors.email }}</span>
```

### usePagination
Pagination logic.

```js
import { usePagination } from '@/composables'

const {
  currentPage,
  itemsPerPage,
  totalItems,
  totalPages,
  hasNextPage,
  hasPrevPage,
  startIndex,
  endIndex,
  nextPage,
  prevPage,
  goToPage,
  reset,
  setTotalItems,
  setItemsPerPage
} = usePagination(10) // Initial items per page

// Set total items
setTotalItems(100)

// Navigate
nextPage()
prevPage()
goToPage(5)

// Reset to first page
reset()

// Change items per page
setItemsPerPage(20)

// Use in template
<div>
  Page {{ currentPage }} of {{ totalPages }}
  <button @click="prevPage" :disabled="!hasPrevPage">Previous</button>
  <button @click="nextPage" :disabled="!hasNextPage">Next</button>
</div>
```

## Importing

You can import composables individually:

```js
import { useAuth } from '@/composables/useAuth'
import { useApi } from '@/composables/useApi'
```

Or import multiple at once from the index:

```js
import { useAuth, useApi, useModal, useForm, usePagination } from '@/composables'
```
