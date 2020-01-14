import random


print('This is an interactive guessing game!')
print('You have to enter a number between 1 and 99 to find out the secret number.')
print("Type 'exit' to end the game.\nGood luck!")

x = random.randrange(1, 100, 1)
exit = 0
while exit == 0:
    i = input("What's your guess between 1 and 99?\n")
    if (i == str(x) or i == 'exit'):
        exit = 1
    elif not i.isdigit():
        print("That's not a number.")
    elif int(i) > x:
        print('Too high!')
    elif int(i) < x:
        print('Too low!')
