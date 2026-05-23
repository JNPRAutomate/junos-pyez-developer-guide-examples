# Junos PyEZ Example Scripts

Complete Python scripts extracted from the **Junos PyEZ Developer Guide**.

## Content and Source Information

**Content:** About 86 scripts for your scripting enjoyment!
**Source Document:** [Junos® OS Junos PyEZ Developer Guide](junos-pyez-developer.pdf) from Juniper Networks, Inc.
**Online:** <https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/index.html>

### Connect to Junos Devices Using Junos PyEZ

| Script | Description |
|--------|-------------|
| `connect_ssh_password.py` | SSH — open/close with interactive credentials |
| `connect_ssh_context_manager.py` | SSH — context manager with interactive credentials |
| `connect_via_console_server_ssh.py` | SSH through a console server |
| `connect_outbound_ssh.py` | Outbound SSH — listener for device-initiated sessions |
| `connect_telnet.py` | Telnet — open/close with interactive credentials |
| `connect_serial_console_load_config.py` | Serial console — connect and load a config file |

### Authenticate Junos PyEZ Users

| Script | Description |
|--------|-------------|
| `connect_console_server_ssh_key.py` | Console server with SSH private key file |
| `auth_snippets.md` | Snippets: ssh_config and ssh_private_key_file parameters |

### Use Junos PyEZ to Retrieve Facts from Junos Devices

| Script | Description |
|--------|-------------|
| `get_device_facts.py` | Connect via SSH keys; print device facts |

### Use Junos PyEZ to Access the Shell on Junos Devices

| Script | Description |
|--------|-------------|
| `shell_access_open_close.py` | Shell — explicit open/close |
| `shell_access_context_manager.py` | Shell — context manager |
| `shell_access_shell_type.py` | Shell — specify Bourne-style shell (shell_type="sh") |
| `shell_access_with_timeout.py` | Shell — custom timeout on run() |
| `shell_access_stagger.py` | Shell — staggered commands with sleep argument |
| `shell_monitor_traffic.py` | Shell — capture output of a non-returning command |

### Use Junos PyEZ to Execute RPCs on Junos Devices

| Script | Description |
|--------|-------------|
| `rpc_display_xml_rpc.py` | Map CLI command to RPC via display_xml_rpc() |
| `rpc_show_version.py` | Execute get_software_information() RPC |
| `rpc_text_format.py` | RPC output in text format |
| `rpc_json_format.py` | RPC output in JSON format |
| `rpc_filter_xml.py` | Filter RPC reply with filter_xml; SAX parsing with use_filter=True |
| `rpc_snippets.md` | Snippets: terse/value options, dev_timeout, normalize |

### Suppress RpcError Exceptions Raised for Warnings

| Script | Description |
|--------|-------------|
| `ignore_warnings_all.py` | Suppress all warnings with ignore_warning=True |
| `ignore_warnings_specific.py` | Suppress specific warnings by string list |

### Use Junos PyEZ to Halt, Reboot, or Shut Down Junos Devices

| Script | Description |
|--------|-------------|
| `reboot_device.py` | Reboot all REs immediately (prompts for credentials) |
| `poweroff_device.py` | Power off all REs immediately (prompts for credentials) |
| `reboot_in_min.py` | Reboot all REs after a delay in minutes |
| `reboot_at_time.py` | Reboot all REs at a scheduled time |
| `poweroff_at_time.py` | Power off all REs at a scheduled time |
| `reboot_all_re.py` | Reboot all REs explicitly (all_re=True) |
| `reboot_connected_re_only.py` | Reboot only the connected RE (all_re=False) |
| `reboot_other_re.py` | Reboot all REs except the connected RE (other_re=True) |
| `reboot_specific_node.py` | Reboot a specific node on Junos OS Evolved |
| `reboot_vc_members.py` | Reboot specific Virtual Chassis members |
| `reboot_vmhost.py` | Reboot VM host (reboots both guest Junos OS and host OS) |
| `halt_device.md` | Snippet: halt() method — no complete standalone script in documentation |

### Use Junos PyEZ to Install Software on Junos Devices

| Script | Description |
|--------|-------------|
| `install_software_basic.py` | Basic install with checksum validation |
| `install_software_timeouts.py` | Install with extended installation and checksum timeouts |
| `install_software_with_progress.py` | Install with a custom progress callback |
| `install_software_vmhost.py` | VM host upgrade (upgrades host OS and Junos OS) |
| `install_software_issu.py` | Unified ISSU (no control-plane disruption) |
| `install_software_nssu.py` | NSSU (nonstop upgrade for EX/QFX Virtual Chassis) |
| `install_software_vc_members.py` | Install on specific EX Series Virtual Chassis members |
| `install_software.py` | Full example with logging and error handling |
| `install_software_vmhost_issu.md` | Snippet: vmhost=True + issu=True combination |

### Use Junos PyEZ to Perform File System Operations

| Script | Description |
|--------|-------------|
| `file_ls.py` | List files and directories at a given path |
| `file_cat.py` | View the contents of a file |
| `file_cp.py` | Copy a file on the device |
| `file_checksum.py` | Calculate the SHA256 checksum of a file |
| `file_storage_usage.py` | View file system disk space usage |
| `file_directory_usage.py` | View disk space usage for a directory |
| `file_storage_cleanup.py` | Preview and execute a storage cleanup |

### Transfer Files Using Junos PyEZ

| Script | Description |
|--------|-------------|
| `scp_file_transfer.py` | SCP files to/from a device with default and custom progress |

