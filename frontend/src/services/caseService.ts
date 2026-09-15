import api from './api'

export interface Case {
  id: string
  applicant_type: string
  market: string
  status: string
  description?: string
  created_at: string
}

export const caseService = {
  async getAll() {
    const { data } = await api.get('/cases')
    return data
  },

  async getById(caseId: string) {
    const { data } = await api.get(`/cases/${caseId}`)
    return data
  },

  async create(caseData: any) {
    const { data } = await api.post('/cases', caseData)
    return data
  },

  async update(caseId: string, caseData: any) {
    const { data } = await api.put(`/cases/${caseId}`, caseData)
    return data
  },

  async delete(caseId: string) {
    await api.delete(`/cases/${caseId}`)
  },
}
