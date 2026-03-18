# WARNING: MAKE A COPY before using this script, this will rename files if they can't be used correctly.

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
            if file.endswith(".flac") or file.endswith(".wav"):
                # force rename removing quotes
                os.rename(file,file.replace("'","").replace('"',''))
                print(f"Converting {file.replace('\'','').replace('\"','')}")
                os.system(f"ffmpeg -i '{file.replace('\'','').replace('\"','')}' 'OUT/{file.replace('\'','').replace('\"','').replace('.flac', '.mp3').replace('.wav', '.mp3')}'")

            if file.endswith(".mkv"):
                # force rename removing quotes
                os.rename(file,file.replace("'","").replace('"',''))
                print(f"Converting {file.replace('\'','').replace('\"','')}")
                os.system(f"ffmpeg -i '{file.replace('\'','').replace('\"','')}' 'OUT/{file.replace('\'','').replace('\"','').replace('.mkv', '.mp4')}'")
