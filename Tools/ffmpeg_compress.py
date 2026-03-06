import os

files = os.listdir(".")
files.sort()

hwaccel = input("hardware acceleration: ")

if not os.path.exists("OUT"):
    os.mkdir("OUT")
    
for file in files:
    if file.endswith(".mkv"):
        print(f"Converting {file}")
        os.system(f"ffmpeg -hwaccel {hwaccel} -i '{file}' 'OUT/{file.replace('.mkv','.mp4')}'")

    if file.endswith(".wav"):
        print(f"Converting {file}")
        os.system(f"ffmpeg -hwaccel {hwaccel} -i '{file}' 'OUT/{file.replace('.wav','.flac')}'")
