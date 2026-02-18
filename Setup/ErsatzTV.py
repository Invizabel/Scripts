import os

os.system("mkdir ~/config")
user = input("user:\n")
os.system(f"sudo docker run -d --name ersatztv --gpus all -e TZ=America/Chicago -p 80:8409 -v /home/{user}/Videos/Movies:/media/movies:ro -v /home/{user}/Videos/TV:/media/tv:ro -v /home/{user}/Music:/media/music:ro -v /home/{user}/config:/config --restart always ghcr.io/ersatztv/ersatztv")
