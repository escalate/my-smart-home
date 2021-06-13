[![Lint](https://github.com/escalate/my-smart-home/actions/workflows/lint.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/my-smart-home/actions/workflows/lint.yml)

# My Smart Home
My Smart Home on Raspberry Pi

## Preparation

### Build Raspberry Pi OS Lite custom image
```
$ git clone git@github.com:escalate/raspberry-pi-os-custom-image.git
cd raspberry-pi-os-custom-image

make build32

or

make build64
```

### Flash Raspberry Pi OS Lite custom image on SD Card
* Open balenaEtcher tool
* Click "Flash from file" button
* Select YYYY-MM-DD-raspios-buster-\[armhf|arm64\]-lite.img
* Click "Flash!" button
* Close balenaEtcher tool

### Bootstrap system after successful boot of Raspberry Pi
* Copy Raspberry Pi OS Lite custom image on Raspberry Pi
* Format attached USB storage device
* Copy root filesystem of Raspberry Pi OS Lite to attached USB storage device
* Switch root partition

```
$ make bootstrap
```

Hint: During the reboot task, delete old known_hosts entry and connect to machine to accept new host key

## Update Raspberry Pi OS Lite
```
$ make update
```

## Deploy Ansible smart-home playbook
```
$ make deploy
```

## License
MIT
