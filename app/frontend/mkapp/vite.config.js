import { defineConfig , loadEnv} from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig(({mode}) =>{
  const env = loadEnv(mode,process.cwd());

  const API_URL = `${env.VITE_BACKEND_URL}`;
  return {
  plugins: [react()],
  server:{
    proxy:{
      '/api':{
        target: API_URL,
        changeOrigin:true,
        secure:false
      }
    }
  }
};
});