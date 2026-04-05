import os

host_name = input("host name: ")
admin_email = input("admin email: ")
admin_password = input("admin password: ")

os.system(f"sudo docker run -d --name=pelican --restart always "
          f"-p 80:80 -p 443:443 "
          f"-v pelican-data:/pelican-data "
          f"-v pelican-logs:/var/www/html/storage/logs "
          f"-e XDG_DATA_HOME=/pelican-data "
          f"-e APP_URL='http://{host_name}' "
          f"-e ADMIN_EMAIL='{admin_email}' "
          f"-e PANEL_PASSWORD='{admin_password}' "
          f"-e PANEL_HOST=0.0.0.0 "
          f"-e PANEL_PORT=80 "
          f"-e DB_CONNECTION=sqlite "
          f"-e DB_DATABASE=/pelican-data/database.sqlite "
          f"ghcr.io/pelican-dev/panel:main")
