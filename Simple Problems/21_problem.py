# Print Odd Numbers form 1 to 20

def odd_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            continue
        else: 
            print(i)


if __name__ == "__main__":
    odd_numbers()