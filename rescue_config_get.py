"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Manage the Rescue Configuration on Junos Devices > How to Manage the Rescue Configuration > Retrieve the Rescue Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-configuration-rescue-managing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree

with Device(host='dc1a.example.com') as dev:
    cu = Config(dev)
    rescue = cu.rescue(action='get', format='xml')
    if rescue is None:
        print ('No existing rescue configuration.')
    else:
        print (etree.tostring(rescue, encoding='unicode'))
