import os

os.system("sudo docker run -d --name=forgejo --restart always -p 80:3000 codeberg.org/forgejo/forgejo:14.0.2")

