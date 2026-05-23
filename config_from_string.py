"""
Source Document : Junos PyEZ Developer Guide
Source Section  : Use the Junos PyEZ Config Utility to Configure Junos Devices > Load Configuration Data from a String
Source URL      : https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/task/junos-pyez-program-configuration-data-loading.html
"""

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


dev = Device(host='dc1a.example.com').open()
cu = Config(dev)

# For configuration formatted as text
config_text = """
system {
    scripts {
         op {
              file test.slax;
         }
    }
}
"""
cu.load(config_text, format='text', merge=True)

# For configuration formatted as xml
config_xml = """
<configuration>
      <system>
          <scripts>
               <op>
                    <file>
                        <name>test.slax</name>
                   </file>
              </op>
          </scripts>
      </system>
</configuration>
"""
cu.load(config_xml, format='xml', merge=True)

# For configuration formatted as text with set action
config_set = """
set system scripts op file test.slax
"""
cu.load(config_set, format='set', merge=True)

# For configuration data formatted using json
config_json = """{
    "configuration" : {
        "system" : {
            "scripts" : {
                "op" : {
                     "file" : [
                     {
                         "name" : "test.slax"
                     }
                       ]
                  }
             }
         }
    }
}"""
cu.load(config_json, format='json', merge=True)
