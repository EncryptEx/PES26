import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import i18n from './i18n'

const app = createApp(App)

// Plugins
app.use(router)
app.use(i18n)

// Mount
app.mount('#app')
