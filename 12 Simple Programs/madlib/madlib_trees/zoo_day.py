'''
Mad Lib: "A Day at the Zoo"
Today, I went to the zoo with my [person] and saw a [adj] [noun]. It was [verb ending in -ing] so loudly that it scared all the [plural noun] away. Then, we visited the [noun] exhibit and saw a very [adj] [noun] doing a funny dance. I couldn't stop [verb ending in -ing]. It was the best day ever!
'''

def madlib():
    person = input("Enter a person: ")
    adj = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    plural_noun = input("Enter a plural noun: ")
    noun2 = input("Enter another noun: ")
    adj2 = input("Enter another adjective: ")
    noun3 = input("Enter another noun: ")
    verb_ing2 = input("Enter another verb ending in -ing: ")

    madlib = f"Today, I went to the zoo with my {person} and saw a {adj} {noun1}. It was {verb_ing} so loudly that it scared all the {plural_noun} away. Then, we visited the {noun2} exhibit and saw a very {adj2} {noun3} doing a funny dance. I couldn't stop {verb_ing2}. It was the best day ever!"

    print(madlib)

if __name__ == "__main__":
    madlib()