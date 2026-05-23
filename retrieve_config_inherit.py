"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Retrieve a Configuration > Specify Additional RPC Options
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-configuration-retrieving.html
"""

from jnpr.junos import Device
from lxml import etree


with Device(host='router1.example.net') as dev:
    data = dev.rpc.get_config(filter_xml='system/services', options={'inherit':'inherit'})
    print (etree.tostring(data, encoding='unicode', pretty_print=True))
