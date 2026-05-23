"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Connect to Junos Devices Using Junos PyEZ > Connect to a Device Using a Serial Console Connection
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-connection-methods.html

Note: Replace 'port' with the actual serial port path on your system (e.g. /dev/ttyUSB0).
      The default when port is omitted is /dev/ttyUSB0.
      For new or zeroized devices use user='root' and omit passwd.
"""

import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

junos_username = input("Junos OS username: ")
junos_password = getpass("Junos OS password: ")

try:
    with Device(mode='serial', port='port', user=junos_username, passwd=junos_password) as dev:
        print (dev.facts)
        cu = Config(dev)
        cu.lock()
        cu.load(path='/tmp/config_mx.conf')
        cu.commit()
        cu.unlock()

except Exception as err:
    print (err)
    sys.exit(1)
