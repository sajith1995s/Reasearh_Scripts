# from bson import ObjectId
# from pymongo import MongoClient
#
# client = MongoClient('mongodb://localhost:27017')
# db = client.techRingdb
#
# cpu = db.CPU
#
# cpu_pro = cpu.find_one({"_id": ObjectId("5d958c01c9c71f8444c31118")})
#
# print(cpu_pro)

size = "2Gb, 4GB, 100GB"

a = size.split("/")
b = size.split(",")
c = size.split(" ")
if a.__len__() > 1:
    for x in a:
        x = x.strip(" ").strip(",")
        if "1" <= x <= "5":
            print("if a ".x)
elif b.__len__() > 1:
    for x in b:
        x = x.strip(" ").strip(",")
        if "1" <= x <= "5":
            print("elif b "+x)
elif c.__len__() > 1:
    for x in c:
        x = x.strip(" ").strip(",")
        if "1" <= x <= "5":
            print("elif c ".x)
else:
    size = size.strip(" ").strip(",")
    if "1" <=size  <= "5":
        print("else".size)
