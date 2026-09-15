# Privacy & Data Protection

**KYC Guardian AI** - Hackathon Prototype

> This document outlines privacy principles, data minimisation strategies, and protection mechanisms.

---

## Privacy by Design

KYC Guardian AI is built with **privacy as a core principle**, not an afterthought:

### Core Privacy Features

✅ **Synthetic Data Only** - No real customer or employee information ever processed  
✅ **Local Processing** - All data stays on user's machine  
✅ **No External Transmission** - No API calls to external services  
✅ **Automatic Masking** - Sensitive values masked before any processing  
✅ **Data Minimisation** - Only required fields extracted  
✅ **User Control** - Reviewer controls what happens to each case  
✅ **Transparency** - Complete audit trail of all processing  
✅ **No Retention Beyond Case** - Demo data can be reset anytime  

---

## Data Classification

### Tier 1: Sensitive Personal Information (SPI)
- Identity document numbers
- Tax identifiers
- Date of birth
- Biometric data (photos, fingerprints)
- Financial account numbers
- Phone numbers
- Email addresses
- Residential address
- Signature images

**Handling**:
- Immediately detected and masked
- Original value never logged
- Placeholder used throughout application
- Mapping kept local to case
- Never sent to external AI service

### Tier 2: Business Sensitive Information
- Legal business names (masked in some contexts)
- Business registration numbers
- Beneficial ownership details
- Director/signatory information
- Business addresses

**Handling**:
- Extracted with evidence references
- Masked before AI processing
- Cross-document consistency checked
- Reviewer-correctable

### Tier 3: Processing & Audit Data
- OCR confidence scores
- Extraction methods used
- Reviewer corrections and reasons
- Case state transitions
- Model/rules versions used

**Handling**:
- Stored in audit trail
- No raw PII included
- Retention based on configuration
- Anonymised in analytics

---

## Data Lifecycle

### Collection

```
User Upload
    ↓
[File Validation]
    ↓
[MIME-type Check] → Reject if unsafe
    ↓
[File Hash] → Detect duplicates
    ↓
[Store Securely] → Outside public directory
    ↓
[OCR/Extraction]
    ↓
[PII Detection & Masking] ← IMMEDIATE MASKING
    ↓
[Masked Processing]
```

### Processing

```
Masked Text
    ↓
[Document Classification]
    ↓
[Field Extraction with Evidence]
    ↓
[Validation Rules]
    ↓
[Human Review]
    ↓
[Confirmation/Correction]
    ↓
[Audit Event]
```

### Retention

```
Case Active
    ↓
[Data Available for Review]
    ↓
Case Archived
    ↓
[Data Retained in Audit Trail]
    ↓
[RESET DEMO DATA]
    ↓
[All Deleted]
```

### Deletion

- Cases can be archived (soft delete)
- Demo data reset clears all cases and documents
- File hashes deleted with documents
- Audit trail trimmed after retention period
- Placeholder mappings discarded

---

## Sensitive Data Masking

### Automatic Detection Patterns

```python
PII_PATTERNS = {
    "IDENTITY_NUMBER": r"\b[A-Z]{2}\d{6,9}\b",  # Example
    "TAX_ID": r"\b\d{2}-\d{7}\b",                 # Example
    "PHONE_NUMBER": r"\+?[0-9]{10,15}",
    "EMAIL_ADDRESS": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "DATE_OF_BIRTH": r"\b(?:19|20)\d{2}[/-]?(?:0[1-9]|1[0-2])[/-]?(?:[0-2][0-9]|3[01])\b",
    "ACCOUNT_NUMBER": r"\b\d{8,17}\b",  # Generic
    "ADDRESS": r"\b\d+\s+[A-Za-z]+\s+(?:Street|Avenue|Road|Drive|Lane)\b",
    # ... more patterns
}
```

### Masking Output

```
Original OCR:
"John Smith, ID: 123456789, DOB: 1985-06-15, lives at 42 Main Street"

Masked Output:
"[PERSON_NAME_01], ID: [ID_NUMBER_01], DOB: [DATE_OF_BIRTH_01], lives at [ADDRESS_01]"

Case-Local Mapping (never shared):
{
  "PERSON_NAME_01": "[ORIGINAL_MASKED]",
  "ID_NUMBER_01": "[ORIGINAL_MASKED]",
  "DATE_OF_BIRTH_01": "[ORIGINAL_MASKED]",
  "ADDRESS_01": "[ORIGINAL_MASKED]"
}
```

### Masking Determinism

- Same value → Same placeholder (within case)
- "John Smith" always → [PERSON_NAME_01]
- "42 Main Street" always → [ADDRESS_01]
- Ensures consistency across documents
- Allows human comparison
- Prevents actual value exposure

---

## Third-Party Data Sharing

### What We DON'T Do

❌ Send data to cloud services  
❌ Use third-party AI APIs  
❌ Share data with external parties  
❌ Store data off-device  
❌ Create cloud backups  
❌ Sell or monetise user data  
❌ Use data for analytics (beyond local aggregates)  
❌ Train models on user data  

### Optional Ollama Integration

If user enables local Ollama:
- Only **masked text** sent to model
- Ollama runs **locally** (not cloud-hosted)
- Model is **user-controlled** (downloaded locally)
- No data leaves the machine
- Can be disabled via configuration

