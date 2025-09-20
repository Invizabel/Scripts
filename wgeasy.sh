sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt autoclean
sudo docker pull ghcr.io/wg-easy/wg-easy:latest
sudo docker run -d --name=wgeasy --restart always -p 51820:51820 ghcr.io/wg-easy/wg-easy:latest