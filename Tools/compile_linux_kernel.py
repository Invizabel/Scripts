import os

if os.path.exists("KERNEL"):
    os.system("rm -rf KERNEL")
os.mkdir("KERNEL")

fetch_files = "linux-6.18.tar.xz"

os.chdir("KERNEL")

os.system("sudo apt update")
os.system("sudo apt install bc binutils bison dwarves flex gcc git gnupg2 gzip libelf-dev libncurses5-dev libssl-dev make openssl pahole perl-base rsync tar xz-utils")
os.system(f"wget https://cdn.kernel.org/pub/linux/kernel/v6.x/{fetch_files}")
os.system(f"tar -xvf {fetch_files}")
os.system("cd linux-*/")
os.system("make olddefconfig")
os.system("./scripts/config --file .config --disable MODULE_SIG")
os.system("make -j$(nproc) 2>&1 | tee log")
