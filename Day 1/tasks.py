def os(os_name):
    if os_name == "Windows":
        return "Go To Linux"
    elif os_name == "Linux":
        return "Good to Go"
    elif os_name == "Mac":
        return "Go To Linux"
    
for i in range(4):
    print(os("Windows"))