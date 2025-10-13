import React, { createContext, useState, useContext, useEffect } from 'react'
import api from '../services/api'


const AppContext = createContext(null)


export function AppProvider({ children }) {
const [user, setUser] = useState({ name: 'Carlos', role: 'admin' })
const [metrics, setMetrics] = useState(null)
const [loading, setLoading] = useState(false)


useEffect(() => {
setLoading(true)
api.getOverview().then((data) => {
setMetrics(data)
setLoading(false)
})
}, [])


return (
<AppContext.Provider value={{ user, setUser, metrics, loading }}>
{children}
</AppContext.Provider>
)
}


export function useAppContext() {
return useContext(AppContext)
}