import random

class GuessingGame:
    def guess(n):
        random_number = random.randint(1, n)

        guess = 0
        count = 0
        while guess != random_number:
            guess = int(input(f"Guess a number between 1 and {n}: "))
            count += 1
            if guess < random_number:
                print("Sorry, guess again. Too low.")
            elif guess > random_number:
                print("Sorry, guess again. Too high.")
        print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")
        print(f"It took you {count} guesses.")

    def computer_guess(n):
        low = 1
        high = n
        feedback = ""
        print(f"Please think of a number between 1 and {n}")
        while feedback != "c":
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low
            feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
            if feedback == "h":
                high = guess - 1
            elif feedback == "l":
                low = guess + 1

if __name__ = "__main__":
    GuessingGame.guess(10)
    GuessingGame.computer_guess(10)