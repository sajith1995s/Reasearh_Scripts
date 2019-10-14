import csv

result = []
predicted = []

# Change product Algorithm
def algorithm(want_product, motherboard_pro, cpu_pro, ram_pro, vga_pro, hard_disk_pro, min_price, max_price):
    products = []
    with open('csv/products.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] == want_product:
                if row[0] == "motherboard":
                    list = {"name": row[1], "size": row[2], "price": row[3], "type": row[4], "warranty": row[5], "image": row[6], "owner": row[7], "cpu_brand": row[8],"model": row[9], "user_rating": row[10]}
                    if min_price <= list["price"] and max_price >= list["price"]:
                        products.append(list)
                elif row[0] == "cpu":
                    list = {"name": row[1], "size": row[2], "price": row[3], "warranty": row[4], "image": row[5], "owner": row[6], "model": row[7], "socket": row[8], "speed": row[9], "proccessor_type": row[10], "user_rating": row[11]}
                    if min_price <= list["price"] and max_price >= list["price"]:
                        products.append(list)
                elif row[0] == "ram":
                    list = {"name": row[1], "size": row[2], "price": row[3], "type": row[4], "warranty": row[5], "image": row[6], "owner": row[7], "model": row[8], "user_rating": row[9]}
                    if min_price <= list["price"] and max_price >= list["price"]:
                        products.append(list)
                elif row[0] == "vga":
                    list = {"name": row[1], "size": row[2], "price": row[3], "type": row[4], "warranty": row[5], "image": row[6], "owner": row[7], "chipset": row[8], "capacity": row[9], "user_rating": row[10]}
                    if min_price <= list["price"] and max_price >= list["price"]:
                        products.append(list)
                elif row[0] == "hard_disk":
                    list = {"name": row[1], "size": row[2], "price": row[3], "warranty": row[4], "image": row[5], "owner": row[6], "user_rating": row[7]}
                    if min_price <= list["price"] and max_price >= list["price"]:
                        products.append(list)
    if want_product == "motherboard":
        for pro in products:
            if (pro["cpu_brand"] in cpu_pro["socket"]) or (cpu_pro["socket"] in pro["cpu_brand"]):
                if pro["memory_type"] == ram_pro["type"]:
                    if pro["pci_slot"] == vga_pro["slot"]:
                        result.append(pro)
    elif want_product == "cpu":
        for pro in products:
            if (pro["socket"] in motherboard_pro["cpu_brand"]) or (motherboard_pro["cpu_brand"] in pro["socket"]):
                result.append(pro)
    elif want_product == "ram":
        for pro in products:
            if (pro["type"] in motherboard_pro["memory_type"]) or (motherboard_pro["memory_type"] in pro["type"]):
                result.append(pro)
    elif want_product == "ram":
        for pro in products:
            if (pro["slot"] in motherboard_pro["pci_slot"]) or (motherboard_pro["pci_slot"] in pro["slot"]):
                result.append(pro)

with open('csv/test_change_product.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    want_product = ''
    for row in readCSV:
        if row[0] == "motherboard":
            col_motherboard = {"name": row[1], "size": row[2], "price": row[3], "type": row[4], "warranty": row[5], "image": row[6], "owner": row[7], "cpu_brand": row[8], "model": row[9], "user_rating": row[10]}
        elif row[0] == "cpu":
            col_cpu = {"name": row[1], "size": row[2], "price": row[3], "warranty": row[4], "image": row[5], "owner": row[6], "model": row[7], "socket": row[8], "speed": row[9], "proccessor_type": row[10], "user_rating": row[11]}
        elif row[0] == "ram":
            col_ram = {"name": row[1], "size": row[2], "price": row[3], "type": row[4], "warranty": row[5], "image": row[6], "owner": row[7], "model": row[8], "user_rating": row[9]}
        elif row[0] == "vga":
            col_vga = {"name": row[1], "size": row[2], "price": row[3], "type": row[4], "warranty": row[5], "image": row[6], "owner": row[7], "chipset": row[8], "capacity": row[9], "user_rating": row[10]}
        elif row[0] == "hard_disk":
            col_hard_disk = {"name": row[1], "size": row[2], "price": row[3], "warranty": row[4], "image": row[5], "owner": row[6], "user_rating": row[7]}
        elif row[0] == "want_product":
            want_product = row[1]
            min_price = row[2]
            max_price = row[3]
            algorithm(want_product, col_motherboard, col_cpu, col_ram, col_vga, col_hard_disk, min_price, max_price)

with open('csv/real_change_product.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        predicted.append(row)

i = 0
correct = 0
incorrect = 0
for res in result:
    if res["category"] == "motherboard":
        if res["name"] == predicted[i][0] and res["size"] == predicted[i][1] and res["price"] == predicted[i][2] and res["type"] == predicted[i][3] and res["warranty"] == predicted[i][4] and res["image"] == predicted[i][5] and res["owner"] == predicted[i][6] and res["cpu_brand"] == predicted[i][7] and res["model"] == predicted[i][8] and res["user_rating"] == predicted[i][9]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
    elif res["category"] == "cpu":
        if res["name"] == predicted[i][0] and res["size"] == predicted[i][1] and res["price"] == predicted[i][2] and res["warranty"] == predicted[i][3] and res["image"] == predicted[i][4] and res["owner"] == predicted[i][5] and res["model"] == predicted[i][6] and res["socket"] == predicted[i][7] and res["speed"] == predicted[i][8] and res["proccessor_type"] == predicted[i][9] and res["user_rating"] == predicted[i][10]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
    elif res["category"] == "ram":
        if res["name"] == predicted[i][0] and res["size"] == predicted[i][1] and res["price"] == predicted[i][2] and res["type"] == predicted[i][3] and res["warranty"] == predicted[i][4] and res["image"] == predicted[i][5] and res["owner"] == predicted[i][6] and res["model"] == predicted[i][7] and res["user_rating"] == predicted[i][8]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
    elif res["category"] == "vga":
        if res["name"] == predicted[i][0] and res["size"] == predicted[i][1] and res["price"] == predicted[i][2] and res["type"] == predicted[i][3] and res["warranty"] == predicted[i][4] and res["image"] == predicted[i][5] and res["owner"] == predicted[i][6] and res["chipset"] == predicted[i][7] and res["capacity"] == predicted[i][8] and res["user_rating"] == predicted[i][9]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
    elif res["category"] == "hard_disk":
        if res["name"] == predicted[i][0] and res["size"] == predicted[i][1] and res["price"] == predicted[i][2] and res["warranty"] == predicted[i][3] and res["image"] == predicted[i][4] and res["owner"] == predicted[i][5] and res["user_rating"] == predicted[i][6]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
    i = i + 1

accuracy = (correct / (correct + incorrect)) * 100

print("Accuracy Level = " + accuracy)



