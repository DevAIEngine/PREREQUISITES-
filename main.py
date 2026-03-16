from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="GUCE Engine Blueprint")

class EngineStatus(BaseModel):
    status: str
    version: str

@app.get("/", response_model=EngineStatus)
async def get_status():
    return {"status": "operational", "version": "1.0.0"}

@app.get("/engine/test/{test_id}")
async def run_test(test_id: int):
    if test_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid test ID")
    return {"message": f"Test {test_id} executed successfully"}
