from pymongo import MongoClient
import sys

# price_min = sys.argv[1]
# price_max = sys.argv[2]
price_min = 0
price_max = 100000.00
ram_min = price_min * (10/100)
ram_max = price_max * (10/100)
motherboard_min = price_min * (30/100)
motherboard_max = price_max * (30/100)
vga_min = price_min * (20/100)
vga_max = price_max * (20/100)
cpu_min = price_min * (20/100)
cpu_max = price_max * (20/100)
hard_disk_min = price_min * (20/100)
hard_disk_max = price_max * (20/100)

ram_arr = []
vga_arr = []
cpu_arr = []
motherboard_arr = []
hard_disk_arr = []

build_arr = []
build_arr2 = []

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb

def check_compatibility(pro_name, pro, arr):
    if pro_name == "motherboard":
        for item in arr:
            if item == "cpu":
                return True
        return False
    elif pro_name == "ram":
        for item in arr:
            if item == "motherboard":
                return True
        return False
    elif pro_name == "vga":
        for item in arr:
            if item == "motherboard":
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
    elif category == "hard_disk":
        build_arr.append("hard_disk")
        for item in lists:
            build_arr.append(item)
            break

def build_sequence2(lists, category):
    if category == "cpu":
        count = 1
        build_arr2.append("cpu")
        for item in lists:
            if count != 1:
                build_arr2.append(item)
                break
            count = count + 1
    elif category == "motherboard":
        count = 1
        build_arr2.append("motherboard")
        for item in lists:
            if count != 1:
                x = check_compatibility("motherboard", item, build_arr)
                if x==True:
                    build_arr2.append(item)
                    break
            count = count + 1
    elif category == "ram":
        count = 1
        build_arr2.append("ram")
        for item in lists:
            if count != 1:
                x = check_compatibility("ram", item, build_arr)
                if x==True:
                    build_arr2.append(item)
                    break
            count = count + 1
    elif category == "vga":
        count = 1
        build_arr2.append("vga")
        for item in lists:
            if count != 1:
                x = check_compatibility("vga", item, build_arr)
                if x == True:
                    build_arr2.append(item)
                    break
            count = count + 1
    elif category == "hard_disk":
        count = 1
        build_arr2.append("hard_disk")
        for item in lists:
            if count != 1:
                build_arr2.append(item)
                break
            count = count+1

cpu = db.CPU
for record in cpu.find().sort("points"):
    if cpu_min <= float(record['price']) and cpu_max >= float(record["price"]):
        cpu_arr.append(record)
build_sequence(cpu_arr, "cpu")
build_sequence2(cpu_arr, "cpu")

motherboard = db.Motherboard
for record in motherboard.find().sort("points"):
    if motherboard_min <= float(record['price']) and motherboard_max >= float(record["price"]):
        motherboard_arr.append(record)
build_sequence(motherboard_arr, "motherboard")
build_sequence2(motherboard_arr, "motherboard")

ram = db.RAM
for record in ram.find().sort("points"):
    if ram_min <= float(record['price']) and ram_max >= float(record["price"]):
        ram_arr.append(record)
build_sequence(ram_arr, "ram")
build_sequence2(ram_arr, "ram")

vga = db.VGA
for record in vga.find().sort("points"):
    if vga_min <= float(record['price']) and vga_max >= float(record["price"]):
        vga_arr.append(record)
build_sequence(vga_arr, "vga")
build_sequence2(vga_arr, "vga")

hard_disk = db.Hard_Disk
for record in hard_disk.find().sort("points").limit(1):
    if hard_disk_min <= float(record['price']) and hard_disk_max >= float(record['price']):
        hard_disk_arr.append(record)
build_sequence(hard_disk_arr, "hard_disk")
build_sequence2(hard_disk_arr, "hard_disk")

for x in build_arr:
    print(x)
for x in build_arr2:
    print(x)