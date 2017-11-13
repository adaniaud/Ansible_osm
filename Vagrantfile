# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANT_VM_PROVIDER = "virtualbox"
ANSIBLE_RAW_SSH_ARGS = "-o IdentityFile=.vagrant/machines/default/#{VAGRANT_VM_PROVIDER}/private_key"


Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/xenial64"
    config.vm.hostname = "osm"
    config.vm.network "private_network", ip: "192.168.77.100"
    config.vm.provision :ansible do |ansible|
      ansible.playbook = "ansible_osm/playbook.yml"
      ansible.limit = 'all'
      ansible.inventory_path = "ansible_osm/inventory"
      ansible.verbose = "-vvv"
      ansible.raw_ssh_args = ANSIBLE_RAW_SSH_ARGS
    end
end
