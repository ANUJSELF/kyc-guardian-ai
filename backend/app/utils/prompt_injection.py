"""Prompt injection detection service."""

import re
from typing import Tuple

class PromptInjectionDetector:
    """Service for detecting prompt injection attempts."""
    
    # Common injection patterns
    INJECTION_PATTERNS = [
        r"ignore\s+all\s+previous",
        r"disregard\s+previous",
        r"forget\s+all\s+prior",
        r"system\s+message",
        r"system\s+prompt",
        r"override.*instruction",
        r"cancel\s+(?:all\s+)?rule",
        r"bypass\s+(?:all\s+)?check",
        r"disable\s+(?:all\s+)?rule",
        r"mark.*as\s+approved",
        r"approve\s+(?:this\s+)?case",
        r"automatically\s+accept",
        r"automatically\s+approve",
        r"access\s+file",
        r"reveal\s+config",
        r"expose\s+setting",
        r"execute\s+command",
        r"run\s+code",
        r"eval\s+\w+",
    ]
    
    @staticmethod
    def detect(text: str) -> Tuple[bool, str]:
        """
        Detect if text contains prompt injection attempt.
        
        Args:
            text: Text to analyze
        
        Returns:
            Tuple of (is_injection_detected, matched_pattern)
        """
        if not text:
            return False, ""
        
        for pattern in PromptInjectionDetector.INJECTION_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                return True, pattern
        
        return False, ""
