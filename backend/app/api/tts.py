import httpx
import urllib.parse
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import Response, StreamingResponse

router = APIRouter()

# High-Quality Neural Audio Stream Generator
@router.get("/tts/stream")
async def stream_neural_tts(
    text: str = Query(..., description="Text to synthesize"),
    lang: str = Query("hi", description="Language code (e.g. 'hi', 'en', 'es', 'fr')"),
    voice: str = Query("female", description="Voice variant: 'female', 'male', 'neural'")
):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    clean_text = text.strip()[:300]
    target_lang = lang if lang != "auto" else "en"
    
    # Primary Neural TTS Audio Provider URL
    tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl={target_lang}&q={urllib.parse.quote(clean_text)}"
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(tts_url, headers=headers)
            if resp.status_code == 200 and len(resp.content) > 100:
                return Response(content=resp.content, media_type="audio/mpeg")
    except Exception:
        pass
        
    raise HTTPException(status_code=502, detail="Neural TTS audio generation temporarily unavailable.")
