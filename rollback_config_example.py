"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Example: Use Junos PyEZ to Roll Back the Configuration
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/example/junos-pyez-program-configuration-rolling-back.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from jnpr.junos.exception import LockError
from jnpr.junos.exception import RpcError
from jnpr.junos.exception import CommitError
from jnpr.junos.exception import UnlockError


host = 'dc1a.example.com'


def main():
    dev = Device(host=host)
    # open a connection with the device and start a NETCONF session
    try:
         dev.open()
    except ConnectError as err:
         print ("Cannot connect to device: {0}".format(err))
         return


    # Set up config object
    cu = Config(dev)


    # Lock the configuration
    print ("Locking the configuration")
    try:
         cu.lock()
    except LockError as err:
         print ("Unable to lock configuration: {0}".format(err))
         dev.close()
         return


    # Roll back and commit configuration
    try:
         print ("Rolling back the configuration")
         cu.rollback(rb_id=1)
         print ("Committing the configuration")
         cu.commit()
    except CommitError as err:
         print ("Error: Unable to commit configuration: {0}".format(err))
    except RpcError as err:
         print ("Unable to roll back configuration changes: {0}".format(err))


    finally:
        print ("Unlocking the configuration")
        try:
             cu.unlock()
        except UnlockError as err:
             print ("Unable to unlock configuration: {0}".format(err))
        dev.close()
        return


if __name__ == "__main__":
    main()
