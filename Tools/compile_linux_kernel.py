import os

if os.path.exists("KERNEL"):
    os.system("rm -rf KERNEL")
os.mkdir("KERNEL")

kernel_version = "linux-6.18"

os.chdir("KERNEL")

os.system("sudo apt update")
os.system("sudo apt-get install git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison")
os.system(f"wget https://cdn.kernel.org/pub/linux/kernel/v6.x/{kernel_version}.tar.xz")
os.system(f"tar -xvf {kernel_version}.tar.xz")
os.chdir(kernel_version)
os.system("make olddefconfig")
os.system("./scripts/config --disable SYSTEM_TRUSTED_KEYS")
os.system("./scripts/config --disable SYSTEM_REVOCATION_KEYS")
os.system("make -j$(nproc) 2>&1 | tee log")
