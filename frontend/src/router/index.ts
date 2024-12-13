import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/Login.vue'
import Layout from '@/views/Layout.vue'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/login',
            name: 'login',
            component: Login,
            meta: { guest: true }
        },
        {
            path: '/',
            component: Layout,
            children: [
                {
                    path: '',
                    component: () => import('@/views/Home.vue'),
                    meta: { requiresAuth: true }
                },
                {
                    path: 'home',
                    name: 'home',
                    component: () => import('@/views/Home.vue'),
                    meta: { requiresAuth: true }
                },
                {
                    path: 'customers',
                    name: 'customers',
                    component: () => import('@/views/Customers.vue'),
                    meta: { requiresAuth: true }
                },
                {
                    path: 'opportunities',
                    name: 'opportunities',
                    component: () => import('@/views/Opportunities.vue'),
                    meta: { requiresAuth: true }
                },
            ]
        }
    ],
})

router.beforeEach((to, from, next) => {
    const auth = useAuthStore()

    if (to.matched.some(record => record.meta.requiresAuth)) {
        let user = null
        let userInStorage = localStorage.getItem('user')
        if (userInStorage) {
            user = JSON.parse(userInStorage)
        }
        if ((user && user.access_token) || auth.authenticated) {
            next()
            return
        }
        next('/login')
    } else {
        next()
    }
})

export default router
