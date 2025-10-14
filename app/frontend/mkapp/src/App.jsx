import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Clients from "./pages/Clients";
import Settings from "./pages/Settings";
import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";
import { useRefreshToken } from "./hooks/useRefreshToken";
import Login from "./pages/Login";
import { useAuth } from "./context/AuthContext";

export default function App() {
  // executa o hook de refresh (renova o token se ainda for válido)
  useRefreshToken();

  const { user } = useAuth(); 

  if (!user) {

    return <Login />;
  }

  return (
    <div className="flex min-h-screen">
      <Sidebar />
      <main className="flex-1 p-6 lg:p-8">
        <div className="max-w-7xl mx-auto">
          <Topbar />
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/clients" element={<Clients />} />
            <Route path="/settings" element={<Settings />} />
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </div>
      </main>
    </div>
  );
}
