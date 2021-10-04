[![Molecule](https://github.com/escalate/ansible-raspberry-smb-mount/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-smb-mount/actions/workflows/molecule.yml)

# Ansible Role: Raspberry - SMB Mount

An Ansible role that manages SMB (Server Message Block) mounts on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.smb_mount
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-smb-mount/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: [collections.yml](https://github.com/escalate/ansible-raspberry-smb-mount/blob/master/collections.yml)

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.smb_mount
      tags: smbmount
```

## License

MIT
