import time
import httpx
import urllib.parse
from typing import Dict, Any, List, Optional
from backend.app.core.config import settings
from backend.app.services.language_detector import language_detector
from backend.app.services.context_reasoner import context_reasoner
from backend.app.services.emotion_analyzer import emotion_analyzer
from backend.app.services.translation_memory import translation_memory

class TranslationEngine:
    """High-Performance Async Translation Orchestrator using Neural Google GTX, MyMemory, and Cloud LLMs."""

    def __init__(self):
        self.google_gtx_url = "https://translate.googleapis.com/translate_a/single"
        self.mymemory_url = "https://api.mymemory.translated.net/get"
        # In-memory fast LRU cache for 0ms responses on duplicate phrases
        self._fast_cache: Dict[str, Dict[str, Any]] = {}

    async def translate_async(
        self,
        text: str,
        source_lang: str = "auto",
        target_lang: str = "hi",
        domain: str = "general",
        formality: str = "default"
    ) -> Dict[str, Any]:
        start_time = time.time()
        text_clean = text.strip()
        
        # 1. Automatic Language Detection
        detected_info = language_detector.detect_language(text_clean)
        actual_source = detected_info["detected_language"] if source_lang == "auto" else source_lang
        
        cache_key = f"{actual_source}|{target_lang}|{domain}|{formality}|{text_clean.lower()}"
        
        # 2. Check Fast In-Memory Cache (0ms latency)
        if cache_key in self._fast_cache:
            res = self._fast_cache[cache_key].copy()
            res["processing_time_ms"] = round((time.time() - start_time) * 1000, 2)
            return res

        # 3. Check Persistent Translation Memory
        cached = translation_memory.get_cached_translation(text_clean, actual_source, target_lang)
        if cached:
            elapsed = (time.time() - start_time) * 1000
            result = {
                "translated_text": cached["translated_text"],
                "detected_source_lang": actual_source,
                "target_lang": target_lang,
                "confidence_score": 0.99,
                "alternatives": [f"[Cached Alternate]: {cached['translated_text']}"],
                "ai_suggestions": context_reasoner.generate_ai_suggestions(text_clean, cached["translated_text"], target_lang),
                "detected_emotions": emotion_analyzer.detect_emotions(text_clean),
                "processing_time_ms": round(elapsed, 2)
            }
            self._fast_cache[cache_key] = result
            return result

        # 4. Check Context & Idiom Dictionary
        ctx = context_reasoner.analyze_context(text_clean, domain, formality)
        idiom_match = ctx.get("detected_idiom")
        
        if idiom_match and idiom_match in context_reasoner.IDIOMS and target_lang in context_reasoner.IDIOMS[idiom_match]:
            translated_text = context_reasoner.IDIOMS[idiom_match][target_lang]
            confidence = 0.98
        else:
            # 5. Execute High-Accuracy Neural Translation (Google GTX Primary -> MyMemory Fallback)
            translated_text, confidence = await self._fetch_neural_translation(text_clean, actual_source, target_lang)

        # 6. Apply Formality Post-Processing if requested
        if formality == "formal" and target_lang == "hi":
            translated_text = translated_text.replace("तुम", "आप").replace("तू", "आप")
        elif formality == "informal" and target_lang == "hi":
            translated_text = translated_text.replace("आप", "तुम")

        # 7. Emotion Analysis & Phrasing Suggestions
        emotions = emotion_analyzer.detect_emotions(text_clean)
        ai_suggestions = context_reasoner.generate_ai_suggestions(text_clean, translated_text, target_lang)
        
        alternatives = [
            f"Primary: {translated_text}",
            f"Alternative: {translated_text} ({formality.capitalize()} Tone)"
        ]

        # 8. Save to Memory
        translation_memory.save_translation(text_clean, translated_text, actual_source, target_lang, domain)

        elapsed = (time.time() - start_time) * 1000
        
        result = {
            "translated_text": translated_text,
            "detected_source_lang": actual_source,
            "target_lang": target_lang,
            "confidence_score": round(confidence, 2),
            "alternatives": alternatives,
            "ai_suggestions": ai_suggestions,
            "detected_emotions": emotions,
            "processing_time_ms": round(elapsed, 2)
        }
        
        # Save to fast cache
        self._fast_cache[cache_key] = result
        return result

    async def _fetch_neural_translation(self, text: str, source_lang: str, target_lang: str) -> (str, float):
        """Fetches translation asynchronously using Neural Google GTX API (high accuracy) with MyMemory fallback."""
        src = "auto" if source_lang == "auto" else source_lang
        
        # 1. Primary Engine: Neural Google GTX API
        try:
            params = {
                "client": "gtx",
                "sl": src,
                "tl": target_lang,
                "dt": "t",
                "q": text
            }
            async with httpx.AsyncClient(timeout=3.0) as client:
                resp = await client.get(self.google_gtx_url, params=params)
                if resp.status_code == 200:
                    data = resp.json()
                    # Google GTX format: [[["translated_segment", "original_segment"], ...]]
                    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
                        segments = [item[0] for item in data[0] if isinstance(item, list) and len(item) > 0 and item[0]]
                        full_translation = "".join(segments).strip()
                        if full_translation:
                            return full_translation, 0.98
        except Exception:
            pass

        # 2. Secondary Fallback Engine: MyMemory API
        try:
            url = f"{self.mymemory_url}?q={urllib.parse.quote(text)}&langpair={src}|{target_lang}"
            async with httpx.AsyncClient(timeout=3.0) as client:
                resp = await client.get(url)
                if resp.status_code == 200:
                    data = resp.json()
                    translated = data.get("responseData", {}).get("translatedText")
                    match_score = float(data.get("responseData", {}).get("match", 0.85))
                    if translated and not translated.startswith("MYMEMORY WARNING"):
                        return translated, min(0.95, max(0.65, match_score))
        except Exception:
            pass

        # 3. Emergency Offline Fallback
        return text, 0.50

    def translate(self, text: str, source_lang: str = "auto", target_lang: str = "hi", domain: str = "general", formality: str = "default") -> Dict[str, Any]:
        """Synchronous wrapper for backward compatibility."""
        import asyncio
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # If already in event loop, create task or run until complete
                import nest_asyncio
                nest_asyncio.apply()
                return loop.run_until_complete(self.translate_async(text, source_lang, target_lang, domain, formality))
            else:
                return loop.run_until_complete(self.translate_async(text, source_lang, target_lang, domain, formality))
        except Exception:
            return asyncio.run(self.translate_async(text, source_lang, target_lang, domain, formality))

translation_engine = TranslationEngine()
