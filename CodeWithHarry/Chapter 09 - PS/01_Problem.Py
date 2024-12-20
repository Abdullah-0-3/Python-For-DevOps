with open("poem.txt", "r") as file:
    content = file.read()
    if "twinkle" in content.lower():
        print("Twinkle is present")
    else:
        print("Twinkle is not present")