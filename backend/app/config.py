import os
from datetime import timedelta
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API Configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:5173")
    API_BASE_URL: str = os.getenv("API_BASE_URL", "http://localhost:8000")
    
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./kyc_guardian.db")
    DATABASE_ECHO: bool = os.getenv("DATABASE_ECHO", "false").lower() == "true"
    
    # Document Storage
    DOCUMENT_STORAGE_PATH: str = os.getenv("DOCUMENT_STORAGE_PATH", "./storage/documents")
    TEMP_UPLOAD_PATH: str = os.getenv("TEMP_UPLOAD_PATH", "./storage/temp")
    DEMO_DATA_PATH: str = os.getenv("DEMO_DATA_PATH", "./demo-data/generated")
    
    # File Upload Configuration
    MAX_UPLOAD_SIZE_MB: int = int(os.getenv("MAX_UPLOAD_SIZE_MB", "50"))
    MAX_TOTAL_CASE_SIZE_MB: int = int(os.getenv("MAX_TOTAL_CASE_SIZE_MB", "500"))
    ALLOWED_EXTENSIONS: str = os.getenv("ALLOWED_EXTENSIONS", "pdf,png,jpg,jpeg")
    ALLOWED_MIME_TYPES: str = os.getenv(
        "ALLOWED_MIME_TYPES", 
        "application/pdf,image/png,image/jpeg"
    )
    
    # OCR Configuration
    OCR_ENGINE: str = os.getenv("OCR_ENGINE", "tesseract")
    OCR_LANGUAGE: str = os.getenv("OCR_LANGUAGE", "eng")
    OCR_CONFIDENCE_THRESHOLD: float = float(
        os.getenv("OCR_CONFIDENCE_THRESHOLD", "0.5")
    )
    
    # AI Service Configuration
    AI_SERVICE: str = os.getenv("AI_SERVICE", "mock")  # 'mock' or 'ollama'
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama2")
    OLLAMA_TIMEOUT_SECONDS: int = int(os.getenv("OLLAMA_TIMEOUT_SECONDS", "60"))
    OLLAMA_ENABLED: bool = os.getenv("OLLAMA_ENABLED", "false").lower() == "true"
    
    # Extraction & Validation Thresholds
    HIGH_CONFIDENCE_THRESHOLD: float = float(
        os.getenv("HIGH_CONFIDENCE_THRESHOLD", "0.90")
    )
    MEDIUM_CONFIDENCE_THRESHOLD: float = float(
        os.getenv("MEDIUM_CONFIDENCE_THRESHOLD", "0.70")
    )
    ADDRESS_SIMILARITY_THRESHOLD: float = float(
        os.getenv("ADDRESS_SIMILARITY_THRESHOLD", "0.85")
    )
    DOCUMENT_EXPIRY_WARNING_DAYS: int = int(
        os.getenv("DOCUMENT_EXPIRY_WARNING_DAYS", "90")
    )
    
    # Masking Configuration
    ENABLE_PII_MASKING: bool = os.getenv("ENABLE_PII_MASKING", "true").lower() == "true"
    MASK_NAMES: bool = os.getenv("MASK_NAMES", "true").lower() == "true"
    MASK_PHONE_NUMBERS: bool = os.getenv("MASK_PHONE_NUMBERS", "true").lower() == "true"
    MASK_EMAIL_ADDRESSES: bool = os.getenv("MASK_EMAIL_ADDRESSES", "true").lower() == "true"
    MASK_IDENTITY_NUMBERS: bool = os.getenv("MASK_IDENTITY_NUMBERS", "true").lower() == "true"
    MASK_TAX_IDENTIFIERS: bool = os.getenv("MASK_TAX_IDENTIFIERS", "true").lower() == "true"
    MASK_ACCOUNT_NUMBERS: bool = os.getenv("MASK_ACCOUNT_NUMBERS", "true").lower() == "true"
    MASK_ADDRESSES: bool = os.getenv("MASK_ADDRESSES", "true").lower() == "true"
    MASK_DATES_OF_BIRTH: bool = os.getenv("MASK_DATES_OF_BIRTH", "true").lower() == "true"
    
    # Demo & Testing
    ENABLE_MOCK_DATA: bool = os.getenv("ENABLE_MOCK_DATA", "true").lower() == "true"
    ENABLE_DEMO_RESET: bool = os.getenv("ENABLE_DEMO_RESET", "true").lower() == "true"
    ENABLE_SYNTHETIC_ANALYTICS: bool = os.getenv(
        "ENABLE_SYNTHETIC_ANALYTICS", "true"
    ).lower() == "true"
    DEMO_NOTICE_TEXT: str = os.getenv(
        "DEMO_NOTICE_TEXT",
        "Synthetic demonstration data only. Do not upload customer, colleague, "
        "proprietary, restricted or regulated information."
    )
    
    # Security Configuration
    LOG_SENSITIVE_DATA: bool = os.getenv("LOG_SENSITIVE_DATA", "false").lower() == "true"
    ENABLE_PROMPT_INJECTION_DETECTION: bool = os.getenv(
        "ENABLE_PROMPT_INJECTION_DETECTION", "true"
    ).lower() == "true"
    ENABLE_AUDIT_LOGGING: bool = os.getenv("ENABLE_AUDIT_LOGGING", "true").lower() == "true"
    AUDIT_LOG_RETENTION_DAYS: int = int(os.getenv("AUDIT_LOG_RETENTION_DAYS", "365"))
    
    # CORS Configuration
    CORS_ORIGINS: str = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173"
    )
    CORS_ALLOW_CREDENTIALS: bool = os.getenv(
        "CORS_ALLOW_CREDENTIALS", "true"
    ).lower() == "true"
    CORS_ALLOW_METHODS: str = os.getenv(
        "CORS_ALLOW_METHODS",
        "GET,POST,PUT,DELETE,OPTIONS"
    )
    CORS_ALLOW_HEADERS: str = os.getenv("CORS_ALLOW_HEADERS", "*")
    
    # Logging Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = os.getenv("LOG_FORMAT", "json")
    LOG_FILE: str = os.getenv("LOG_FILE", "./logs/kyc-guardian.log")
    
    # Feature Flags
    FEATURE_CROSS_DOCUMENT_COMPARISON: bool = os.getenv(
        "FEATURE_CROSS_DOCUMENT_COMPARISON", "true"
    ).lower() == "true"
    FEATURE_EXCEPTION_MANAGEMENT: bool = os.getenv(
        "FEATURE_EXCEPTION_MANAGEMENT", "true"
    ).lower() == "true"
    FEATURE_EVIDENCE_PACK_EXPORT: bool = os.getenv(
        "FEATURE_EVIDENCE_PACK_EXPORT", "true"
    ).lower() == "true"
    FEATURE_ANALYTICS_DASHBOARD: bool = os.getenv(
        "FEATURE_ANALYTICS_DASHBOARD", "true"
    ).lower() == "true"
    FEATURE_AUDIT_TRAIL: bool = os.getenv(
        "FEATURE_AUDIT_TRAIL", "true"
    ).lower() == "true"
    
    # Computed paths
    @property
    def cors_origins_list(self) -> list:
        return [o.strip() for o in self.CORS_ORIGINS.split(",")]
    
    @property
    def allowed_extensions_list(self) -> list:
        return [e.strip() for e in self.ALLOWED_EXTENSIONS.split(",")]
    
    @property
    def allowed_mime_types_list(self) -> list:
        return [m.strip() for m in self.ALLOWED_MIME_TYPES.split(",")]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
