"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Connect to Junos Devices Using Junos PyEZ > Connect to a Device Using Telnet
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-connection-methods.html
"""

import sys
from getpass import getpass
from jnpr.junos import Device

hostname = input("Device hostname: ")
junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS password: ")

dev = Device(host=hostname, user=junos_username, passwd=junos_password, mode='telnet', port='23')

try:
    dev.open()
except Exception as err:
    print (err)
    sys.exit(1)

print (dev.facts)
dev.close()
