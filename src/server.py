from fastapi import FastAPI, Request, HTTPException
from src.auth import verify_token
from src.task_router import route_task

app = FastAPI()

@app.post("/task")
async def handle_task(request: Request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Unauthorized")
    payload = await request.json()
    return route_task(payload)
