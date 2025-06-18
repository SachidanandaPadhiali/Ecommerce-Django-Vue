import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'; // 👈 make sure this path is correct

const app = createApp(App);
app.use(router);
app.mount('#app');