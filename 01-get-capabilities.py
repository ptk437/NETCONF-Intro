from ncclient import manager
from router_info import router


# just checking to see if the length of the m.server_capabilities below actually equals the number counted, and it does
num_capabilities = 0

with manager.connect(
    host=router["host"],
    port=router["port"],
    username=router["username"],
    password=router["password"],
    hostkey_verify=False,
) as m:
    for capability in m.server_capabilities:
        print("*" * 50)
        print(capability)
        num_capabilities += 1
    print(f"This router supports {len(m.server_capabilities)} YANG models.")
    print(f"This router supports {num_capabilities} YANG models.")
