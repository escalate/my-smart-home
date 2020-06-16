# -*- mode: ruby -*-
# vi: set ft=ruby :

ansible_playbook = "smart_home.yml"
ansible_group = "smart_home"
ansible_host = "smart-home.fritz.box"

Vagrant.configure("2") do |config|
  config.vm.box = "debian/buster64"

  config.vm.define ansible_host do |test|
    test.vm.network "private_network", type: "dhcp"
    data_disk = ".vagrant/disks/" + ansible_host + "_" + ansible_group + "_sdb.vdi"
    test.vm.provider "virtualbox" do |v|
      v.cpus = 1
      v.memory = 4096
      if !File.exist?(data_disk)
        v.customize ["createmedium", "disk", "--filename", data_disk, "--format", "VDI", "--size", 10240]
      end
      v.customize ["storageattach", :id, "--storagectl", "SATA Controller", "--port", 1, "--device", 0, "--type", "hdd", "--medium", data_disk]
    end

    test.vm.provision "ansible" do |ansible|
      ansible.playbook = ansible_playbook
      ansible.groups = {
        ansible_group => [ansible_host],
      }
      ansible.become = true
      ansible.limit = ansible_host
      ansible.compatibility_mode = "2.0"
      if ENV["ANSIBLE_ARGS"]
        ansible.raw_arguments = Shellwords.shellsplit(ENV["ANSIBLE_ARGS"])
      end
    end

  end

end
