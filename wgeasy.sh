sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt autoclean
sudo docker pull ghcr.io/wg-easy/wg-easy:latest
sudo docker run -d --name=wgeasy --restart always -p 51820:51820/udp -p 80:51821/tcp ghcr.io/wg-easy/wg-easy:latest