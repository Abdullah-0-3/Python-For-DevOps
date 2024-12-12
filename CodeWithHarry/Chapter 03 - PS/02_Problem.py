name = input('Enter your name: ')

letter = '''
Dear |Name|,
You are Selected!
|Date|
'''

letter = letter.replace("|Name|", name).replace("|Date|", '11 December 2024')
print(letter)