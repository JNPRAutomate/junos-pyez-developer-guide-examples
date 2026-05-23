# Authentication — Code Snippets

**Source Document:** Junos® OS Junos PyEZ Developer Guide
**Source Section:** Authenticate Junos PyEZ Users > Authenticate Junos PyEZ Users Using SSH Keys
**Source URL:** https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-authentication.html

> These are code snippets from the documentation demonstrating specific authentication
> parameters. They cannot run standalone. See `connect_console_server_ssh_key.py` for a
> complete runnable script using an SSH key file through a console server.

---

## Specify a Custom SSH Configuration File

```python
ssh_config_file = "~/.ssh/config_dc"
dev = Device(host='198.51.100.1', ssh_config=ssh_config_file)
```

---

## Specify an SSH Private Key File

For a direct device connection (no console server):

```python
dev = Device(host='router.example.com', passwd=key_password,
             ssh_private_key_file='/home/user/.ssh/id_rsa_dc')
dev.open()
# ...
dev.close()
```
