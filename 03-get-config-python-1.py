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
# notice that we need to add the ".xml" to the end of our variable, this is the xml part of the object returned to 
interface_python = xmltodict.parse(str(interface_netconf))["rpc-reply"]["data"]
pprint(interface_python)
