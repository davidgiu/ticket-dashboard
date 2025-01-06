import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3001, // Changez 3001 par le port de votre choix
    host: '0.0.0.0', // Permet d'accéder via l'adresse IP locale
  },
});
