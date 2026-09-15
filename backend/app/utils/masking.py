"""Utilities for PII masking and log redaction."""

import re
import uuid
from typing import Dict, Tuple
from app.config import settings

class PIIMaskingService:
    """Service for detecting and masking PII patterns."""
    
    # PII pattern definitions
    PII_PATTERNS = {
        "PERSON_NAME": r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b",
        "PHONE_NUMBER": r"\+?[0-9]{7,15}",
        "EMAIL_ADDRESS": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "ID_NUMBER": r"\b[A-Z]{2}\d{6,9}\b",
        "TAX_ID": r"\b\d{2}-\d{7}\b",
        "ACCOUNT_NUMBER": r"\b\d{8,17}\b",
        "DATE_OF_BIRTH": r"\b(?:19|20)\d{2}[/-]?(?:0[1-9]|1[0-2])[/-]?(?:[0-2][0-9]|3[01])\b",
        "ADDRESS": r"\b\d+\s+[A-Za-z]+\s+(?:Street|Avenue|Road|Drive|Lane|St|Ave|Rd)\b",
    }
    
    def __init__(self):
        self.mask_mapping: Dict[str, str] = {}
        self.counter: Dict[str, int] = {}
    
    def mask_text(self, text: str, case_id: str = None) -> Tuple[str, Dict[str, str]]:
        """
        Mask PII in text and return masked text with mapping.
        
        Args:
            text: Text to mask
            case_id: Case ID for logging purposes
        
        Returns:
            Tuple of (masked_text, mask_mapping)
        """
        if not settings.ENABLE_PII_MASKING or not text:
            return text, {}
        
        masked_text = text
        mapping = {}
        
        for pii_type, pattern in self.PII_PATTERNS.items():
            # Check if masking is enabled for this type
            if not self._is_masking_enabled(pii_type):
                continue
            
            matches = re.finditer(pattern, text, re.IGNORECASE)
            
            for match in matches:
                original_value = match.group()
                placeholder = self._get_placeholder(pii_type)
                masked_text = masked_text.replace(original_value, placeholder, 1)
                mapping[placeholder] = "[ORIGINAL_MASKED]"
        
        return masked_text, mapping
    
    def _get_placeholder(self, pii_type: str) -> str:
        """Generate unique placeholder for PII type."""
        if pii_type not in self.counter:
            self.counter[pii_type] = 0
        
        self.counter[pii_type] += 1
        return f"[{pii_type}_{self.counter[pii_type]:02d}]"
    
    def _is_masking_enabled(self, pii_type: str) -> bool:
        """Check if masking is enabled for PII type."""
        masking_config = {
            "PERSON_NAME": settings.MASK_NAMES,
            "PHONE_NUMBER": settings.MASK_PHONE_NUMBERS,
            "EMAIL_ADDRESS": settings.MASK_EMAIL_ADDRESSES,
            "ID_NUMBER": settings.MASK_IDENTITY_NUMBERS,
            "TAX_ID": settings.MASK_TAX_IDENTIFIERS,
            "ACCOUNT_NUMBER": settings.MASK_ACCOUNT_NUMBERS,
            "DATE_OF_BIRTH": settings.MASK_DATES_OF_BIRTH,
            "ADDRESS": settings.MASK_ADDRESSES,
        }
        return masking_config.get(pii_type, True)


class LogRedactor:
    """Service for redacting sensitive information from logs."""
    
    # Patterns to redact
    REDACTION_PATTERNS = [
        r"\b[A-Z]{2}\d{6,9}\b",  # ID numbers
        r"\d{2}-\d{7}",  # Tax IDs
        r"\+?[0-9]{7,15}",  # Phone numbers
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",  # Email
        r"\b(?:19|20)\d{2}[/-]?(?:0[1-9]|1[0-2])[/-]?(?:[0-2][0-9]|3[01])\b",  # Dates
    ]
    
    @staticmethod
    def redact(message: str) -> str:
        """
        Redact sensitive patterns from log message.
        
        Args:
            message: Log message to redact
        
        Returns:
            Redacted message
        """
        if not settings.LOG_SENSITIVE_DATA:
            for pattern in LogRedactor.REDACTION_PATTERNS:
                message = re.sub(pattern, "[REDACTED]", message)
        
        return message


def generate_id(prefix: str = "") -> str:
    """Generate unique ID with optional prefix."""
    unique_id = str(uuid.uuid4())
    if prefix:
        return f"{prefix}-{unique_id}"
    return unique_id
