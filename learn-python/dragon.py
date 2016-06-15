import random
import time

# In this game, the player is in a land full of dragons. The dragons all live in caves with their large
# piles of collected treasure. Some dragons are friendly and share their treasure with you. Other
# dragons are hungry and eat anyone who enters their cave. The player is in front of two caves, one
# with a friendly dragon and the other with a hungry dragon. The player must choose between the
# two.

def print_intro():
    print('You are in a land full of dragons. In front of you,'+
          '\nyou see two caves. In one cave, the dragon is friendly'+
          '\nand will share his treasure with you. The other dragon'+
          '\nis greedy and hungry, and will eat you on sight.')

def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def enter_cave(cave_number):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    if cave_number == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbels you down in one bite!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    print_intro()
    cave_number = choose_cave()
    enter_cave(cave_number)
    print('Do you want to play again? (yes or no)')
    playAgain = input()



