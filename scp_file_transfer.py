"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Transfer Files Using Junos PyEZ
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-files-transferring-scp.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP


def log(dev, report):
    print (dev.hostname + ': ' + report)


def main():


    dev = Device('router1.example.com')
    msgfile = 'logs/'+dev.hostname+'-messages'


    try:


        #Default progress messages
        with SCP(dev, progress=True) as scp1:
            scp1.put('scp-test1.txt', remote_path='/var/tmp/')
            scp1.get('/var/log/messages', local_path=msgfile)


        #Custom progress messages
        with SCP(dev, progress=log) as scp2:
            scp2.put('scp-test2.txt', remote_path='/var/tmp/')
            scp2.get('/var/log/messages', local_path=msgfile)


    except Exception as err:
        print (err)
        return


if __name__ == "__main__":
    main()
