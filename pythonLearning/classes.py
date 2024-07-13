#Classes
class animal:
    def walk(self):
        print("walking")
class Dog(animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger ", 8)

print(roger.age)
print(roger.name)
print(roger.bark())
roger.bark()
roger.walk()