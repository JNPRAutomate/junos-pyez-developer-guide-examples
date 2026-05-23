"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Install Software on Junos Devices > Installation Process Overview
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-software-installing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW


pkg = 'junos-install-mx-x86-64-17.2R1.13.tgz'


with Device(host='router1.example.net') as dev:
    sw = SW(dev)


    # In Junos PyEZ Release 2.4.1 and earlier, install() returns a Boolean
    # ok = sw.install(package=pkg, validate=True, checksum_algorithm='sha256')

    # In Junos PyEZ Release 2.5.0 and later, install() returns a tuple
    ok, msg = sw.install(package=pkg, validate=True, checksum_algorithm='sha256')
    print("Status: " + str(ok) + ", Message: " + msg)
    if ok:
         sw.reboot()
