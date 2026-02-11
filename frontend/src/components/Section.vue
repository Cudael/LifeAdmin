<template>
  <section class="mb-10">
    
    <!-- Header -->
    <div 
      v-if="title || $slots.header || $slots.action"
      class="flex items-center justify-between mb-6"
      :class="headerClass"
    >
      
      <!-- Left Side: Title + Description -->
      <div class="flex-1">
        <slot name="header">
          <!-- Icon + Title -->
          <div class="flex items-center gap-3 mb-1">
            <!-- Icon Slot -->
            <div
              v-if="icon || $slots.icon"
              class="w-10 h-10 rounded-xl flex items-center justify-center"
              :class="iconBgColor"
            >
              <slot name="icon">
                <component 
                  v-if="icon"
                  :is="icon" 
                  :size="20" 
                  :class="iconColor"
                />
              </slot>
            </div>

            <!-- Title -->
            <h2 
              class="font-bold"
              :class="[
                titleSize === 'sm' ? 'text-lg' : 
                titleSize === 'lg' ? 'text-2xl' : 
                'text-xl',
                titleClass
              ]"
            >
              {{ title }}
            </h2>

            <!-- Badge Slot -->
            <slot name="badge" />
          </div>

          <!-- Description -->
          <p 
            v-if="description || $slots.description"
            class="text-sm text-gray-600"
            :class="descriptionClass"
          >
            <slot name="description">
              {{ description }}
            </slot>
          </p>
        </slot>
      </div>

      <!-- Right Side: Actions -->
      <div 
        v-if="$slots.action"
        class="flex items-center gap-2 ml-4"
      >
        <slot name="action" />
      </div>
    </div>

    <!-- Content -->
    <div :class="contentClass">
      <slot />
    </div>

    <!-- Footer (optional) -->
    <div 
      v-if="$slots.footer"
      class="mt-6"
      :class="footerClass"
    >
      <slot name="footer" />
    </div>

  </section>
</template>

<script setup>
defineProps({
  title: { type: String, default: '' },
  description: { type: String, default: '' },
  icon: { type: [Object, Function], default: null },
  iconBgColor: { type: String, default: 'bg-gray-100' },
  iconColor: { type: String, default: 'text-gray-600' },
  
  titleSize: { 
    type: String, 
    default: 'md',
    validator: (value) => ['sm', 'md', 'lg'].includes(value)
  },
  
  titleClass: { type: String, default: 'text-gray-900' },
  descriptionClass: { type: String, default: '' },
  headerClass: { type: String, default: '' },
  contentClass: { type: String, default: '' },
  footerClass: { type: String, default: '' }
})
</script>