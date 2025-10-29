import os
import socket

s = socket.socket()
s.connect(("1.1.1.1", 80))
localhost = s.getsockname()[0]
s.close()

with open("index.html","r") as file:
    data = file.read()

with open("index.html","w") as file:
    file.write(data.replace("localhost",localhost))

os.system("sudo apt update")
os.system("sudo apt install p7zip-full curl wget nginx git -y")

os.system("wget https://buildbot.libretro.com/stable/1.21.0/emscripten/RetroArch.7z")
os.system("7z x RetroArch.7z")
os.system("git clone https://github.com/ppeccin/javatari.js")
os.system("git clone https://github.com/mitxela/swotGB")
os.system("sudo mkdir /var/www/html/retroarch")
os.system("sudo mkdir /var/www/html/javatari")
os.system("sudo mkdir /var/www/html/swotgb")
os.system("sudo cp -r retroarch/* /var/www/html/retroarch")
os.system("sudo cp -r javatari.js/release/stable/5.0/standalone/* /var/www/html/javatari")
os.system("sudo cp -r swotGB/gbjs.htm /var/www/html/swotgb/index.html")
os.system("wget https://raw.githubusercontent.com/Invizabel/Scripts/refs/heads/main/All%20The%20Things/index.html")
os.system("sudo cp index.html /var/www/html/index.html")

# docker pull

# port 80
os.system("sudo docker run -d --name=drawio --restart always -p 81:8080 jgraph/drawio")
# port 81
os.system("sudo docker run -d --name=forgejo --restart always -p 82:3000 codeberg.org/forgejo/forgejo:13")
# port 82
os.system("sudo docker run -d --name=mealie --restart always -p 83:9000 ghcr.io/mealie-recipes/mealie:latest")

# docker compose

os.system("mkdir ./immich-app")

# port 3000
os.system("wget -O ./immich-app/docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml")
os.system("wget -O ./immich-app/.env https://github.com/immich-app/immich/releases/latest/download/example.env")
os.system("sudo docker compose -f ./immich-app/docker-compose.yml up -d")
