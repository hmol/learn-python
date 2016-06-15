import random

print('What is your name?')
name = input()
number = random.randint(0,100)

print('Well, ' + name + ', I am thinking of a number between 0 and 100')

guess = -1
tries = 0

while True:
    tries += 1
    print('Take a guess')
    guess = int(input())

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

print('Congratulations, {}, you guessed correct after {} tries :)'.format(name, tries))