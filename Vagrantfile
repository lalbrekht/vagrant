# -*- mode: ruby -*-
# vim: set ft=ruby :
home = ENV['HOME']

MACHINES = {
  :otuslinux => {
        :box_name => "centos/7",
#        :box_version => "1.0",
        :ip_addr => '192.168.11.101',
        :disks => {
            :sata1 => {
            :dfile => home + '/VirtualBox\ VMs/sata1.vdi',
            :size => 1024,
            :port => 2
            },
            :sata2 => {
            :dfile => home + '/VirtualBox\ VMs/sata2.vdi',
            :size => 1024, # Megabytes
            :port => 3
        }
    }
  },
}

Vagrant.configure("2") do |config|

  MACHINES.each do |boxname, boxconfig|

      config.vm.define boxname do |box|

          box.vm.box = boxconfig[:box_name]
 #         box.vm.box_version = boxconfig[:box_version]
          box.vm.host_name = boxname.to_s

          box.vm.network "private_network", ip: boxconfig[:ip_addr]

          box.vm.provider :virtualbox do |vb|
                  vb.customize ["modifyvm", :id, "--memory", "256"]
          vb.customize ["storagectl", :id, "--name", "SATA", "--add", "sata" ]

          boxconfig[:disks].each do |dname, dconf|
              unless File.exist?(dconf[:dfile])
                vb.customize ['createhd', '--filename', dconf[:dfile], '--variant', 'Fixed', '--size', dconf[:size]]
              end
              vb.customize ['storageattach', :id,  '--storagectl', 'SATA', '--port', dconf[:port], '--device', 0, '--type', 'hdd', '--medium', dconf[:dfile]]
          end
          end

      #box.vm.synced_folder "files/", "/usr/share/nginx/html/"

      box.vm.provision "shell", inline: <<-SHELL
          mkdir -p ~root/.ssh
          cp ~vagrant/.ssh/auth* ~root/.ssh
          sh /vagrant/script.sh
      SHELL

      config.vm.provision "ansible" do |ansible|
        ansible.playbook = "site.yml"
        ansible.verbose = "vv"
      end
    
    #   config.vm.provision :puppet do |puppet|
    #     puppet.manifests_path = "puppet/manifests"
    #     puppet.module_path = "puppet/modules"
    #     puppet.manifest_file  = "init.pp"
    #     puppet.options="--verbose --debug"
    #   end

    end
  end
end