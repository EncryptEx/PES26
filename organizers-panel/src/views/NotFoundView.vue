<template>
    <div class="flex min-h-screen flex-col items-center justify-center overflow-hidden bg-black p-8 text-center text-white">
        <div class="mb-4" data-purpose="error-code-section">
            <h1
                class="text-[12rem] md:text-[18rem] font-black leading-none bg-gradient-to-br from-[#00f2ff] to-[#00a2ab] bg-clip-text text-transparent animate-glow-primay select-none">
                404
            </h1>
        </div>

        <div class="space-y-4 max-w-2xl" data-purpose="error-message-section">
            <h2 class="text-3xl md:text-4xl font-bold uppercase tracking-widest text-white italic">
                <i18n-t keypath="not-found.title">
                    <template #outstanding>
                        <span class="text-bold text-primary">
                            {{ $t('not-found.outstanding') }}
                        </span>
                    </template>
                </i18n-t>
            </h2>

            <p class="text-gray-400 text-lg md:text-xl font-medium">
                {{ t('not-found.description-1') }}<br />
                {{ t('not-found.description-2') }}
            </p>
        </div>

        <div class="absolute bottom-8 opacity-20" data-purpose="branding-watermark">
            <span class="text-xl font-bold tracking-tighter text-white">GRESCA <span
                    class="text-primary">.</span></span>
        </div>
    </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>