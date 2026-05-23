"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Manage the Rescue Configuration on Junos Devices > How to Manage the Rescue Configuration > Load and Commit the Rescue Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-configuration-rescue-managing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


with Device(host='dc1a.example.com') as dev:


    with Config(dev, mode='exclusive') as cu:
        rescue = cu.rescue(action='reload')
        if rescue is False:
            print ('No existing rescue configuration.')
        else:
            cu.pdiff()
            cu.commit()
