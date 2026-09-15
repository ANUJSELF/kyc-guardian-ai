import api from './api'

export const documentService = {
  async upload(caseId: string, formData: FormData) {
    const { data } = await api.post(`/documents/upload?case_id=${caseId}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    return data
  },

  async getById(documentId: string) {
    const { data } = await api.get(`/documents/${documentId}`)
    return data
  },

  async getPreview(documentId: string) {
    const { data } = await api.get(`/documents/${documentId}/preview`)
    return data
  },

  async confirmField(fieldId: string) {
    const { data } = await api.post(`/reviews/${fieldId}/confirm-field`)
    return data
  },

  async correctField(fieldId: string, correction: any) {
    const { data } = await api.post(`/reviews/${fieldId}/correct-field`, correction)
    return data
  },
}
