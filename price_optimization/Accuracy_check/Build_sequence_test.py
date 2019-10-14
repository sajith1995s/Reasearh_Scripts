price_min = 0
price_max = 0
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
    elif category == "hard_disk":
        build_arr.append("hard_disk")
        for item in lists:
            build_arr.append(item)
            break

# cpu
build_sequence(cpu_arr, "cpu")

# motherboard
build_sequence(motherboard_arr, "motherboard")

# ram
build_sequence(ram_arr, "ram")

# vga
build_sequence(vga_arr, "vga")

# hard disk
build_sequence(vga_arr, "hard_disk")

#
# Compare the results
#
