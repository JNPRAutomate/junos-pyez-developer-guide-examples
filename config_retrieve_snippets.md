# Configuration Retrieval — Code Snippets

**Source Document:** Junos® OS Junos PyEZ Developer Guide
**Source Section:** Use Junos PyEZ to Retrieve a Configuration > Retrieve Configuration Data for Standard or Custom YANG Data Models
**Source URL:** https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-configuration-retrieving.html

> These are code snippets from the documentation. They are continuation fragments shown inside
> the OpenConfig example and cannot run standalone. The OpenConfig example in
> `retrieve_config_openconfig.py` establishes the `Device` connection; these snippets show
> additional `get_config()` call patterns within that same session.

---

## Retrieve IETF YANG Model Configuration

```python
data = dev.rpc.get_config(filter_xml='interfaces', model='ietf')
print (etree.tostring(data, encoding='unicode', pretty_print=True))
```

---

## Retrieve Custom YANG Model Configuration

```python
data = dev.rpc.get_config(filter_xml='l2vpn', model='custom',
    namespace='http://yang.juniper.net/customyang/demo/l2vpn')
print (etree.tostring(data, encoding='unicode', pretty_print=True))
```

---

## Retrieve All Configuration Including All YANG Data Models

```python
data = dev.rpc.get_config(model=True)
print (etree.tostring(data, encoding='unicode', pretty_print=True))
```
