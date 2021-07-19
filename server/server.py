import os
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


@app.get("/songs")
async def songs():
    return music_mixer.database


@app.post("/song/song_mix")
def first_post(song_mix: SongMix, request: Request):
    # request.client.host to get IP: for slowapi
    print(song_mix.parts)
    mixed_song_filestream = music_mixer.mix(song_mix.song, song_mix.parts)
    if mixed_song_filestream is None:
        return {"error": "bad input"}
    mixed_song_filestream.seek(0)
    return StreamingResponse(mixed_song_filestream, media_type="audio/mp3")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=7880)
