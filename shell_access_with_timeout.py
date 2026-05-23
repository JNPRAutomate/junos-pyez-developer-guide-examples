"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Access the Shell on Junos Devices > How to Specify a Timeout
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-shell-accessing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell


dev = Device(host='router1.example.net')


with StartShell(dev) as ss:
    ss.run('cli -c "request support information | save /var/tmp/information.txt"', timeout=60)
    version = ss.run('cli -c "show version"')
    print (version)
