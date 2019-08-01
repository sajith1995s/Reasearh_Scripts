from pymongo import MongoClient

price_min = 15000.00
price_max = 85000.00
price_range = price_max - price_min
ram_perc = price_range * (10/100)
motherboard_perc = price_range * (30/100)
vga_perc = price_range * (20/100)
cpu_perc = price_range * (20/100)
hard_disk_perc = price_range * (20/100)

ram_arr = []
final_ram_arr = []
vga_arr = []
final_vga_arr = []
cpu_arr = []
final_cpu_arr = []
motherboard_arr = []
final_motherboard_arr = []
hard_disk_arr = []
final_hard_disk_arr = []

client = MongoClient('mongodb://localhost:27017')
db = client.research

def markingProducts(lists, category):
    if category == "ram":
        final_ram_arr.append(lists)
    elif category == "vga":
        final_vga_arr.append(lists)
    elif category == "cpu":
        final_cpu_arr.append(lists)
    elif category == "motherboard":
        final_motherboard_arr.append(lists)
    elif category == "hard_disk":
        final_hard_disk_arr.append(lists)

ram = db.RAM
for record in ram.find():
    if ram_perc <= float(record['price']):
        ram_arr.append(record)
        markingProducts(ram_arr, "ram")

vga = db.VGA
for record in vga.find():
    if vga_perc <= record['price']:
        vga_arr.append(record)
        markingProducts(vga_arr, "vga")

motherboard = db.motherboard
for record in motherboard.find():
    if motherboard_perc <= record['price']:
        motherboard_arr.append(record)
        markingProducts(motherboard_arr, "motherboard")

cpu = db.CPU
for record in cpu.find():
    if cpu_perc <= record['price']:
        cpu_arr.append(record)
        markingProducts(cpu_arr, "cpu")

cpu = db.Hard_disk
for record in cpu.find():
    if cpu_perc <= record['price']:
        hard_disk_arr.append(record)
        markingProducts(hard_disk_arr, "hard_disk")

print(final_ram_arr)
print(final_vga_arr)
print(final_cpu_arr)
print(final_motherboard_arr)
print(final_hard_disk_arr)






