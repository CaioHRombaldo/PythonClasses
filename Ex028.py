from random import randint
from time import sleep

answer = int(input('* Computer sound * Im thinking of a number from 1 to 5, try to guess: '))
rand = randint(1, 5)
print('PROCESSING...')
sleep(2)

if answer == rand:
    print('Congratulations, I dont know how you did it, but you got it right!')
else:
    print('It was not this time my friend, machines 1 x 0 human.')

print('The number I was thinking about was: {}.'.format(rand))
