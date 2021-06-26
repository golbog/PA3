import requests
d = {
  "song": "tipi",
  "parts": ["bobni_rok.mp3", "synth.mp3"]
}
r = requests.post("http://127.0.0.1:7880/song/song_mix", json=d)
print(r)
with open("test.mp3", "wb") as f:
    f.write(r.content)
