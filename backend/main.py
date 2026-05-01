from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import uuid
import logging
import os
import hmac

# Configure Logging for Epistemic Stability
logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger("guce_orchestrator")

app = FastAPI(
    title="Google Universe Cinematic Engine (GUCE)",
    description="Federal-Scale Legacy Preservation Engine",
    version="4.0.0"
)

# Core State Machine: The Project Manifest
class ProjectManifest(BaseModel):
    project_id: str
    user_id: str
    status: str = "INITIALIZED"
    target_duration: str = "LONG_FORM" # SHORTS (1min) or LONG_FORM (5-30min)
    voice_profile_id: str | None = None
    language: str = "en"
    scenes: list = []

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Validates the bearer token against the GUCE_API_KEY environment variable.
    Fails securely (500) if the server environment is not configured.
    """
    expected_api_key = os.environ.get("GUCE_API_KEY")
    if not expected_api_key:
        logger.error("GUCE_API_KEY environment variable is not set. Failing securely.")
        raise HTTPException(status_code=500, detail="Internal Server Error: Authentication configuration missing.")

    if not hmac.compare_digest(credentials.credentials, expected_api_key):
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return credentials.credentials

@app.post("/api/v1/capture/stream", response_model=ProjectManifest)
async def start_capture_stream(
    user_id: str,
    background_tasks: BackgroundTasks,
    token: str = Depends(get_current_user)
):
    """
    Entrypoint for the Cell Phone First UI.
    Initializes a live WebSocket/Stream connection for A-Roll and Gemini Live Scene Decomposition.
    """
    project_id = f"guce_proj_{uuid.uuid4().hex[:8]}"
    logger.info(f"Initialized Capture Stream. User: {user_id}, Project: {project_id}")

    manifest = ProjectManifest(project_id=project_id, user_id=user_id, status="STREAMING")

    # In a real implementation, this would establish the WebSocket and trigger Gemini Live.
    return manifest

@app.get("/health")
def health_check():
    """Validates the API is online and the backend is responsive."""
    return {"status": "ok", "version": "4.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
