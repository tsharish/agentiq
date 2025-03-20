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
            meta: { requiresAuth: true },
            children: [
                {
                    path: '',
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
                {
                    path: 'events',
                    name: 'events',
                    component: () => import('@/views/Events.vue'),
                    meta: { requiresAuth: true }
                },
            ]
        }
    ],
})

router.beforeEach((to, from, next) => {
    const auth = useAuthStore()

    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (auth.authenticated) {
            next()
        } else {
            next('/login')
        }
    } else {
        next()
    }
})

export default router
