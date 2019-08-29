from pymongo import MongoClient
import sys

ram_min = sys.argv[1]
ram_max = sys.argv[2]
motherboard_min = sys.argv[3]
motherboard_max = sys.argv[4]
vga_min = sys.argv[5]
vga_max = sys.argv[6]
cpu_min = sys.argv[7]
cpu_max = sys.argv[8]
hard_disk_min = sys.argv[9]
hard_disk_max = sys.argv[10]

ram_arr = []
vga_arr = []
cpu_arr = []
motherboard_arr = []
hard_disk_arr = []

build_arr = []

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb

def check_compatibility(pro_name, pro, arr):
    if pro_name == "motherboard":
        for item in arr:
            if item == "cpu":
                if arr[1]["socket"] in pro["cpu_brand"]:
                    return True
                elif pro["cpu_brand"] in arr[1]["socket"]:
                    return True
        return False
    elif pro_name == "ram":
        for item in arr:
            if item == "motherboard":
                if arr[3]["memory_type"] in pro["type"]:
                    return True
                elif pro["type"] in arr[3]["memory_type"]:
                    return True
        return False
    elif pro_name == "vga":
        for item in arr:
            if item == "motherboard":
                if arr[3]["pci_slot"] in pro["slot"]:
                    return True
                elif pro["slot"] in arr[3]["pci_slot"]:
                    return True
        return False

def build_sequence(lists, category):
    if category == "cpu":
        build_arr.append("cpu")
        for item in lists:
            build_arr.append(item)
            break
    elif category == "motherboard":
        build_arr.append("motherboard")
        for item in lists:
            x = check_compatibility("motherboard", item, build_arr)
            if x==True:
                build_arr.append(item)
                break
    elif category == "ram":
        build_arr.append("ram")
        for item in lists:
            x = check_compatibility("ram", item, build_arr)
            if x==True:
                build_arr.append(item)
                break
    elif category == "vga":
        build_arr.append("vga")
        for item in lists:
            x = check_compatibility("vga", item, build_arr)
            if x == True:
                build_arr.append(item)
                break

cpu = db.CPU
for record in cpu.find().sort("points"):
    if cpu_min <= float(record['price']) and cpu_max >= float(record["price"]):
        cpu_arr.append(record)
build_sequence(cpu_arr, "cpu")

motherboard = db.Motherboard
for record in motherboard.find().sort("points"):
    if motherboard_min <= float(record['price']) and motherboard_max >= float(record["price"]):
        motherboard_arr.append(record)
build_sequence(motherboard_arr, "motherboard")

ram = db.RAM
for record in ram.find().sort("points"):
    if ram_min <= float(record['price']) and ram_max >= float(record["price"]):
        ram_arr.append(record)
build_sequence(ram_arr, "ram")

vga = db.VGA
for record in vga.find().sort("points"):
    if vga_min <= float(record['price']) and vga_max >= float(record["price"]):
        vga_arr.append(record)
build_sequence(vga_arr, "vga")

hard_disk = db.Hard_Disk
for record in hard_disk.find().sort("points").limit(1):
    if hard_disk_min <= float(record['price']) and hard_disk_max >= float(record['price']):
        hard_disk_arr.append(record)
        build_arr.append("hard_disk")
        build_arr.append(record)

# for x in build_arr:
#     print(x)