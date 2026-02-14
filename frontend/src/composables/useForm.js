import { reactive, computed } from "vue"

export function useForm() {
  const errors = reactive({})

  function setError(field, message) {
    errors[field] = message
  }

  function clearErrors() {
    Object.keys(errors).forEach(key => {
      delete errors[key]
    })
  }

  function clearError(field) {
    delete errors[field]
  }

  const hasErrors = computed(() => {
    return Object.keys(errors).length > 0
  })

  function getError(field) {
    return errors[field]
  }

  return {
    errors,
    setError,
    clearError,
    clearErrors,
    hasErrors,
    getError
  }
}
