"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Install Software on Junos Devices > How to Specify Installation and Checksum Timeouts
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-software-installing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW


pkg = 'junos-install-mx-x86-64-17.2R1.13.tgz'


with Device(host='router1.example.net') as dev:
    sw = SW(dev)

    # Starting in Release 2.5.0, install() returns a tuple instead of a Boolean
    ok, msg = sw.install(package=pkg, validate=True, timeout=2400, checksum_timeout=400)
    if ok:
        sw.reboot()
