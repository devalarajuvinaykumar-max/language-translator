from typing import List, Dict, Any

class EmotionAnalyzer:
    """Detects primary and secondary emotions to preserve tone in translated text & voice."""

    EMOTION_KEYWORDS = {
        "happy": ["happy", "great", "awesome", "wonderful", "love", "joy", "excited", "glad", "delighted"],
        "excited": ["congratulations", "hurray", "lets go", "amazing", "incredible", "thrilled"],
        "sad": ["sad", "sorry", "unfortunate", "grief", "depressed", "heartbroken", "disappointed"],
        "angry": ["angry", "furious", "hate", "unacceptable", "horrible", "outraged", "annoyed"],
        "fear": ["afraid", "scared", "fear", "worried", "anxious", "terrified", "danger"],
        "surprise": ["wow", "surprised", "unexpected", "unbelievable", "astonishing", "shocker"]
    }

    def detect_emotions(self, text: str) -> List[str]:
        words = text.lower().split()
        emotions_found = set()
        
        for emotion, keywords in self.EMOTION_KEYWORDS.items():
            for kw in keywords:
                if kw in words or kw in text.lower():
                    emotions_found.add(emotion)
                    
        if not emotions_found:
            return ["neutral"]
        return list(emotions_found)

emotion_analyzer = EmotionAnalyzer()
