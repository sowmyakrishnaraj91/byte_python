number = 19

guess = int(input('Enter an int:'))

if guess == number:
    print('Spot on')

elif guess < number:
    print('A little higher')

else:
    print('A öittle lower')

print('Done')