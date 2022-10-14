import pandas as pd
import requests
import reddit_access as ra


def get_posts(subreddit, sort='hot', limit=100):
    headers = ra.get_token()
    res = requests.get(f'https://oauth.reddit.com/r/{subreddit}/{sort}', headers=headers, params={'limit': limit})
    df = pd.DataFrame()
    for post in res.json()['data']['children']:
        df = df.append({'uID': post['data']['name'],
        'created_utc': post['data']['created_utc'],
        'subreddit': post['data']['subreddit'],
        'title': post['data']['title'],
        'text': post['data']['selftext'],
        'upvotes': post['data']['ups'],
        'downvotes': post['data']['downs'],
        'total_awards_received': post['data']['total_awards_received'],
        'num_comments': post['data']['num_comments']
        }, 
        ignore_index=True)
    
    df2 = df.loc[:,['uID', 'created_utc', 'subreddit', 'title', 'text', 'upvotes', 'downvotes', 'total_awards_received', 'num_comments']]
    
    return df2
