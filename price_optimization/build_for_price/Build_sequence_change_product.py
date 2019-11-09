# from pymongo import MongoClient
# import sys
#
# want_product = sys.argv[1]
# price_range = sys.argv[2]
#
# motherboard = ''
# cpu = ''
# ram = ''
# vga = ''
#
# res = []
#
# client = MongoClient('mongodb://localhost:27017')
# db = client.techRingdb
#
# if motherboard != "":
#     col_motherboard = db.Motherboard
#     motherboard_pro = col_motherboard.find({"id": motherboard})
#
# if cpu != "":
#     col_cpu = db.CPU
#     cpu_pro = col_cpu.find({"id": cpu})
#
# if ram != "":
#     col_ram = db.RAM
#     ram_pro = col_ram.find({"id": ram})
#
# if vga != "":
#     col_vga = db.VGA
#     vga_pro = col_vga.find({"id": col_vga})
#
# if want_product == "motherboard":
#     for col in col_motherboard.find():
#         if (col["cpu_brand"] in cpu_pro["socket"]) or (cpu_pro["socket"] in col["cpu_brand"]):
#             if col["memory_type"] == ram_pro["type"]:
#                 if col["pci_slot"] == vga_pro["slot"]:
#                     res.append(col)
#
# elif want_product == "cpu":
#     for col in col_cpu.find():
#         if (col["socket"] in motherboard_pro["cpu_brand"]) or (motherboard_pro["cpu_brand"] in col["socket"]):
#             res.append(col)
#
# elif want_product == "ram":
#     for col in col_ram.find():
#         if (col["type"] in motherboard_pro["memory_type"]) or (motherboard_pro["memory_type"] in col["type"]):
#             res.append(col)
#
# elif want_product == "vga":
#     for col in col_vga.find():
#         if (col["pci_slot"] in vga_pro["slot"]) or (vga_pro["slot"] in col["pci_slot"]):
#             res.append(col)
#
# print(res)


from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb

want_product = sys.argv[1]
min_price = sys.argv[2]
max_price = sys.argv[3]

# want_product = "cpu"
# min_price = "0"
# max_price = "25000"

# cpu_arr = "5d6aabfac9c3e2a971b5cd77"
cpu_arr = sys.argv[4]
cpu_new_arr = []
# motherboard_arr = "5d6ab2a6204a1c169b0422f9"
motherboard_arr = sys.argv[5]
motherboard_new_arr = []
# ram_arr = "5d6ab5bec863baf5005fa70c"
ram_arr = sys.argv[6]
ram_new_arr = []
# vga_arr = "5d6ac0e0c31e8d690f3033bd"
vga_arr = sys.argv[7]
vga_new_arr = []
# hard_disk_arr = "5d6aaf377e6f92a252a6e731"
hard_disk_arr = sys.argv[8]
hard_disk_new_arr = []

result = ''
myquery1 = { "_id": ObjectId(cpu_arr)}
myquery2 = { "_id": ObjectId(motherboard_arr)}
myquery3 = { "_id": ObjectId(ram_arr)}
myquery4 = { "_id": ObjectId(vga_arr)}
myquery5 = { "_id": ObjectId(hard_disk_arr)}

cpu = db.CPU
cpu_new_arr = cpu.find_one(myquery1)
motherboard = db.Motherboard
motherboard_new_arr = motherboard.find_one(myquery2)
ram = db.RAM
ram_new_arr = ram.find_one(myquery3)
vga = db.VGA
vga_new_arr = vga.find_one(myquery4)
hard_disk = db.Hard_Disk
hard_disk_new_arr = hard_disk.find_one(myquery5)


def check_compatibility(pro_name, pro):
    if pro_name == "motherboard":
        if (cpu_new_arr["socket"] == pro["socket"]) or (cpu_new_arr["socket"] in pro["socket"]) or (pro["socket"] in cpu_new_arr["socket"]):
            return True
        return False
    if pro_name == "ram":
        if (motherboard_new_arr["type"] == pro["type"]) or (motherboard_new_arr["type"] in pro["type"]) or (pro["type"] in motherboard_new_arr["type"]):
            return True
        return False
    if pro_name == "vga":
        # if (motherboard_arr["slot"] == pro["pci_slot"]) or (motherboard_arr["slot"] in pro["pci_slot"]) or (pro["pci_slot"] == motherboard_arr["slot"]):
        #     return True
        return True

def checkPrice(word):
    for x in word:
        if not x.isdigit():
            if x != ".":
                return False
    return True

if want_product == "cpu":
    for record in cpu.find().sort("ratings"):
        if record["price"] != "" and record["price"] != " ":
            x = checkPrice(record["price"])
            if x == True:
                if float(min_price) <= float(record['price']) and float(max_price) >= float(record["price"]):
                    if cpu_arr != record["_id"]:
                        y = check_compatibility(want_product, cpu_new_arr)
                        if y == True:
                            result = record
                            break

if want_product == "motherboard":

    for record in motherboard.find().sort("ratings"):
        if record["price"] != "" and record["price"] != " ":
            x = checkPrice(record["price"])
            y = checkPrice(min_price)
            if x == True and y == True:
                if float(min_price) <= float(record['price']) and float(max_price) >= float(record["price"]):
                    if motherboard_arr != record["_id"]:
                        y = check_compatibility(want_product, motherboard_new_arr)
                        if y == True:
                            result = record
                            break

if want_product == "ram":

    for record in ram.find().sort("ratings"):
        if record["price"] != "" and record["price"] != " ":
            x = checkPrice(record["price"])
            if x == True:
                if float(min_price) <= float(record['price']) and float(max_price) >= float(record["price"]):
                    if ram_arr != record["_id"]:
                        y = check_compatibility(want_product, ram_new_arr)
                        if y == True:
                            result = record
                            break

if want_product == "vga":

    for record in vga.find().sort("ratings"):
        if record["price"] != "" and record["price"] != " ":
            x = checkPrice(record["price"])
            if x == True:
                if float(min_price) <= float(record['price']) and float(max_price) >= float(record["price"]):
                    if vga_arr != record["_id"]:
                        y = check_compatibility(want_product, vga_new_arr)
                        if y == True:
                            result = record
                            break

if want_product == "hard_disk":

    for record in hard_disk.find().sort("ratings"):
        if record["price"] != "" and record["price"] != " ":
            x = checkPrice(record["price"])
            if x == True:
                if float(min_price) <= float(record['price']) and float(max_price) >= float(record["price"]):
                    if hard_disk_arr != record["_id"]:
                        result = record
                        break

print(result)
