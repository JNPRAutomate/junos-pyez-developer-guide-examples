"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Install Software on Junos Devices > How to Install Software on an EX Series Virtual Chassis Member
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-software-installing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW


pkg = 'junos-install-ex-x86-64-23.2R1.13.tgz'



def myprogress(dev, report):
    print("host: {}, report: {}".format(dev.hostname, report))


with Device(host='switch2.example.net') as dev:
    sw = SW(dev)
    ok, msg = sw.install(package=pkg, member_id=['0', '1'],
                         progress=myprogress, no_copy=True,
                         reboot=False, cleanfs=False,
                         force_host=False, timeout=4000)
    if ok:
        sw.reboot(all_re=False, member_id=['0', '1'])
