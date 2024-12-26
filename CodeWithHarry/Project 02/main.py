print('The Perfect Guess!!!')

import random

guess_count = 0

def guess():
    global guess_count
    random_number = random.randint(1, 10)
    while True:
        guess = int(input('Enter a number between 1 and 10: '))
        guess_count += 1
        if guess == 0:
            print('You have exited the game.')
            break
        elif guess < random_number:
            print('Try again. Too low.')
        elif guess > random_number:
            print('Try again. Too high.')
        else:
            print(f'Congratulations! You have guessed the number {random_number} correctly.')
            print(f'You got it in {guess_count} guesses.')
            break

if __name__ == "__main__":
    guess()