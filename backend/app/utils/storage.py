"""Document storage and file management utilities."""

import os
import hashlib
from pathlib import Path
from typing import Optional, Tuple
from app.config import settings
from app.utils.masking import generate_id

class StorageManager:
    """Service for managing document storage."""
    
    @staticmethod
    def ensure_storage_dirs():
        """Ensure storage directories exist."""
        Path(settings.DOCUMENT_STORAGE_PATH).mkdir(parents=True, exist_ok=True)
        Path(settings.TEMP_UPLOAD_PATH).mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def calculate_file_hash(file_path: str) -> str:
        """
        Calculate SHA-256 hash of file for duplicate detection.
        
        Args:
            file_path: Path to file
        
        Returns:
            SHA-256 hash hex string
        """
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    @staticmethod
    def get_safe_filename(original_filename: str) -> str:
        """
        Generate safe filename to prevent directory traversal.
        
        Args:
            original_filename: Original filename from user
        
        Returns:
            Safe filename
        """
        # Generate UUID-based filename with original extension
        _, ext = os.path.splitext(original_filename)
        safe_name = f"{generate_id('doc')}{ext.lower()}"
        return safe_name
    
    @staticmethod
    def get_document_path(case_id: str, filename: str) -> str:
        """
        Get full path for storing document.
        
        Args:
            case_id: Case ID
            filename: Safe filename
        
        Returns:
            Full file path
        """
        case_dir = os.path.join(settings.DOCUMENT_STORAGE_PATH, case_id)
        Path(case_dir).mkdir(parents=True, exist_ok=True)
        return os.path.join(case_dir, filename)
    
    @staticmethod
    def validate_file_extension(filename: str, allowed_extensions: list = None) -> bool:
        """
        Validate file extension.
        
        Args:
            filename: Filename to validate
            allowed_extensions: List of allowed extensions (without dot)
        
        Returns:
            True if valid, False otherwise
        """
        if not allowed_extensions:
            allowed_extensions = settings.allowed_extensions_list
        
        _, ext = os.path.splitext(filename)
        ext = ext.lstrip('.').lower()
        return ext in allowed_extensions
    
    @staticmethod
    def validate_file_size(file_size_mb: float, max_size_mb: int = None) -> bool:
        """
        Validate file size.
        
        Args:
            file_size_mb: File size in MB
            max_size_mb: Maximum allowed size in MB
        
        Returns:
            True if valid, False otherwise
        """
        if not max_size_mb:
            max_size_mb = settings.MAX_UPLOAD_SIZE_MB
        return file_size_mb <= max_size_mb
