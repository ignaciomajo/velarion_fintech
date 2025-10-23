import React from 'react'
import { NavLink } from 'react-router-dom'
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function LinkItem({ to, children }) {



return (
    <NavLink
        to={to}
        className={({ isActive }) =>
        `flex items-center gap-3 px-4 py-2 rounded-lg transition-colors ${
        isActive ? 'bg-primary/10 dark:bg-primary/20 text-primary font-semibold' : 'hover:bg-primary/10 dark:hover:bg-primary/20 hover:text-primary'
        }`
        }
        >
        {children}
    </NavLink>
    )
}


export default function Sidebar() {
    const { logout } = useAuth();
    const navigate = useNavigate();

    const handleLogout = () => {
        logout();            
        navigate("/login");  
    };
return (
    <aside className="w-64 bg-background-light dark:bg-background-dark border-r border-gray-200 dark:border-gray-800 flex flex-col">
        <div className="p-6">
            <h1 className="text-xl font-bold text-gray-900 dark:text-white">Analytics</h1>
            <p className="text-sm text-gray-500 dark:text-gray-400">Painel de controle</p>
            </div>
                <nav className="flex-1 px-4 py-2">
                    <ul className="space-y-2">
                        <li>
                        <LinkItem to="/">
                        <span>Visão Geral</span>
                        </LinkItem>
                        </li>
                        <li>
                        <LinkItem to="/clients">Clientes</LinkItem>
                        </li>
                        <li>
                        <LinkItem to="/settings">Configurações</LinkItem>
                        </li>
                        <li>
                            <button
                            onClick={handleLogout}
                            className="w-full text-left px-3 py-2 rounded hover:bg-primary/10 dark:hover:bg-primary/20 hover:text-primary"
                            >
                            Sair
                            </button>
                        </li>
                    </ul>
                </nav>
            <div className="mt-auto p-4">
            <LinkItem to="/settings">Configurações</LinkItem>
        </div>
    </aside>
    )
}