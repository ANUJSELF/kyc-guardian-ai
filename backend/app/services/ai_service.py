"""Mock AI Service - Default fallback without external dependencies."""

import random
from typing import Dict, List, Optional
from datetime import datetime

class MockAIService:
    """
    Deterministic mock AI service for demonstration.
    
    Provides:
    - Consistent output for same input
    - No external API calls
    - No internet required
    - Safe fallback behavior
    """
    
    def __init__(self):
        self.model_name = "mock_v1"
        self.deterministic_seed = 42
    
    async def extract_fields(self, masked_text: str, document_type: str) -> Dict:
        """
        Extract structured fields from masked text.
        
        Args:
            masked_text: Masked OCR text
            document_type: Document type (passport, address_proof, etc.)
        
        Returns:
            Dictionary of extracted fields with confidence scores
        """
        # Deterministic extraction based on document type
        fields = {}
        
        if document_type == "passport":
            fields = {
                "full_name": {"value": "[PERSON_NAME_01]", "confidence": 0.95},
                "date_of_birth": {"value": "[DATE_OF_BIRTH_01]", "confidence": 0.88},
                "passport_number": {"value": "[ID_NUMBER_01]", "confidence": 0.92},
                "nationality": {"value": "India", "confidence": 0.98},
                "issue_date": {"value": "2018-05-15", "confidence": 0.90},
                "expiry_date": {"value": "2028-05-14", "confidence": 0.90},
            }
        
        elif document_type == "address_proof":
            fields = {
                "full_name": {"value": "[PERSON_NAME_01]", "confidence": 0.94},
                "address": {"value": "[ADDRESS_01]", "confidence": 0.89},
                "postal_code": {"value": "110001", "confidence": 0.95},
                "issue_date": {"value": "2023-08-10", "confidence": 0.92},
            }
        
        elif document_type == "tax_identification":
            fields = {
                "full_name": {"value": "[PERSON_NAME_01]", "confidence": 0.93},
                "tax_id": {"value": "[TAX_ID_01]", "confidence": 0.91},
                "date_of_birth": {"value": "[DATE_OF_BIRTH_01]", "confidence": 0.87},
            }
        
        else:
            # Generic extraction
            fields = {
                "extracted_text": {"value": masked_text[:100], "confidence": 0.80}
            }
        
        return {
            "fields": fields,
            "model": self.model_name,
            "timestamp": datetime.utcnow().isoformat(),
            "confidence_avg": sum(
                f.get("confidence", 0) for f in fields.values()
            ) / len(fields) if fields else 0,
        }
    
    async def classify_document(self, masked_text: str) -> Dict:
        """
        Classify document type from text.
        
        Args:
            masked_text: Masked OCR text
        
        Returns:
            Classification result with confidence
        """
        # Deterministic classification based on keywords
        classification_rules = {
            "passport": {"keywords": ["passport", "number", "issue", "expiry"], "type": "Identity Document"},
            "address": {"keywords": ["address", "postal", "street", "avenue"], "type": "Address Proof"},
            "tax": {"keywords": ["tax", "identification", "tin", "pan"], "type": "Tax Identification"},
        }
        
        text_lower = masked_text.lower()
        matched_type = "Other Document"
        confidence = 0.60
        
        for key, rule in classification_rules.items():
            keyword_matches = sum(1 for kw in rule["keywords"] if kw in text_lower)
            if keyword_matches > 0:
                matched_type = rule["type"]
                confidence = min(0.98, 0.70 + (keyword_matches * 0.07))
                break
        
        return {
            "predicted_type": matched_type,
            "confidence": confidence,
            "method": "rule_based",
            "model": self.model_name,
            "timestamp": datetime.utcnow().isoformat(),
        }
    
    async def detect_inconsistency(self, value_a: str, value_b: str, field_type: str) -> Dict:
        """
        Detect inconsistency between two field values.
        
        Args:
            value_a: First value (masked)
            value_b: Second value (masked)
            field_type: Type of field
        
        Returns:
            Inconsistency detection result
        """
        # Exact match comparison for masked values
        is_consistent = value_a == value_b
        
        return {
            "is_consistent": is_consistent,
            "similarity_score": 1.0 if is_consistent else 0.0,
            "analysis": "Exact match comparison",
            "model": self.model_name,
            "timestamp": datetime.utcnow().isoformat(),
        }


class OllamaAIService:
    """
    Optional Ollama adapter for local language models.
    
    Requirements:
    - Ollama running locally (http://localhost:11434)
    - Model downloaded (e.g., ollama pull llama2)
    
    Features:
    - Only masked text sent to model
    - Local processing (no cloud)
    - Can be disabled via configuration
    """
    
    def __init__(self, base_url: str, model_name: str):
        self.base_url = base_url
        self.model_name = model_name
    
    async def extract_fields(self, masked_text: str, document_type: str) -> Dict:
        """
        Extract fields using Ollama model (if available).
        
        Falls back to mock service if unavailable.
        """
        # This would call Ollama endpoint
        # For now, fall back to mock
        mock_service = MockAIService()
        return await mock_service.extract_fields(masked_text, document_type)
