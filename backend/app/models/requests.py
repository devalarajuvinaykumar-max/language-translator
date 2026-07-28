from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class TranslationRequest(BaseModel):
    text: str = Field(..., description="Text to translate", json_schema_extra={"example": "Hello world, how are you?"})
    source_lang: str = Field("auto", description="Source language code (e.g. 'en', 'auto')", json_schema_extra={"example": "en"})
    target_lang: str = Field("hi", description="Target language code (e.g. 'hi', 'fr')", json_schema_extra={"example": "hi"})
    context_domain: Optional[str] = Field("general", description="Domain context: general, business, technical, academic, casual")
    formality: Optional[str] = Field("default", description="Formality level: default, formal, informal")

class DetectLanguageRequest(BaseModel):
    text: str = Field(..., description="Text to detect language for")

class YouTubeTranslateRequest(BaseModel):
    url: str = Field(..., description="YouTube video URL")
    target_lang: str = Field("hi", description="Target language code")

class MeetingAnalyzeRequest(BaseModel):
    meeting_title: Optional[str] = "Team Meeting"
    transcript: str = Field(..., description="Raw meeting transcript text")
    target_lang: str = Field("hi", description="Target language code")

class MemorySaveRequest(BaseModel):
    source_text: str
    translated_text: str
    source_lang: str
    target_lang: str
    domain: Optional[str] = "general"

class WritingAssistantRequest(BaseModel):
    text: str = Field(..., description="Text to improve or rewrite")
    mode: str = Field("grammar", description="Mode: 'grammar', 'simplify', 'formal', 'casual', 'summarize'")

class CompareTranslationRequest(BaseModel):
    text: str = Field(..., description="Text to compare across engines")
    source_lang: str = Field("en", description="Source language")
    target_lang: str = Field("hi", description="Target language")

class WebsiteTranslateRequest(BaseModel):
    url: str = Field(..., description="Webpage URL to translate")
    target_lang: str = Field("hi", description="Target language")

class AIChatRequest(BaseModel):
    user_message: str = Field(..., description="User message in chat")
    chat_history: List[Dict[str, str]] = Field(default_factory=list)
    user_lang: str = Field("en", description="User's native language")
    partner_lang: str = Field("hi", description="Partner's language")
