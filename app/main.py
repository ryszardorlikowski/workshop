from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()
settings = get_settings()

@app.get("/")
async def show_config(current_settings: Settings = Depends(get_settings)):
    return current_settings.dict()
