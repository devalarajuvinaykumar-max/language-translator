import time
from collections import defaultdict
from fastapi import HTTPException, Request, status

class SimpleRateLimiter:
    def __init__(self, requests_per_minute: int = 100):
        self.requests_per_minute = requests_per_minute
        self.requests = defaultdict(list)

    def check_rate_limit(self, client_ip: str):
        current_time = time.time()
        # Clean timestamps older than 60s
        self.requests[client_ip] = [
            ts for ts in self.requests[client_ip] if current_time - ts < 60
        ]
        
        if len(self.requests[client_ip]) >= self.requests_per_minute:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Please try again later."
            )
        self.requests[client_ip].append(current_time)

rate_limiter = SimpleRateLimiter()

def sanitize_text(text: str) -> str:
    """Basic input sanitization to strip unwanted executable script injections."""
    if not text:
        return ""
    # Strip dangerous HTML script tags if present
    cleaned = text.replace("<script>", "").replace("</script>", "")
    return cleaned.strip()
