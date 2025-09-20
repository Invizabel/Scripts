sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt clean
sudo docker pull ghcr.io/mealie-recipes/mealie:latest

sudo docker run -d --name=mealie --restart always -p 80:9000 ghcr.io/mealie-recipes/mealie:latest
