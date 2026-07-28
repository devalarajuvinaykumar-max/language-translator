import io
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text or "OmniTranslate" in response.text

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_text_translation_endpoint():
    payload = {
        "text": "Hello, world! How are you today?",
        "source_lang": "en",
        "target_lang": "hi"
    }
    response = client.post("/api/v1/translate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "translated_text" in data
    assert data["target_lang"] == "hi"
    assert data["confidence_score"] > 0.0

def test_language_detection_endpoint():
    payload = {"text": "Bonjour tout le monde!"}
    response = client.post("/api/v1/detect", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "detected_language" in data

def test_ocr_translation_endpoint():
    file_data = io.BytesIO(b"Fake image content")
    response = client.post(
        "/api/v1/ocr",
        files={"file": ("sample_invoice.png", file_data, "image/png")},
        data={"target_lang": "hi"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "extracted_text" in data
    assert "translated_text" in data

def test_document_translation_endpoint():
    file_data = io.BytesIO(b"Sample document text content for parsing.")
    response = client.post(
        "/api/v1/document",
        files={"file": ("report.docx", file_data, "text/plain")},
        data={"target_lang": "hi"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "translated_text" in data
    assert data["filename"] == "report.docx"

def test_youtube_translation_endpoint():
    payload = {
        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "target_lang": "hi"
    }
    response = client.post("/api/v1/youtube", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "original_transcript" in data
    assert "translated_transcript" in data

def test_meeting_assistant_endpoint():
    payload = {
        "meeting_title": "Sprint Planning Sync",
        "transcript": "Alex: Let's discuss backend architecture.\nMaria: The neural translation speed is optimized.",
        "target_lang": "hi"
    }
    response = client.post("/api/v1/meeting", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert len(data["diarization"]) > 0
    assert "action_items" in data

def test_writing_assistant_endpoint():
    payload = {"text": "hello world this is a test sentence", "mode": "grammar"}
    response = client.post("/api/v1/writing-assistant", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "rewritten" in data

def test_compare_engines_endpoint():
    payload = {"text": "Artificial Intelligence is transforming global communication.", "source_lang": "en", "target_lang": "hi"}
    response = client.post("/api/v1/compare", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "engines" in data

def test_website_translation_endpoint():
    payload = {"url": "https://example.com", "target_lang": "hi"}
    response = client.post("/api/v1/website", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "translated_title" in data

def test_ai_chat_translator_endpoint():
    payload = {"user_message": "Hello, nice to meet you!", "user_lang": "en", "partner_lang": "hi"}
    response = client.post("/api/v1/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "user_translated" in data

def test_analytics_endpoint():
    response = client.get("/api/v1/analytics")
    assert response.status_code == 200
    data = response.json()
    assert data["total_translations"] > 0

def test_translation_memory_history():
    response = client.get("/api/v1/memory/history")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_tts_stream_endpoint():
    response = client.get("/api/v1/tts/stream?text=Hello+world&lang=hi")
    assert response.status_code in [200, 502]
