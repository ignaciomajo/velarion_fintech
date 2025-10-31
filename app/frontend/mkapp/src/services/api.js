import axios from "axios";

const axiosInstance = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_URL+ "/api"
});

// --- MOCK / FAKE API SECTION ---
const fakeDelay = (ms = 600) => new Promise((r) => setTimeout(r, ms));

const mockAPI = {
  async getOverview() {
   
     try {
      const response = await api.axios.get("/churn-prediction/resumen_riesgo/");
      const resumen = response.data;
      console.log(resumen)
      // Transforma os dados recebidos em métricas agregadas
      const total = resumen.reduce((acc, r) => acc + r.total, 0);
      console.log(total)
      const critical = resumen.find(r => r.riesgo === "Critical")?.total || 0;
      const alto = resumen.find(r => r.riesgo === "Alto")?.total || 0;
      const medio = resumen.find(r => r.riesgo === "Medio")?.total || 0;
      const bajo = resumen.find(r => r.riesgo === "Bajo")?.total || 0;
      // Exemplo de cálculo (ajuste conforme a lógica do seu negócio)
      const churn = total > 0 ? (critical + alto) / total : 0;
      const retention = 1 - churn;

      return {
        churn: churn.toFixed(2),          // 0.12
        retention: retention.toFixed(2),  // 0.88
        critical,
        alto,
        medio,
        bajo,
        total,
      };

    } catch (error) {
      console.error("❌ Erro Resumen:", error.response?.data || error.message);
      throw error;
    }
  }
,

  async getClients() {

     try {
      const profile = await api.axios.get("/churn-prediction/?page=1&page_size=50")
      return profile.data.results

    } catch (error) {
      console.error("❌ Erro em userProfile:", error.response?.data || error.message);
      throw error;
    }
  },

  async getChurnProbability(clientId) {
    await fakeDelay(450);
    const score = ((clientId * 9301 + 49297) % 233280) / 233280;
    return { clientId, probability: Number(score.toFixed(2)) };
  },
};

// --- REAL AXIOS INSTANCE SECTION ---

// Intercepta e adiciona o token JWT
axiosInstance.interceptors.request.use(
  (config) => {
    const access = localStorage.getItem("access");
    if (access) config.headers.Authorization = `Bearer ${access}`;
    return config;
  },
  (error) => Promise.reject(error)
);


const api = {
  ...mockAPI,
  axios: axiosInstance, // agora api.axios.get(...) 
};

export default api;
