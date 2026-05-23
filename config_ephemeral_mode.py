"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Configure Junos Devices > How to Specify the Configuration Mode
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/concept/junos-pyez-configuration-process-and-data-formats.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


with Device(host='router1.example.com') as dev:
    with Config(dev, mode='ephemeral') as cu:
        cu.load('set protocols mpls label-switched-path to-hastings to 192.0.2.1', format='set')
        cu.commit()
