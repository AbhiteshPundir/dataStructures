dict1={"Name": "Abhitesh","Course": "B.Tech","roll no.": 5,"section": "x"}

# copy() copy method
x = dict1.copy()
print("copied dicitonary:",x, end='\n')

# fromkeys() method
y ={"k1","k2","k3"}
z =dict.fromkeys(y,1)
print(z, end='\n')

# get() method
a= dict1.get("Name")
print(a, end='\n')

# items() method
a1=dict1.items()
print(a1, end='\n')

# keys() method
a2=dict1.keys()
print(a2, end='\n')

# pop() method
dict1.pop("section")
print("after popping 1 element:",dict1, end='\n')

# popitem() method
dict1.popitem()
print("after removing the last added element:",dict1, end='\n')

# setdefault() method
dict1.setdefault("College", "GEU")
print(dict1, end='\n')

# update() method
dict1.update({"sem": 2})
print("After updation:",dict1, end='\n')

# values() method
a3=dict1.values()
print("the values are:",a3, end='\n')

# clear() method
print("clearing the dictionary:", end='\n')
dict1.clear()
print("After clearing:",dict1, end='\n')
