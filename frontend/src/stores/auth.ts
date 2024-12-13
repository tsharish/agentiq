import { defineStore } from "pinia"
import { ref } from "vue"
import axios from "axios"

export const useAuthStore = defineStore('auth', () => {
    const authenticated = ref(false)

    async function login(username: string, password: string) {
        const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })
        let formData = new FormData()
        formData.append('username', username)
        formData.append('password', password)

        try {
            const response = await api.post('/login', formData)
            if (response.data.access_token) {
                localStorage.setItem('user', JSON.stringify(response.data))
                authenticated.value = true
            }
        } catch (error: any) {
            authenticated.value = false
        }
    }

    function logout() {
        localStorage.removeItem('user')
        authenticated.value = false
    }

    return { authenticated, login, logout }
})
