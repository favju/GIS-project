import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from "./router"

//createApp(App).mount('#app')

const app = createApp(App)
app.use(router)
//app.component("font-awesome-icon", FontAwesomeIcon)
app.mount("#app")
