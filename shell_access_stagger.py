"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Access the Shell on Junos Devices > How to Stagger Command Execution
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-shell-accessing.html

Note: 'from pprint import pprint' was added — the documentation omits this import but the script
      uses pprint(). The script will fail without it.
"""

from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
from pprint import pprint


dev = Device(host='router1.example.net')


tables = ['inet.0', 'inet.6']
with StartShell(dev) as ss:
    for table in tables:
        command = 'cli -c "show route table ' + table + '"'
        rsp = ss.run(command, sleep=5)
        pprint (rsp)
