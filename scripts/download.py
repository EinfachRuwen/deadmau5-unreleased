import os

def download():
    x = input("URL? | ")
    os.system(f"youtube-dl -x --audio-format mp3 {x}")
    download()

download()