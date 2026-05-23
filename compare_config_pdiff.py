"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Compare the Candidate Configuration and a Previously Committed Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-comparing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


with Device(host='router1.example.com') as dev:
    with Config(dev, mode='exclusive') as cu:
        cu.load(path='configs/junos-config-mx.conf', merge=True)
        cu.pdiff()
        cu.commit()
