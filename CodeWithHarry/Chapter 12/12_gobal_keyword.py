# Global Keyword

a = 10
print(a)

def func():
    global a
    a = 12
    print(a)

func()
print(a)