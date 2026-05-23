"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Execute RPCs on Junos Devices > Map Junos OS Commands to Junos PyEZ RPCs
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-rpcs-executing.html
"""

from jnpr.junos import Device


with Device(host='router.example.com') as dev:
    print (dev.display_xml_rpc('show route', format='text'))
