<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/api'

const customers = ref()

async function loadCustomers() {
    try {
        const response = await api.get('/customers')
        customers.value = response.data
    } catch (error) {
        console.log(error)
    }
}

onMounted(async () => {
    loadCustomers()
})
</script>

<template>
    <DataTable :value="customers">
        <template #header>
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xl font-bold">Customers</span>
                <Button variant="text" rounded @click="loadCustomers">
                    <fa-icon icon="fa-solid fa-rotate" />
                </Button>
            </div>
        </template>
        <Column field="id" header="ID"></Column>
        <Column field="name" header="Name"></Column>
        <Column field="city" header="City"></Column>
        <Column field="state" header="State"></Column>
        <Column field="country" header="Country"></Column>
    </DataTable>
</template>
