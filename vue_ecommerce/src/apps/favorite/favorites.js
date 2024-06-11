import 'vite/modulepreload-polyfill';
import { createApp } from 'vue';
import Favorites from './favorites.vue';

createApp(Favorites).mount('#app');
