"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Perform File System Operations > Perform File Operations > View File Listings
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-file-operations-performing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.fs import FS
from pprint import pprint

with Device(host='router1.example.net') as dev:
    fs = FS(dev)
    pprint (fs.ls(path='/var/db/scripts/commit'))
