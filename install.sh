#! /bin/bash
sudo apt update && sudo apt install -y python3 python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
curl https://get.docker.com | sudo bash
sudo usermod -aG docker $(whoami)
newgrp docker
