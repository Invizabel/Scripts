
import os

os.system("sudo docker run -d --name=cyberchef --restart always docker run -it -p 8080:80 ghcr.io/gchq/cyberchef:latest")
