import service.datascience as ds

def dataAnalysis(post, continent, subreddit, category):
    """ Analyze a post and return the new data. """
    post['time'] = ds.convertTime(post['created_utc'])
    post['emotion'] = ds.getEmotion(post['text'])
    post['aggregate_emotion'] = None
    post['importance'] = ds.calculateImportance(post)
    post['importance_scaled'] = ds.calculateScaledImportance(post['importance'])
    post['continent'] = continent
    post['topic'] = None
    if category == dict:
        sub_name, subs = list(subreddit.items())[0]
        post['subreddit'] = sub_name.capitalize()
    else:
        post['subreddit'] = subreddit.capitalize()
    keys = ['created_utc', 'title', 'text', 'upvotes', 'downvotes', 'total_awards_received', 'num_comments']
    [post.pop(key) for key in keys]
    
    return post