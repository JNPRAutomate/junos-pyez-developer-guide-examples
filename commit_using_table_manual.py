"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Commit the Configuration > How to Commit the Candidate Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-committing.html

Note: This script requires an external Table definition. You must create:
  myTables/__init__.py             (empty file)
  myTables/UserConfigTable.yml     (YAML Table/View definition for UserConfigTable)
  myTables/UserConfigTable.py      (Python loader):
      from jnpr.junos.factory import loadyaml
      from os.path import splitext
      _YAML_ = splitext(__file__)[0] + '.yml'
      globals().update(loadyaml(_YAML_))
"""

from jnpr.junos import Device
from myTables.UserConfigTable import UserConfigTable


with Device(host='router1.example.com') as dev:


    userconfig = UserConfigTable(dev)
    # ...set the values for the configuration data...
    userconfig.append()
    userconfig.lock()
    userconfig.load(merge=True)
    userconfig.commit()
    userconfig.unlock()
