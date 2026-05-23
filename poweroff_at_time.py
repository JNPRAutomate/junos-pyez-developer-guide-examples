"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Halt, Reboot, or Shut Down Junos Devices > How to Halt, Reboot, or Shut Down the System with a Delay or at a Specified Time
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-device-rebooting.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW


with Device(host='dc1a.example.com') as dev:
    sw = SW(dev)
    sw.poweroff(at='22
