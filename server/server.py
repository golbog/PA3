import io
from typing import List

from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

from mixer import MusicMixer

# import slowapi # to limit requests

app = FastAPI()
music_mixer = MusicMixer()


class SongMix(BaseModel):
    song: str
    parts: List[str]


@app.get("/")
async def root():
    return {"Parliament attack": "Thrapp"}


@app.post("/song/song_mix")
async def first_post(song_mix: SongMix, request: Request):
    # request.client.host to get IP: for slowapi
    mixed_song = music_mixer.mix(song_mix.song, song_mix.parts)
    if mixed_song is None:
        return {"error": "bad input"}
    return StreamingResponse(io.BytesIO(mixed_song), media_type="media/mp3")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=7880)
