thisdict={
    "brand": "Ford",
    "year": 2023
}
print('index',thisdict['year'])
print('whole',thisdict)
print('length',len(thisdict))
print('type',type(thisdict))
#constructor
thisdict1 =  dict(name = "Krishika", age = 20, country = "India")
print(thisdict1)
#getMethod
x = thisdict1.get("name")
print(x)

#keys()
x = thisdict1.keys()
#change values
thisdict1["city"] = "Rajkot"
print(x)

#values()
x=thisdict1.values()
print(x)

#items()
x=thisdict1.items()
print(x)

if "name" in thisdict1:
    print("yes, 'name' there")
else:
    print("not there")

#update()
thisdict1.update({"city": "Ahmedabad"})
print(thisdict1)

#remove
thisdict1.popitem()
print(thisdict1)

thisdict1.pop("name")
print(thisdict1)

del thisdict1["age"] #can delete whole dict
print(thisdict1)

#empty dict
thisdict1.clear()
print(thisdict1)

thisdict1.update({"name": "krishu", "age":20})
print(thisdict1)

#loops
for x in thisdict1.values():
    print(x)
for x in thisdict1.keys():
    print(x)
for x,y in thisdict1.items():
    print(x,y)

#copy
#dict2=dict1 can't

mydict=thisdict1.copy()
print(mydict)

#not change if update in previous
thisdict1.update({"name": "abc"})
print(mydict)

mydict = dict(thisdict1)
print(mydict)

#nested dict
dict1 ={
    "name": "abc",
    "age": 21
}
dict2 ={
    "name": "cde",
    "age": 21
}
dict3 ={
    "name": "efg",

    "age":21
}
fam ={
    "dict1" :  dict1,
    "dict2" :  dict2,
    "dict3" :  dict3
}
print(fam)
print('nested dict 3 age',fam["dict3"]["age"])

#fromkeys uses to create multiple dict with same values to each dict
x= fam.fromkeys("age", 21)
print(x)
print(fam)
