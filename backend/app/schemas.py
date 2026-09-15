"""Pydantic schemas for API requests/responses."""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

# ============================================================================
# Case Schemas
# ============================================================================

class CaseCreate(BaseModel):
    """Schema for creating a case."""
    applicant_type: str = Field(..., description="individual or business")
    market: str = Field(..., description="Market/country")
    onboarding_journey: str = Field(..., description="Onboarding journey type")
    description: Optional[str] = Field(None, description="Case description")
    reviewer: Optional[str] = Field(None, description="Assigned reviewer")

class CaseUpdate(BaseModel):
    """Schema for updating a case."""
    status: Optional[str] = None
    description: Optional[str] = None
    reviewer: Optional[str] = None

class CaseResponse(BaseModel):
    """Schema for case response."""
    id: str
    applicant_type: str
    market: str
    status: str
    description: Optional[str]
    reviewer: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# ============================================================================
# Document Schemas
# ============================================================================

class DocumentResponse(BaseModel):
    """Schema for document response."""
    id: str
    case_id: str
    category: str
    file_name: str
    status: str
    ocr_confidence: Optional[float]
    quality_score: Optional[float]
    created_at: datetime

    class Config:
        from_attributes = True

# ============================================================================
# Extracted Field Schemas
# ============================================================================

class ExtractedFieldResponse(BaseModel):
    """Schema for extracted field."""
    id: str
    field_name: str
    masked_value: str
    confidence: float
    page_number: Optional[int]
    extraction_method: str
    review_status: str
    reviewer_correction: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

class FieldCorrection(BaseModel):
    """Schema for field correction."""
    field_id: str
    corrected_value: str
    reason: str = Field(..., description="Correction reason")
    notes: Optional[str] = None

# ============================================================================
# Validation & Exception Schemas
# ============================================================================

class ValidationResultResponse(BaseModel):
    """Schema for validation result."""
    id: str
    rule_id: str
    rule_name: str
    severity: str
    status: str
    message: str
    guidance: Optional[str]

    class Config:
        from_attributes = True

class ExceptionResponse(BaseModel):
    """Schema for exception."""
    id: str
    case_id: str
    exception_type: str
    description: str
    severity: str
    status: str
    reviewer_action: Optional[str]
    reviewer_notes: Optional[str]

    class Config:
        from_attributes = True

class ExceptionResolution(BaseModel):
    """Schema for resolving exception."""
    exception_id: str
    action: str
    notes: str

# ============================================================================
# Cross-Document Comparison Schemas
# ============================================================================

class ComparisonResponse(BaseModel):
    """Schema for cross-document comparison."""
    id: str
    field_name: str
    value_a: str
    value_b: str
    similarity_score: Optional[float]
    result: str
    reviewer_action: Optional[str]

    class Config:
        from_attributes = True

# ============================================================================
# Audit Trail Schemas
# ============================================================================

class AuditEventResponse(BaseModel):
    """Schema for audit event."""
    id: str
    case_id: str
    event_type: str
    actor: str
    role: str
    object_type: Optional[str]
    reason: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

# ============================================================================
# Analytics Schemas
# ============================================================================

class DashboardMetrics(BaseModel):
    """Schema for dashboard metrics."""
    total_cases: int
    cases_requiring_review: int
    cases_missing_info: int
    documents_processed: int
    processing_failures: int
    low_confidence_fields: int
    reviewer_corrections: int
    average_processing_time_minutes: float
    evidence_linked_percentage: float
    exceptions_by_type: Dict[str, int]

# ============================================================================
# Evidence Pack Schemas
# ============================================================================

class EvidencePackResponse(BaseModel):
    """Schema for evidence pack export."""
    case_id: str
    applicant_type: str
    documents_count: int
    fields_extracted: int
    fields_confirmed: int
    fields_corrected: int
    exceptions_resolved: int
    audit_trail_events: int
    processing_time_minutes: float
    review_status: str
    versions: Dict[str, str]
    masked_data: bool
    external_transmission: bool
    exported_at: datetime

class ErrorResponse(BaseModel):
    """Schema for error response."""
    detail: str
    error_code: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
