export interface DashboardMetrics {
  total_cases: number
  cases_requiring_review: number
  documents_processed: number
  low_confidence_fields: number
  reviewer_corrections: number
  average_processing_time_minutes: number
  exceptions_by_type: Record<string, number>
}

export interface CaseStatus {
  draft: string
  documents_uploaded: string
  processing: string
  review_required: string
  information_missing: string
  ready_for_review: string
  processing_failed: string
  review_completed: string
  archived: string
}

export interface DocumentCategory {
  individual: string[]
  business: string[]
}

export const CASE_STATUSES: CaseStatus = {
  draft: 'Draft',
  documents_uploaded: 'Documents Uploaded',
  processing: 'Processing',
  review_required: 'Review Required',
  information_missing: 'Information Missing',
  ready_for_review: 'Ready for Human Review',
  processing_failed: 'Processing Failed',
  review_completed: 'Review Completed',
  archived: 'Archived',
}

export const DOCUMENT_CATEGORIES: DocumentCategory = {
  individual: [
    'Identity Document',
    'Address Proof',
    'Tax Identification',
    'Bank Statement',
    'Application Form',
    'Supporting Declaration',
    'Other Supporting Document',
  ],
  business: [
    'Certificate of Incorporation',
    'Business Registration',
    'Registered Address Proof',
    'Ownership Declaration',
    'Authorised Signatory Document',
    'Beneficial Ownership Sample',
    'Tax Registration Sample',
    'Other Business Document',
  ],
}

export const MARKETS = [
  { key: 'india', text: 'India' },
  { key: 'hong_kong', text: 'Hong Kong' },
  { key: 'singapore', text: 'Singapore' },
  { key: 'taiwan', text: 'Taiwan' },
  { key: 'thailand', text: 'Thailand' },
]

export const DEMO_DISCLAIMER =
  'Synthetic demonstration data only. Do not upload customer, colleague, proprietary, restricted or regulated information. This prototype provides document-processing assistance only and does not make KYC, credit, onboarding or customer decisions.'
