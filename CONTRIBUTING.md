# Contributing to KYC Guardian AI

**KYC Guardian AI** is a hackathon prototype designed to demonstrate AI-assisted KYC/KYB document processing with responsible AI and privacy principles.

---

## Code of Conduct

All contributors are expected to:

- ✅ Be respectful and inclusive
- ✅ Focus on the technical and educational value
- ✅ Respect intellectual property and privacy
- ✅ Not submit real customer or proprietary data
- ✅ Follow responsible AI principles

---

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. **Search existing issues** first
2. **Provide details**:
   - What were you doing?
   - What did you expect?
   - What actually happened?
   - Include error messages or logs
3. **Use descriptive titles**
4. **Label appropriately** (bug, enhancement, documentation)

### Submitting Pull Requests

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make your changes**
4. **Add tests** for new functionality
5. **Update documentation** if needed
6. **Run tests locally**:
   ```bash
   # Backend tests
   cd backend && pytest tests/ -v
   
   # Frontend tests
   cd frontend && npm run test
   ```
7. **Commit with descriptive messages**:
   ```bash
   git commit -m "Add feature: description of change"
   ```
8. **Push to your fork**
9. **Create pull request** with:
   - Clear title
   - Description of changes
   - Reference to related issues
   - Test results

---

## Development Setup

### Prerequisites

- Python 3.9+
- Node.js 18+
- Docker & Docker Compose (optional)
- Git

### Local Development

```bash
# Clone repository
git clone https://github.com/ANUJSELF/kyc-guardian-ai.git
cd kyc-guardian-ai

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m pytest tests/

# Frontend setup
cd ../frontend
npm install
npm run test
npm run dev
```

### Using Docker

```bash
docker compose up --build
```

---

## Code Style

### Python

```bash
# Format code
black backend/app/

# Sort imports
isort backend/app/

# Lint
pylint backend/app/
```

### JavaScript/TypeScript

```bash
# Format code
npm run format

# Lint
npm run lint
```

---

## Testing Requirements

### Backend Tests

```bash
cd backend
pytest tests/ -v --cov=app --cov-report=html
```

Include tests for:
- Unit tests (functions, services)
- Integration tests (API endpoints, workflows)
- Security tests (input validation, masking, injection)
- Accessibility tests (where applicable)

### Frontend Tests

```bash
cd frontend
npm run test
npm run test:ui
```

Include tests for:
- Component rendering
- User interactions
- API integration
- Accessibility (a11y)

---

## Documentation

### When to Document

- ✅ New features should have user-facing documentation
- ✅ API changes should update API docs
- ✅ Complex logic should have code comments
- ✅ Security changes should update SECURITY.md
- ✅ Breaking changes should update CHANGELOG

### Documentation Format

- Use Markdown for documentation
- Include code examples
- Use clear, simple language
- Keep lines under 80 characters where possible
- Add headers and structure

---

## Areas for Contribution

### High Priority

- [ ] Additional OCR language support
- [ ] More document type classifiers
- [ ] Enhanced extraction rules
- [ ] Frontend accessibility improvements
- [ ] Additional test coverage

### Medium Priority

- [ ] Performance optimizations
- [ ] UI/UX improvements
- [ ] Documentation enhancements
- [ ] Additional analytics
- [ ] Localization (i18n)

### Low Priority

- [ ] Visual theme variations
- [ ] Additional demo documents
- [ ] Example integrations
- [ ] Tutorial videos
- [ ] Blog posts

---

## Security Considerations

### When Contributing Security-Related Code

1. **Do NOT** include real customer data in commits
2. **Do NOT** log sensitive values
3. **Do** sanitize all user inputs
4. **Do** test with malicious inputs
5. **Do** review threat model changes
6. **Do** update SECURITY.md with mitigations

### Reporting Security Issues

**Do NOT** create a public GitHub issue for security vulnerabilities.

Instead, contact the maintainers privately with:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)

---

## Release Process

Contributors with release rights:

1. Update version in `package.json` and `setup.py`
2. Update `CHANGELOG.md`
3. Create git tag: `git tag v1.2.3`
4. Push tag: `git push origin v1.2.3`
5. GitHub Actions create release automatically

---

## Getting Help

- **Questions**: Open a GitHub Discussion
- **Bugs**: Create a GitHub Issue
- **Security**: Email maintainers privately
- **Improvements**: Submit a Pull Request

---

## Licensing

By contributing to KYC Guardian AI, you agree that your contributions will be licensed under the MIT License. See [LICENSE_NOTICE.md](./LICENSE_NOTICE.md) for details.

---

## Recognition

Contributors will be recognized in:
- Git commit history
- GitHub contributors page
- CONTRIBUTORS.md (to be created)

Thank you for contributing to KYC Guardian AI! 🎉

---

**Last Updated**: 2024  
**Status**: Hackathon Prototype
