import 'vite/modulepreload-polyfill';
import { createApp } from 'vue';
import cart from './cart.vue';

createApp(cart).mount('#app');