#! /bin/bash
set -e

apt update
apt install -y python3-pip
pip3 install ansible
ansible-playbook site.yml
