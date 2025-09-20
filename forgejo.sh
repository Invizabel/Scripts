sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt autoclean
sudo docker run -d --name=forgejo --restart always -p 80:3000 codeberg.org/forgejo/forgejo:11.0.6