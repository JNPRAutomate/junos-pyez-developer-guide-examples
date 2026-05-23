"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Execute RPCs on Junos Devices > Specify the Scope of Data to Return
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-rpcs-executing.html

Note: use_filter=True enables SAX parsing for memory-efficient processing of large XML replies
      when combined with filter_xml. See also: Specify the XML Parser for a Junos PyEZ Session.
"""

from jnpr.junos import Device
from lxml import etree

with Device(host='router.example.com', use_filter=True) as dev:
    filter = '<interface-information><physical-interface><name/></physical-interface></interface-information>'
    result = dev.rpc.get_interface_information(filter_xml=filter)
    print (etree.tostring(result, encoding='unicode'))
