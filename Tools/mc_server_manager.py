import os
import requests
import subprocess

users_os = "unix"
if os.name == "nt":
    users_os = "windows"

choice = input("1: Download new server\n2: Upgrade server\nChoose: ")
version = input("version:\n")
found_version = False
content = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json", headers={"User-Agent": "Mozilla/5.0 (Minecraft Server Manager)"}, timeout=10).json()
for i in content["versions"]:
    if i["id"] == version:
        found_version = True
        content = requests.get(i["url"], headers={"User-Agent": "Mozilla/5.0 (Minecraft Server Manager)"}, timeout=10).json()
        if users_os == "windows":
            print(f"Found version {version} {i['type']} @ {content['downloads']['windows_server']['url']}")
            content = requests.get(content['downloads']['windows_server']['url'], headers={"User-Agent": "Mozilla/5.0 (Minecraft Server Manager)"}, timeout=10).content
            with open(f"{version}.jar","wb") as file:
                file.write(content)
        else: 
            print(f"Found version {version} {i['type']} @ {content['downloads']['server']['url']}")
            print(f"Downloading: {version}")
            content = requests.get(content['downloads']['server']['url'], headers={"User-Agent": "Mozilla/5.0 (Minecraft Server Manager)"}, timeout=10).content
            with open(f"{version}.jar","wb") as file:
                file.write(content)
            if os.path.exists(f"{version}.jar") and os.path.getsize(f"{version}.jar") > 1024:
                print("Download successful")
                devnull = open(os.devnull,"w")
                retval = subprocess.call(["dpkg","-s","default-jre"],stdout=devnull,stderr=subprocess.STDOUT)
                devnull.close()
                if retval == 0:
                    print("Package default-jre is installed.")
                else:
                    print("Package default-jre not installed. Please install it.")
            else:
                print("Download failed")
            

if not found_version:
    print(f"Unknown version {version}")