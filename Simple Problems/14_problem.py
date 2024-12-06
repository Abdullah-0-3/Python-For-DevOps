# Convert Tempreature from Degree Celsius to Fahrenheit

def c_to_f(temp):
    print("Tempreature in Celsius is", temp)
    temp_f = (temp * 9//5) + 32 
    print("Tempreature in Fahrenheit is", temp_f)

if __name__ == "__main__":
    c_to_f(100)