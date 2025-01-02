'''
MadLib: "The Cooking Disaster"
I decided to cook [dish] for dinner. First, I gathered all the [plural noun] and [plural noun]. Then, I started [verb ending in -ing] everything together. But I accidentally added a [adj] amount of [noun] instead of [noun]. The kitchen was a complete [noun]! In the end, I served it to [person], and we both ended up [verb ending in -ing] because it tasted so [adj].
'''

def madlib():
    dish = input("Enter a dish: ")
    plural_noun1 = input("Enter a plural noun: ")
    plural_noun2 = input("Enter another plural noun: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    adj = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    person = input("Enter a person: ")
    adj2 = input("Enter another adjective: ")

    madlib = f"I decided to cook {dish} for dinner. First, I gathered all the {plural_noun1} and {plural_noun2}. Then, I started {verb_ing} everything together. But I accidentally added a {adj} amount of {noun1} instead of {noun2}. The kitchen was a complete {noun1}! In the end, I served it to {person}, and we both ended up {verb_ing} because it tasted so {adj2}."

    print(madlib)

if __name__ == "__main__":
    madlib()