'''
Mad Lib: "The Strange Pet"
I wanted a pet, so I decided to get a [adj] [noun]. I named it [name]. It loves to [verb] every day and it can [verb] like a [animal]. One time, it got loose and started [verb ending in -ing] all over the [place]. Everyone thought it was so [adj]. Now, it's the most loved [noun] in the neighborhood!
'''

def madlib():
    adj = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    name = input("Enter a name: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    animal = input("Enter an animal: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    place = input("Enter a place: ")
    adj2 = input("Enter another adjective: ")

    madlib = f"I wanted a pet, so I decided to get a {adj} {noun}. I named it {name}. It loves to {verb1} every day and it can {verb2} like a {animal}. One time, it got loose and started {verb_ing} all over the {place}. Everyone thought it was so {adj2}. Now, it's the most loved {noun} in the neighborhood!"

    print(madlib)

if __name__ == "__main__":
    madlib()