import os

os.system("sudo apt update")
os.system("sudo apt upgrade")
os.system("sudo apt git npm nodejs nginx")
os.system("sudo apt install unattended-upgrades")
os.system("sudo dpkg-reconfigure unattended-upgrades")
os.system("sudo apt autoremove")
os.system("sudo apt autoclean")
os.system("mkdir ./immich-app")
os.system("wget -O ./immich-app/docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml")
os.system("wget -O ./immich-app/.env https://github.com/immich-app/immich/releases/latest/download/example.env")
os.system("sudo docker compose up -d")