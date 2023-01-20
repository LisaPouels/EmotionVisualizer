from langdetect import detect
import text2emotion as te
import numpy as np
import datetime

def convertTime(time):
    """Converts a unix timestamp to a readable date"""
    return datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

def calculateImportance(post):
    """Calculates the importance of a post based on upvotes, downvotes, awards and comments"""
    importance = ((post['upvotes'] - post['downvotes']) + 100 * post['total_awards_received']) * 1.01 ** post['num_comments']
    if importance > 9999999999:
        importance = 9999999999
    return round(importance, 10)

def calculateScaledImportance(importance):
    """Scales the importance of a post using arcsinh"""
    scaled_importance = np.arcsinh(importance)
    if scaled_importance > 99999:
        scaled_importance = 99999
    return round(scaled_importance, 15)

def getEmotion(text):
    """Returns the emotion of a text"""
    result = te.get_emotion(text)
    return max(te.get_emotion(text), key=result.get)

def isEnglish(text):
    """Returns whether a text is in English"""
    try :
        return detect(text) == 'en'
    except:
        return False