# dictionary
d = {"Tom" : 4568791, "Rob" : 7895323, "Joe": 54542126}
print(d)
print(d["Tom"]) #using the key
d["Sam"] = 54548789
print(d)
del d["Sam"]
print(d)

for key in d:
    print("Key:", key, "value:",d[key])
    
for k, v in d.items():
    print("Key", key, "value:",v)
    
print("Tom" in d)
d.clear()
print(d)


# Tuples
point = (5,9)
print(point[0])
print(point[1])

