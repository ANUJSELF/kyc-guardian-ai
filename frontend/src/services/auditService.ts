import api from './api'

export const auditService = {
  async getTrail(caseId: string) {
    const { data } = await api.get(`/audit/trail/${caseId}`)
    return data
  },

  async getEventDetails(eventId: string) {
    const { data } = await api.get(`/audit/events/${eventId}`)
    return data
  },
}
