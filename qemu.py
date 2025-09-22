import os

os.system("sudo apt install qemu-kvm qemu-system qemu-utils python3 python3-pip libvirt-clients libvirt-daemon-system bridge-utils virtinst libvirt-daemon virt-manager -y")
os.system("sudo virsh net-start default")
os.system("sudo virsh net-autostart default")
os.system("sudo usermod -aG libvirt $USER")
os.system("sudo usermod -aG libvirt-qemu $USER")
os.system("sudo usermod -aG kvm $USER")
os.system("sudo usermod -aG input $USER")
os.system("sudo usermod -aG disk $USER")
