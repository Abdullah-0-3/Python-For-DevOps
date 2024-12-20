import random

def game():
    print("You are Playing a Game...")
    score = random.randint(1, 62)
    try:
        with open("high_score.txt", "r") as file:
            his_score = file.read()
            if his_score:
                his_score = int(his_score)
            else:
                his_score = 0
    except FileNotFoundError:
        his_score = 0

    print(f"Your Score is {score}")
    if score > his_score:
        with open("high_score.txt", "w") as file:
            file.write(str(score))
            print("You have just broken the High Score!")

    return score

game()