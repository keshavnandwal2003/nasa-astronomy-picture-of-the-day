import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


def get_data():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
