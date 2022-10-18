import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Get the access token and headers
def get_token():
    client_id = os.getenv('client_id')
    secret_key = os.getenv('secret_key')
    password = os.getenv('reddit_pw')

    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)

    data = {'grant_type': 'password',
            'username': 'LPouels',
            'password': password}
    headers = {'User-Agent': 'EmotionVisualizer/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'

    return headers
