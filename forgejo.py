import os

os.system("sudo apt update")
os.system("sudo apt upgrade")
os.system("sudo apt install unattended-upgrades")
os.system("sudo dpkg-reconfigure unattended-upgrades")
os.system("sudo apt autoremove")
os.system("sudo apt autoclean")
os.system("sudo docker run -d --name=forgejo --restart always -p 80:3000 codeberg.org/forgejo/forgejo:13")
