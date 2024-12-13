<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()
const items = ref([
    {
        label: 'Home',
        icon: 'fa-solid fa-house',
        route: { name: 'home' }
    },
    {
        label: 'Customers',
        icon: 'fa-solid fa-users-line',
        route: { name: 'customers' }
    },
    {
        label: 'Opportunities',
        icon: 'fa-solid fa-money-bills',
        route: { name: 'opportunities' }
    },
])

function logout() {
    auth.logout()
    router.push('/login')
}
</script>

<template>
    <div class="m-1">
        <Menubar :model="items" class="p-1">
            <template #item="{ item, props, hasSubmenu }">
                <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
                    <a v-ripple :href="href" v-bind="props.action" @click="navigate">
                        <fa-icon :icon="item.icon" />
                        <span>{{ item.label }}</span>
                    </a>
                </router-link>
                <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
                    <fa-icon :icon="item.icon" />
                    <span>{{ item.label }}</span>
                    <fa-icon v-if="hasSubmenu" icon="fa-solid fa-angle-down" />
                </a>
            </template>
            <template #end>
                <div>
                    <Button v-tooltip="'Log out'" variant="text" rounded @click="logout">
                        <fa-icon icon="fa-solid fa-arrow-right-from-bracket" />
                    </Button>
                </div>
            </template>
        </Menubar>
    </div>
    <!--<div class="mx-2 p-1 border-solid border rounded-md" style="min-height: 89vh">-->
    <div class="mx-2 p-1">
        <router-view />
    </div>
</template>
