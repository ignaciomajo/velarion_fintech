import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Clients from './pages/Clients'
import Settings from './pages/Settings'
import Sidebar from './components/Sidebar'
import Topbar from './components/Topbar'


export default function App() {
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
</Routes>
</div>
</main>
</div>
)
}