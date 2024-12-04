<script setup lang="ts">
import axios from 'axios'
import { RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })
const message = ref('')

onMounted(async () => {
    try {
        const response = await api.get('/')
        message.value = response.data.message
    } catch (error) {
        console.log(error)
    }
})

</script>

<template>
    <header>
        <div>
            <p>{{ message }}</p>
        </div>
    </header>

    <RouterView />
</template>
