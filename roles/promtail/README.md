[![Molecule](https://github.com/escalate/ansible-raspberry-promtail-docker/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-promtail-docker/actions/workflows/molecule.yml)

# Ansible Role: Raspberry - Promtail (Docker)

An Ansible role that manages [Promtail](https://grafana.com/docs/loki/latest/clients/promtail/) Docker container with systemd on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.promtail
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-promtail-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: [requirements.yml](https://github.com/escalate/ansible-raspberry-promtail-docker/blob/master/requirements.yml)
* Collections: [collections.yml](https://github.com/escalate/ansible-raspberry-promtail-docker/blob/master/collections.yml)

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.promtail
      tags: promtail
```

## License

MIT
