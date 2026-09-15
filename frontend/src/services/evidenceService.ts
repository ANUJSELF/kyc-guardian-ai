import api from './api'

export const evidenceService = {
  async generatePack(caseId: string) {
    const { data } = await api.get(`/evidence-pack/${caseId}`)
    return data
  },

  async exportPDF(caseId: string) {
    const response = await api.get(`/evidence-pack/${caseId}/pdf`, {
      responseType: 'blob',
    })
    return response.data
  },

  async exportJSON(caseId: string) {
    const response = await api.get(`/evidence-pack/${caseId}/json`)
    return response.data
  },
}
