# Snake, Water and Gun Game

import random

computer = random.choice([0, 1, 2])
player = input("Enter s for Snake, w for Water, g for Gun\n")
player = player.lower()

correspondence = {0: "Snake", 1: "Water", 2: "Gun"}
reverse_correspondence = {"s": 0, "w": 1, "g": 2}

print(f"Computer chose {correspondence[computer]}")
print(f"You chose {correspondence[reverse_correspondence[player]]}")

if computer == reverse_correspondence[player]:
    print("It's a draw!")
elif computer == 0 and reverse_correspondence[player] == 2:
    print("You win!")
elif computer == 1 and reverse_correspondence[player] == 0:
    print("You win!")
elif computer == 2 and reverse_correspondence[player] == 1:
    print("You win!")
else:
    print("You lose!")