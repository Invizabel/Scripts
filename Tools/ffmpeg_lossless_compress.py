import os

files = os.listdir(".")
files.sort()
if not os.path.exists("OUT"):
    os.mkdir("OUT")
for file in files:
    if file.endswith(".mkv"):
        print(f"Converting {file}")
        os.system(f"ffmpeg -i {file.replace(' ','\\ ')} -c:v ffv1 -c:a flac OUT/{file.replace(' ','\\ ')}")

    if file.endswith(".wav"):
        print(f"Converting {file}")
        os.system(f"ffmpeg -i {file.replace(' ','\\ ')} OUT/{file.replace('.wav','.flac').replace(' ','\\ ')}")
