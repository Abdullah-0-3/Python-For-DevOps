# Match Case In Python

'''
The match case statement is a new feature in Python 3.10. It is used to compare the value of an expression to a series of patterns. The match case statement is similar to the switch statement in other programming languages.
'''

def http_status(status_code: int) -> str:
    match status_code:
        case 200:
            return f"OK - {status_code}"
        case 400:
            return f"Bad Request - {status_code}"
        case 404:
            return f"Not Found - {status_code}"
        case 500:
            return f"Internal Server Error - {status_code}"
        case _:
            return "Unknown Status Code"

print(http_status(200))
print(http_status(400))
print(http_status(404))
print(http_status(500))
print(http_status(300))