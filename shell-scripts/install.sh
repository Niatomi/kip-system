#!/bin/bash

sudo apt-get -y install python3

sudo apt-get -y install python3-dev

sudo apt-get -y install python-is-python3

cd ..
base_path="$PWD"
export base_path=$base_path

docker-compose build

source /etc/environment

cd $base_path/shell-scripts/js-install
sudo apt -y remove nodejs npm
sudo autoremove
sudo bash nodesource_setup.sh
sudo apt-get install -y nodejs
sudo apt-get install aptitude
sudo aptitude install npm

cd $base_path/shell-scripts/daemon-scripts
sudo chmod +x install-daemon.sh
./install-daemon.sh

cd $base_path/shell-scripts/python-dependencies
sudo chmod +x install-python-deps.sh
./install-python-deps.sh

cd $base_path/shell-scripts/system-resources
sudo chmod +x install-swap.sh
./install-swap.sh
