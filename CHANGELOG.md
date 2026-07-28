# Changelog - OmniTranslate AI

All notable changes to the OmniTranslate AI platform will be documented in this file.

## [2.0.0] - 2.0 Architectural Refactor & Multimodal Transformation

### Added
- **Python FastAPI Microservice (`backend/`)**:
  - `translation_engine.py`: Multi-provider translation orchestrator with MyMemory API fallback and LLM context reasoning.
  - `language_detector.py`: Multi-language detection & mixed-language parsing.
  - `context_reasoner.py`: Analyzes domain (business, technical, academic, casual), tone, and idioms.
  - `ocr_engine.py`: Extract text from images, posters, invoices, and signboards with bounding box layout metadata.
  - `document_parser.py`: Process PDF, DOCX, PPTX, TXT, and Markdown files while preserving layout.
  - `speech_diarization.py`: Speaker separation (Speaker 1, Speaker 2), emotion indicators, meeting summaries, and action item tracking.
  - `youtube_service.py`: YouTube URL transcription, translation, and summary extraction.
  - `translation_memory.py`: Vector & IndexedDB caching, term consistency, search history, and JSON export.
  - `analytics.py`: Dashboard metrics counter for translated words, latency, confidence stats, and top language pairs.
- **Recruiter-Grade Multimodal Frontend (`frontend/` & `index.html`)**:
  - Sleek dark/light theme design system with glassmorphism aesthetic.
  - Interactive workspaces for Text, Speech, OCR, Documents, YouTube, Meetings, Memory, and Analytics.
  - High contrast and Dyslexia-friendly font accessibility suite.
- **DevOps & Infrastructure**:
  - `docker/Dockerfile.backend`, `docker/Dockerfile.frontend`, and `docker/nginx.conf`.
  - `docker-compose.yml` for single-command orchestration.
  - `.github/workflows/ci-cd.yml` for automated PyTest testing and build verification.

### Improved
- Upgraded root `index.html` to load modern UI modules while maintaining full backward compatibility with all original HTML element IDs (`inputText`, `sourceLang`, `targetLang`, `translateBtn`, `outputText`, `copyBtn`).
- Preserved MyMemory API as standard fast fallback engine.
