"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Halt, Reboot, or Shut Down Junos Devices > How to Reboot a VM Host
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-device-rebooting.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW


with Device(host='switch1.example.net') as dev:
    sw = SW(dev)
    sw.reboot(vmhost=True)
