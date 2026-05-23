"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Suppress RpcError Exceptions Raised for Warnings in Junos PyEZ Applications > Ignore All Warnings
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-warnings-ignoring.html

Note: 'from lxml import etree' was added — the documentation omits this import but the script
      uses etree.tostring(). The script will fail without it.
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree


dev = Device(host='router1.example.com')
dev.open()


with Config(dev, mode='exclusive') as cu:
    cu.load(path='mx-config.conf', ignore_warning=True)
    cu.commit(ignore_warning=True)


data = dev.rpc.get_configuration()
print(etree.tostring(data, encoding='unicode'))


dev.close()
