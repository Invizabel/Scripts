import os

os.system("mkdir ~/config")
os.system("sudo docker run -d --name ersatztv -e TZ=America/Chicago -p 80:8409 -v ~/config:/config --restart always ghcr.io/ersatztv/ersatztv")
