sudo apt update
sudo apt upgrade
sudo apt install curl
sudo apt autoremove
sudo apt autoclean
curl -fsSL https://ollama.com/install.sh | sh
sudo docker run -d --network=host -v open-webui://app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main