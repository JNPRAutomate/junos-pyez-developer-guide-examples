"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Load Inline or External Tables and Views in Junos PyEZ Applications > Import Junos PyEZ's Predefined Tables and Views
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-tables-views-loading.html
"""

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable


with Device(host='router1.example.net') as dev:
    eth = EthPortTable(dev)
    eth.get()


    for item in eth:
        print ("{}: {}".format(item.name, item.oper))
