#! /bin/bash
set -o errexit

if [[ "$(id -u)" -eq 0 ]]
then
    echo "First-time installation running as root."
    set -o verbose
    apt update
    apt install -y python-pip
    sudo -H pip install ansible
    sudo -u $(hostname) ansible-playbook -K site.yml -l "$(hostname)" $@
    set +o verbose
else
    if ! command -v ansible-playbook > /dev/null
    then
        echo "ansible-playbook not found; did you mean to run as root and install prereqs?"
        exit 1
    fi
    set -o verbose
    ansible-playbook site.yml -l "$(hostname)" $@
    set +o verbose
fi
