import os

os.system("sudo apt update")
os.system("sudo apt upgrade")
os.system("sudo apt install unattended-upgrades")
os.system("sudo dpkg-reconfigure unattended-upgrades")
os.system("sudo apt autoremove")
os.system("sudo apt autoclean")
os.system("sudo docker pull jgraph/drawio")
os.system("sudo docker run -d --name=drawio --restart always -p 80:8080 jgraph/drawio")
