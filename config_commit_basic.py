"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use the Junos PyEZ Config Utility to Configure Junos Devices > Commit the Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-data-loading.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


conf_file = 'configs/junos-config-interfaces.conf'


with Device(host='dc1a.example.com') as dev:
    with Config(dev, mode='exclusive') as cu:
        cu.load(path=conf_file, merge=True)
        cu.commit()
