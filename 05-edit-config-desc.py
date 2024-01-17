from ncclient import manager
from router_info import router


config_template = open('config-desc.xml').read()

# format is a method you can run on string data types
config = config_template.format(interface_name="GigabitEthernet1", interface_desc="interface programmed by code")

with manager.connect(host=router["host"], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    device_reply = m.edit_config(config, target='running')
    print(device_reply)
