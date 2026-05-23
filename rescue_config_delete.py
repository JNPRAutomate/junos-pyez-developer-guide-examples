"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Manage the Rescue Configuration on Junos Devices > How to Manage the Rescue Configuration > Delete the Rescue Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-configuration-rescue-managing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


with Device(host='dc1a.example.com') as dev:
    cu = Config(dev)
    cu.rescue(action='delete')
