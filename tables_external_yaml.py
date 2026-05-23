"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Load Inline or External Tables and Views in Junos PyEZ Applications > Import External Tables and Views
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-tables-views-loading.html

Note: This script requires external Table definition files. You must create:

  myTables/__init__.py          (empty file)

  myTables/ConfigTables.yml:
    ---
    UserTable:
      get: system/login/user
      view: UserView
    UserView:
      fields:
        username: name
        userclass: class

  myTables/ConfigTables.py:
    from jnpr.junos.factory import loadyaml
    from os.path import splitext
    _YAML_ = splitext(__file__)[0] + '.yml'
    globals().update(loadyaml(_YAML_))
"""

from jnpr.junos import Device
from myTables.ConfigTables import UserTable


with Device(host='router.example.com') as dev:
     users = UserTable(dev)
     users.get()


     for account in users:
         print("Username is {}\nUser class is {}".format(account.username, account.userclass))
