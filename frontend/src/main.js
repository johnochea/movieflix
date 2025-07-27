import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

// Adjust the API base URL during production
app.config.globalProperties.$apiBaseUrl = 'http://localhost:8000/api';

app.mount('#app')
