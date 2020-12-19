#!/bin/bash

sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable

sudo apt install fail2ban -y

sudo apt install nethogs -y
sudo apt install net-tools -y

sudo apt install foremost -y
sudo apt install testdisk -y

sudo apt install gufw -y
sudo apt install clamav clamtk -y

curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -

echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list

sudo apt install apt-transport-https curl -y
sudo apt install audacity -y
sudo apt install bleachbit -y
sudo apt install brave-browser -y
sudo apt install chromium -y
sudo apt install exfat-fuse exfat-utils -y
sudo apt install gimp -y
sudo apt install gnome-control-center -y
sudo apt install kdenlive -y
sudo apt install libreoffice -y
sudo apt install numix-gtk-theme numix-icon-theme-circle -y
sudo apt install timeshift -y
sudo apt install vlc -y

sudo apt autoclean -y
sudo apt autoremove -y
sudo apt dist-upgrade -y
sudo apt update -y
sudo apt upgrade -y
