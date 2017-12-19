# flipvlan #

## About ##
flipvlan.py

Flip all VLANs on a switch to a second VLAN  

Usage: ./flipvlan <CSV of switches> <original VLAN> <new VLAN>  

You will need netmiko and ciscoconfparse python libraries

Format of CSV file:

<switch ip>,<switch user>,<switch password>  

## Installation instructions ##

### Ubuntu ###
\# sudo apt install python-netmiko python-csvkit 
\# git clone https://github.com/mpenning/ciscoconfparse.git  
\# cd ciscoconfparse  
\# sudo python setup.py install  

