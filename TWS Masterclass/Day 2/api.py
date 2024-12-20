# DevOps Engineer
# API - Application Programming Interface

import requests

def api_check():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        print('API is working')
    else:
        print('API is not working')
    
api_check()