# We will do this using Chatgpt

import os

# Specify the directory you want to list
directory = "."  # Current directory

# Get the list of entries in the directory
entries = os.listdir(directory)

# Print each entry
for entry in entries:
    print(entry)