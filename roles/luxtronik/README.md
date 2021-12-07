[![Molecule](https://github.com/escalate/ansible-raspberry-luxtronik/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-luxtronik/actions/workflows/molecule.yml)

# Ansible Role: Raspberry - Luxtronik

An Ansible role that manages Luxtronik statistics backup on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.luxtronik
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-luxtronik/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: [requirements.yml](https://github.com/escalate/ansible-raspberry-luxtronik/blob/master/requirements.yml)
* Collections: None

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.luxtronik
      tags: luxtronik
```

## License

MIT
