from fastapi import FastAPI
from pydantic import BaseModel
import edge_tts
import uuid

app = FastAPI()

class TTSRequest(BaseModel):
    text: str

@app.post("/tts")
async def tts(req: TTSRequest):
    filename = f"/tmp/{uuid.uuid4()}.mp3"

    communicate = edge_tts.Communicate(
        text=req.text,
        voice="pt-BR-FranciscaNeural",
        rate="-10%",
        volume="+0%"
    )

    await communicate.save(filename)

    return {"status": "ok", "file": filename}
