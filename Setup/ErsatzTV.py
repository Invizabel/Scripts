import os

os.system("sudo docker run -d --name ersatztv -e TZ=America/Chicago -p 80:8409 --restart always ghcr.io/ersatztv/ersatztv")
