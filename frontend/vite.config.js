import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// ✅ Vite config
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': 'http://localhost:8000', // FastAPI backend
    },
  },
  build: {
    outDir: 'dist',
  },
})
