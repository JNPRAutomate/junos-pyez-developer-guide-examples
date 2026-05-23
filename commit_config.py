"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Commit the Configuration > How to Commit the Candidate Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-committing.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConfigLoadError, CommitError


with Device(host='router1.example.com') as dev:


    with Config(dev, mode='exclusive') as cu:
        try:
            cu.load(path='configs/mx_config.conf', merge=True)
            cu.commit()
        except (ConfigLoadError, CommitError) as err:
            print (err)
