"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Suppress RpcError Exceptions Raised for Warnings in Junos PyEZ Applications > Ignore Specific Warnings
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-warnings-ignoring.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


commit_warnings = ['Advertisement-interval is less than four times',
     'Chassis configuration for network services has been changed.']

dev = Device(host='router1.example.com')
dev.open()


with Config(dev, mode='exclusive') as cu:
    cu.load(path='mx-config.conf')
    cu.commit(ignore_warning=commit_warnings)


dev.close()
