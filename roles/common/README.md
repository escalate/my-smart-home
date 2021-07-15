[![Molecule](https://github.com/escalate/ansible-raspberry-common/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-common/actions/workflows/molecule.yml)
[![Ansible Quality Score](https://img.shields.io/ansible/quality/54162?label=Quality%20Score)](https://galaxy.ansible.com/escalate/common)

# Ansible Role: Raspberry - Common

An Ansible role that manages basic operating system configuration on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.common
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-common/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: [collections.yml](https://github.com/escalate/ansible-raspberry-common/blob/master/collections.yml)

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.common
      tags: common
```

## License

MIT
