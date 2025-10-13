import React, { useEffect, useState } from 'react'
import api from '../services/api'


export default function Clients() {
const [clients, setClients] = useState(null)
const [loading, setLoading] = useState(false)


useEffect(() => {
setLoading(true)
api.getClients().then((data) => {
setClients(data)
setLoading(false)
})
}, [])


if (loading || !clients) return <div>Carregando clientes...</div>


return (
<div>
<h2 className="text-2xl font-semibold text-gray-900 dark:text-white">Clientes</h2>
<div className="mt-4 grid gap-3">
{clients.map((c) => (
<ClientCard key={c.id} client={c} />
))}
</div>
</div>
)
}


function ClientCard({ client }) {
const [prob, setProb] = useState(null)
const [loading, setLoading] = useState(false)


const loadProb = async () => {
setLoading(true)
const r = await api.getChurnProbability(client.id)
setProb(r.probability)
setLoading(false)
}


return (
<div className="p-4 bg-background-light dark:bg-background-dark border border-gray-200 dark:border-gray-800 rounded-lg flex items-center justify-between">
<div>
<div className="font-medium">{client.name}</div>
<div className="text-sm text-gray-500">Plano: {client.plan}</div>
</div>
<div className="flex items-center gap-4">
<div className="text-sm">{prob == null ? '—' : `${Math.round(prob * 100)}%`}</div>
<button onClick={loadProb} className="px-3 py-1 rounded-lg bg-primary/10 dark:bg-primary/20 hover:bg-primary/20 transition">
{loading ? '...' : 'Calcular risco'}
</button>
</div>
</div>
)
}