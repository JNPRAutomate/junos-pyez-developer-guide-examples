"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use the Junos PyEZ Config Utility to Configure Junos Devices > Load Configuration Data Formatted as an XML Object
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-data-loading.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml.builder import E


config_xml_obj = (
    E.configuration(       # create an Element called "configuration"
     E.system(
       E.scripts(
         E.op (
           E.file (
             E.name("test.slax"),
           )
         )
       )
     )
  )
)


with Device(host='dc1a.example.com') as dev:
    with Config(dev, mode='exclusive') as cu:
        cu.load(config_xml_obj, merge=True)
        cu.commit()
