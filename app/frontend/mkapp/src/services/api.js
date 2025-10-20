import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000/api", 
});

// --- MOCK / FAKE API SECTION ---
const fakeDelay = (ms = 600) => new Promise((r) => setTimeout(r, ms));

const mockAPI = {
  async getOverview() {
    await fakeDelay(700);
    return {
      churn: 0.12,
      retention: 0.88,
      newCustomers: 500,
      avgRevenue: 150,
    };
  },

  async getClients() {
    // await fakeDelay(600);
    // return Array.from({ length: 20 }).map((_, i) => ({
    //   id: i + 1,
    //   name: `Cliente ${i + 1}`,
    //   plan: i % 3 === 0 ? "Pro" : "Basic",
    //   lastActive: new Date(Date.now() - i * 86400000).toISOString(),
    // }));

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
