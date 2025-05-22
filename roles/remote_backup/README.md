[![Molecule](https://github.com/escalate/ansible-raspberry-remote-backup/actions/workflows/molecule.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-remote-backup/actions/workflows/molecule.yml)

# Ansible Role: Raspberry - Remote Backup

An Ansible role that manages remote backup job configuration on Raspberry Pi OS (Debian Bookworm).

The remote backup job expects a mountpoint for backing up the local files via rsync.

Use for e.g. an [smb mount](https://github.com/escalate/ansible-raspberry-smb-mount) to backup your files to a NAS.

## Install

```
$ ansible-galaxy install escalate.remote_backup
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-remote-backup/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: [requirements.yml](https://github.com/escalate/ansible-raspberry-remote-backup/blob/master/requirements.yml)
* Collections: None

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.remote_backup
      tags: remotebackup
```

## License

MIT
