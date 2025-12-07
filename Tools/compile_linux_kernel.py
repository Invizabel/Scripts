import os

if os.path.exists("KERNEL"):
    os.system("rm -rf KERNEL")
os.mkdir("KERNEL")

kernel_version = "linux-6.18"

os.chdir("KERNEL")

os.system("sudo apt update")
os.system("sudo apt install bc binutils bison dwarves flex gcc git gnupg2 gzip libelf-dev libncurses5-dev libssl-dev make openssl pahole perl-base rsync tar xz-utils")
os.system("sudo apt install libdwarf-dev libelf-dev dwarves")
os.system(f"wget https://cdn.kernel.org/pub/linux/kernel/v6.x/{kernel_version}.tar.xz")
os.system(f"tar -xvf {kernel_version}.tar.xz")
os.chdir(kernel_version)
os.system("make olddefconfig")
os.system("./scripts/config --file .config --disable MODULE_SIG")
os.system("make -j$(nproc) 2>&1 | tee log")
