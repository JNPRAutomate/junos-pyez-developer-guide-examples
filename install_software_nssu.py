"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Install Software on Junos Devices > How to Perform a Unified ISSU or NSSU
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-software-installing.html

Note: The documentation shows the package filename with an em-dash character (jinstall-ex-4300–14.1X53...)
      which is a PDF formatting artifact. Real Junos package filenames use standard hyphens only.
      Replace with the correct package filename for your platform and release.
"""

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW


pkg = 'jinstall-ex-4300-14.1X53-D44.3-domestic-signed.tgz'
with Device(host='switch1.example.net') as dev:
    sw = SW(dev)

    # Starting in Release 2.5.0, install() returns a tuple instead of a Boolean
    ok, msg = sw.install(package=pkg, nssu=True, progress=True)
    if ok:
        sw.reboot(all_re=False)