---

## User Consent & Control

### Synthetic Data Disclaimer

Prominent notice on every page:

> "Synthetic demonstration data only. Do not upload customer, colleague, proprietary, restricted or regulated information. This prototype provides document-processing assistance only and does not make KYC, credit, onboarding or customer decisions."

### User Actions

Users can:
- ✅ View all extracted data
- ✅ Correct any extraction
- ✅ Reject unsupported extractions
- ✅ Add reviewer notes
- ✅ Request human escalation
- ✅ View complete audit trail
- ✅ Export masked evidence pack
- ✅ Reset all demo data

Users cannot:
- ❌ Approve a case automatically
- ❌ Export unmasked data
- ❌ Modify audit trail
- ❌ Access another user's cases (demo roles only)

---

## GDPR & Privacy Compliance

### GDPR Article 6 (Lawfulness)

✅ **Consent**: Prototype explicitly labeled as synthetic demo  
✅ **Legitimate Interest**: Document processing assistance only  
✅ **No Data Subject Rights**: Using synthetic data only  

### GDPR Key Principles

| Principle | Implementation |
|-----------|----------------|
| **Lawfulness** | Synthetic data only; no real personal data |
| **Purpose Limitation** | Document processing for demonstration only |
| **Data Minimisation** | Only required fields extracted |
| **Accuracy** | User corrections maintain accuracy |
| **Storage Limitation** | Demo reset clears all data |
| **Integrity** | Append-only audit trail |
| **Confidentiality** | Masking before processing |
| **Accountability** | Complete audit trail provided |

### Right to be Forgotten

✅ Implemented via demo data reset  
✅ All cases and documents deleted  
✅ Database cleared and recreated  
✅ File storage cleaned up  
✅ Audit trail (if retained) anonymised  

---

## Data Protection Impact Assessment (DPIA)

### Risk Rating: LOW

**Reasoning**:
- Synthetic data only (no real personal data)
- Local processing (no external transmission)
- No automated decision-making
- Human oversight required
- Data deletion possible
- Audit trail maintained

### Risk Mitigations

| Risk | Mitigation |
|------|------------|
| Accidental real data upload | Prominent warning; synthetic-only workflow |
| Data breach via API | No external APIs; local processing only |
| Model poisoning | No automatic decisions; human review required |
| Unauthorized access | Local SQLite; file permissions; audit trail |
| Data retention | Demo reset capability; retention config |

---

## Privacy by Configuration

### `.env` Settings

```env
# Masking Controls
ENABLE_PII_MASKING=true
MASK_NAMES=true
MASK_PHONE_NUMBERS=true
MASK_EMAIL_ADDRESSES=true
MASK_IDENTITY_NUMBERS=true
MASK_TAX_IDENTIFIERS=true
MASK_ACCOUNT_NUMBERS=true
MASK_ADDRESSES=true
MASK_DATES_OF_BIRTH=true

# Logging Controls
LOG_SENSITIVE_DATA=false  # Never log raw PII
ENABLE_AUDIT_LOGGING=true
AUDIT_LOG_RETENTION_DAYS=365

# Analytics
ENABLE_SYNTHETIC_ANALYTICS=true  # Aggregates only, no raw data
```

---

## Privacy Testing

```bash
# Privacy-focused tests
pytest backend/tests/privacy/ -v

# Includes:
# - Masking effectiveness
# - No raw PII in logs
# - No sensitive data in exceptions
# - Audit trail integrity
# - DPIA controls
```

---

## Transparency Report

For each case:

```json
{
  "case_id": "case-uuid",
  "data_processed": [
    {"type": "document", "category": "identity"},
    {"type": "field", "name": "full_name", "masked": true}
  ],
  "masking_applied": [
    "PERSON_NAME_01",
    "ID_NUMBER_01",
    "ADDRESS_01"
  ],
  "external_transmission": false,
  "ai_used": "mock_service",
  "human_review": true,
  "audit_trail_events": 24,
  "data_retention": "case_active"
}
```

---

## Privacy Incident Response

If synthetic data is accidentally replaced with real customer data:

1. **Stop Processing** - Immediately halt case processing
2. **Isolate** - Take system offline if necessary
3. **Notify** - Inform stakeholders immediately
4. **Audit** - Review logs for exposure
5. **Remediate** - Wipe database and reinit with demo data
6. **Document** - Create incident report

---

## Future Privacy Enhancements

For production deployment:

- [ ] Database encryption at rest
- [ ] End-to-end encryption for API communication
- [ ] Data anonymisation for analytics
- [ ] Privacy-preserving differential privacy
- [ ] Federated learning (if AI model required)
- [ ] Hardware security module (HSM) integration
- [ ] Privacy audit trail (separate from functional audit)
- [ ] CCPA/LGPD compliance features

---

## References

- [GDPR Article 32 (Security)](https://gdpr-info.eu/art-32-gdpr/)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [OWASP Data Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Data_Protection_Cheat_Sheet.html)
- [ICO Data Protection](https://ico.org.uk/for-organisations/data-protection-module/)

---

**Last Updated**: 2024  
**Status**: Hackathon Prototype  
**Data Classification**: Synthetic Demonstration Only
