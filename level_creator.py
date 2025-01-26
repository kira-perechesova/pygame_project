import json

print("type level name which you want to edit or type name for a new level")
level_name = input()
try:
    f = open("levels/" + level_name + ".json")
    data = json.load(f)
    f.close()
except FileNotFoundError:
    f = open("levels/" + level_name + ".json", "a")
    f.close()
    data = {}
    data["platforms"] = []

f = open("levels/" + level_name + ".json", "w")
print("write coords of a platform you want to add, width and height")
print("example: 0 0 1 1")
print("one platform will appear in 0 0")
print("example 2: 10 10 2 2")
print("four platforms will appear in 10 10, 40 10, 10 40, 40 40")
print("write stop to stop editing and save changes")
k = input()
while k != "stop":
    x, y, width, height = k.split()
    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    for i in range(0, width):
        for j in range(0, height):
            a = dict()
            a["x"] = x + i * 30
            a["y"] = y + j * 30
            data["platforms"].append(a)
    k = input()

f.write(json.dumps(data))
f.close()

print('according to the above instructions, enter the coordinates for the coins')
print('no need to enter the level name')
print('write stop to stop editing and save changes')
try:
    f = open("levels_coins/" + level_name + ".json")
    data = json.load(f)
    f.close()
except FileNotFoundError:
    f = open("levels_coins/" + level_name + ".json", "a")
    f.close()
    data = {}
    data["platforms"] = []
f = open("levels_coins/" + level_name + ".json", "w")
k = input()
while k != "stop":
    x, y, width, height = k.split()
    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    for i in range(0, width):
        for j in range(0, height):
            a = dict()
            a["x"] = x + i * 30
            a["y"] = y + j * 30
            data["platforms"].append(a)
    k = input()

f.write(json.dumps(data))
f.close()