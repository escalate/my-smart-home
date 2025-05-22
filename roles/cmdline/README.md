[![Test](https://github.com/escalate/ansible-raspberry-cmdline/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-cmdline/actions/workflows/test.yml)

# Ansible Role: Raspberry - Cmdline

An Ansible role that manages the [Linux kernel command line](https://www.raspberrypi.com/documentation/computers/configuration.html#the-kernel-command-line) on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-cmdline/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: None

## Installation

```
$ ansible-galaxy role install escalate.cmdline
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.cmdline
      tags: cmdline
```

## License

MIT
