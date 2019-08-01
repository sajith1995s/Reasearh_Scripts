import json
import sys
import subprocess

one = [{"id": "123456", "name": "one", "price": 10.00, "speed": 45},{"id": "456321", "name": "two", "price": 20.00, "speed": 2},{"id": "752369", "name": "three", "price": 5.00, "speed": 25}]
one_final = []

for ones in one:
    one_final.append({"id": ones["id"], "name": ones["name"], "price": ones["price"], "speed": ones["speed"], "points": 0})

# print(sorted(one_final, key=lambda i: i['price']))

count = 0
for item in sorted(one_final, key=lambda i: i['price']):
    count = count + 1
    item["points"] = item["points"] + count

count = 0
for item in sorted(one_final, key=lambda i: i['speed']):
    count = count + 1
    item["points"] = item["points"] + count

for item in one_final:
    ratings = subprocess.check_output([sys.executable, "test_fb.py", item["name"]])



print(sorted(one_final, key=lambda i: i['points']))

# s2_out = subprocess.check_output([sys.executable, "test_fb.py", ])
# print(s2_out)
