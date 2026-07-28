import re
from typing import Dict, List, Any
from backend.app.core.config import settings

class IntelligentLanguageDetector:
    """Detects primary language, multiple languages in text, and mixed-language conversations."""
    
    # Common character sets / scripts regex patterns for instant detection
    SCRIPTS = {
        "hi": re.compile(r'[\u0900-\u097F]'),  # Devanagari
        "te": re.compile(r'[\u0C00-\u0C7F]'),  # Telugu
        "zh": re.compile(r'[\u4E00-\u9FFF]'),  # Chinese
        "ja": re.compile(r'[\u3040-\u30FF]'),  # Japanese
        "ar": re.compile(r'[\u0600-\u06FF]'),  # Arabic
        "ru": re.compile(r'[\u0400-\u04FF]'),  # Cyrillic
        "ko": re.compile(r'[\uAC00-\uD7AF]'),  # Hangul
    }
    
    # Common words for European language estimation
    COMMON_WORDS = {
        "fr": {"le", "la", "les", "des", "est", "et", "en", "que", "du", "une"},
        "es": {"el", "la", "los", "las", "por", "para", "con", "que", "una", "del"},
        "de": {"der", "die", "das", "und", "ist", "in", "den", "zu", "mit", "nicht"},
        "it": {"il", "la", "che", "per", "non", "del", "con", "una", "sono", "gli"},
        "pt": {"com", "para", "como", "esta", "que", "por", "uma", "mais", "dos"}
    }

    def detect_language(self, text: str) -> Dict[str, Any]:
        cleaned = text.strip()
        if not cleaned:
            return {
                "detected_language": "en",
                "language_name": "English",
                "confidence": 1.0,
                "is_mixed": False,
                "detected_languages": [{"lang": "en", "confidence": 1.0}]
            }
            
        # Check non-Latin script patterns first
        for lang_code, pattern in self.SCRIPTS.items():
            matches = pattern.findall(cleaned)
            if len(matches) > 0 and len(matches) / max(len(cleaned), 1) > 0.15:
                lang_name = settings.SUPPORTED_LANGUAGES.get(lang_code, lang_code.upper())
                return {
                    "detected_language": lang_code,
                    "language_name": lang_name,
                    "confidence": 0.96,
                    "is_mixed": False,
                    "detected_languages": [{"lang": lang_code, "confidence": 0.96}]
                }
                
        # Word frequency check for Latin-script languages
        words = [w.lower() for w in re.findall(r'\b\w+\b', cleaned)]
        if not words:
            return {
                "detected_language": "en",
                "language_name": "English",
                "confidence": 0.9,
                "is_mixed": False,
                "detected_languages": [{"lang": "en", "confidence": 0.9}]
            }
            
        scores = {"en": 1} # base English weight
        detected_parts = []
        
        for lang, vocab in self.COMMON_WORDS.items():
            matches = sum(1 for w in words if w in vocab)
            if matches > 0:
                scores[lang] = matches * 3
                
        primary_lang = max(scores, key=scores.get)
        total_score = sum(scores.values())
        
        is_mixed = len([k for k, v in scores.items() if v > 1]) > 1
        confidence = min(0.98, max(0.65, scores[primary_lang] / total_score))
        
        for lang_code, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            if score > 0:
                detected_parts.append({
                    "lang": lang_code,
                    "name": settings.SUPPORTED_LANGUAGES.get(lang_code, lang_code.upper()),
                    "confidence": round(score / total_score, 2)
                })

        return {
            "detected_language": primary_lang,
            "language_name": settings.SUPPORTED_LANGUAGES.get(primary_lang, "English"),
            "confidence": round(confidence, 2),
            "is_mixed": is_mixed,
            "detected_languages": detected_parts
        }

language_detector = IntelligentLanguageDetector()
