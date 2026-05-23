"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Install Software on Junos Devices > How to Perform a VM Host Upgrade
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-software-installing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW


with Device(host='switch1.example.net') as dev:
    sw = SW(dev)


    # Starting in Release 2.5.0, install() returns a tuple instead of a Boolean
    ok, msg = sw.install(package='junos-vmhost-install-qfx-x86-64-18.1R1.9.tgz', vmhost=True,
no_copy=True)
    if ok:
        sw.reboot(vmhost=True)
