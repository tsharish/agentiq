<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/api'
import EventCard from '@/components/EventCard.vue'

const events = ref()
const date = ref(new Date())

async function loadEvents() {
    try {
        const response = await api.get('/events?date=' + formatDate(date.value))
        events.value = response.data
    } catch (error) {
        console.log(error)
    }
}

onMounted(async () => {
    loadEvents()
})

function formatDate(date: Date) {
    const year = date.getFullYear()
    const month = String(date.getMonth() + 1).padStart(2, '0')
    const day = String(date.getDate()).padStart(2, '0')
    return `${year}-${month}-${day}`
}
</script>

<template>
    <div class="p-4 dark:bg-surface-900 rounded-lg">
        <div class="text-xl font-bold mb-3 text-gray-700 dark:text-white">Events</div>
        <DatePicker v-model="date" size="small" showIcon iconDisplay="input" class="mb-5" />
        <Button variant="text" rounded @click="loadEvents">
            <fa-icon icon="fa-solid fa-rotate" />
        </Button>
        <EventCard v-for="event in events" :name="event.name" :date="event.date" :startTime="event.start_time"
            :endTime="event.end_time" />
    </div>
</template>
