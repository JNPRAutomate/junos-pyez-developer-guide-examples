# Halt Device — Code Snippets

**Source Document:** Junos® OS Junos PyEZ Developer Guide
**Source Section:** Use Junos PyEZ to Halt, Reboot, or Shut Down Junos Devices > Perform a System Halt, Reboot, or Shut Down
**Source URL:** https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-device-rebooting.html

> The documentation lists `halt()` in its method reference table and describes its behaviour
> (gracefully shut down Junos OS but maintain system power) but does not provide a complete
> standalone script. The equivalent complete scripts for `reboot()` and `poweroff()` are in
> `reboot_device.py` and `poweroff_device.py`. The pattern below follows those examples.

---

## Halt All Routing Engines Immediately

```python
#Python 3
from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import ConnectError
from getpass import getpass

hostname = input("Device hostname: ")
username = input("Device username: ")
password = getpass("Device password: ")

try:
    with Device(host=hostname, user=username, passwd=password) as dev:
        sw = SW(dev)
        print(sw.halt())
except ConnectError as err:
    print (err)
```
