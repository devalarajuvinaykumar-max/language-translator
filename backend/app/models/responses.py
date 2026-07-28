from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class TranslationResponse(BaseModel):
    translated_text: str
    detected_source_lang: str
    target_lang: str
    confidence_score: float = Field(..., description="Translation confidence (0.0 - 1.0)")
    alternatives: List[str] = Field(default_factory=list)
    ai_suggestions: Dict[str, str] = Field(default_factory=dict)
    detected_emotions: List[str] = Field(default_factory=list)
    processing_time_ms: float

class LanguageDetectionResponse(BaseModel):
    detected_language: str
    language_name: str
    confidence: float
    is_mixed: bool = False
    detected_languages: List[Dict[str, Any]] = Field(default_factory=list)

class OCRTranslationResponse(BaseModel):
    extracted_text: str
    translated_text: str
    source_lang: str
    target_lang: str
    bounding_boxes: List[Dict[str, Any]] = Field(default_factory=list)
    confidence: float

class DocumentTranslationResponse(BaseModel):
    filename: str
    translated_text: str
    source_lang: str
    target_lang: str
    word_count: int
    download_url: Optional[str] = None

class YouTubeTranslationResponse(BaseModel):
    video_id: str
    title: str
    original_transcript: str
    translated_transcript: str
    summary: str
    key_takeaways: List[str]
    target_lang: str

class SpeakerDiarizationItem(BaseModel):
    speaker: str
    timestamp: str
    original_speech: str
    translated_speech: str
    emotion: str

class MeetingTranslationResponse(BaseModel):
    title: str
    diarization: List[SpeakerDiarizationItem]
    summary: str
    action_items: List[str]
    detected_emotions: Dict[str, int]

class AnalyticsResponse(BaseModel):
    total_translations: int
    total_words_translated: int
    average_response_time_ms: float
    average_confidence: float
    top_language_pairs: List[Dict[str, Any]]
    daily_stats: List[Dict[str, Any]]
