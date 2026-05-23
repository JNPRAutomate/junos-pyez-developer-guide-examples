# RPC Execution — Code Snippets

**Source Document:** Junos® OS Junos PyEZ Developer Guide
**Source Section:** Use Junos PyEZ to Execute RPCs on Junos Devices
**Source URL:** https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-rpcs-executing.html

> These are code snippets from the documentation. They are fragments that require a surrounding
> `Device` context and cannot run standalone. See `rpc_show_version.py`, `rpc_text_format.py`,
> `rpc_json_format.py`, and `rpc_filter_xml.py` for complete runnable scripts.

---

## Fixed-Form Option

Equivalent to `show interfaces terse`:

```python
rsp = dev.rpc.get_interface_information(terse=True)
```

---

## Value Option

Equivalent to `show interfaces ge-0/0/0`:

```python
rsp = dev.rpc.get_interface_information(interface_name='ge-0/0/0')
```

---

## Specify the RPC Timeout

Override the timeout for a single RPC call only:

```python
dev.rpc.get_route_information(table='inet.0', dev_timeout=55)
```

---

## Normalize the XML RPC Reply — Device Level

Enable normalization for the entire session (either form is equivalent):

```python
dev = Device(host='router1.example.com', user='root', normalize=True)
```

```python
dev.open(normalize=True)
```

---

## Normalize the XML RPC Reply — Single RPC

Normalize the reply for one specific RPC call:

```python
dev.rpc.rpc_method(normalize=True)
```

Example using `get_interface_information`:

```python
rsp = dev.rpc.get_interface_information(interface_name='ge-0/0/0.0', terse=True, normalize=True)
```

---

## XPath Without Normalization

Must account for whitespace in text nodes:

```python
rsp = dev.rpc.get_interface_information(interface_name='ge-0/0/0.0', terse=True)
print (rsp.xpath('.// \
    address-family[normalize-space(address-family-name)="inet"]/ \
    interface-address/ifa-local')[0].text)
```

---

## XPath With Normalization

Clean XPath with no whitespace handling required:

```python
rsp = dev.rpc.get_interface_information(interface_name='ge-0/0/0.0', terse=True, normalize=True)
print (rsp.xpath('.//address-family[address-family-name="inet"]/ \
    interface-address/ifa-local')[0].text)
```