### Use Junos PyEZ to Retrieve a Configuration

| Script | Description |
|--------|-------------|
| `retrieve_config_complete.py` | Retrieve the complete candidate configuration |
| `retrieve_config_committed.py` | Retrieve from the committed configuration database |
| `retrieve_config_ephemeral.py` | Retrieve from the default ephemeral configuration database |
| `retrieve_config_ephemeral_instance.py` | Retrieve from a named ephemeral configuration instance |
| `retrieve_config_filter_multi.py` | Filter multiple hierarchies ([edit interfaces] and [edit protocols]) |
| `retrieve_config_filter_services.py` | Filter [edit system services] — three equivalent filter forms |
| `retrieve_config_filter_interface_names.py` | Filter: interface names only (post-inheritance) |
| `retrieve_config_filter_interface_subtree.py` | Filter: full subtree for a specific interface |
| `retrieve_config_formats.py` | Retrieve in XML, text, set, and JSON formats |
| `retrieve_config_openconfig.py` | Retrieve OpenConfig BGP configuration |
| `retrieve_config_inherit.py` | Retrieve post-inheritance configuration |
| `retrieve_config_namespace.py` | Retain namespace in returned configuration data |
| `config_retrieve_snippets.md` | Snippets: IETF, custom YANG, and model=True |

### Use Junos PyEZ to Compare Configurations

| Script | Description |
|--------|-------------|
| `compare_config_pdiff.py` | Load changes, print diff (pdiff), then commit |
| `compare_config_table.py` | Compare using a configuration Table (requires external Table files) |
| `compare_config_rollback.py` | Compare candidate against rollback ID 5 without committing |

### Use Junos PyEZ to Configure Junos Devices

| Script | Description |
|--------|-------------|
| `config_ephemeral_mode.py` | Configure the default ephemeral configuration database |
| `config_ephemeral_instance.py` | Configure a named ephemeral configuration instance |

### Use the Junos PyEZ Config Utility to Configure Junos Devices

| Script | Description |
|--------|-------------|
| `config_private_mode.py` | Load a set command using configure private mode |
| `config_load_from_local_file.py` | Load configuration from a local file (exclusive mode) |
| `config_from_string.py` | Load configuration from strings — text, XML, set, and JSON formats |
| `config_from_xml_object.py` | Load configuration from an lxml XML object |
| `config_jinja2_template.py` | Load configuration from a Jinja2 template file |
| `config_rollback.py` | Prompt for rollback ID, roll back, pdiff, and commit |
| `config_load_rescue.py` | Load and commit the rescue configuration |
| `config_commit_basic.py` | Basic load and commit |
| `config_load_snippets.md` | Snippets: URL-based load and format-without-extension |

### Use Junos PyEZ to Commit the Configuration

| Script | Description |
|--------|-------------|
| `commit_config.py` | Commit with ConfigLoadError and CommitError handling |
| `commit_using_table_set.py` | Commit using a configuration Table's set() method (requires external Table files) |
| `commit_using_table_manual.py` | Commit using a configuration Table's individual methods (requires external Table files) |
| `commit_options.md` | Snippets: comment, confirm, detail, sync, force_sync, timeout, ignore_warning, commit_check |

### Example: Load Configuration Data from a File

| Script | Description |
|--------|-------------|
| `load_config_from_file_example.py` | Full example — lock, load (merge), commit, unlock with full error handling |

### Example: Roll Back the Configuration

| Script | Description |
|--------|-------------|
| `rollback_config_example.py` | Full example — lock, rollback, commit, unlock with full error handling |

### Use Junos PyEZ to Manage the Rescue Configuration

| Script | Description |
|--------|-------------|
| `rescue_config_save.py` | Save the active configuration as the rescue configuration |
| `rescue_config_get.py` | Retrieve and print the rescue configuration |
| `rescue_config_load.py` | Load and commit the rescue configuration |
| `rescue_config_delete.py` | Delete the rescue configuration |
| `rescue_config_save_example.py` | Full example — check for existing rescue config or save one |

### Load Inline or External Tables and Views

| Script | Description |
|--------|-------------|
| `tables_predefined_ethport.py` | Use the predefined EthPortTable to list Ethernet interface status |
| `tables_inline_yaml.py` | Define a custom Table/View inline with YAML and query user accounts |
| `tables_external_yaml.py` | Import an external YAML Table/View file and query user accounts (requires external files) |

---

## Prerequisites

- Python 3.5 or later (3.8–3.12 recommended)
- Junos PyEZ 2.0 or later: `pip install junos-eznc`
- NETCONF enabled on target devices: `set system services netconf ssh`
- Appropriate user account permissions on the device

---

## Quick Start

```bash
git clone https://github.com/<your-username>/junos-pyez-examples.git
cd junos-pyez-examples
pip install junos-eznc
python3 get_device_facts.py
```

---

## Notes on Scripts Requiring External Files

The following scripts import from a `myTables/` directory that you must create before running them. See the docstring in each script for the required file contents.

- `compare_config_table.py`
- `commit_using_table_set.py`
- `commit_using_table_manual.py`
- `tables_external_yaml.py`

---

## References

- [Junos PyEZ Developer Guide (PDF)](junos-pyez-developer.pdf)
- [Junos PyEZ Developer Guide (Online)](https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/index.html)
- [Junos PyEZ API Reference](https://junos-pyez.readthedocs.io/en/latest/)
- [Junos PyEZ on GitHub](https://github.com/Juniper/py-junos-eznc)
