import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.app.core.config import settings
from backend.app.api.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Enterprise-grade AI Multimodal Communication Platform supporting Text, Speech, OCR, Documents, Webpages, YouTube, and Meetings.",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API v1 Router
app.include_router(api_router, prefix=settings.API_V1_STR)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
frontend_dir = os.path.join(base_dir, "frontend")

if os.path.exists(frontend_dir):
    app.mount("/frontend", StaticFiles(directory=frontend_dir), name="frontend")

@app.get("/style.css")
async def serve_style():
    path = os.path.join(base_dir, "style.css")
    if os.path.exists(path):
        return FileResponse(path)
    return FileResponse(os.path.join(frontend_dir, "css", "style.css"))

@app.get("/script.js")
async def serve_script():
    path = os.path.join(base_dir, "script.js")
    if os.path.exists(path):
        return FileResponse(path)
    return FileResponse(os.path.join(frontend_dir, "js", "app.js"))

@app.get("/")
async def serve_index():
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "ok", "uptime": "healthy"}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
