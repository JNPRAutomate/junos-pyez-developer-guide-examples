"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Perform File System Operations > Perform File Operations > Manage Files
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-file-operations-performing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.fs import FS


src='/var/tmp/bgp-neighbors.slax'
dest='/var/db/scripts/op'


with Device(host='router1.example.net') as dev:
    fs = FS(dev)
    print(fs.cp(from_path=src, to_path=dest))
