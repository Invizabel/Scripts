import os

os.system("sudo apt update")
os.system("sudo apt upgrade")
os.system("sudo apt install curl")
os.system("sudo apt install unattended-upgrades")
os.system("sudo dpkg-reconfigure unattended-upgrades")
os.system("sudo apt autoremove")
os.system("sudo apt autoclean")
os.system("curl -fsSL https://ollama.com/install.sh | sh")
os.system("sudo docker run -d --network=host -v open-webui://app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main")
