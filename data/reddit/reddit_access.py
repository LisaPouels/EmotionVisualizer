import os
import data.reddit.reddit_api as api
from dotenv import load_dotenv

load_dotenv()

def get_token(): 
        """ Returns a token for the Reddit API based on a reddit account and API client ID and key."""
        return api.generate_token(
                os.getenv('REDDIT_CLIENT_ID'), 
                os.getenv('REDDIT_SECRET_KEY'), 
                os.getenv('REDDIT_NAME'), 
                os.getenv('REDDIT_PW'), 
                os.getenv('ARTIFACT_ID')
        )

def get_headers(token):
        """ Returns a header for the Reddit API based on a token. """
        return {
                'User-Agent': 'EmotionVisualizer/0.0.1', 
                'Authorization': f'bearer {token}'
        }
                