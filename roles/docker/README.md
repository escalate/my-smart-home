[![Test](https://github.com/escalate/ansible-raspberry-docker/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-docker/actions/workflows/test.yml)

# Ansible Role: Raspberry - Docker

An Ansible role that manages [Docker CE](https://www.docker.com) on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: [requirements.yml](https://github.com/escalate/ansible-raspberry-docker/blob/master/requirements.yml)
* Collections: [requirements.yml](https://github.com/escalate/ansible-raspberry-docker/blob/master/requirements.yml)

## Installation

```
$ ansible-galaxy role install escalate.docker
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.docker
      tags: docker
```

## License

MIT
