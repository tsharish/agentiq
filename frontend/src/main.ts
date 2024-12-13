import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faArrowRightFromBracket, faHouse, faUsersLine, faMoneyBills, faAngleDown } from '@fortawesome/free-solid-svg-icons'
import PrimeVue from 'primevue/config'
import Aura from '@primevue/themes/aura'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import Menubar from 'primevue/menubar'
import Message from 'primevue/message'
import Tooltip from 'primevue/tooltip'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            cssLayer: {
                name: 'primevue',
                order: 'tailwind-base, primevue, tailwind-utilities'
            }
        }
    }
})

// Add font awesome icons
library.add(faArrowRightFromBracket, faHouse, faUsersLine, faMoneyBills, faAngleDown)

app.directive('tooltip', Tooltip)
app.component('fa-icon', FontAwesomeIcon)
app.component('Button', Button)
app.component('InputText', InputText)
app.component('Menubar', Menubar)
app.component('Message', Message)

app.mount('#app')
