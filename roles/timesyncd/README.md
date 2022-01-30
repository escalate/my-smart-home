[![Molecule](https://github.com/escalate/ansible-raspberry-systemd-timesyncd/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-systemd-timesyncd/actions/workflows/molecule.yml)

# Ansible Role: systemd-timesyncd

An Ansible role that manages [systemd-timesyncd](https://www.freedesktop.org/software/systemd/man/systemd-timesyncd.service.html) on Raspberry Pi OS (Debian Bullseye).

## Install

```
$ ansible-galaxy install escalate.timesyncd
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-systemd-timesyncd/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: [collections.yml](https://github.com/escalate/ansible-raspberry-systemd-timesyncd/blob/master/collections.yml)

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.timesyncd
      tags: timesyncd
```

## License

MIT
