<script setup lang="ts">
const props = defineProps<{ name: string, date: string, startTime: string, endTime: string }>()
</script>

<template>
    <div
        class="text-gray-600 dark:text-white border-solid border-2 border-l-8 rounded-lg border-fuchsia-600 mb-3 p-3 max-w-full md:max-w-xl">
        <div class="font-semibold">{{ props.name }}</div>
        <div class="mt-1">
            <fa-icon icon="fa-solid fa-clock" class="mr-1" /> {{ props.date }}: {{ props.startTime }} - {{ props.endTime
            }}
        </div>
    </div>
</template>
