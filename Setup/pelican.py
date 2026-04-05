import os

os.system("sudo docker run -d --name=pelican --restart always -p 80:80 -p 443:443 ghcr.io/pelican-dev/panel:latest")
