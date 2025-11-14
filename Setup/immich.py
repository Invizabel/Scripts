import os

os.system("wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml")
os.system("wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env")

os.system("sudo docker compose up -d")

