[![Molecule](https://github.com/escalate/ansible-raspberry-dhcpcd/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-dhcpcd/actions/workflows/molecule.yml)

# Ansible Role: Raspberry - dhcpcd

An Ansible role that manages [dhcpcd](https://roy.marples.name/projects/dhcpcd/) on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.dhcpcd
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-dhcpcd/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: None

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.dhcpcd
      tags: dhcpcd
```

## License

MIT
