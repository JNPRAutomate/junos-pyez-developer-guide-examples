"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Install Software on Junos Devices > How to Perform a Unified ISSU or NSSU
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-software-installing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW


pkg = 'junos-install-mx-x86-64-17.2R1.13.tgz'
with Device(host='router1.example.net') as dev:
    sw = SW(dev)

    # Starting in Release 2.5.0, install() returns a tuple instead of a Boolean
    ok, msg = sw.install(package=pkg, issu=True, progress=True)
    if ok:
        sw.reboot(all_re=False)
