birth_year= input("birthyear: ")
age= 2023 - int( birth_year)
print(age)


#float()
#bool()
#str()
#int()


first=input("first:")
second=input("second:")
sum= float(first)+float(second)
print(sum)

def  hello(name):
    print("hello  " + name)
hello("beautiful")

def hello(name=" my frnd"):
    print("hello hows u "+name)
hello()
hello(" k")

def change(value):
    value["name"] = "kkkk"

val ={"name": "b"}
change(val)
print(val)

def function(name):
    if not name:
        return
    print("hello  "+ name)

function("")

#to return something complusory add it with return 