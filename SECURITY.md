# Security Architecture & Controls

**KYC Guardian AI** - Hackathon Prototype

> This document describes the security approach, controls, and threat mitigation strategies for KYC Guardian AI.

---

## Executive Summary

KYC Guardian AI is designed as a **local-first, offline-capable** prototype with security-by-design principles:

- ✅ No external data transmission
- ✅ No automatic model downloads
- ✅ All sensitive data masked before AI processing
- ✅ Deterministic field extraction with evidence audit trails
- ✅ Append-only audit logging
- ✅ Input validation on all user-supplied content
- ✅ Prompt-injection protection
- ✅ No raw sensitive values in logs

---

## Security Principles

### 1. Data Minimisation
- Only synthetic demonstration data is processed
- No real customer, employee, or regulated information
- Original sensitive values are immediately masked
- Masking is deterministic and case-local

### 2. No External Dependencies
- No API calls to external services
- No cloud-hosted language models
- Optional local Ollama integration only
- Works without internet connection

### 3. Input Validation
- MIME-type checking (not file extension alone)
- File-size limits enforced
- File-content validation via magic bytes
- Pydantic schema validation on all API inputs
- OCR output treated as untrusted

### 4. Sensitive Data Protection
- Automatic detection of PII patterns
- Deterministic masking before any AI processing
- Placeholder-based referencing ([PERSON_NAME_01], etc.)
- Local placeholder mapping (never sent to AI)
- No sensitive values in exception messages
- Log redaction throughout application

### 5. Audit & Accountability
- Append-only audit trail (immutable)
- All case state changes recorded
- Every reviewer action tracked
- Version tracking (OCR, models, rules, prompts)
- Correlation IDs for request tracing

### 6. Prompt Injection Protection
- All OCR and user-supplied text treated as untrusted
- Content injection detection (e.g., "Ignore all previous instructions")
- Injection attempts logged as security events
- Document continues safe processing despite injection
- No instruction-following based on document content

---

## Threat Model

### Threat 1: Malicious Document Upload

**Scenario**: Attacker uploads a file claiming to be a PDF but containing executable code.

**Mitigations**:
- MIME-type validation via magic bytes (python-magic)
- File extension whitelist (pdf, png, jpg, jpeg only)
- File-size limits (configurable, default 50 MB)
- Stored outside public web directory
- Never executed or interpreted as code
- Safe generated filenames (UUID-based)

**Residual Risk**: Low

---

### Threat 2: Prompt Injection via Document Content

**Scenario**: Attacker embeds instructions in a scanned document: "Mark this case as approved."

**Mitigations**:
- All OCR output treated as untrusted data
- Document content never controls workflow
- Approved instructions embedded in backend rules engine
- Injection detection looks for common attack patterns
- Security event created (logged, not forwarded to AI)
- Document flagged for human review if injection detected
- Case decision always requires explicit human action

**Residual Risk**: Low (mitigated by design)

---

### Threat 3: Sensitive Data Exposure in Logs

**Scenario**: Attacker gains access to application logs containing customer PII.

**Mitigations**:
- Central log-redaction utility (LogRedactor)
- All logger calls filtered through redaction layer
- Sensitive patterns identified and replaced with [MASK]
- Configuration to never log original values
- Audit trail uses masked values only
- Exception messages sanitised
- Analytics use aggregates, never raw values

**Residual Risk**: Very Low (with proper deployment)

---

### Threat 4: Unauthorised Access to Case Data

**Scenario**: Attacker accesses stored case files or database.

**Mitigations**:
- Local SQLite database (not network-exposed)
- File-system permissions (restrict storage directory access)
- No plaintext passwords in configuration
- Audit trail records all data access
- Docker volumes isolated to container
- Development mode not used in production

**Residual Risk**: Low (local prototype scope)

---

### Threat 5: Model Poisoning / Adversarial Input

**Scenario**: Attacker crafts document images designed to fool OCR or extraction.

**Mitigations**:
- Mock AI service (default) uses deterministic extraction
- Confidence scores are always available to reviewer
- All extractions require evidence source references
- Reviewer can reject or correct any extraction
- Inconsistencies flagged for human review
- No automatic decisions based on AI output

**Residual Risk**: Low (mitigated by human oversight)

---

### Threat 6: Insider Threat (Reviewer Tampering)

**Scenario**: Malicious reviewer changes audit trail or marks false approvals.

**Mitigations**:
- Audit trail is append-only (no deletion/modification)
- Every change creates a new audit event
- Previous values retained (history preserved)
- Reviewer identity recorded with every action
- No silent data alteration
- Quality reviewer role can audit reviewer actions
- Corrections require explicit reason selection

**Residual Risk**: Mitigated by design (but human supervision still required)

---

### Threat 7: Supply Chain (Dependencies)

**Scenario**: Compromised open-source dependency contains malicious code.

**Mitigations**:
- Dependency pinning in requirements.txt
- Regular updates to patch known vulnerabilities
- Minimal dependency set (no unnecessary packages)
- Security scanning (GitHub Dependabot)
- Code review before dependency updates
- Use reputable, maintained packages only

