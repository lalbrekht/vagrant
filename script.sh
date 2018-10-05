#!/bin/bash

cat << EOF >> /etc/sysctl.conf

#### Added by Vagrant ####

net.core.somaxconn = 65535
vm.swappiness = 10

EOF

sysctl -p