"""Application main entry point."""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine
from app.models import Base

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context for app startup and shutdown."""
    # Startup
    logger.info("KYC Guardian AI starting up...")
    logger.info(f"AI Service: {settings.AI_SERVICE}")
    logger.info(f"Database: {settings.DATABASE_URL}")
    logger.info(f"Document Storage: {settings.DOCUMENT_STORAGE_PATH}")
    logger.info(f"CORS Origins: {settings.CORS_ORIGINS}")
    yield
    # Shutdown
    logger.info("KYC Guardian AI shutting down...")

# Create FastAPI app
app = FastAPI(
    title="KYC Guardian AI",
    description="AI-Powered KYC/KYB Document Intelligence and Evidence Management",
    version="0.1.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS.split(","),
    allow_headers=settings.CORS_ALLOW_HEADERS.split(",") if settings.CORS_ALLOW_HEADERS != "*" else ["*"],
)

# Health check endpoint
@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "kyc-guardian-ai",
        "version": "0.1.0",
        "ai_service": settings.AI_SERVICE,
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "KYC Guardian AI - AI-Powered KYC/KYB Document Intelligence",
        "api_docs": "/docs",
        "openapi_schema": "/openapi.json",
        "disclaimer": settings.DEMO_NOTICE_TEXT,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.API_PORT,
    )
