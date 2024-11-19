# String Formatting

name = input('Enter your name: ')


city = input('Enter your City: ')
print('You live in ' + city)

intro = f"I'm {name} and I live in {city}"

nickname = input('Enter your nickname: ')

intro = intro.replace(name, nickname)
print(intro)

a = 5
print(dir(a))
print(dir(intro))