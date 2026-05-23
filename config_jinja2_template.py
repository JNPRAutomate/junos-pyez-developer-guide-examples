"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use the Junos PyEZ Config Utility to Configure Junos Devices > Load Configuration Data Using Jinja2 Templates
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-data-loading.html

Note: Requires a Jinja2 template file at the path specified in conf_file.
      See the documentation for the expected template format.
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


conf_file = 'configs/junos-config-interfaces-mpls.conf'
config_vars = {
    'interfaces': ['ge-1/0/1', 'ge-1/0/2', 'ge-1/0/3'],
    'description': 'MPLS interface',
    'family': 'mpls'
}


with Device(host='router1.example.com') as dev:
    with Config(dev, mode='exclusive') as cu:
        cu.load(template_path=conf_file, template_vars=config_vars, merge=True)
        cu.commit()
