# Commit Options — Code Snippets

**Source Document:** Junos® OS Junos PyEZ Developer Guide
**Source Section:** Use Junos PyEZ to Commit the Configuration > How to Specify Commit Options
**Source URL:** https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-committing.html

> These are code snippets from the documentation. They require a surrounding `Device` and `Config`
> context and cannot run standalone. See `commit_config.py` for a complete runnable script.

---

## Commit Comment

```python
cu.commit(comment='Configuring ge-0/0/0 interface')
```

---

## Commit Confirm

Require confirmation within 15 minutes, or the device auto-rolls back:

```python
cu.commit(confirm=15)
```

Confirm the previous commit:

```python
cu.commit()
```

---

## Commit Detail

Returns an XML object with detailed commit information:

```python
commit_result = cu.commit(detail=True)
```

---

## Commit Synchronize

Synchronize and commit on both Routing Engines:

```python
cu.commit(sync=True)
```

---

## Commit Force Synchronize

Force sync even if the other RE has open sessions:

```python
cu.commit(force_sync=True)
```

---

## Commit and Commit Check Timeout

```python
cu.commit_check(timeout=60)
cu.commit(timeout=360)
```

---

## Ignore Warnings

```python
cu.commit(ignore_warning=True)
```

---

## Commit Check

Verify syntax without committing:

```python
cu.commit_check()
```
