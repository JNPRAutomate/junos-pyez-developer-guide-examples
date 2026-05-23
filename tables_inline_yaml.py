"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Load Inline or External Tables and Views in Junos PyEZ Applications > Load Inline Tables and Views
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-tables-views-loading.html
"""

from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

myYAML = """
---
UserTable:
  get: system/login/user
  view: UserView
UserView:
  fields:
    username: name
    userclass: class
"""

globals().update(FactoryLoader().load(yaml.load(myYAML, Loader=yaml.FullLoader)))

with Device(host='router.example.com') as dev:
    users = UserTable(dev)
    users.get()


    for account in users:
        print("Username is {}\nUser class is {}".format(account.username, account.userclass))
