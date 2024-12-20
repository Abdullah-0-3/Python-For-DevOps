# Print Even Numbers form 1 to 20

def even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    even_numbers()