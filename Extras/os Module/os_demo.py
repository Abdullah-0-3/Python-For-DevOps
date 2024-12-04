import os

# Checking Commands
print(dir(os))

# Get Current Working Directory
currect_dir = os.getcwd()
print(currect_dir)

# Change Directory
os.chdir("D:\Works\Alnafi\DevOps")
print(os.getcwd())
os.chdir(currect_dir)

# List Directory
print(os.listdir())

# Make Directory
os.mkdir("Test")
os.makedirs("Test/SubTest")

# Remove Directory
os.rmdir("Test")
os.removedirs("Test/SubTest")

# Rename File
os.rename("python.txt", "python3.txt")

# File Information
print(os.stat("python3.txt"))
print(os.stat("python3.txt").st_size)

# Last Modified Time
print(os.stat("python3.txt").st_mtime)

# Convert Time
from datetime import datetime
mod_time = os.stat("python3.txt").st_mtime
print(datetime.fromtimestamp(mod_time))

# Walk Through Directory
for dirpath, dirnames, filenames in os.walk("D:\Works\Alnafi\DevOps"):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()

# Environment Variables
print(os.environ.get("HOME"))

# File Path
file_path = os.path.join(os.environ.get("HOME"), "test.txt")
print(file_path)

# Path Modules
print(os.path.basename("/tmp/test.txt"))
print(os.path.dirname("/tmp/test.txt"))
print(os.path.split("/tmp/test.txt"))
print(os.path.exists("/tmp/test.txt"))
print(os.path.isdir("/tmp/test.txt"))
print(os.path.isfile("/tmp/test.txt"))
print(os.path.splitext("/tmp/test.txt"))
print(dir(os.path))