import requests

def get_weather(command):
    url = f'https://wttr.in/{command}'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print('API is not working')