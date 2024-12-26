# Problem 05

def table(num):
    table = [num * i for i in range(1, 13)]
    with open('table.txt', 'a') as file:
        file.write(f"Table of {num}: {str(table)} \n")

if __name__ == "__main__":
    [table(i) for i in range(1, 101)]