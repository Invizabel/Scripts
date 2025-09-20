sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt clean
sudo docker pull jgraph/drawio
sudo docker run -d --name=drawio --restart always -p 80:8080 jgraph/drawio