import os

files = os.listdir(".")
files.sort()
for file in files:
    if file.endswith(".mkv"):
        print(f"Converting {file}")
        os.system(f"ffmpeg -i {file} -preset placebo {file.replace('.mkv','.mp4')}")
