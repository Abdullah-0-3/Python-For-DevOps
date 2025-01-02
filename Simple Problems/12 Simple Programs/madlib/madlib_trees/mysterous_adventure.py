'''
Mad Lib: "A Mysterious Adventure"
Once upon a time, there was a [adj] [noun] who lived in a [noun]. One day, [person] found a [adj] treasure map that led to the [noun]. They had to [verb] through [plural noun] and [verb] up a [adj] mountain. Finally, they reached the spot and discovered a treasure full of [plural noun]. It was the [adj] adventure of their life!
'''

def madlib():
    adj = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    person = input("Enter a person: ")
    adj2 = input("Enter another adjective: ")
    verb = input("Enter a verb: ")
    plural_noun1 = input("Enter a plural noun: ")
    verb2 = input("Enter another verb: ")
    adj3 = input("Enter another adjective: ")
    plural_noun2 = input("Enter another plural noun: ")

    madlib = f"Once upon a time, there was a {adj} {noun1} who lived in a {noun2}. One day, {person} found a {adj2} treasure map that led to the {noun2}. They had to {verb} through {plural_noun1} and {verb2} up a {adj3} mountain. Finally, they reached the spot and discovered a treasure full of {plural_noun2}. It was the {adj2} adventure of their life!"

    print(madlib)

if __name__ == "__main__":
    madlib()