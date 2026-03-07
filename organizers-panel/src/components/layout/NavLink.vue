<template>
  <RouterLink
    :to="to"
    :class="[
      'flex items-center gap-3 px-4 py-3 rounded-xl transition-all border',
      isActive 
        ? 'bg-primary/10 text-primary border-primary/20'
        : 'text-slate-400 hover:bg-white/5 hover:text-white border-transparent'
    ]"
  >
    <component :is="icon" class="w-5 h-5" />
    <span class="text-sm font-medium">{{ label }}</span>
  </RouterLink>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const props = defineProps({
  to: {
    type: [String, Object],
    required: true
  },
  label: {
    type: String,
    required: true
  },
  icon: {
    type: [Object, Function],
    required: true
  }
})

const route = useRoute()
const isActive = computed(() => route.path === props.to)

</script>