import json
import os

files = os.listdir(".")
files.sort()

if not os.path.exists("OUT"):
    os.mkdir("OUT")
    
for file in files:
    if file.endswith(".mkv"):
        print(f"Converting {file}")
        os.system(f"ffmpeg -i '{file}' -c:v copy -c:s copy  -c:a flac 'OUT/{file}'")
