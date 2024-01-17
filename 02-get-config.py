from ncclient import manager
from pprint import pprint
from router_info import router
import xml.dom.minidom


filter = open("filter2.xml").read()

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    # using get(filter) because get_config('running', filter) only returns config, not operational state
    interface_netconf = m.get_config('running',filter)

# to see what the xml looks like, cleaned up
xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
print(xmlDom.toprettyxml(indent="  "))
