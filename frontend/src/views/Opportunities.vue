<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/api'

const opportunities = ref()

async function loadOpportunities() {
    try {
        const response = await api.get('/opportunities')
        opportunities.value = response.data
    } catch (error) {
        console.log(error)
    }
}

onMounted(async () => {
    loadOpportunities()
})
</script>

<template>
    <DataTable :value="opportunities">
        <template #header>
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xl font-bold">Opportunities</span>
                <Button variant="text" rounded @click="loadOpportunities">
                    <fa-icon icon="fa-solid fa-rotate" />
                </Button>
            </div>
        </template>
        <Column field="id" header="ID"></Column>
        <Column field="name" header="Name"></Column>
        <Column field="customer_name" header="Customer"></Column>
        <Column field="amount" header="Amount"></Column>
        <Column field="stage" header="Stage"></Column>
    </DataTable>
</template>
