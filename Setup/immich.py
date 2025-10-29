import os

os.system("mkdir ./immich-app")
os.system("wget -O ./immich-app/docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml")
os.system("wget -O ./immich-app/.env https://github.com/immich-app/immich/releases/latest/download/example.env")

os.system("sudo docker compose up -d")
