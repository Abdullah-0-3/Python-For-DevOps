import random
from madlib_trees import cooking_diaster, zoo_day, strange_pet, mysterous_adventure

def main():
    madlibs = [cooking_diaster, zoo_day, strange_pet, mysterous_adventure]
    madlib = random.choice(madlibs)
    madlib.madlib()

if __name__ == "__main__":
    main()