# flipvlan

# About
=====
flipvlan.py

Flip all VLANs on a switch to a second VLAN
19-12-2017 G. de Boer - aaZoo 
Contactdetails: gert-jan@aazoo.nl

Usage: ./flipvlan <IP of switch> <original VLAN> <new VLAN>

You will need netmiko and ciscoconfparse python libraries

# Installation instructions
=========================

## Ubuntu:
-------
\# sudo apt install python-netmiko

\# git clone https://github.com/mpenning/ciscoconfparse.git

\# cd ciscoconfparse

\# sudo python setup.py install

