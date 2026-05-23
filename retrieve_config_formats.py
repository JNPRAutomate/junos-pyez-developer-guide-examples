"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Retrieve a Configuration > Specify the Format for Configuration Data to Return
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-configuration-retrieving.html
"""

from jnpr.junos import Device
from lxml import etree
from pprint import pprint


with Device(host='router1.example.net') as dev:


    # XML format (default)
    data = dev.rpc.get_config()
    print (etree.tostring(data, encoding='unicode', pretty_print=True))


    # Text format
    data = dev.rpc.get_config(options={'format':'text'})
    print (etree.tostring(data, encoding='unicode', pretty_print=True))


    # Junos OS set format
    data = dev.rpc.get_config(options={'format':'set'})
    print (etree.tostring(data, encoding='unicode', pretty_print=True))


    # JSON format
    data = dev.rpc.get_config(options={'format':'json'})
    pprint (data)
