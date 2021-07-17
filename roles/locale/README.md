[![Molecule](https://github.com/escalate/ansible-raspberry-locale/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-locale/actions/workflows/molecule.yml)

# Ansible Role: Raspberry - Locale

An Ansible role that manages [locale](https://wiki.debian.org/Locale) on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.locale
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-locale/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: [collections.yml](https://github.com/escalate/ansible-raspberry-locale/blob/master/collections.yml)

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.locale
      tags: locale
```

## License

MIT
