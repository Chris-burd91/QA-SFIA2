#! /bin/bash
echo "Installing python and pip"
sudo apt-get update
sudo apt sinstall -y python3
sudo apt install -y python3-pip
echo "Installing Ansible"
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
pip3 install --user ansible
ansible --version

echo "Ansible Playbook Running.."
~/.local/bin/ansible-playbook -v -i inventory.config playbook.yaml



sudo chmod 666 /var/run/docker.sock

echo "Installing docker-compose"
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose



