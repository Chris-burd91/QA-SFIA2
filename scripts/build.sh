#! /bin/bash
sudo apt-get update
sudo apt install -y python3
sudo apt install -y python3-pip
mkdir -p /home/$USER/.local/bin
echo 'PATH=$PATH:~/home/$USER/.local/bin' >> ~/.bashrc