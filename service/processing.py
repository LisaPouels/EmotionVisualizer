import data.database.database_interface as db
import data.reddit.reddit_access as ra
import data.reddit.reddit_api as api
import data.reddit.reddit_ratelimit as rl
import service.datascience as ds
import service.data_analysis as da
import yaml
import time

def analyzePosts(posts, continent, subreddit, category):
    """ Analyze posts and return a list with the data. """
    return [da.dataAnalysis(post, continent, subreddit, category) for post in posts]
    
def getPosts(subreddit, continent, headers):
    """ Get posts from a subreddit and return a list with analyzed posts. """
    if type(subreddit) == dict:
        posts = []
        for list in subreddit.values():
            posts = [post for sub in list for post in api.get_posts(sub, headers) if ds.isEnglish(post['text'])]
        category = dict
    else:
        posts = [post for post in api.get_posts(subreddit, headers) if ds.isEnglish(post['text'])]
        category = str
    print(f'{subreddit}: {len(posts)}')
    posts = analyzePosts(posts, continent, subreddit, category)

    return posts

def postPosts(posts):
    """ Post posts to the database. """
    for post in posts:
        db.insertEmotions(post)

def main():
    """ Runs the main program and tracks runtime."""
    starttime = time.time()

    TOKEN = ra.get_token()
    HEADERS = ra.get_headers(TOKEN)

    with open('data/subreddits.yml', 'r') as f:
        subreddits = yaml.load(f)	

    for continent in subreddits:
        if rl.requests_remaining(HEADERS) <= len(subreddits[continent]):
            print('Waiting for rate limit to reset...')
            time.sleep(rl.reset_time(HEADERS))
        for subreddit in subreddits[continent]:
            posts = getPosts(subreddit, continent, HEADERS)
            postPosts(posts)

    print(f'Time elapsed: {time.time() - starttime}')