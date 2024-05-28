import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

const backendPath = '../ecommerce';

export default defineConfig({
  plugins: [vue()],
  base: '/static/vite/',
  server: {
    watch: {
      ignored: [],
    },
  },
  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: `${backendPath}/core/static/vite/`,
    rollupOptions: {
      input: {
        vue_product_show: "./src/apps/product_show/product_show.js",
      },
    },
  },
});
