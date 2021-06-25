import logging
import os
import json
from typing import List


from pydub import AudioSegment


class MusicMixer:
    def __init__(self, songs_json="songs.json", songs_folder="./songs/"):
        self.songs_folder = songs_folder
        self.database = json.load(open(songs_json, "r"))

    def is_valid_song(self, song_name):
        return self.database.get(song_name, None) is not None

    def are_valid_tracks(self, song_name, track_names):
        if self.database.get(song_name, None) is None:
            return False

        for track in track_names:
            if self.database.get(song_name, None) is None:
                return False

        return True

    def mix(self, song: str, tracks: List[str]):
        if not self.is_valid_song(song):
            return False

        if not self.are_valid_tracks(song, tracks):
            return False

        track_files = list()

        for track in tracks[1:]:
            track_files.append(AudioSegment.from_file(os.path.join(self.songs_folder, song, track)))

        # TODO: check length of the tracks list
        result = track_files[0]
        for track in track_files[1:]:
            result = result.overlay(track)

        return result


if __name__ == '__main__':
    mm = MusicMixer()
    print(mm.database)

    a = mm.mix("tipi", ["bobni_elektro.mp3", "guitar.mp3", "synth.mp3", "vocal_main.mp3"])
    a.export("tipi.mp3", format="mp3")
