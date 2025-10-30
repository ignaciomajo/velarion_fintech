import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { login , userProfile} from "../services/auth";
import { useAuth } from "../context/AuthContext";
import logo from "../assets/velarion_logo.png";


export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const { setUser } = useAuth();
  

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      await login(username, password);
      const profile = await userProfile()
      if (profile) {
        setUser(profile.data)
        navigate("/dashboard");
      }else{
        navigate("/login");
      }
    } catch {
      setError("Usuário ou senha inválidos");
    }
  }

  return (
    <div className="flex dark:bg-background-dark  justify-center items-center h-screen bg-gray-100">
      <form
        onSubmit={handleSubmit}
        className="dark:bg-background-dark p-6 rounded-xl shadow-md w-80"
      >
        <img src={logo} alt="Logo" className="w-30 h-auto mb-2" />
        <h1 className="text-xl font-semibold mb-4 text-center">Login</h1>
        {error && <p className="text-red-500 text-sm mb-2">{error}</p>}
        <input
          type="text"
          placeholder="Nombre de usuario"
          className="border w-full p-2 mb-2 rounded"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Contraseña"
          className="border w-full p-2 mb-4 rounded"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button
          type="submit"
          className="bg-blue-600 text-white w-full py-2 rounded hover:bg-blue-700"
        >
          Iniciar sesión
        </button>
      </form>
    </div>
  );
}
