from pymongo import MongoClient
import sys

want_product = sys.argv[1]
price_range = sys.argv[2]

motherboard = ''
cpu = ''
ram = ''
vga = ''

res = []

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb

if motherboard != "":
    col_motherboard = db.Motherboard
    motherboard_pro = col_motherboard.find({"id": motherboard})

if cpu != "":
    col_cpu = db.CPU
    cpu_pro = col_cpu.find({"id": cpu})

if ram != "":
    col_ram = db.RAM
    ram_pro = col_ram.find({"id": ram})

if vga != "":
    col_vga = db.VGA
    vga_pro = col_vga.find({"id": col_vga})

if want_product == "motherboard":
    for col in col_motherboard.find():
        if (col["cpu_brand"] in cpu_pro["socket"]) or (cpu_pro["socket"] in col["cpu_brand"]):
            if col["memory_type"] == ram_pro["type"]:
                if col["pci_slot"] == vga_pro["slot"]:
                    res.append(col)

elif want_product == "cpu":
    for col in col_cpu.find():
        if (col["socket"] in motherboard_pro["cpu_brand"]) or (motherboard_pro["cpu_brand"] in col["socket"]):
            res.append(col)

elif want_product == "ram":
    for col in col_ram.find():
        if (col["type"] in motherboard_pro["memory_type"]) or (motherboard_pro["memory_type"] in col["type"]):
            res.append(col)

elif want_product == "vga":
    for col in col_vga.find():
        if (col["pci_slot"] in vga_pro["slot"]) or (vga_pro["slot"] in col["pci_slot"]):
            res.append(col)

print(res)
