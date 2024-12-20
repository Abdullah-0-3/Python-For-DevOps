import os

def table():
    if not os.path.exists("tables"):
        os.mkdir("tables")

    for i in range(1, 21):
        gen_table(i)

def gen_table(i):
    lines = []
    for n in range(1, 13):
        data = f"{i} x {n} = {i * n}\n"
        lines.append(data)
    gen_file(lines, i)  

def gen_file(data, i):
    with open(f"tables/table_{i}.txt", "w") as file:
        file.writelines(data)  

if __name__ == "__main__":
    table()