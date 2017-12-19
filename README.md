# flipvlan

# About
flipvlan.py\n

Flip all VLANs on a switch to a second VLAN\n
19-12-2017 G. de Boer - aaZoo\n
Contactdetails: gert-jan@aazoo.nl\n

Usage: ./flipvlan <IP of switch> <original VLAN> <new VLAN>\n

You will need netmiko and ciscoconfparse python libraries\n

# Installation instructions

## Ubuntu:
\# sudo apt install python-netmiko

\# git clone https://github.com/mpenning/ciscoconfparse.git

\# cd ciscoconfparse

\# sudo python setup.py install

