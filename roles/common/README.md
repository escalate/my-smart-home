[![Test](https://github.com/escalate/ansible-raspberry-common/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-common/actions/workflows/test.yml)

# Ansible Role: Raspberry - Common

An Ansible role that manages basic operating system configuration on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-common/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: [requirements.yml](https://github.com/escalate/ansible-raspberry-common/blob/master/requirements.yml)

## Installation

```
$ ansible-galaxy role install escalate.common
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.common
      tags: common
```

## License

MIT
