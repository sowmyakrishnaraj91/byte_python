number = 19
condition = True

while condition:
    guess = int(input('Enter an int:'))

    if guess == number:
        print('Spot on')
        condition = False

    elif guess < number:
        print('A little higher')

    else:
        print('A öittle lower')

else:
    print('game over')

