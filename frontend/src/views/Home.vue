<script setup lang="ts">
import axios from 'axios'
import { ref, onMounted } from 'vue'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })
const message = ref('')

onMounted(async () => {
    try {
        const response = await api.get('/')
        message.value = response.data.message
    } catch (error) {
        message.value = "Unable to reach the backend"
        console.log(error)
    }
})

</script>

<template>
    <p>{{ message }}</p>
</template>
