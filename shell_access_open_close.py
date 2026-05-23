"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Access the Shell on Junos Devices > Execute Commands from the Shell
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-shell-accessing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell


dev = Device(host='router1.example.net')


ss = StartShell(dev)
ss.open()
ss.run('cli -c "request support information | save /var/tmp/information.txt"')
version = ss.run('cli -c "show version"')
print (version)
ss.close()
