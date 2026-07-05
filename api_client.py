import requests

API_URL = "https://official-joke-api.appspot.com/jokes/ten"

def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()