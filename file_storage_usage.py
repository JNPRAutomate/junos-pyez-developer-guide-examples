"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Perform File System Operations > Manage File System Storage > View File System Disk Space Usage
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-file-operations-performing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.fs import FS
from pprint import pprint


with Device(host='router1.example.net') as dev:
    fs = FS(dev)
    pprint(fs.storage_usage())
