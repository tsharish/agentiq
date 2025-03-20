<script setup lang="ts">
const props = defineProps<{ role: string, message: string }>()
</script>

<template>
    <div v-if="props.role === 'agent'"
        class="flex flex-row items-center rounded-md p-2 mb-3 w-fit bg-blue-50 dark:bg-blue-950">
        <fa-icon icon="fa-solid fa-robot" class="text-blue-600" />
        <span style="white-space: pre-line;" class="ml-4 text-sm text-blue-600 dark:text-blue-400">{{ props.message
            }}</span>
    </div>
    <div v-if="props.role === 'user'"
        class="flex flex-row items-center justify-self-end rounded-md p-2 mb-3 w-fit bg-green-50 dark:bg-green-950">
        <span class="mr-4 text-sm text-green-600 dark:text-green-400">{{ props.message }}</span>
        <fa-icon icon="fa-solid fa-user" class="text-green-600" />
    </div>
</template>
