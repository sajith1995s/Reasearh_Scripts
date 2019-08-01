import json
import sys
import subprocess

one = []
one_final = []
category = ""

for ones in one:
    if category == "ram":
        one_final.append({"name": ones["name"], "price": ones["price"], "type": ones["type"], "size": ones["size"], "points": 0})
        count = 0
        for item in sorted(one_final, key=lambda i: i['price']):
            count = count + 1
            item["points"] = item["points"] + count

        count = 0
        for item in sorted(one_final, key=lambda i: i['speed']):
            count = count + 1
            item["points"] = item["points"] + count
    elif category == "vga":
        one_final.append({"name": ones["name"], "price": ones["price"], "chipset": ones["chipset"], "type": ones["type"], "size": ones["size"], "points": 0})
        count = 0
        for item in sorted(one_final, key=lambda i: i['price']):
            count = count + 1
            item["points"] = item["points"] + count

        count = 0
        for item in sorted(one_final, key=lambda i: i['speed']):
            count = count + 1
            item["points"] = item["points"] + count
    elif category == "cpu":
        one_final.append({"name": ones["name"], "price": ones["price"], "proccessor_type": ones["proccessor_type"], "speed": ones["speed"], "size": ones["size"], "points": 0})
        count = 0
        for item in sorted(one_final, key=lambda i: i['price']):
            count = count + 1
            item["points"] = item["points"] + count

        count = 0
        for item in sorted(one_final, key=lambda i: i['speed']):
            count = count + 1
            item["points"] = item["points"] + count
    elif category == "motherboard":
        one_final.append({"name": ones["name"], "price": ones["price"], "type": ones["type"], "size": ones["size"], "points": 0})
        count = 0
        for item in sorted(one_final, key=lambda i: i['price']):
            count = count + 1
            item["points"] = item["points"] + count

        count = 0
        for item in sorted(one_final, key=lambda i: i['speed']):
            count = count + 1
            item["points"] = item["points"] + count
    elif category == "hard_disk":
        one_final.append({"name": ones["name"], "price": ones["price"], "size": ones["size"], "points": 0})
        count = 0
        for item in sorted(one_final, key=lambda i: i['price']):
            count = count + 1
            item["points"] = item["points"] + count

        count = 0
        for item in sorted(one_final, key=lambda i: i['speed']):
            count = count + 1
            item["points"] = item["points"] + count

print(sorted(one_final, key=lambda i: i['points']))