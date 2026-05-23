"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use the Junos PyEZ Config Utility to Configure Junos Devices > Specify the Configuration Mode
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-data-loading.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


dev = Device(host='dc1a.example.com').open()
with Config(dev, mode='private') as cu:
    cu.load('set system services netconf traceoptions file test.log', format='set')
    cu.pdiff()
    cu.commit()


dev.close()
