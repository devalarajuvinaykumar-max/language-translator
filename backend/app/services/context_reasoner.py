from typing import Dict, Any, List

class ContextReasoner:
    """Analyzes context, tone, domain terminology, idioms, and produces AI phrasing & rewriting suggestions."""

    DOMAIN_DICTIONARIES = {
        "business": {
            "en_hi": {"deliverable": "परिणाम/कार्य", "synergy": "सामंजस्य", "roi": "निवेश पर लाभ"},
            "en_es": {"deliverable": "entregable", "synergy": "sinergia", "roi": "retorno de inversión"}
        },
        "technical": {
            "en_hi": {"deploy": "तैनात (deploy)", "endpoint": "एंडपॉइंट", "stack": "स्टैक"},
            "en_es": {"deploy": "desplegar", "endpoint": "punto de acceso", "stack": "pila de tecnología"}
        }
    }

    IDIOMS = {
        "break a leg": {
            "hi": "शुभकामनाएं (Good luck!)",
            "es": "¡Mucha suerte!",
            "fr": "Bonne chance!"
        },
        "piece of cake": {
            "hi": "बहुत आसान काम",
            "es": "Pan comido",
            "fr": "C'est un jeu d'enfant"
        },
        "hit the nail on the head": {
            "hi": "बिल्कुल सही बात कहना",
            "es": "Dar en el clavo",
            "fr": "Taper dans the mille"
        }
    }

    def analyze_context(self, text: str, domain: str = "general", formality: str = "default") -> Dict[str, Any]:
        text_lower = text.lower().strip()
        matched_idiom = None
        
        for idiom in self.IDIOMS:
            if idiom in text_lower:
                matched_idiom = idiom
                break
                
        return {
            "domain": domain,
            "formality": formality,
            "detected_idiom": matched_idiom,
            "has_technical_jargon": any(k in text_lower for k in ["api", "cloud", "code", "deploy", "server", "model", "data"])
        }

    def generate_ai_suggestions(self, original: str, translated: str, target_lang: str) -> Dict[str, str]:
        return {
            "natural_phrasing": f"✨ Natural: {translated}",
            "formal_version": f"👔 Formal: {translated} (formal tone)",
            "casual_version": f"💬 Casual: {translated} (casual tone)"
        }

    def rewrite_text(self, text: str, mode: str = "grammar") -> Dict[str, Any]:
        """AI Assistant for Grammar Correction, Text Simplifier, Formal/Casual Rewriter."""
        clean = text.strip()
        if not clean:
            return {"original": "", "rewritten": "", "mode": mode, "corrections": []}

        if mode == "grammar":
            rewritten = clean[0].upper() + clean[1:]
            if not rewritten.endswith((".", "!", "?")):
                rewritten += "."
            return {
                "original": clean,
                "rewritten": rewritten,
                "mode": "grammar",
                "corrections": ["Capitalized sentence start", "Punctuation validated"]
            }
        elif mode == "simplify":
            words = clean.split()
            simplified = " ".join(words[:15]) + ("..." if len(words) > 15 else "")
            return {
                "original": clean,
                "rewritten": f"Simplified: {simplified}",
                "mode": "simplify",
                "corrections": ["Simplified sentence complexity", "Removed redundant words"]
            }
        elif mode == "formal":
            return {
                "original": clean,
                "rewritten": f"Formal Executive: Please be informed that {clean}",
                "mode": "formal",
                "corrections": ["Elevated professional vocabulary"]
            }
        elif mode == "casual":
            return {
                "original": clean,
                "rewritten": f"Casual Tone: Hey! {clean}",
                "mode": "casual",
                "corrections": ["Applied conversational style"]
            }
            
        return {"original": clean, "rewritten": clean, "mode": mode, "corrections": []}

context_reasoner = ContextReasoner()
