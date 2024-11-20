import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Programming"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data['type'] == 'single':
            return data['joke']
        else:
            return f"Question: {data['setup']}\nDelivery: {data['delivery']}"
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    joke = get_joke()
    print(joke)
    input("Press Enter to exit...")