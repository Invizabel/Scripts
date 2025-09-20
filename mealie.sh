sudo apt update
sudo apt upgrade
sudo apt install unattended-upgrades
sudo dpkg-reconfigure unattended-upgrades
sudo apt autoremove
sudo apt autoclean
sudo docker pull ghcr.io/mealie-recipes/mealie:latest
sudo docker run -d --name=mealie --restart always -p 80:9000 ghcr.io/mealie-recipes/mealie:latest
