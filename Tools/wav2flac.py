import os

files = os.listdir(".")
files.sort()
for file in files:
    if file.endswith(".wav"):
        print(f"Converting {file}")
        os.system(f"ffmpeg -i {file.replace(' ','\\ ')} {file.replace('.wav','.flac').replace(' ','\\ ')}")
