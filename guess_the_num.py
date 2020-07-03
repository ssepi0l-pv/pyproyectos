#!/usr/bin/env python3

import random

madeattempts = 0

print('Hey, what\'s your name?')
name = input('> ')

rand_num = random.randint(1, 10)
print('Well, ' + name + ', i\'m thinking of a number between 1 and 10. Try to guess it!')

while madeattempts <  6:
    print('Try it!')
    esti = int(input())

    madeattempts = madeattempts + 1

    if esti < rand_num:
        print('Your guess is too low!')
    if esti > rand_num:
        print('Your guess is too high!')
    if esti == rand_num:
        break

if esti == rand_num:
    madeattempts = str(madeattempts)
    print('Nice work ' + name +  '. I was thinking in that exact number! It took you ' + madeattempts + ' attempts to guess right!')

if esti != rand_num: 
     rand_num = str(rand_num)
     print('Oh ' + name + 'you weren\' able to guess it! The number was ' + rand_num + ', but don\'t get sad! You can always try it again! \'Till next time!')




