import os

os.system("sudo docker run -d --name=pelican --restart always -p 80:80 -p 443:443 -e PANEL_HOST=0.0.0.0 -e PANEL_PORT=80 ghcr.io/pelican-dev/panel:main")
