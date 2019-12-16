#! /bin/bash
set -o errexit
hostname="$(hostname)"

function log {
    echo "[bootstrap.sh]: " "$@"
}

if [[ "$(id -u)" -eq 0 ]]
then
    log "First-time installation running as root."
    apt update
    apt install -y python-pip
    sudo -H pip install ansible
    sudo -u "$hostname" ansible-playbook -K site.yml -l "$hostname" "$@" -e '{"initial_setup": true}'
else
    if ! command -v ansible-playbook > /dev/null
    then
        log "ansible-playbook not found; did you mean to run as root and install prereqs?"
        exit 1
    fi
    log "Starting ansible."
    ansible-playbook site.yml -l "$hostname" "$@"
fi
