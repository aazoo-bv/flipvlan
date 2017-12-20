#!/usr/bin/env python

# flipvlan.py
# Flip all VLANs on a switch to a second VLAN
#
# Usage: ./flipvlan <CSV file of switches> <original VLAN> <new VLAN>
#
# You will need netmiko and ciscoconfparse python libraries

from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
import sys
import csv

# Check for the correct number of arguments
if ((len(sys.argv) < 4 or  len(sys.argv) > 4)):
    print """\
This script will flip all VLANs from an original to a target VLAN

Usage:  ./flipvlan.py <CSV file of switches> <original VLAN> <new VLAN>
"""
    sys.exit(1)

# Get the variables
config_file = sys.argv[1]
original_vlan = sys.argv[2]
target_vlan = sys.argv[3]

# Read CSV config file
configuration_file = open(config_file, "rb")
config_reader = csv.reader(configuration_file)

for config_row in config_reader:
  device_ip = config_row[0]
  device_user = config_row[1]
  device_password = config_row[2]
  
  # Connect to device
  net_connect = ConnectHandler(device_type='cisco_ios', ip=device_ip, username=device_user, password=device_password)
  
  # Go into enable mode
  net_connect.enable()
  
  # Fetch current configuration
  run_config = net_connect.send_command("show run all")
  run_config = run_config.splitlines()
  
  # Parse configuration
  cisco_cfg = CiscoConfParse(run_config)
  config_obj = cisco_cfg.find_objects_w_all_children(parentspec=r"^interface",childspec=[r"switchport access vlan "+original_vlan])
  
  # Loop the config and 
  for parent in config_obj:
      print("Changing "+parent.text)
      config_commands = [parent.text,'switchport access vlan '+target_vlan] 
      net_connect.send_config_set(config_commands)

  # Save config
  net_connect.send_command("write mem")

# Close CSV file
configuration_file.close()
 
# Exit cleanly
sys.exit(0)