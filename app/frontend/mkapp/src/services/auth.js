import api from "./api";
export async function login(username, password) {

  const response = await api.axios.post("/token/", { username, password });
  const { access, refresh } = response.data;
  localStorage.setItem("access", access);
  localStorage.setItem("refresh", refresh);
  return response.data;
}

export async function refreshToken() {
  const refresh = localStorage.getItem("refresh");
  if (!refresh) return;
  try {
    const response = await api.axios.post("/token/refresh/", { refresh });
    localStorage.setItem("access", response.data.access);
    return response.data.access;
  } catch (err) {
    console.error("Erro ao atualizar token:", err);
  }


}

export async function userProfile() {
  
  try {

    const profile = await api.axios.get("/user/me/")
    return profile

  } catch (error) {
     console.error("❌ Erro em userProfile:", error.response?.data || error.message);
    throw error;
  }
  

}