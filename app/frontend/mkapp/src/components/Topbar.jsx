import React from 'react'
import { useAppContext } from '../context/AppContext'


export default function Topbar() {
const { user } = useAppContext()
return (
<div className="mb-6 flex items-center justify-between">
<div>
<h1 className="text-3xl font-bold text-gray-900 dark:text-white">Visão Geral</h1>
<p className="mt-2 text-lg text-gray-600 dark:text-gray-400">Acompanhe seus principais indicadores de desempenho.</p>
</div>
<div className="flex items-center gap-4">
<div className="text-sm text-gray-600 dark:text-gray-400">{user.name}</div>
</div>
</div>
)
}