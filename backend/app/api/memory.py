from fastapi import APIRouter
from typing import List, Dict, Any
from backend.app.services.translation_memory import translation_memory

router = APIRouter()

@router.get("/memory/history")
async def get_translation_history():
    return translation_memory.get_history()

@router.post("/memory/bookmark/{entry_id}")
async def bookmark_translation(entry_id: int):
    success = translation_memory.bookmark_item(entry_id)
    return {"success": success, "entry_id": entry_id}

@router.get("/memory/bookmarks")
async def get_bookmarks():
    return translation_memory.get_bookmarks()
