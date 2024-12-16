# For Loop with String

city = 'Islamabad'

for char in city:
    print(char)

# For Loop with List

cities = ['Islamabad', 'New York', 'Paris', 'London', 'Tokyo', 'New Delhi']

for city in cities:
    print(city)

# For Loop with Tuple

cities = ('Islamabad', 'New York', 'Paris', 'London', 'Tokyo', 'New Delhi')

for city in cities:
    print(city)

# For Loop with Set

cities = {'Islamabad', 'New York', 'Paris', 'London', 'Tokyo', 'New Delhi'}

for city in cities:
    print(city)


# For Loop with Dictionary

cities = {
    'Pakistan': 'Islamabad',
    'USA': 'New York',
    'France': 'Paris',
    'UK': 'London',
    'Japan': 'Tokyo',
    'India': 'New Delhi'
}

for country, city in cities.items():
    print(f'{country} : {city}')