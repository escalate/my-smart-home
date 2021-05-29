[![Lint](https://github.com/escalate/my-smart-home/actions/workflows/lint.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/my-smart-home/actions/workflows/lint.yml)

# My Smart Home
My Smart Home on Raspberry Pi

## Preparation

### Build Raspberry Pi OS Lite custom image
```
$ git clone git@github.com:escalate/raspberry-pi-os-custom-image.git
cd raspberry-pi-os-custom-image
make build
```

### Flash Raspberry Pi OS Lite custom image on SD Card
* Open balenaEtcher tool
* Click "Flash from file" button
* Select YYYY-MM-DD-raspios-buster-armhf-lite.img
* Click "Flash!" button
* Close balenaEtcher tool

## Next steps after successful boot of Raspberry Pi

### SSH login credential for Raspberry Pi
* Username: pi
* Password: raspberry

### Copy Raspberry Pi OS Lite custom image on Raspberry Pi
```
$ scp YYYY-MM-DD-raspios-buster-armhf-lite.img pi@IPADDRESS:/var/tmp
```

### Format attached USB storage device
```
$ make format-usb-disk
```

### Copy root filesystem of Raspberry Pi OS Lite to attached USB storage device
```
$ mkdir /mnt/usbdisk
$ mount /dev/sda1 /mnt/usbdisk
$ mkdir /mnt/raspios
$ losetup --show --find --read-only --partscan /tmp/YYYY-MM-DD-raspios-buster-armhf-lite.img
$ mount /dev/loop0p2 /mnt/raspios
$ rsync -ax --progress /mnt/raspios/ /mnt/usbdisk
$ umount /mnt/raspios
$ losetup --detach-all
```

### Switch root partition
```
$ cp /etc/fstab /mnt/usbdisk/etc/fstab
$ blkid
$ vi /mnt/usbdisk/etc/fstab
proc                  /proc           proc    defaults          0       0
PARTUUID=418a81cb-01  /boot           vfat    defaults          0       2
PARTUUID=8538718e-01  /               ext4    defaults,noatime  0       1
$ vi /boot/cmdline.txt
console=serial0,115200 console=tty1 root=PARTUUID=8538718e-01 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
$ touch /boot/ssh
$ sync
$ reboot
```

### Update Raspberry Pi OS Lite
```
$ apt update
$ apt full-upgrade
$ reboot
```

### Update Raspberry Pi firmware
```
$ rpi-update
$ reboot
```

### Run Ansible bootstrap playbook
```
$ ANSIBLE_PLAYBOOK=bootstrap.yml make deploy
```

### Run Ansible smart-home playbook
```
$ make deploy
```

## More information
* https://www.raspberrypi.org/documentation/installation/installing-images/linux.md
* https://www.raspberrypi.org/documentation/raspbian/updating.md
* https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/README.md
* http://elinux.org/RPi_Resize_Flash_Partitions
* https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=44177

## License
MIT
