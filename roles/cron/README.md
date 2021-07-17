[![Molecule](https://github.com/escalate/ansible-raspberry-cron/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-cron/actions/workflows/molecule.yml)

# Ansible Role: Raspberry - Cron

An Ansible role that manages [cron](https://wiki.debian.org/cron) on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.cron
```

## Role Variables

This roles has no variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: None

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.cron
      tags: cron
```

## License

MIT
