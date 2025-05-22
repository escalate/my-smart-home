[![Test](https://github.com/escalate/ansible-raspberry-dhcpcd/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-dhcpcd/actions/workflows/test.yml)

# Ansible Role: Raspberry - dhcpcd

An Ansible role that manages [dhcpcd](https://roy.marples.name/projects/dhcpcd/) on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-dhcpcd/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: None

## Installation

```
$ ansible-galaxy role install escalate.dhcpcd
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.dhcpcd
      tags: dhcpcd
```

## License

MIT
