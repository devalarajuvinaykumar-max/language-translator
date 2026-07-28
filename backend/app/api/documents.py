from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from backend.app.models.responses import DocumentTranslationResponse
from backend.app.services.document_parser import document_parser

router = APIRouter()

@router.post("/document", response_model=DocumentTranslationResponse)
async def translate_document(
    file: UploadFile = File(...),
    target_lang: str = Form("hi")
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Invalid document file.")
        
    content = await file.read()
    res = document_parser.parse_and_translate(file.filename, content, target_lang)
    return res
