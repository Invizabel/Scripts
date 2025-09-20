sudo apt update
sudo apt upgrade
sudo apt install unattended-upgrades
sudo dpkg-reconfigure unattended-upgrades
sudo apt autoremove
sudo apt autoclean
sudo docker pull jgraph/drawio
sudo docker run -d --name=drawio --restart always -p 80:8080 jgraph/drawio

