[![Test](https://github.com/escalate/ansible-raspberry-swap/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-swap/actions/workflows/test.yml)

# Ansible Role: Raspberry - Swap

An Ansible role that manages [swap](https://wiki.debian.org/Swap) with [dphys-swapfile](http://neil.franklin.ch/Projects/dphys-swapfile/) on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-swap/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: [requirements.yml](https://github.com/escalate/ansible-raspberry-swap/blob/master/requirements.yml)

## Installation

```
$ ansible-galaxy role install escalate.swap
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.swap
      tags: swap
```

## License

MIT
