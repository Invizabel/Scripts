# increase volume to 1000% (-filter:a 'volume=10')

import os

os.system("ls -R > directory_listing.txt")

if not os.path.exists("OUT"):
    os.mkdir("OUT")
    
folder = ""
with open("directory_listing.txt", "r") as file:
    for line in file:
        if line.startswith("./"):
            folder = line.strip()[:-1].replace("./", "")
            if not os.path.exists(f"OUT/{folder}"):
                os.mkdir(f"OUT/{folder}")
        else:
            file = f"{folder}/{line}".strip()
            if file.endswith(".mp3"):
                print(f"Converting {file}")
                os.system(f"ffmpeg -i '{file}' -filter:a 'volume=10' 'OUT/{file}'")

            if file.endswith(".mp4"):
                print(f"Converting {file}")
                os.system(f"ffmpeg -i '{file}' -filter:a 'volume=10' 'OUT/{file}'")
