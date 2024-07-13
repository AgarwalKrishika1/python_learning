#if
#if - else
#if - elif - else
#nested if - else

print("if statement")
num = 6
if num > 0:
    print(num *  num)
print("end of if")

print("if - else statement")
num = input("enter number ")
if num > str(0) or num == str(0):
    print("its positive")
else:
    print("its negative")

print("if-elif-else statement")
num = input("enter number ")
if num > str(0):
    print("its positive")
elif num == str(0):
    print("its zero")
else:
    print("its negative")

print("nested if-else")
i = 0
j = 5
if i <= j:
    if j < 6:
        print(i)
    else:
        print(j)
else:
    print("else")