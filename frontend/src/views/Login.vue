<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()
const username = ref('')
const password = ref('')
const message = ref('')

async function login() {
    if (username.value.trim() === '' || password.value.trim() === '') {
        message.value = 'Username and Password are required fields'
    } else {
        await auth.login(username.value, password.value)

        if (auth.authenticated) {
            password.value = ''
            message.value = ''
            router.push({ name: 'home' })
        } else {
            password.value = ''
            message.value = 'Login error - Try again'
        }
    }
}
</script>

<template>
    <div class="min-h-screen flex items-center justify-center">
        <div class="flex flex-col w-80 p-5 bg-surface-100 dark:bg-surface-900 rounded-lg">
            <p class="text-center text-2xl font-medium text-color mb-5">Welcome</p>
            <InputText id="username" type="text" v-model="username" placeholder="Username" class="mb-5"
                @keyup.enter="login" />
            <InputText id="password" type="password" v-model="password" placeholder="Password" class="mb-5"
                @keyup.enter="login" />
            <Button label="Log on" @click="login" class="mb-5"></Button>
            <Message severity="error" v-if="message" :closable="false">{{ message }}</Message>
        </div>
    </div>
</template>
