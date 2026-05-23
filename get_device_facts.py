"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Retrieve Facts from Junos Devices > Example: Retrieve Facts from a Junos Device
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-device-connecting.html
"""

import sys
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from pprint import pprint

dev = Device(host='router1.example.net')
try:
    dev.open()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)

pprint (dev.facts['hostname'])
pprint (dev.facts)

dev.close()
