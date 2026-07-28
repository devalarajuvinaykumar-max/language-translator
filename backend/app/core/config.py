import os
from typing import List, Dict

class Settings:
    PROJECT_NAME: str = "OmniTranslate AI Platform"
    VERSION: str = "2.0.0"
    API_V1_STR: str = "/api/v1"
    
    # API Keys (Loaded from environment variables with safe fallbacks)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:5500",
        "*"
    ]
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 100
    
    # Default Supported Languages
    SUPPORTED_LANGUAGES: Dict[str, str] = {
        "auto": "Auto Detect",
        "en": "English",
        "hi": "Hindi",
        "te": "Telugu",
        "fr": "French",
        "es": "Spanish",
        "de": "German",
        "zh": "Chinese (Simplified)",
        "ja": "Japanese",
        "ar": "Arabic",
        "ru": "Russian",
        "pt": "Portuguese",
        "it": "Italian",
        "ko": "Korean"
    }

settings = Settings()
