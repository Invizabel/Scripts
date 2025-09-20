sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt clean all
sudo docker pull ghcr.io/mealie-recipes/mealie:latest
sudo docker run -d --name=mealie --restart always -p 80:9000 -v ghcr.io/mealie-recipes/mealie:latest
sudo reboot