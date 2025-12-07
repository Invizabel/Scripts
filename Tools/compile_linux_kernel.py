import os

os.system("clear")

if os.path.exists("KERNEL"):
    os.system("rm -rf KERNEL")
os.mkdir("KERNEL")

kernel_version = "linux-6.18"

os.chdir("KERNEL")

os.system("sudo apt update")
os.system("sudo apt install git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison")
# needed on ubuntu and maybe others? https://groups.google.com/g/syzkaller-bugs/c/lBS-kjONLSw/m/j6jOom9SEAAJ?pli=1
os.system("sudo apt install libdw-dev")
os.system("sudo apt install gawk")
os.system(f"wget https://cdn.kernel.org/pub/linux/kernel/v6.x/{kernel_version}.tar.xz")
os.system(f"tar -xvf {kernel_version}.tar.xz")
os.chdir(kernel_version)
os.system("make clean")
os.system("make olddefconfig")
os.system("./scripts/config --disable SYSTEM_TRUSTED_KEYS")
os.system("./scripts/config --disable SYSTEM_REVOCATION_KEYS")
os.system("make -j$(nproc) 2>&1 | tee log")
if os.path.exists("arch/x86/boot/bzImage") and os.path.getsize("arch/x86/boot/bzImage") > 0:
    print("compiled succesfully")
