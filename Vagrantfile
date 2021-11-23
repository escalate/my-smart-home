# -*- mode: ruby -*-
# vi: set ft=ruby :

ansible_playbook = "site.yml"
ansible_group = "gitops"
ansible_host = "smart-home.fritz.box"

Vagrant.configure("2") do |config|
  config.vm.box = "debian/bullseye64"

  config.vm.define ansible_host do |test|
    test.vm.network "private_network", type: "dhcp"
    test.vm.provider "virtualbox" do |v|
      v.cpus = 1
      v.memory = 4096
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
      ansible.extra_vars = {
        sshd_allow_users: [],
        sshd_allow_groups: ["root", "vagrant"]
      }
    end

  end

end
