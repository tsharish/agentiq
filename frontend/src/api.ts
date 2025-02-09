import router from "@/router"
import axios from "axios"

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

api.interceptors.request.use((config) => {
    let user = null
    let userInStorage = localStorage.getItem('user')
    if (userInStorage) {
        user = JSON.parse(userInStorage)
    }
    if (user && user.access_token) {
        config.headers["Authorization"] = `Bearer ${user.access_token}`
    }
    return config
}, (error) => {
    return Promise.reject(error)
})

api.interceptors.response.use((response) => {
    return response
}, (error) => {
    if (error.response) {
        if (error.response.status === 401) {
            router.push({ name: 'login' })
        }
    }
    return Promise.reject(error)
})

export default api
