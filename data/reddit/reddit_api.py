import requests

def generate_token(client_id, secret_key, name, password, artifactID):
    """ Generates a access token and headers for the Reddit API. """
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    data = {
            'grant_type': 'password',
            'username': name,
            'password': password
    }
    headers = {'User-Agent': artifactID}
    return post('https://www.reddit.com/api/v1/access_token', headers, None, auth=auth, data=data)['access_token']

def get_posts(subreddit, headers):
    """ Returns a list of top posts from a subreddit for the last hour. """
    return [
        {
            "uID": post["data"]["name"],
            "created_utc": post["data"]["created_utc"],
            "subreddit": subreddit,
            "title": post["data"]["title"],
            "text": post["data"]["selftext"],
            "upvotes": post["data"]["ups"],
            "downvotes": post["data"]["downs"],
            "total_awards_received": post["data"]["total_awards_received"],
            "num_comments": post["data"]["num_comments"]
        } for post in get(f'https://oauth.reddit.com/r/{subreddit}/top', headers, {'limit': 100, 't': 'hour'})['data']['children'] if len(post['data']['selftext']) > 10 
    ]

def get(url, headers, params):
    """ Returns a JSON object from a GET request except if it cannot be parsed. """
    try:
        return requests.get(url, headers=headers, params=params).json()
    except Exception as e:
        print(e)
        exit()

def post(url, headers, params, *, auth, data):
    """ Returns a JSON object from a POST request except if it cannot be parsed. """
    try:
        return requests.post(url, headers=headers, params=params, auth=auth, data=data).json()
    except Exception as e:
        print(e)
        exit()