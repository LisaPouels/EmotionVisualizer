import requests

# Get the access token and headers
def get_token():
    with open('reddit_cli.txt', 'r') as f:
        client_id= f.read()
    with open('reddit_sk.txt', 'r') as f:
        secret_key= f.read()

    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    with open('reddit_me.txt', 'r') as f:
        password = f.read()

    data = {'grant_type': 'password',
            'username': 'LPouels',
            'password': password}
    headers = {'User-Agent': 'EmotionVisualizer/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    TOKEN = res.json()['access_token']
    headers['Authorization'] = f'bearer {TOKEN}'

    return headers
