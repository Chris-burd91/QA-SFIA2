#! /bin/bash
export TEST_DB_URI=${TEST_DB_URI}
echo "Installing python and pip"
sudo apt-get update
sudo apt sinstall -y python3
sudo apt install -y python3-pip
echo "Installing Ansible"
export onPATH=$(echo $PATH | grep "/home/$USER/.local/bin")
if [ ! $onPATH ]; then
	if [ ! -d "/home/$USER/.local/bin" ]; then
		mkdir -p /home/$USER/.local/bin
	fi
	echo "Adding ~/.local/bin to path."
	echo "# Adds ansible install location to PATH" >> /home/$USER/.bashrc
	echo "PATH=$PATH:/home/$USER/.local/bin" >> /home/$USER/.bashrc
	source /home/$USER/.bashrc
figit 
pip3 install --user ansible
ansible --version

echo "Ansible Playbook Running.."
~/.local/bin/ansible-playbook -i inventory.config playbook.yaml



sudo chmod 666 /var/run/docker.sock

echo "Installing docker-compose"
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose



