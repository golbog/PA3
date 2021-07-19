import io
import os
import json
from typing import List

from pydub import AudioSegment  # maybe use SoX


class MusicMixer:
    def __init__(self, songs_json="songs.json", songs_folder="./songs/"):
        self.songs_folder = songs_folder
        self.database = json.load(open(songs_json, "r"))

    def is_valid_song(self, song_name):
        return self.database.get(song_name, None) is not None

    def are_valid_tracks(self, song_name, track_names):
        if len(track_names) == 0:
            return False

        for track in track_names:
            if track not in self.database[song_name]:
                return False
        return True

    def mix(self, song: str, tracks: List[str]):
        if not self.is_valid_song(song):
            return

        if not self.are_valid_tracks(song, tracks):
            return

        track_files = list()
        for track in tracks:
            track_files.append(AudioSegment.from_file(os.path.join(self.songs_folder, song, track)))

        result = track_files[0]
        for track in track_files[1:]:
            result = result.overlay(track)  # TODO: check for clipping and reduce gain if needed?
        filestream = io.BytesIO()
        result.export(filestream)
        return filestream

    @staticmethod
    def raw_from_file(filename):
        return AudioSegment.from_file(filename).raw_data


if __name__ == '__main__':
    mm = MusicMixer()
    print(mm.database)

    a = mm.mix("tipi", ["bobni_elektro.mp3", "guitar.mp3", "synth.mp3", "vocal_main.mp3"])
    a.export("tipi.mp3", format="mp3")
