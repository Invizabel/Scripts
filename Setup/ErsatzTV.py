import os

os.system("sudo rm -rf ~/config")
os.system("mkdir ~/config")
user = input("user:\n")
os.system("sudo apt remove docker-desktop")
os.system("sudo apt purge docker-desktop")
os.system("sudo rm -rf ~/.docker")
os.system(f"""sudo docker run --runtime=nvidia --gpus all -d --name ersatztv -e TZ=America/Chicago -p 80:8409 -v /home/{user}/Videos/Movies:/media/movies:ro -v /home/{user}/Videos/TV:/media/tv:ro -v /home/{user}/Music:/media/music:ro -v /home/{user}/config:/config --restart always ghcr.io/ersatztv/ersatztv""")
