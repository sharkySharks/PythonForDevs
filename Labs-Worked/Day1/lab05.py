
import random
from random import randrange

computerNumber = random.randrange(1,101)
attempts = 0

while True:
    guess = int(raw_input('Enter your guess: ' ))

    if guess == 'q' or guess == 'Q':
        break
    elif guess == computerNumber:
        attempts += 1
        print '{} <=== You got it in {} guesses!'.format(guess, attempts)
        break
    elif guess > computerNumber:
        print '{} IS TOO HIGH!'.format(guess)
        attempts += 1
    elif guess < computerNumber:
        print '{} is too loooow'.format(guess)
        attempts += 1
