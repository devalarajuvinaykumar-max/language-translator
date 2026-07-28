from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from backend.app.models.responses import OCRTranslationResponse
from backend.app.services.ocr_engine import ocr_engine

router = APIRouter()

@router.post("/ocr", response_model=OCRTranslationResponse)
async def translate_ocr_image(
    file: UploadFile = File(...),
    target_lang: str = Form("hi")
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Invalid image file.")
        
    content = await file.read()
    res = ocr_engine.process_image(file.filename, content, target_lang)
    return res
