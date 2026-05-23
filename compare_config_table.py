"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Compare the Candidate Configuration and a Previously Committed Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-comparing.html

Note: This script requires an external Table definition. You must create:
  myTables/__init__.py          (empty file)
  myTables/ConfigTables.yml     (YAML Table/View definition containing UserConfigTable)
  myTables/ConfigTables.py      (Python loader):
      from jnpr.junos.factory import loadyaml
      from os.path import splitext
      _YAML_ = splitext(__file__)[0] + '.yml'
      globals().update(loadyaml(_YAML_))
"""

from jnpr.junos import Device
from myTables.ConfigTables import UserConfigTable


with Device(host='router1.example.com') as dev:
    with UserConfigTable(dev, mode='exclusive') as userconf:
        userconf.user = 'user1'
        userconf.class_name = 'read-only'
        userconf.append()


        userconf.load(merge=True)
        userconf.pdiff()
        userconf.commit()
