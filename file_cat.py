"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Perform File System Operations > Perform File Operations > Manage Files
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-file-operations-performing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.fs import FS


with Device(host='router1.example.net') as dev:
    fs = FS(dev)
    filepath = '/var/db/scripts/commit/filter_type_check.py'
    print(fs.cat(path=filepath))
