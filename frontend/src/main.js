import { createApp } from 'vue'
import App from './App.vue'
import store from './store/index.js';
import router from './router/index.js'
import './axios'

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

const app = createApp(App)

app.use(store)

app.use(router)

app.mount('#app')


