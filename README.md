# KYC Guardian AI

**AI-Powered KYC/KYB Document Intelligence and Evidence Management**

> From document submission to review-ready evidence, securely, accurately and transparently.

---

## ⚠️ IMPORTANT NOTICE

**Synthetic demonstration data only.** Do not upload customer, colleague, proprietary, restricted or regulated information. This prototype provides document-processing assistance only and does not make KYC, credit, onboarding or customer decisions.

---

## Project Overview

KYC Guardian AI is a **local-first, hackathon-grade prototype** that demonstrates how AI and deterministic rules can assist in Know-Your-Customer (KYC) and Know-Your-Business (KYB) document management workflows.

The application:
- ✅ Converts synthetic identity and business documents into masked, structured evidence
- ✅ Runs entirely locally with optional Ollama integration
- ✅ Maintains complete audit trails and version control
- ✅ Protects sensitive data through deterministic masking
- ✅ Supports human review and reviewer corrections
- ✅ Generates masked evidence packs for downstream review

The application **does not**:
- ❌ Approve or decline a customer
- ❌ Make credit, onboarding or account-opening decisions
- ❌ Make sanctions or watchlist determinations
- ❌ Claim documents are fraudulent
- ❌ Automatically reject documents
- ❌ Transmit data to external services

---

## Quick Start

### Prerequisites

- **Docker & Docker Compose** (recommended)
- **OR**: Python 3.9+, Node.js 18+, npm/yarn

### Option 1: Docker Compose (Recommended)

```bash
git clone https://github.com/ANUJSELF/kyc-guardian-ai.git
cd kyc-guardian-ai
docker compose up --build
```

The application will be available at:
- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### Option 2: Local Setup

#### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Option 3: PowerShell (Windows)

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

```powershell
# In another terminal
cd frontend
npm install
npm run dev
```

---

## Key Features

### 1. Document Management
- Secure synthetic-document upload (PDF, PNG, JPG, JPEG)
- Drag-and-drop interface
- File validation and duplicate detection
- Safe storage with SHA-256 hashing

### 2. Document Processing Pipeline
- Local PDF text extraction (PyMuPDF)
- Local OCR for scanned images (Tesseract)
- Image-quality assessment
- Sensitive-data detection and masking
- Document classification
- Structured field extraction

### 3. Intelligent Review
- Confidence-driven extraction scores
- Evidence highlighting with source references
- Reviewer confirmations and corrections
- Cross-document comparison
- Exception management queue

### 4. Audit & Compliance
- Complete append-only audit trail
- Version tracking (OCR, model, rules, prompts)
- Case state transitions
- Reviewer action tracking
- Masked evidence-pack generation

### 5. Optional AI Enhancement
- **Default**: Deterministic mock AI (no internet required)
- **Optional**: Ollama adapter for local language models
- All AI inputs automatically masked
- Safe fallback if AI unavailable

### 6. Security & Privacy
- No external API calls
- No automatic data downloads
- Sensitive values never logged
- Prompt-injection protection
- Deterministic masking
- Log redaction throughout

---

## Project Structure

```
kyc-guardian-ai/
├── README.md
├── .env.example
├── .gitignore
├── docker-compose.yml
├── SECURITY.md
├── PRIVACY.md
├── RESPONSIBLE_AI.md
├── ACCESSIBILITY.md
├── THREAT_MODEL.md
├── DEMO_GUIDE.md
├── LICENSE_NOTICE.md
│
├── frontend/                    # React + TypeScript + Vite
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   ├── routes/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── contexts/
│   │   ├── types/
│   │   ├── utils/
│   │   ├── theme/
│   │   └── tests/
│   └── Dockerfile
│
├── backend/                     # Python + FastAPI
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── api/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── rules/
│   │   ├── security/
│   │   ├── utils/
│   │   └── tests/
│   └── scripts/
│
└── demo-data/                   # Synthetic test data
    ├── README.md
    ├── generate_demo_documents.py
    ├── generated/
    └── expected-results/
```

