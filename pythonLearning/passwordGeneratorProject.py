import random

print("Password Generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('amount of password to generate: ')
number = int(number)

length = input('input length of password: ')
length = int(length)

print("\nhere are the passwords:  ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)