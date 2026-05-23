"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Retrieve a Configuration > Specify the Source Database for the Configuration Data > Ephemeral Configuration Database
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-configuration-retrieving.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from lxml import etree


dev = Device(host='router1.example.net')


try:
    dev.open()
    with Config(dev, mode='ephemeral', ephemeral_instance='eph1') as cu:
        data = dev.rpc.get_config(options={'format':'text'})
        print(etree.tostring(data, encoding='unicode'))
    dev.close()


except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
except Exception as err:
    print (err)
