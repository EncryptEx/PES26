<script setup>
  import { RouterView } from 'vue-router'
  import SideBar from '@/components/layout/SideBar.vue'
</script>

<template>
  <div class="flex h-screen overflow-hidden">
    <SideBar v-if="!$route.meta.hideSidebar" />

    <main class="flex-1 flex flex-col overflow-y-auto bg-[radial-gradient(circle_at_top_right,_var(--tw-gradient-stops))] from-primary/5 via-transparent to-transparent">
      <router-view />
    </main>
  </div>
</template>