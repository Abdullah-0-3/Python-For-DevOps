# Problem 01

def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                print(line, end='')  # Added end='' to avoid double newlines
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    for file_name in files:
        print(f"{file_name} --- ", end="")
        read_file(file_name)  # Changed to call read_file instead of file