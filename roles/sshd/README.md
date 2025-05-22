[![Test](https://github.com/escalate/ansible-raspberry-sshd/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-sshd/actions/workflows/test.yml)

# Ansible Role: Raspberry - sshd

An Ansible role that manages [OpenSSH - sshd](https://www.openssh.com) on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-sshd/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: None

## Installation

```
$ ansible-galaxy role install escalate.sshd
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.sshd
      tags: sshd
```

## License

MIT
