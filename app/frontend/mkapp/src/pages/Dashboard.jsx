import React from 'react'
import { useAppContext } from '../context/AppContext'


export default function Dashboard() {
const { metrics, loading } = useAppContext()


if (loading || !metrics) {
return <div>Carregando métricas...</div>
}


return (
<>
<div className="mt-8">
<h2 className="text-2xl font-semibold text-gray-900 dark:text-white">Principais Indicadores</h2>
<div className="mt-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
<div className="bg-background-light dark:bg-background-dark border border-gray-200 dark:border-gray-800 rounded-xl p-6 shadow-sm hover:shadow-lg transition-shadow duration-300">
<p className="text-base font-medium text-gray-600 dark:text-gray-400">Churn Total</p>
<p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">{Math.round(metrics.churn * 100)}%</p>
</div>


<div className="bg-background-light dark:bg-background-dark border border-gray-200 dark:border-gray-800 rounded-xl p-6 shadow-sm hover:shadow-lg transition-shadow duration-300">
<p className="text-base font-medium text-gray-600 dark:text-gray-400">Retenção</p>
<p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">{Math.round(metrics.retention * 100)}%</p>
</div>


<div className="bg-background-light dark:bg-background-dark border border-gray-200 dark:border-gray-800 rounded-xl p-6 shadow-sm hover:shadow-lg transition-shadow duration-300">
<p className="text-base font-medium text-gray-600 dark:text-gray-400">Novos Clientes</p>
<p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">{metrics.newCustomers}</p>
</div>


<div className="bg-background-light dark:bg-background-dark border border-gray-200 dark:border-gray-800 rounded-xl p-6 shadow-sm hover:shadow-lg transition-shadow duration-300">
<p className="text-base font-medium text-gray-600 dark:text-gray-400">Receita Média</p>
<p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">${metrics.avgRevenue}</p>
</div>
</div>
</div>
</>
)
}