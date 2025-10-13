// Simulated API service. Keep all calls here so components use services instead of fetch directly.
const fakeDelay = (ms = 600) => new Promise((r) => setTimeout(r, ms))


const api = {
async getOverview() {
await fakeDelay(700)
return {
churn: 0.12,
retention: 0.88,
newCustomers: 500,
avgRevenue: 150
}
},


async getClients() {
await fakeDelay(600)
return Array.from({ length: 20 }).map((_, i) => ({
id: i + 1,
name: `Cliente ${i + 1}`,
plan: i % 3 === 0 ? 'Pro' : 'Basic',
lastActive: new Date(Date.now() - i * 86400000).toISOString()
}))
},


// Simulate an endpoint that returns a probability score for churn when given an id
async getChurnProbability(clientId) {
await fakeDelay(450)
// Deterministic pseudo-random for reproducibility
const score = ((clientId * 9301 + 49297) % 233280) / 233280
return { clientId, probability: Number(score.toFixed(2)) }
}
}


export default api