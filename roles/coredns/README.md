[![Molecule](https://github.com/escalate/ansible-raspberry-coredns-docker/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-coredns-docker/actions/workflows/molecule.yml)

# Ansible Role: Raspberry - CoreDNS (Docker)

An Ansible role that manages [CoreDNS](https://coredns.io/) Docker container with systemd on Raspberry Pi OS (Debian Bullseye).

## Install

```
$ ansible-galaxy install escalate.coredns
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-coredns-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: [requirements.yml](https://github.com/escalate/ansible-raspberry-coredns-docker/blob/master/requirements.yml)
* Collections: [collections.yml](https://github.com/escalate/ansible-raspberry-coredns-docker/blob/master/collections.yml)

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.coredns
      tags: coredns
```

## License

MIT
