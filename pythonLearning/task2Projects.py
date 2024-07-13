#pattern
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
i = 1
num = 6
for num in range(1,num, 1):
    for i in range(1, num+1):
        print(i, end=' ')

    print("")
print("done")


#sum
num = int(input("Enter terms of number to be sumed "))
sum = 0
for i in range(1, num+1, 1):
    sum = sum + i
print(sum ,'sum')
print("done")

#table
num = int(input("Enter number for which multiplication you need"))
for i in range(1, num, 1):
    product = num * i
    print(product)
print('done')

#count digits
num = int(input('enter number '))
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("digits", count)

#prime number
start = int(input("enter start number"))
end = int(input("enter end number"))
print("Prime number between ", start, "and", end, "are: ")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


#factorial
num = int(input("enter number to calc factorial "))
factorial = 1
if num  < 0:
    print("no factorial exists")
elif num == 0:
    print('factorial of 0 is 1')
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("factorial is ", factorial)
















