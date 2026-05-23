"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Authenticate Junos PyEZ Users > Authenticate Junos PyEZ Users Using SSH Keys
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-authentication.html

Note: Replace '/home/user/.ssh/id_rsa_dc' with the path to the actual SSH private key file.
"""

from jnpr.junos import Device
from getpass import getpass

junos_username = input('Junos OS username: ')
junos_password = getpass('Junos OS password: ')

cs_username = input('Console server username: ')
key_password = getpass('Password for SSH private key file: ')

with Device(host='router.example.com', user=junos_username, passwd=junos_password,
cs_user=cs_username, cs_passwd=key_password, ssh_private_key_file='/home/user/.ssh/id_rsa_dc') as dev:
    print (dev.facts)
