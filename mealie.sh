sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt clean all
sudo docker run -d --name=mealie --restart always -p 80:9000 -v ghcr.io/mealie-recipes/mealie:latest
sudo reboot