from pymongo import MongoClient
import sys

ram_arr = []
vga_arr = []
cpu_arr = []
motherboard_arr = []
hard_disk_arr = []

build_arr = []
build_arr2 = []

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb

vga = db.VGA
i = 0
for record in vga.find():
    if i==0:
        build_arr2.append("vga")
        build_arr2.append(record)
    elif i==1:
        build_arr.append("vga")
        build_arr.append(record)
    i=i+1

cpu = db.CPU
i = 0
for record in cpu.find():
    if i==0:
        build_arr2.append("cpu")
        build_arr2.append(record)
    elif i==1:
        build_arr.append("cpu")
        build_arr.append(record)
    i = i + 1

ram = db.RAM
i = 0
for record in ram.find():
    if i==0:
        build_arr2.append("ram")
        build_arr2.append(record)
    elif i==1:
        build_arr.append("ram")
        build_arr.append(record)
    i = i + 1

motherboard = db.Motherboard
i = 0
for record in motherboard.find():
    if i==0:
        build_arr2.append("motherboard")
        build_arr2.append(record)
    elif i==1:
        build_arr.append("motherboard")
        build_arr.append(record)
    i = i + 1

hard_disk = db.Hard_Disk
i = 0
for record in hard_disk.find():
    if i==0:
        build_arr2.append("hard_disk")
        build_arr2.append(record)
    elif i==1:
        build_arr.append("hard_disk")
        build_arr.append(record)
    i = i + 1

for x in build_arr:
    print(x)

for y in build_arr2:
    print(y)

