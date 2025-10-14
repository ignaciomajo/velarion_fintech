import { createContext, useContext, useState, useEffect} from "react";

const AuthContext = createContext();

export function AuthProvider({ children }) {
const [user, setUser] = useState(() => {
    // 🔹 tenta recuperar o user salvo no localStorage
    const storedUser = localStorage.getItem("user");
    return storedUser ? JSON.parse(storedUser) : null;
  });

  // 🔹 sempre que o user mudar, salva no localStorage
  useEffect(() => {
    if (user) {
      localStorage.setItem("user", JSON.stringify(user));
    } else {
      localStorage.removeItem("user");
    }
  }, [user]);

    const logout = () => {
    setUser(null);
    localStorage.removeItem("user");
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
  };

  return (
    <AuthContext.Provider value={{ user, setUser,logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
