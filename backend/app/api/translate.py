from fastapi import APIRouter, Request, HTTPException
from backend.app.models.requests import TranslationRequest, DetectLanguageRequest
from backend.app.models.responses import TranslationResponse, LanguageDetectionResponse
from backend.app.services.translation_engine import translation_engine
from backend.app.services.language_detector import language_detector
from backend.app.core.security import rate_limiter, sanitize_text

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
async def translate_text(req: Request, payload: TranslationRequest):
    rate_limiter.check_rate_limit(req.client.host)
    cleaned_text = sanitize_text(payload.text)
    
    if not cleaned_text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
        
    res = await translation_engine.translate_async(
        text=cleaned_text,
        source_lang=payload.source_lang,
        target_lang=payload.target_lang,
        domain=payload.context_domain,
        formality=payload.formality
    )
    return res

@router.post("/detect", response_model=LanguageDetectionResponse)
async def detect_language(req: Request, payload: DetectLanguageRequest):
    rate_limiter.check_rate_limit(req.client.host)
    res = language_detector.detect_language(payload.text)
    return res
