# Personal Ansible bootstrap configuration

To use:

    umask 022 && mkdir projects && cd projects \
    && git clone https://github.com/9999years/personal-ansible.git \
    && cd personal-ansible \
    && sudo -H ./bootstrap.sh

Some tasks are gated behind the variable `initial_setup` being true; to enable
it, run `./bootstrap.sh -e '{"initial_setup": true}'`.
