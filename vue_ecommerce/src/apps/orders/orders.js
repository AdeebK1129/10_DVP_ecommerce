import 'vite/modulepreload-polyfill';
import { createApp } from 'vue';
import orders from './orders.vue';

createApp(orders).mount('#app');
