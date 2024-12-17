# Question 02

def cel_to_fah(cel):
    fah = (cel * 9/5) + 32
    return fah

cel = float(input("Enter the temperature in Celsius: "))
print(f"The temperature in Fahrenheit is {cel_to_fah(cel)}")