import random

def guess(x):
    random_number = random.randint(1, x)
    count = 0
    while count < 3:
        count  += 1
        #f-string to add variable in statement
        guess = int(input(f'Guess number between 1 and {x}  '))
        if guess == random_number:
            print("you got it ")
            break
        elif guess < random_number:
            print("guess another , too low")
        elif guess > random_number:
            print("too high")
    #if count > 3:
            #print("End Of Game")
            #print("You Lost")
y = int(input("enter number for guess "))
guess(y)

print("\n\n")
print("computer guess game")
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'{guess} too high(H), too low(L), or correct(C)'.lower())
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'yay! coorect {guess}')
y = int(input("enter number for guess "))
computer_guess(y)