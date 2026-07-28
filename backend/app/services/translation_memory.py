import time
import json
from typing import List, Dict, Any, Optional

class TranslationMemory:
    """Manages translation memory, phrase caching, terminology consistency, and search history."""

    def __init__(self):
        self._memory_store: List[Dict[str, Any]] = []
        self._bookmarks: List[Dict[str, Any]] = []

    def get_cached_translation(self, source_text: str, source_lang: str, target_lang: str) -> Optional[Dict[str, Any]]:
        key = source_text.strip().lower()
        for entry in self._memory_store:
            if (entry["source_text"].strip().lower() == key and 
                entry["source_lang"] == source_lang and 
                entry["target_lang"] == target_lang):
                return entry
        return None

    def save_translation(self, source_text: str, translated_text: str, source_lang: str, target_lang: str, domain: str = "general") -> Dict[str, Any]:
        entry = {
            "id": len(self._memory_store) + 1,
            "source_text": source_text,
            "translated_text": translated_text,
            "source_lang": source_lang,
            "target_lang": target_lang,
            "domain": domain,
            "timestamp": time.time(),
            "is_bookmarked": False
        }
        self._memory_store.append(entry)
        return entry

    def get_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        return sorted(self._memory_store, key=lambda x: x["timestamp"], reverse=True)[:limit]

    def bookmark_item(self, entry_id: int) -> bool:
        for item in self._memory_store:
            if item["id"] == entry_id:
                item["is_bookmarked"] = True
                if item not in self._bookmarks:
                    self._bookmarks.append(item)
                return True
        return False

    def get_bookmarks(self) -> List[Dict[str, Any]]:
        return self._bookmarks

translation_memory = TranslationMemory()
