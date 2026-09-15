"""SQLAlchemy models for database tables."""

from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text, Float, Boolean, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Case(Base):
    """KYC/KYB Case model."""
    __tablename__ = "cases"
    
    id = Column(String, primary_key=True, index=True)
    applicant_type = Column(String, index=True)  # individual or business
    market = Column(String, index=True)
    onboarding_journey = Column(String)
    description = Column(Text, nullable=True)
    status = Column(String, default="draft", index=True)
    reviewer = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata_json = Column(JSON, nullable=True)

class Document(Base):
    """Document model."""
    __tablename__ = "documents"
    
    id = Column(String, primary_key=True, index=True)
    case_id = Column(String, ForeignKey("cases.id"), index=True)
    category = Column(String, index=True)
    file_name = Column(String)
    file_hash = Column(String, unique=True, index=True)
    file_path = Column(String)
    mime_type = Column(String)
    file_size_mb = Column(Float)
    status = Column(String, default="uploaded", index=True)
    ocr_confidence = Column(Float, nullable=True)
    quality_score = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DocumentClassification(Base):
    """Document classification result."""
    __tablename__ = "document_classifications"
    
    id = Column(String, primary_key=True, index=True)
    document_id = Column(String, ForeignKey("documents.id"), index=True)
    predicted_type = Column(String)
    confidence = Column(Float)
    method = Column(String)  # rules or ml
    evidence = Column(Text, nullable=True)
    reviewer_correction = Column(String, nullable=True)
    correction_reason = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class ExtractedField(Base):
    """Extracted structured field."""
    __tablename__ = "extracted_fields"
    
    id = Column(String, primary_key=True, index=True)
    document_id = Column(String, ForeignKey("documents.id"), index=True)
    field_name = Column(String, index=True)
    masked_value = Column(String)  # Displayed value (masked)
    original_available = Column(Boolean, default=False)
    confidence = Column(Float)
    page_number = Column(Integer, nullable=True)
    source_text = Column(Text, nullable=True)  # Where it came from
    source_bbox = Column(JSON, nullable=True)  # Bounding box if available
    extraction_method = Column(String)  # ocr, ml, manual
    review_status = Column(String, default="pending")  # pending, confirmed, rejected
    reviewer_correction = Column(String, nullable=True)
    correction_reason = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ValidationResult(Base):
    """Validation rule result."""
    __tablename__ = "validation_results"
    
    id = Column(String, primary_key=True, index=True)
    case_id = Column(String, ForeignKey("cases.id"), index=True)
    rule_id = Column(String, index=True)
    rule_name = Column(String)
    severity = Column(String)  # info, warning, error
    status = Column(String)  # passed, failed
    message = Column(Text)
    guidance = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class CrossDocumentComparison(Base):
    """Cross-document field comparison."""
    __tablename__ = "cross_document_comparisons"
    
    id = Column(String, primary_key=True, index=True)
    case_id = Column(String, ForeignKey("cases.id"), index=True)
    field_name = Column(String, index=True)
    document_a_id = Column(String)
    document_b_id = Column(String)
    value_a = Column(String)  # Masked
    value_b = Column(String)  # Masked
    normalized_a = Column(String, nullable=True)
    normalized_b = Column(String, nullable=True)
    similarity_score = Column(Float, nullable=True)
    result = Column(String)  # consistent, inconsistent, missing, unable_to_compare
    reviewer_action = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Exception(Base):
    """Flagged exception or issue."""
    __tablename__ = "exceptions"
    
    id = Column(String, primary_key=True, index=True)
    case_id = Column(String, ForeignKey("cases.id"), index=True)
    document_id = Column(String, nullable=True)
    exception_type = Column(String, index=True)  # missing_doc, low_confidence, etc.
    description = Column(Text)
    severity = Column(String)  # info, warning, error
    status = Column(String, default="open", index=True)  # open, resolved
    reviewer_action = Column(String, nullable=True)
    reviewer_notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)

class AuditEvent(Base):
    """Immutable audit trail event."""
    __tablename__ = "audit_events"
    
    id = Column(String, primary_key=True, index=True)
    case_id = Column(String, ForeignKey("cases.id"), index=True)
    event_type = Column(String, index=True)
    actor = Column(String)
    role = Column(String)
    object_type = Column(String, nullable=True)
    object_id = Column(String, nullable=True)
    previous_masked_value = Column(String, nullable=True)
    new_masked_value = Column(String, nullable=True)
    reason = Column(Text, nullable=True)
    version_ocr = Column(String, nullable=True)
    version_model = Column(String, nullable=True)
    version_rules = Column(String, nullable=True)
    version_prompt = Column(String, nullable=True)
    correlation_id = Column(String, nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

class PIIMask(Base):
    """Locally stored PII mask mapping."""
    __tablename__ = "pii_masks"
    
    id = Column(String, primary_key=True, index=True)
    case_id = Column(String, ForeignKey("cases.id"), index=True)
    placeholder = Column(String, unique=True, index=True)
    pii_type = Column(String)  # name, address, phone, etc.
    created_at = Column(DateTime, default=datetime.utcnow)