---

## Documentation

| Document | Purpose |
|----------|---------|
| [DEMO_GUIDE.md](./DEMO_GUIDE.md) | Step-by-step walkthrough and use cases |
| [SECURITY.md](./SECURITY.md) | Security architecture and controls |
| [PRIVACY.md](./PRIVACY.md) | Data minimisation and privacy approach |
| [RESPONSIBLE_AI.md](./RESPONSIBLE_AI.md) | AI governance and limitations |
| [ACCESSIBILITY.md](./ACCESSIBILITY.md) | WCAG 2.1 AA compliance approach |
| [THREAT_MODEL.md](./THREAT_MODEL.md) | Security threat analysis |
| [LICENSE_NOTICE.md](./LICENSE_NOTICE.md) | Open-source license information |

---

## Technology Stack

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Fluent UI** - Enterprise components
- **React Router** - Navigation
- **Recharts** - Analytics visualisation
- **React Dropzone** - File upload
- **Vitest + React Testing Library** - Tests

### Backend
- **Python 3.9+** - Language
- **FastAPI** - Web framework
- **Pydantic** - Data validation
- **SQLAlchemy** - ORM
- **SQLite** - Local database
- **Uvicorn** - ASGI server

### Document Processing
- **PyMuPDF (fitz)** - PDF text extraction
- **Tesseract OCR** - Scanned image OCR
- **Pillow** - Image handling
- **OpenCV** - Image quality checks
- **python-magic** - MIME-type validation

### Local AI
- **Ollama** - Optional local LLM (disabled by default)
- **MockAIService** - Deterministic default fallback

### Testing
- **Pytest** - Backend unit/integration tests
- **Vitest** - Frontend unit tests
- **React Testing Library** - Frontend component tests

### Deployment
- **Docker** - Containerisation
- **Docker Compose** - One-command startup

---

## Configuration

### Environment Variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Key variables:

```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
FRONTEND_URL=http://localhost:5173

# Database
DATABASE_URL=sqlite:///./kyc_guardian.db

# Document Storage
DOCUMENT_STORAGE_PATH=./storage/documents
TEMP_UPLOAD_PATH=./storage/temp

# AI Service
AI_SERVICE=mock  # or 'ollama'
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# Security
MAX_UPLOAD_SIZE_MB=50
ALLOWED_EXTENSIONS=pdf,png,jpg,jpeg

# Demo Settings
ENABLE_MOCK_DATA=true
ENABLE_DEMO_RESET=true
```

---

## API Endpoints

### Case Management
- `POST /api/cases` - Create case
- `GET /api/cases` - List cases
- `GET /api/cases/{case_id}` - Get case details
- `PUT /api/cases/{case_id}` - Update case

### Document Processing
- `POST /api/documents/upload` - Upload document
- `GET /api/documents/{doc_id}` - Get document
- `GET /api/documents/{doc_id}/preview` - Preview document

### Review
- `GET /api/reviews/{case_id}` - Get review state
- `POST /api/reviews/{doc_id}/confirm-field` - Confirm extracted field
- `POST /api/reviews/{doc_id}/correct-field` - Correct extracted field

### Analytics & Audit
- `GET /api/analytics/dashboard` - Dashboard metrics
- `GET /api/audit/trail/{case_id}` - Audit trail
- `GET /api/evidence-pack/{case_id}` - Generate evidence pack

