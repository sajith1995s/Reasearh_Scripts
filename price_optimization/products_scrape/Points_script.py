from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb


def sorting_algorithm(category, product):
    count = 0
    if category == "ram":
        if product["type"]:
            # DDR3 RAM
            if (product["type"].lower() in "ddr3") or ("ddr3" in product["type"].lower()):
                count = count + 2
                if product["size"]:
                    if 1 < product["size"] <= 2:
                        count = count + 1
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 2 < int(product["size"]) <= 4:
                        count = count + 3
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 4 < int(product["size"]) <= 8:
                        count = count + 5
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 8 < int(product["size"]) <= 16:
                        count = count + 8
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1

            # DDR4 RAM
            elif (product["type"].lower() in "ddr4") or ("ddr4" in product["type"].lower()):
                count = count + 5
                if product["size"]:
                    if 1 < product["size"] <= 2:
                        count = count + 1
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 2 < int(product["size"]) <= 4:
                        count = count + 3
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 4 < int(product["size"]) <= 8:
                        count = count + 5
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 8 < int(product["size"]) <= 16:
                        count = count + 8
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1

            # DDR2 RAM
            elif (product["type"].lower() in "ddr2") or ("ddr2" in product["type"].lower()):
                count = count + 1
                if product["size"]:
                    if 1 < product["size"] <= 2:
                        count = count + 1
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 2 < product["size"] <= 4:
                        count = count + 3
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 4 < product["size"] <= 8:
                        count = count + 5
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 8 < product["size"] <= 16:
                        count = count + 8
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1

            # DDR1 RAM
            elif (product["type"].lower() in "ddr1") or ("ddr1" in product["type"].lower()):
                count = count + 1
                if product["size"]:
                    if 1 < product["size"] <= 2:
                        count = count + 1
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 2 < product["size"] <= 4:
                        count = count + 3
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 4 < product["size"] <= 8:
                        count = count + 5
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 8 < product["size"] <= 16:
                        count = count + 8
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1

        elif product["size"]:
            if 1 < product["size"] <= 2:
                count = count + 1
                if product["price"]:
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1
            elif 2 < product["size"] <= 4:
                count = count + 3
                if product["price"]:
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1
            elif 4 < product["size"] <= 8:
                count = count + 5
                if product["price"]:
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1
            elif 8 < product["size"] <= 16:
                count = count + 8
                if product["price"]:
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1

        if product["price"]:
            if float(product["price"]) <= 1500.00:
                count = count + 1
            elif 1500.00 < float(product["price"]) <= 3500.00:
                count = count + 2
            elif 3500.00 < float(product["price"]) <= 5000.00:
                count = count + 1


    ## VGA ##
    elif category == "vga":
        if product["name"]:
            if "nvidia" in product["name"].lower() or "gtx" in product["name"].lower() or "geforce" in product["name"].lower():
                if product["size"]:
                    if 1 < product["size"] <= 2:
                        count = count + 1
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 2 < int(product["size"]) <= 4:
                        count = count + 3
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 4 < int(product["size"]) <= 8:
                        count = count + 5
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 8 < product["size"] <= 16:
                        count = count + 8
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                else:
                    if product["price"]:
                        if float(product["price"]) <= 1500.00:
                            count = count + 1
                        elif 1500.00 < float(product["price"]) <= 3500.00:
                            count = count + 2
                        elif 3500.00 < float(product["price"]) <= 5000.00:
                            count = count + 1

            elif "amd" in product["name"].lower():
                if product["size"]:
                    if 1 < product["size"] <= 2:
                        count = count + 1
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 2 < int(product["size"]) <= 4:
                        count = count + 3
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 4 < int(product["size"]) <= 8:
                        count = count + 5
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 8 < product["size"] <= 16:
                        count = count + 8
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                else:
                    if product["price"]:
                        if float(product["price"]) <= 1500.00:
                            count = count + 1
                        elif 1500.00 < float(product["price"]) <= 3500.00:
                            count = count + 2
                        elif 3500.00 < float(product["price"]) <= 5000.00:
                            count = count + 1

            else:
                if product["size"]:
                    if 1 < product["size"] <= 2:
                        count = count + 1
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 2 < int(product["size"]) <= 4:
                        count = count + 3
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 4 < int(product["size"]) <= 8:
                        count = count + 5
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                    elif 8 < product["size"] <= 16:
                        count = count + 8
                        if product["price"]:
                            if float(product["price"]) <= 1500.00:
                                count = count + 1
                            elif 1500.00 < float(product["price"]) <= 3500.00:
                                count = count + 2
                            elif 3500.00 < float(product["price"]) <= 5000.00:
                                count = count + 1
                else:
                    if product["price"]:
                        if float(product["price"]) <= 1500.00:
                            count = count + 1
                        elif 1500.00 < float(product["price"]) <= 3500.00:
                            count = count + 2
                        elif 3500.00 < float(product["price"]) <= 5000.00:
                            count = count + 1


    ## CPU ##
    elif category == "cpu":
        if product["name"]:
            if "xeon" in product["name"].lower():
                count = count + 1
                if product["price"]:
                    count = count + 1
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1
            else:
                if product["price"]:
                    count = count + 1
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1


    ## Motherboard ##
    elif category == "motherboard":
        if product["model"]:
            if "asus" in product["model"].lower():
                count = count + 1
        if product["price"]:
            if float(product["price"]) <= 1500.00:
                count = count + 1
            elif 1500.00 < float(product["price"]) <= 3500.00:
                count = count + 2
            elif 3500.00 < float(product["price"]) <= 5000.00:
                count = count + 1


    ## Hard Disk ##
    elif category == "hard_disk":
        if product["size"]:
            if 1 < product["size"] <= 2:
                count = count + 1
                if product["price"]:
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1
            elif 2 < product["size"] <= 4:
                count = count + 3
                if product["price"]:
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1
            elif 4 < product["size"] <= 8:
                count = count + 5
                if product["price"]:
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1
            elif 8 < product["size"] <= 16:
                count = count + 8
                if product["price"]:
                    if float(product["price"]) <= 1500.00:
                        count = count + 1
                    elif 1500.00 < float(product["price"]) <= 3500.00:
                        count = count + 2
                    elif 3500.00 < float(product["price"]) <= 5000.00:
                        count = count + 1
        else:
            if product["price"]:
                if float(product["price"]) <= 1500.00:
                    count = count + 1
                elif 1500.00 < float(product["price"]) <= 3500.00:
                    count = count + 2
                elif 3500.00 < float(product["price"]) <= 5000.00:
                    count = count + 1

    return count
