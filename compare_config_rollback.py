"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Compare the Candidate Configuration and a Previously Committed Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-comparing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


with Device(host='router1.example.com') as dev:
   cu = Config(dev)
   cu.pdiff(rb_id=5)
