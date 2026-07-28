# ⚡ OmniTranslate AI — Enterprise Multimodal Communication Platform

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=flat&logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg?style=flat&logo=docker)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF.svg?style=flat&logo=githubactions)](https://github.com/features/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**OmniTranslate AI** is a production-grade, enterprise-ready **AI Multimodal Communication Platform** designed to deliver low-latency, context-aware, and multi-modal translations across **Text, Speech, OCR Images, Documents (PDF/DOCX/PPTX), YouTube Videos, and Meeting Transcripts**. 

Transformed from a static translation utility into a high-performance distributed microservice architecture, OmniTranslate AI showcases production AI software engineering standards suitable for engineering leaders at Google, Meta, OpenAI, Anthropic, DeepMind, and NVIDIA.

---

## 🌟 Key Capabilities & Workspaces

### 1. 💬 Context-Aware & Intelligent Text Studio
- **Multi-Language & Mixed Language Auto-Detection**: Identifies primary languages, mixed-language phrases, and non-Latin scripts (Devanagari, Telugu, Cyrillic, Kanji, Arabic).
- **Context & Domain Adaptation**: Optimizes translations for **Business**, **Technical/Code**, **Academic**, and **Casual/Slang** contexts.
- **Formality & Tone Control**: Select between formal, standard, and informal registers.
- **AI Phrasing Suggestions & Confidence Scoring**: Displays confidence percentage metrics, alternative phrasing suggestions, and emotion tone tracking.

### 2. 🎙️ Live Speech-to-Speech & Tone Preservation
- **Real-Time Speech Recognition**: Mic integration with live audio waveform visualization.
- **Audio Playback**: Speech synthesis with pitch and speed control.
- **Emotion Preservation**: Detects emotional tone (*Happy, Sad, Angry, Excited, Neutral*) to keep translated speech expressive.

### 3. 🖼️ Visual OCR Translator
- **Layout-Preserving Text Extraction**: Translates text from photos, posters, menus, invoices, passports, and signboards.
- **Bounding Box Highlights**: Interactive visual overlay mapping extracted bounding coordinates.

### 4. 📄 Document Translation Studio
- **Format Preservation**: Parses and translates `PDF`, `DOCX`, `PPTX`, `TXT`, and `Markdown` files without stripping structure.

### 5. 🎥 YouTube Video Translation Studio
- **Transcript & Subtitle Generator**: Extracts video transcripts from YouTube URLs, generates localized subtitles, and compiles AI video summaries with key takeaways.

### 6. 🎙️ Meeting Assistant & Speaker Diarization
- **Speaker Diarization**: Identifies and labels multiple speakers (`Speaker 1 (Alex)`, `Speaker 2 (Maria)`).
- **Meeting Synthesis**: Generates meeting summaries, emotional distribution metrics, and actionable items.

### 7. 🧠 Translation Memory & Glossary
- **Indexed & Vector Caching**: Sub-millisecond retrieval for repeated phrases and technical glossaries.
- **Search History & Bookmarks**: Save favorites and export memory logs to JSON.

### 8. 📊 Analytics Dashboard
- **Real-Time Operational Insights**: Tracks total translations, words translated, average latency (ms), confidence scores, and top language pairs.

### 9. ♿ Accessibility Suite
- **Dyslexia-Friendly Font Toggle**: One-click switch to `OpenDyslexic` typography.
- **High-Contrast & Light/Dark Glassmorphism Theme**: Accessible contrast modes, keyboard navigation, and screen reader ARIA standards.

---

## 🏗️ Architecture Overview

```
                          ┌────────────────────────┐
                          │    Browser Client UI   │
                          │   (Vanilla JS + CSS)   │
                          └───────────┬────────────┘
                                      │ REST / JSON
                                      ▼
                          ┌────────────────────────┐
                          │    Nginx Reverse Proxy │
                          │     (Port 80 / Docker) │
                          └───────────┬────────────┘
                                      │ /api/v1
                                      ▼
                          ┌────────────────────────┐
                          │   FastAPI Backend App  │
                          │     (Python 3.11)      │
                          └───────────┬────────────┘
                                      │
   ┌───────────────────┬──────────────┼──────────────┬───────────────────┐
   ▼                   ▼              ▼              ▼                   ▼
┌──────────────┐ ┌───────────┐ ┌──────────────┐ ┌───────────┐ ┌────────────────────┐
│ Translation  │ │ Language  │ │ OCR & Doc    │ │ Diarize   │ │ Translation Memory │
│ Engine       │ │ Detector  │ │ Parser       │ │ & Media   │ │ & Analytics        │
└──────────────┘ └───────────┘ └──────────────┘ └───────────┘ └────────────────────┘
```

---

## 🛠️ Technology Stack

- **Backend Framework**: Python 3.11, FastAPI, Uvicorn, Pydantic v2, PyTest, HTTPX.
- **Frontend Architecture**: Modern Vanilla JavaScript (ES Modules), CSS Glassmorphism Design Tokens, HTML5 Semantic Elements.
- **Infrastructure & DevOps**: Docker, Docker Compose, Nginx, GitHub Actions CI/CD.
- **Translation & AI Engines**: Hybrid Orchestration (MyMemory API, Local Context Reasoner, Speech Synthesis, Client-side Fallback Engine).

---

## 🚀 Quick Start Guide

### Option A: Running with Docker Compose (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/vinay/language-translator.git
cd language-translator

# 2. Build and launch container services
docker compose up --build -d

# 3. Access App & API Docs
# App UI:      http://localhost
# Backend API: http://localhost:8000/docs
```

### Option B: Local Python Development

```bash
# 1. Install Python dependencies
pip install -r backend/requirements.txt

# 2. Start the FastAPI server
python -m uvicorn backend.main:app --reload --port 8000

# 3. Open index.html in your browser or serve via static web server
```

---

## 🧪 Testing & Verification

Run the automated PyTest suite to verify API routes, request schemas, and core services:

```bash
PYTHONPATH=. pytest backend/tests/
```

Expected output:
```text
backend/tests/test_api.py ......                                [100%]
====================== 6 passed in 0.85s ======================
```

---

## 📄 API Documentation

Interactive OpenAPI / Swagger UI documentation is served automatically at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Primary Endpoints
- `POST /api/v1/translate` — Perform context-aware text translation.
- `POST /api/v1/detect` — Detect language script and mixed language presence.
- `POST /api/v1/ocr` — Extract and translate text from uploaded image files.
- `POST /api/v1/document` — Parse and translate PDF/DOCX/PPTX files.
- `POST /api/v1/youtube` — Extract transcript and summary from YouTube URLs.
- `POST /api/v1/meeting` — Process meeting transcript and perform speaker diarization.
- `GET /api/v1/analytics` — Fetch operational metrics and language pair stats.
- `GET /api/v1/memory/history` — Retrieve saved translation history log.

---

## 📜 License & Author

Created with ❤️ by **Vinay** — Distributed under the [MIT License](LICENSE).