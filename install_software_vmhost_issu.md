# Install Software — VM Host ISSU Snippet

**Source Document:** Junos® OS Junos PyEZ Developer Guide
**Source Section:** Use Junos PyEZ to Install Software on Junos Devices > How to Perform a Unified ISSU or NSSU
**Source URL:** https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/topic-map/junos-pyez-program-software-installing.html

> The documentation shows the `vmhost=True` + `issu=True` combination as a single-line snippet
> only — not a complete standalone script. See `install_software_vmhost.py` and
> `install_software_issu.py` for the full standalone versions of each individual feature.

---

## VM Host In-Service Upgrade

Combines `vmhost=True` and `issu=True` to perform an in-service upgrade of both the host OS
and Junos OS with no control-plane disruption:

```python
sw.install(package='junos-vmhost-install-qfx-x86-64-18.1R1.9.tgz', vmhost=True, issu=True,
progress=True)
```
