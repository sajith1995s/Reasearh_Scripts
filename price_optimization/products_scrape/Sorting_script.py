
from pymongo import MongoClient

one = []
category = ""

client = MongoClient('mongodb://localhost:27017')
db = client.techRingdb

def sorting_algorithm(category, one):
    for ones in one:
        if category == "ram":
            ram = db.RAM
            count = 0
            for record in ram.find().sort("price", -1):
                if record["price"] < ones["price"]:
                    count = count + 1
                    continue
                elif record["price"] == ones["price"]:
                    count = count + 1
                    break
                else:
                    break
            for record in ram.find().sort("speed", -1):
                if record["speed"] < ones["speed"]:
                    count = count + 1
                    continue
                elif record["speed"] == ones["speed"]:
                    count = count + 1
                    break
                else:
                    break

        elif category == "vga":
            vga = db.VGA
            count = 0
            for record in vga.find().sort("price", -1):
                if record["price"] < ones["price"]:
                    count = count + 1
                    continue
                elif record["price"] == ones["price"]:
                    count = count + 1
                    break
                else:
                    break

            for record in vga.find().sort("speed", -1):
                if record["speed"] < ones["speed"]:
                    count = count + 1
                    continue
                elif record["speed"] == ones["speed"]:
                    count = count + 1
                    break
                else:
                    break

        elif category == "cpu":
            cpu = db.CPU
            count = 0
            for record in cpu.find().sort("price", -1):
                if record["price"] < ones["price"]:
                    count = count + 1
                    continue
                elif record["price"] == ones["price"]:
                    count = count + 1
                    break
                else:
                    break

            for record in cpu.find().sort("speed", -1):
                if record["speed"] < ones["speed"]:
                    count = count + 1
                    continue
                elif record["speed"] == ones["speed"]:
                    count = count + 1
                    break
                else:
                    break

        elif category == "motherboard":
            motherboard = db.Motherboard
            count = 0
            for record in motherboard.find().sort("price", -1):
                if record["price"] < ones["price"]:
                    count = count + 1
                    continue
                elif record["price"] == ones["price"]:
                    count = count + 1
                    break
                else:
                    break

            for record in motherboard.find().sort("speed", -1):
                if record["speed"] < ones["speed"]:
                    count = count + 1
                    continue
                elif record["speed"] == ones["speed"]:
                    count = count + 1
                    break
                else:
                    break

        elif category == "hard_disk":
            hard_disk = db.Hard_Disk
            count = 0
            for record in hard_disk.find().sort("price", -1):
                if record["price"] < ones["price"]:
                    count = count + 1
                    continue
                elif record["price"] == ones["price"]:
                    count = count + 1
                    break
                else:
                    break

            for record in hard_disk.find().sort("speed", -1):
                if record["speed"] < ones["speed"]:
                    count = count + 1
                    continue
                elif record["speed"] == ones["speed"]:
                    count = count + 1
                    break
                else:
                    break
    return count