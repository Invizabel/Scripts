import os

files = os.listdir(".")
files.sort()
for file in files:
    if file.endswith(".mkv"):
        print(f"Converting {file}")
        os.system(f"ffmpeg -i {file} -c:v libx264 -preset placebo -pix_fmt yuv420p {file.replace('.mkv','.mp4')}")
