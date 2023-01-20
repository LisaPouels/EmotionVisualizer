from data.database.database_connector import *

def insertEmotions(data: dict):
    """ Insert a post into the database. """
    insertQuery("REPLACE INTO post VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
        [
            data['uID'], 
            data['subreddit'], 
            data['time'], 
            data['emotion'], 
            data['aggregate_emotion'],
            data['importance'],
            data['importance_scaled'],
            data['continent'],
            data['topic'],
        ]
    )

def selectEmotions():
    """ Select all posts from the database. """
    return selectQuery("SELECT * FROM post")