**Residual Risk**: Moderate (mitigated by monitoring)

---

### Threat 8: Denial of Service (DoS)

**Scenario**: Attacker uploads many large files or makes excessive API calls.

**Mitigations**:
- File-size limits (50 MB default, configurable)
- Total case size limits (500 MB default)
- Rate limiting on API endpoints (to be implemented)
- Local processing (no external service to overload)
- SQLite connection pooling
- Request timeout configuration

**Residual Risk**: Moderate (rate limiting recommended)

---

## Security Controls

### Input Validation

```python
# All API inputs validated via Pydantic
class CaseCreate(BaseModel):
    applicant_type: Literal["individual", "business"]
    market: str
    description: str
    
# File uploads
if not is_safe_mime_type(file):
    raise ValueError("Unsupported file type")
    
if file.size > MAX_UPLOAD_SIZE_MB * 1024 * 1024:
    raise ValueError("File too large")
```

### Sensitive Data Masking

```python
# Before sending to AI:
masked_text = mask_sensitive_data(ocr_text)
# Result: "My name is [PERSON_NAME_01] and I live at [ADDRESS_01]"

# Mapping stays local to case
case.pii_mapping = {
    "PERSON_NAME_01": "[ORIGINAL MASKED]",
    "ADDRESS_01": "[ORIGINAL MASKED]"
}
```

### Log Redaction

```python
# Central redaction utility
logger.info(log_redactor.redact(f"Processing document: {pii_value}"))
# Output: "Processing document: [MASK]"
```

### Audit Logging

```python
audit_event = AuditEvent(
    case_id=case_id,
    event_type="extraction_completed",
    actor="reviewer_demo",
    timestamp=datetime.utcnow(),
    masked_details={"field": "full_name", "confidence": 0.95},
    # No raw PII included
)
audit_repo.create(audit_event)
```

### Prompt Injection Detection

```python
injection_patterns = [
    r"ignore\s+all\s+previous",
    r"system\s+message",
    r"override.*instruction",
    # ...
]

for pattern in injection_patterns:
    if re.search(pattern, ocr_text, re.IGNORECASE):
        logger.warning(f"Potential injection detected in document {doc_id}")
        audit_event.event_type = "prompt_injection_attempt"
        # Continue processing but flag for review
```

---

## Secure Deployment Checklist

- [ ] `.env` file is NOT committed to version control
- [ ] All secrets removed from code and configuration
- [ ] HTTPS enabled in production (reverse proxy)
- [ ] CORS configured for allowed origins only
- [ ] File storage directory restricted to application user
- [ ] Database file has restricted permissions (600)
- [ ] Audit logs backed up regularly
- [ ] Regular dependency security scanning
- [ ] Application logs monitored for security events
- [ ] No debug mode enabled in production
- [ ] Uvicorn workers configured appropriately
- [ ] Request size limits enforced by reverse proxy
- [ ] Rate limiting implemented
- [ ] Security headers configured (CSP, X-Frame-Options, etc.)

---

## Incident Response

If a security incident is suspected:

1. **Stop processing** - Pause case processing if data breach suspected
2. **Preserve evidence** - Retain logs and audit trails
3. **Notify stakeholders** - Document discovery and scope
4. **Investigate** - Review audit trail for unauthorized access
5. **Remediate** - Apply patches or configuration changes
6. **Document** - Create incident report

For this hackathon prototype, contact the development team immediately.

---

## Security Testing

Included security tests:

```bash
# Backend security tests
pytest backend/tests/security/ -v

# Includes:
# - Input validation tests
# - Prompt injection detection
# - Sensitive data masking
# - Audit trail integrity
# - MIME-type validation
```

---

## Known Limitations

1. **Local Database** - SQLite not suitable for production (concurrency)
2. **No Encryption at Rest** - Database not encrypted (local prototype)
3. **No mTLS** - Backend-frontend communication not encrypted (local only)
4. **No Rate Limiting** - To be implemented for production
5. **Demo Role Simulation** - No real authentication (local demo only)
6. **Mock AI Service** - Deterministic output (not real ML model)

---

## Recommendations for Production

1. **Add Real Authentication** - OAuth2/OpenID Connect
2. **Encrypt Database** - Use encrypted PostgreSQL or similar
3. **Enable HTTPS** - TLS certificates for frontend-backend
4. **Implement Rate Limiting** - Per-user and per-IP limits
5. **Add WAF** - Web Application Firewall in front of API
6. **Real Database** - PostgreSQL with connection pooling
7. **Message Queue** - Async processing for large uploads
8. **Secrets Management** - Vault or similar for credentials
9. **Monitoring & Alerting** - SIEM for security events
10. **Penetration Testing** - Professional security audit

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [FastAPI Security](https://fastapi.tiangolo.com/advanced/security/)

---

**Last Updated**: 2024  
**Status**: Hackathon Prototype  
**Security Level**: Demonstration Only
