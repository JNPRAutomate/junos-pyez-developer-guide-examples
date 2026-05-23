"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use Junos PyEZ to Perform File System Operations > Manage File System Storage > Clean Up System Storage
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-file-operations-performing.html

Note: 'from jnpr.junos import Device' was added — the documentation omits this import but the
      script uses Device(). The script will fail without it.
"""

from jnpr.junos import Device
from jnpr.junos.utils.fs import FS
from pprint import pprint


with Device(host='router1.example.net') as dev:
    fs = FS(dev)
    print('\n*** Cleanup Check - files to delete ***\n')
    pprint(fs.storage_cleanup_check())


    cleanup = input('\nProceed with storage cleanup '
                    'and delete these files [yes,no] (no) ? ').lower()
    if cleanup in ['yes', 'y']:
        print('Cleaning up storage.')
        files = fs.storage_cleanup()
        pprint(files)
    elif cleanup in ['no', 'n', '']:
        print('Cleanup operation canceled.')
    else:
        print('Please enter a valid response.')
