[![Test](https://github.com/escalate/ansible-raspberry-systemd-timesyncd/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-systemd-timesyncd/actions/workflows/test.yml)

# Ansible Role: systemd-timesyncd

An Ansible role that manages [systemd-timesyncd](https://www.freedesktop.org/software/systemd/man/systemd-timesyncd.service.html) on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-systemd-timesyncd/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: [requirements.yml](https://github.com/escalate/ansible-raspberry-systemd-timesyncd/blob/master/requirements.yml)

## Installation

```
$ ansible-galaxy role install escalate.timesyncd
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.timesyncd
      tags: timesyncd
```

## License

MIT
