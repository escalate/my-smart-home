[![Molecule](https://github.com/escalate/ansible-raspberry-cmdline/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-cmdline/actions/workflows/molecule.yml)

# Ansible Role: Raspberry - Cmdline

An Ansible role that manages the [Linux kernel command line](https://www.raspberrypi.com/documentation/computers/configuration.html#the-kernel-command-line) on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.cmdline
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-cmdline/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: None

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.cmdline
      tags: cmdline
```

## License

MIT
