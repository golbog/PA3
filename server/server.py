from typing import List

from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel

# import slowapi # to limit requests

app = FastAPI()

class SongMix(BaseModel):
    song: int
    parts: List[int]


@app.get("/")
async def root():
    return {"Parliament attack": "Thrapp"}


@app.post("/song/song_mix")
async def first_post(song_mix: SongMix, request: Request):
    #request.client.host to get IP
    return {"song_mix": song_mix}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=7880)