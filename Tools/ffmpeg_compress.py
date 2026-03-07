import json
import os

files = os.listdir(".")
files.sort()

if not os.path.exists("OUT"):
    os.mkdir("OUT")
    
for file in files:
    if file.endswith(".mkv"):
        print(f"Converting {file}")

        os.system(f"ffprobe -show_streams -print_format json -i '{file}' > out.json")
        with open("out.json", "r") as f:
            data = json.loads(f.read())

        best_audio = -1
        for i in list(data.values())[0]:
            if i["tags"]["language"] == "eng" and i["codec_type"] == "audio":
                if i["channel_layout"] != "stereo" and i["channel_layout"] != "mono":
                    best_audio = i["index"]
                    break

        if best_audio == -1:
             os.system(f"ffmpeg -i '{file}' -c:a flac -c:s copy -c:v copy 'OUT/{file}'")
             
        else:
            os.system(f"ffmpeg -i '{file}' -map 0:v:0 -map 0:a:{best_audio} -c:a flac -c:s copy -c:v copy 'OUT/{file}'")
