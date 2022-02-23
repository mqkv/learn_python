#!/usr/bin/env python
# -*- coding: utf-8 -*-
# date: 2022-02-22
# guess the number game
# A number is randomly created by the program, and the user guesses the number
# If the number entered by the user is greater than a random number, print please enter a smaller number
# If the number entered by the user is less than a random number, print please enter a larger number
# If the number entered by the user equals a random number, print congratulations on your guess.
# Finally. print the number of guesses by the user
#

import random

answer = random.randint(1, 100)
# print(answer)
counter = 0
while True:
    counter += 1
    num = int(input("Enter the number here: "))
    if num < answer:
        print('Please enter a larger number!')
    elif num > answer:
        print('Please enter a lower number!')
    else:
        print('Congratulations, you guessed it right!')
        break


print('You guessed %s times in total' % counter)
