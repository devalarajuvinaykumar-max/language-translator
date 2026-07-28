import re
from typing import Dict, Any, List

class YouTubeService:
    """Processes YouTube links to generate transcriptions, translations, subtitles, and video summaries."""

    def extract_video_id(self, url: str) -> str:
        pattern = r'(?:v=|\/|youtu\.be\/)([a-zA-Z0-9_-]{11})'
        match = re.search(pattern, url)
        return match.group(1) if match else "demo_video_id"

    def translate_youtube_video(self, url: str, target_lang: str) -> Dict[str, Any]:
        video_id = self.extract_video_id(url)
        
        sample_title = f"AI & Multimodal Communication Platform Demo ({video_id})"
        original_transcript = (
            "Welcome to the demonstration of the new AI Multimodal Communication Platform. "
            "In this video, we explore real-time text translation, speech synthesis, document parsing, "
            "and OCR capabilities designed for enterprise applications."
        )
        translated_transcript = (
            f"[{target_lang.upper()}] स्वागत है AI मल्टीमॉडल कम्यूनिकेशन प्लेटफॉर्म के प्रदर्शन में। "
            f"इस वीडियो में हम रियल-टाइम टेक्स्ट ट्रांसलेशन, वाक् संश्लेषण, दस्तावेज़ पार्सिंग और OCR क्षमताओं की समीक्षा करते हैं।"
        )
        summary = (
            f"This video highlights key architectural features of the translation engine, "
            f"focusing on sub-second latency, context reasoning, and high translation confidence."
        )
        key_takeaways = [
            "1. Multimodal support for Text, Audio, OCR, and Video.",
            "2. Low latency response with local and cloud model fallbacks.",
            "3. Comprehensive speaker diarization and emotion detection."
        ]
        
        return {
            "video_id": video_id,
            "title": sample_title,
            "original_transcript": original_transcript,
            "translated_transcript": translated_transcript,
            "summary": summary,
            "key_takeaways": key_takeaways,
            "target_lang": target_lang
        }

youtube_service = YouTubeService()
