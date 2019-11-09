import csv

build_sequence_plans = []
predicted = []

def check_compatibility(pro_name, motherboard, pro):
    if pro_name == "cpu":
        if (motherboard["cpu_brand"] in pro["socket"]) or (pro["socket"] in motherboard["cpu_brand"]):
            return True
        else:
            return False
    elif pro_name == "ram":
        if (motherboard["memory_type"] in pro["type"]) or (pro["type"] in motherboard["memory_type"]):
            return True
        else:
            return False
    elif pro_name == "vga":
        if (motherboard["pci_slot"] in pro["slot"]) or (pro["slot"] in motherboard["pci_slot"]):
            return True
        else:
            return False

def build_sequence(motherboard_arr, cpu_arr, ram_arr, vga_arr, hard_disk_arr):
    for motherboard in motherboard_arr:
        for cpu in cpu_arr:
            x = check_compatibility("cpu", motherboard, cpu)
            if x == True:
                for ram in ram_arr:
                    x = check_compatibility("ram", motherboard, ram)
                    if x == True:
                        for vga in vga_arr:
                            x = check_compatibility("vga", motherboard, vga)
                            if x == True:
                                for hard_disk in hard_disk_arr:
                                    build_sequence_plans.append(motherboard, cpu, ram, vga, hard_disk)
                                    return
    return

with open('csv/test_price_range.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        ram_min = row[0]
        ram_max = row[1]
        motherboard_min = row[2]
        motherboard_max = row[3]
        vga_min = row[4]
        vga_max = row[5]
        cpu_min = row[6]
        cpu_max = row[7]
        hard_disk_min = row[8]
        hard_disk_max = row[9]

        cpu_arr = []
        motherboard_arr = []
        ram_arr = []
        vga_arr = []
        hard_disk_arr = []

        with open('csv/products_price_range.csv') as csvfile1:
            readCSV1 = csv.reader(csvfile1, delimiter=',')
            for row1 in readCSV1:
                if row1[0] == "motherboard":
                    if motherboard_min <= float(row1[3]) and motherboard_max >= float(row1[3]):
                        motherboard_arr.append(row1)
                elif row1[0] == "cpu":
                    if cpu_min <= float(row1[3]) and cpu_max >= float(row1[3]):
                        cpu_arr.append(row1)
                elif row1[0] == "ram":
                    if ram_min <= float(row1[3]) and ram_max >= float(row1[3]):
                        ram_arr.append(row1)
                elif row1[0] == "vga":
                    if vga_min <= float(row1[3]) and vga_max >= float(row1[3]):
                        vga_arr.append(row1)
                elif row1[0] == "hard_disk":
                    if hard_disk_min <= float(row1[3]) and hard_disk_max >= float(row1[3]):
                        hard_disk_arr.append(row1)
                elif row1[0] == "-":
                    build_sequence(cpu_arr, motherboard_arr, ram_arr, vga_arr, hard_disk_arr)
                    cpu_arr = []
                    motherboard_arr = []
                    ram_arr = []
                    vga_arr = []
                    hard_disk_arr = []


with open('csv/real_change_product.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        predicted.append(row)


i = 0
correct = 0
incorrect = 0
for res in build_sequence_plans:
    i = i + 1