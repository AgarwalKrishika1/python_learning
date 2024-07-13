class Person:
    def __init__(self, name):
        self.name = name

    def method1(self):
        print("Hi, my name is ", self.name)


p = Person('Krishika')
p.method1()
print("\n")
print("scope test:")
#scope
#Global(globally)      Non-local(in scope)        Local(to instant)


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

print('\n\n')


class Dog:
    #defining here creates only 1 instance
    trick = []

    def __init__(self, name):
        self.name = name
        #this creates instatnce for each call
        self.trick = []

    def add_trick(self, trick):
        self.trick.append(trick)


d = Dog('abc')
e = Dog('def')
d.add_trick('pull')
e.add_trick('push')
print(d.trick)
print(e.trick)

print('\n\n')
#same instance with different values


class A:
    purpose = 'learn'
    language = 'python'


a1 = A()
print(a1.purpose,  a1.language)
a2 = A()
a2.language = 'Java'
print(a2.purpose,  a2.language)

print('\n\n')


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,  self.lastname)


print("using parent class")
x = Person('Krishika', 'Agarwal')
x.printname()


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        print(self.firstname, self.lastname, 'graduation year', self.graduationyear)


print("using student class")
y = Student('Student', 'abc', 2025)
y.printname()

print('\n\n', 'iterators')


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 4:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)

