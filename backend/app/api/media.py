from fastapi import APIRouter, HTTPException
from backend.app.models.requests import YouTubeTranslateRequest, MeetingAnalyzeRequest
from backend.app.models.responses import YouTubeTranslationResponse, MeetingTranslationResponse
from backend.app.services.youtube_service import youtube_service
from backend.app.services.speech_diarization import speech_diarization

router = APIRouter()

@router.post("/youtube", response_model=YouTubeTranslationResponse)
async def translate_youtube_video(payload: YouTubeTranslateRequest):
    if not payload.url:
        raise HTTPException(status_code=400, detail="YouTube URL required.")
    return youtube_service.translate_youtube_video(payload.url, payload.target_lang)

@router.post("/meeting", response_model=MeetingTranslationResponse)
async def process_meeting_transcript(payload: MeetingAnalyzeRequest):
    if not payload.transcript:
        raise HTTPException(status_code=400, detail="Transcript required.")
    return speech_diarization.process_transcript(payload.meeting_title, payload.transcript, payload.target_lang)
