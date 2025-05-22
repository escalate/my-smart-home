[![Test](https://github.com/escalate/ansible-raspberry-traefik-docker/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-traefik-docker/actions/workflows/test.yml)

# Ansible Role: Raspberry - Traefik Proxy (Docker)

An Ansible role that manages [Traefik Proxy](https://traefik.io/traefik/) Docker container with systemd on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-traefik-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: [requirements.yml](https://github.com/escalate/ansible-raspberry-traefik-docker/blob/master/requirements.yml)
* Collections: [requirements.yml](https://github.com/escalate/ansible-raspberry-traefik-docker/blob/master/requirements.yml)

## Installation

```
$ ansible-galaxy role install escalate.traefik
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.traefik
      tags: traefik
```

## License

MIT
