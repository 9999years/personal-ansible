#! /bin/bash
set -e

apt update
apt install -y python-pip
pip install ansible
ansible-playbook -K site.yml
