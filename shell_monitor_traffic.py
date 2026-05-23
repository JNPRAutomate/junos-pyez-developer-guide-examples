"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Access the Shell on Junos Devices > Execute Nonreturning Shell Commands
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-shell-accessing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
from pprint import pprint


dev = Device(host='router1.example.net')


with StartShell(dev) as ss:
    pprint(ss.run('cli -c "monitor traffic interface fxp0"', this=None, timeout=15))
