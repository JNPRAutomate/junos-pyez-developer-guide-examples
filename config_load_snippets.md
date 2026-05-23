# Configuration Load — Code Snippets

**Source Document:** Junos® OS Junos PyEZ Developer Guide
**Source Section:** Use the Junos PyEZ Config Utility to Configure Junos Devices > Load Configuration Data from a Local or Remote File
**Source URL:** https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-data-loading.html

> These are code snippets from the documentation. They require a surrounding `Device` and `Config`
> context and cannot run standalone. See `config_load_from_local_file.py` for a complete
> runnable script.

---

## Load from a File on the Junos Device

```python
cu.load(url='/var/home/user/golden.conf')
```

---

## Load from a Remote FTP URL

```python
cu.load(url='ftp://username@ftp.hostname.net/path/filename')
```

---

## Load from a Remote HTTP URL

```python
cu.load(url='http://username:password@example.com/path/filename')
```

---

## Load from a File Without a Recognised Extension

When the file has no extension or an unrecognised one, the format must be specified explicitly:

```python
conf_file = 'configs/junos-config-interfaces'
cu.load(path=conf_file, format='text', merge=True)
```
