import requests

def requests_remaining(headers):
    """ Returns the number of requests remaining. """
    ratelimit_remaining = requests.get('https://oauth.reddit.com/', headers=headers).headers['x-ratelimit-remaining']
    print(f'Requests remaining: {ratelimit_remaining}')
    return float(ratelimit_remaining)

def reset_time(headers):
    """ Returns the time until the rate limit resets. """
    ratelimit_reset = requests.get('https://oauth.reddit.com/', headers=headers).headers['x-ratelimit-reset']
    print(f'Reset time: {ratelimit_reset}')
    return float(ratelimit_reset)