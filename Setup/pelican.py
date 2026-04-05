import os

host_name = input("host name: ")
admin_email = input("admin email: ")
os.system(f"sudo docker run -d --name=pelican --restart always -p 80:80 -p 443:443 -v pelican-data:/pelican-data -v pelican-logs:/var/www/html/storage/logs -e XDG_DATA_HOME=/pelican-data -e APP_URL='http://{host_name}' -e ADMIN_EMAIL='{admin_email}' -e PANEL_HOST=0.0.0.0 -e PANEL_PORT=80 ghcr.io/pelican-dev/panel:main")
