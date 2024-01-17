from ncclient import manager
from pprint import pprint
from router_info import router
import xmltodict


filter = open("filter.xml").read()

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    # using get(filter) because get_config('running', filter) only returns config, not operational state
    interface_netconf = m.get(filter)

# convert the xml to a python dictionary
# from 02-get-config.py before, we saw that the xml structure was contained between <rpc-reply> <data> tags
# notice that we need to add the ".xml" to the end of our variable
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]

# we can now take parts of that dict variable and use them in our code
name = interface_python['interfaces']['interface']['name']
ipaddr = interface_python['interfaces']['interface']['ipv4']['address']['ip']
ipnetmask = interface_python['interfaces']['interface']['ipv4']['address']['netmask']
print("the ip address of your device is: " + ipaddr)
print("the netmask of your device is: " + ipnetmask)

# we will make some more specific variables from the main dictionary
config = interface_python['interfaces']['interface']
op_state = interface_python['interfaces-state']['interface']

print("*" * 50)
print("the name of this interface is: " + config['name'])
print("this interface has output the following number of bytes: " + op_state['statistics']['out-octets'])
