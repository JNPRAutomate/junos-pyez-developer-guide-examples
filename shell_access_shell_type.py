"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Access the Shell on Junos Devices > How to Specify the Shell Type
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-shell-accessing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell


dev = Device(host='router1.example.net')


with StartShell(dev, shell_type="sh") as ss:
    version = ss.run('cli -c "show version"')
    print (version)
