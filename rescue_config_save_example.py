"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Manage the Rescue Configuration on Junos Devices > Example: Use Junos PyEZ to Save a Rescue Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-configuration-rescue-managing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError


host = 'dc1a.example.com'


def main():


    dev = Device(host=host)


    # open a connection with the device and start a NETCONF session
    try:
         dev.open()
    except ConnectError as err:
         print ("Cannot connect to device: {0}".format(err))
         return


    # Create an instance of Config
    cu = Config(dev)


    # Print existing rescue configuration or save one if none exists
    try:
         rescue = cu.rescue(action='get', format='text')
         if rescue is None:
             print ('No existing rescue configuration.')
             print ('Saving rescue configuration.')
             cu.rescue(action='save')
         else:
             print ('Rescue configuration found:')
             print (rescue)
    except Exception as err:
        print (err)


    # End the NETCONF session and close the connection
    dev.close()


if __name__ == "__main__":
    main()
