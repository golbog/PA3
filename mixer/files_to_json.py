import os
import sys
import json

if __name__ == '__main__':
    if len(sys.argv) == 1:
        base_path = "../songs/"
    else:
        base_path = sys.argv[0]

    print(base_path)

    songs = dict()
    for dir in os.listdir(base_path):
        work_dir = os.path.join(base_path, dir)
        if os.path.isdir(work_dir):
            songs[dir] = list()
            for file in os.listdir(work_dir):
                work_file = os.path.join(work_dir, file)
                if os.path.isfile(work_file):
                    songs[dir].append(file)
                    print(dir, file)

    json.dump(songs, open("songs.json", "w"))
