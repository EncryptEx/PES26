<template>
    <aside class="w-64 flex-shrink-0 border-r border-white/10 bg-background-dark flex flex-col justify-between">
        <div class="p-6">
            <div class="flex items-center gap-3 mb-10">
                <div>
                    <h1 class="text-xl font-bold tracking-tighter text-white">
                        GRESCA
                        <span class="text-primary">.</span>
                    </h1>
                    <p class="text-[10px] uppercase tracking-widest text-primary font-bold">
                        {{ t('menu.description') }}
                    </p>
                </div>
            </div>
            <nav class="space-y-2">
                <NavLink v-for="item in menuItems" :key="item.to" :to="item.to" :label="item.label" :icon="item.icon" />
            </nav>
        </div>
    </aside>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

import NavLink from './NavLink.vue'
import IconDashboard from '@/assets/icons/dashboard.svg'
import IconParties from '@/assets/icons/confirmation_number.svg'

const { t } = useI18n()

const menuItems = computed(() => [
  { label: t('menu.dashboard'), to: '/dashboard', icon: IconDashboard },
  { label: t('menu.my-parties'), to: '/my-parties', icon: IconParties }
])
</script>