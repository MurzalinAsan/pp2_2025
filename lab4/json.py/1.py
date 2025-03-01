import json

f = open("sample_json.json", "r")
data = json.load(f)
f.close()
print("Interface status")
print("="*50)
print(f"{'DN':<50} {'Description':<15} {'Speed':<10} {'MTU':<5}")
print("-"*50)


for i in data["imdata"]:
    attr = i["l1PhysIf"]["attributes"]
    dn = attr["dn"]



    if "eth1/33" in dn or "eth1/34" in dn or "eth1/35" in dn:
        print(dn + "\t\t" + attr.get("descr", "") + "\t" + attr["speed"] + "\t" + attr["mtu"])





    
