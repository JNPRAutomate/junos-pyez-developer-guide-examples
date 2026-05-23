"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Perform File System Operations > Perform File Operations > Calculate Checksums
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-file-operations-performing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.fs import FS


with Device(host='router1.example.net') as dev:
    fs = FS(dev)

    # if file exists, calculate checksum
    filepath = '/var/db/scripts/commit/filter_type_check.py'
    if fs.cat(path=filepath) is not None:
        print(fs.checksum(path=filepath, calc='sha256'))
    else:
        print('File not found.')
