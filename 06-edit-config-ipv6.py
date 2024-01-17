from ncclient import manager
from router_info import router

config_template = open("config-ipv6-enable.xml").read()

# format is a method you can run on string data types
config = config_template.format(interface_name="GigabitEthernet1", ipv6_addr="2001:db8:1:1::10", ipv6_mask="64")

with manager.connect(host=router["host"], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    device_reply = m.edit_config(config, target='running')
    print(device_reply)
