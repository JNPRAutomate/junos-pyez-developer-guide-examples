"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Execute RPCs on Junos Devices > Specify the Format of the RPC Output
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-rpcs-executing.html
"""

from jnpr.junos import Device
from pprint import pprint

with Device(host='router1.example.com') as dev:
    sw_info_json = dev.rpc.get_software_information({'format':'json'})
    pprint(sw_info_json)
