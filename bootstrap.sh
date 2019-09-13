#! /bin/bash
set -e

if [[ "$(id -u)" -eq 0 ]]
then
    echo "First-time installation running as root."
    set -v
    apt update
    apt install -y python-pip
    pip install ansible
    sudo -u $(hostname) ansible-playbook -K site.yml -l "$(hostname)" $@
    set +v
else
    if ! command -v ansible-playbook > /dev/null
    then
        echo "ansible-playbook not found; did you mean to run as root and install prereqs?"
        exit 1
    fi
    set -v
    ansible-playbook site.yml -l "$(hostname)" $@
    set +v
fi
