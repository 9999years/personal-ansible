#! /bin/bash
set -e

apt update
apt install -y python-pip
pip install ansible
sudo -u $(hostname) ansible-playbook -K site.yml