See [API Documentation](http://localhost:8000/docs) for complete OpenAPI spec.

---

## Development Workflow

### Running Tests

Backend:
```bash
cd backend
pytest tests/ -v --cov=app
```

Frontend:
```bash
cd frontend
npm run test
npm run test:ui
```

### Database Migrations

```bash
cd backend
alembic upgrade head
```

### Resetting Demo Data

```bash
# Docker
docker compose exec backend python scripts/reset_demo.py

# Local
cd backend
python scripts/reset_demo.py
```

---

## Core Use Cases

### Use Case 1: Individual KYC Review
1. Create case (Individual, Market: India)
2. Upload: Passport, Address Proof, Tax ID
3. System extracts fields with confidence scores
4. Reviewer confirms/corrects extractions
5. Generate masked evidence pack
6. Audit trail preserved

### Use Case 2: Business KYB Review
1. Create case (Business, Market: Singapore)
2. Upload: Certificate of Incorporation, Ownership Declaration
3. System classifies documents
4. Cross-document comparison: Legal name, Registration number
5. Resolve inconsistencies
6. Export evidence

### Use Case 3: Exception Resolution
1. Documents uploaded
2. System detects: Expired document, Low OCR confidence
3. Exceptions appear in review queue
4. Reviewer assesses evidence
5. Determines if manual intervention needed
6. Records decision

---

## Responsible AI Approach

### What This System Does
✅ Assist human reviewers with consistent, explainable field extraction  
✅ Flag potential inconsistencies across documents  
✅ Maintain complete audit trails  
✅ Protect sensitive data through masking  
✅ Support evidence-driven decision-making  

### What This System Does NOT Do
❌ Make autonomous KYC/KYB decisions  
❌ Approve or decline customers  
❌ Make credit or onboarding determinations  
❌ Claim documents are genuine or fraudulent  
❌ Train or update models from feedback  

### Human Oversight
Every extracted field can be reviewed, corrected, or rejected by a human. No field extraction automatically triggers a case decision. Every correction creates an audit event.

See [RESPONSIBLE_AI.md](./RESPONSIBLE_AI.md) for detailed governance framework.

---

## Security Features

### Data Protection
- Sensitive values masked before any AI processing
- No raw identifiers in logs, exceptions, or analytics
- SHA-256 file hashing for integrity
- Exact duplicate detection

### Input Validation
- MIME-type and file-extension checking
- File-size limits
- Prompt-injection detection
- Schema validation via Pydantic

### Audit & Traceability
- Append-only audit trail
- Version tracking (OCR, models, rules, prompts)
- All case state changes recorded
- Reviewer actions logged

See [SECURITY.md](./SECURITY.md) for full threat model and controls.

---

## Accessibility

The application meets WCAG 2.1 Level AA standards:
- Keyboard navigation throughout
- Screen reader support (ARIA labels)
- Colour not the only differentiator (icons + text)
- Clear focus indicators
- Sufficient contrast ratios
- Semantic HTML structure

See [ACCESSIBILITY.md](./ACCESSIBILITY.md) for details.

---

## Limitations & Disclaimers

1. **Synthetic Data Only** - All demonstration data is generated and not representative of production workflows.
2. **No Real Decisions** - This system does not make actual KYC, credit, or onboarding decisions.
3. **Optional AI** - The system works without Ollama; default mock service requires no internet.
4. **Local Processing** - No data is transmitted to external services.
5. **Prototype Quality** - This is a hackathon demonstration, not production-ready software.
6. **No Automated Approval** - Every case requires human review.

---

## Contributing

This is a hackathon prototype. Contributions are welcome for:
- Additional test cases
- Improved documentation
- Accessibility enhancements
- Additional demo document types

Please see [CONTRIBUTING.md](./CONTRIBUTING.md) (to be added) for guidelines.

---

## License

This project is provided under the [MIT License](./LICENSE) for hackathon evaluation purposes.

See [LICENSE_NOTICE.md](./LICENSE_NOTICE.md) for open-source dependencies and their licenses.

---

## Support & Feedback

- 🐛 **Issues**: [GitHub Issues](https://github.com/ANUJSELF/kyc-guardian-ai/issues)
- 📧 **Contact**: Refer to repository maintainers
- 📖 **Documentation**: See docs/ folder and wiki

---

## Acknowledgements

Built as a hackathon prototype demonstrating modern AI-assisted document processing with security, privacy, and responsible-AI principles at the core.

**Not affiliated with or endorsed by American Express or any regulated financial institution.**

---

Last updated: 2024 | Hackathon Prototype
