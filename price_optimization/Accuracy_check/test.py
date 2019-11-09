import csv

build_sequence_plans = []

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

with open('csv/test_build_sequence.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        price_min = row[0]
        price_max = row[1]
        ram_min = price_min * (10 / 100)
        ram_max = price_max * (10 / 100)
        motherboard_min = price_min * (30 / 100)
        motherboard_max = price_max * (30 / 100)
        vga_min = price_min * (20 / 100)
        vga_max = price_max * (20 / 100)
        cpu_min = price_min * (20 / 100)
        cpu_max = price_max * (20 / 100)
        hard_disk_min = price_min * (20 / 100)
        hard_disk_max = price_max * (20 / 100)

        cpu_arr = []
        motherboard_arr = []
        ram_arr = []
        vga_arr = []
        hard_disk_arr = []