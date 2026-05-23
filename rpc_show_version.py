"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Execute RPCs on Junos Devices > Execute RPCs as a Property of the Device Instance
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-rpcs-executing.html
"""

from jnpr.junos import Device
from lxml import etree


with Device(host='dc1a.example.com') as dev:
    #invoke the RPC equivalent to "show version"
    sw = dev.rpc.get_software_information()
    print(etree.tostring(sw, encoding='unicode'))
