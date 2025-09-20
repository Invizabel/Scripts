sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt autoclean
sudo docker pull ghcr.io/wg-easy/wg-easy:latest
sudo docker run -d \
  --name=wgeasy \
  -e WG_HOST=#YOUR_EXTERNAL_IP_OR_DOMAIN# \
  -e PASSWORD=#YOUR_PASSWORD# \
  -v ~/.wg-easy:/etc/wireguard \
  -p 51820:51820/udp \
  -p 51821:51821/tcp \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_MODULE \
  --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
  --sysctl="net.ipv4.ip_forward=1" \
  --restart always \
  ghcr.io/wg-easy/wg-easy:latest