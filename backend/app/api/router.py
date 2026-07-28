from fastapi import APIRouter
from backend.app.api import translate, ocr, documents, media, analytics, memory, tts, writing_assistant

api_router = APIRouter()

api_router.include_router(translate.router, tags=["Translation & Detection"])
api_router.include_router(ocr.router, tags=["OCR Translation"])
api_router.include_router(documents.router, tags=["Document Translation"])
api_router.include_router(media.router, tags=["YouTube & Meetings"])
api_router.include_router(analytics.router, tags=["Analytics Dashboard"])
api_router.include_router(memory.router, tags=["Translation Memory"])
api_router.include_router(tts.router, tags=["Neural TTS Speech"])
api_router.include_router(writing_assistant.router, tags=["AI Writing & Flagship Capabilities"])
