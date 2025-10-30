import React from 'react'
import { useAppContext } from '../context/AppContext'


export default function Topbar() {
    const { user } = useAppContext()
    return (
        <div className="mb-6 flex items-center justify-between">
            <div>
                <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Información general</h1>
                <p className="mt-2 text-lg text-gray-600 dark:text-gray-400">Supervise sus indicadores clave de rendimiento.</p>
            </div>
                <div className="flex items-center gap-4">
                <div className="text-sm text-gray-600 dark:text-gray-400">{user.username}</div>
            </div>
        </div>
    )
}