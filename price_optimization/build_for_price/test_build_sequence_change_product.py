from pymongo import MongoClient
import sys

want_product = "ram"
price_min = 0.00

motherboard = ''
cpu = ''
ram = ''
vga = ''
hard_disk = ''

res = []

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb

if want_product == "ram":
    col_ram = db.RAM
    ram_pro = col_ram.find()
    for x in ram_pro:
        if x["_id"] != ram:
            res.append(x)
            break

if want_product == "vga":
    col_vga = db.VGA
    vga_pro = col_vga.find()
    for x in vga_pro:
        if x["_id"] != vga:
            res.append(x)
            break

if want_product == "cpu":
    col_cpu = db.CPU
    cpu_pro = col_cpu.find()
    for x in cpu_pro:
        if x["_id"] != cpu:
            res.append(x)
            break

if want_product == "motherboard":
    col_motherboard = db.Motherboard
    motherboard_pro = col_motherboard.find()
    for x in motherboard_pro:
        if x["_id"] != motherboard:
            res.append(x)
            break

if want_product == "hard_disk":
    col_hard = db.Hard_Disk
    hard_pro = col_hard.find()
    for x in hard_pro:
        if x["_id"] != hard_disk:
            res.append(x)
            break

for x in res:
    print(x)

