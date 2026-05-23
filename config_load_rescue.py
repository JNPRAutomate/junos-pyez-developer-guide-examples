"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use the Junos PyEZ Config Utility to Configure Junos Devices > Load the Rescue Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-data-loading.html
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
