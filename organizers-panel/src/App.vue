<script setup>
  import SideBar from './components/layout/SideBar.vue'
</script>

<template>
  <div class="flex h-screen overflow-hidden">
    <SideBar class="w-64 flex-shrink-0 border-r border-white/10 bg-background-dark flex flex-col justify-between" />

    <main class="flex-1 flex flex-col overflow-y-auto bg-[radial-gradient(circle_at_top_right,_var(--tw-gradient-stops))] from-primary/5 via-transparent to-transparent">
      <router-view />
    </main>
  </div>
</template>