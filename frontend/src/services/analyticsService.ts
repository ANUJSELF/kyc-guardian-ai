import api from './api'

export const analyticsService = {
  async getDashboard() {
    const { data } = await api.get('/analytics/dashboard')
    return data
  },

  async getCaseMetrics(caseId: string) {
    const { data } = await api.get(`/analytics/cases/${caseId}`)
    return data
  },
}
