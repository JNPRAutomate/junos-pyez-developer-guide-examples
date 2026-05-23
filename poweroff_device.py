"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Halt, Reboot, or Shut Down Junos Devices > Perform a System Halt, Reboot, or Shut Down
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-device-rebooting.html
"""

#Python 3
from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import ConnectError
from getpass import getpass


hostname = input("Device hostname: ")
username = input("Device username: ")
password = getpass("Device password: ")


try:
    with Device(host=hostname, user=username, passwd=password) as dev:
        sw = SW(dev)
        print(sw.poweroff())
except ConnectError as err:
    print (err)
