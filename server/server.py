import io
import os
from typing import List

from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel
from fastapi.responses import StreamingResponse, FileResponse  # NOTE: fileresponse need aiofiles
from starlette.background import BackgroundTasks

from mixer import MusicMixer

# import slowapi # to limit requests

app = FastAPI()
music_mixer = MusicMixer()


class SongMix(BaseModel):
    song: str
    parts: List[str]


def remove_file(path: str) -> None:
    os.unlink(path)

@app.get("/")
async def root():
    return {"Parliament attack": "Thrapp"}


@app.post("/song/song_mix")
def first_post(song_mix: SongMix, request: Request):
    # request.client.host to get IP: for slowapi
    # TODO: still need to figure out how to get mp3 file from pydub without saving it into a file first
    mixed_song_filename = music_mixer.mix(song_mix.song, song_mix.parts)
    if mixed_song_filename is None:
        return {"error": "bad input"}
    return FileResponse(mixed_song_filename, media_type="audio/mp3")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=7880)
