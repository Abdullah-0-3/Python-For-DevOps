import requests

class API():
    
    def api_weather(self, city):
        url = f'https://wttr.in/{city}'
        response = requests.get(url)
        if response.status_code == 200:
            print('API is working')
        else:
            print('API is not working')
        print(response.text)

api_a = API()
api_a.api_weather('New York')